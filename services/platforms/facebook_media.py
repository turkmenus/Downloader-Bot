import asyncio
import hashlib
import json
import os
import re
import time
from dataclasses import dataclass
from typing import Any, Awaitable, Callable, Optional
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

import yt_dlp

from services.logger import logger as logging
from services.platforms import CobaltMediaService
from services.platforms.ytdlp_helpers import resolve_downloaded_path, run_ytdlp_download
from utils.cobalt_media import parse_cobalt_media_response
from utils.download_manager import (
    DownloadError as DownloadError,  # noqa: F401  (re-exported for handlers)
    DownloadMetrics,
)

logging = logging.bind(service="facebook_media")

FACEBOOK_URL_REGEX = (
    r"(https?://(?:(?:www|m|web|mbasic)\.)?facebook\.com/"
    r"(?:reel|reels|watch|share|video\.php|[^/\s]+/videos)\S*|https?://fb\.watch/\S+)"
)

_PRESERVED_QUERY_KEYS = frozenset({"v", "id"})


def strip_facebook_url(url: str) -> str:
    """Drop tracking query params/fragments and normalize mobile /reels/ paths."""
    try:
        parsed = urlparse(url)
    except Exception:
        return url

    path = re.sub(r"^/reels/([^/?#]+)", r"/reel/\1", parsed.path)
    kept_query = [
        (key, value)
        for key, value in parse_qsl(parsed.query, keep_blank_values=False)
        if key in _PRESERVED_QUERY_KEYS
    ]
    return urlunparse(
        (
            parsed.scheme,
            parsed.netloc,
            path,
            "",
            urlencode(kept_query),
            "",
        )
    )


def _derive_description(data: dict) -> str:
    output = data.get("output")
    if isinstance(output, dict):
        metadata = output.get("metadata")
        if isinstance(metadata, dict):
            title = metadata.get("title") or metadata.get("description")
            if isinstance(title, str) and title.strip():
                return title.strip()
    metadata = data.get("metadata")
    if isinstance(metadata, dict):
        for field_name in ("title", "description", "caption"):
            value = metadata.get(field_name)
            if isinstance(value, str) and value.strip():
                return value.strip()
    description = data.get("description")
    if isinstance(description, str) and description.strip():
        return description.strip()
    return ""


@dataclass
class FacebookMedia:
    url: str
    type: str
    thumb: Optional[str] = None


@dataclass
class FacebookPost:
    id: str
    description: str
    media_list: list[FacebookMedia]
    source_url: Optional[str] = None
    use_ytdlp: bool = False


def get_facebook_preview_url(media: Optional[FacebookMedia]) -> Optional[str]:
    if not media:
        return None
    if media.type == "photo":
        return media.thumb or media.url
    return media.thumb or None


def parse_facebook_post(data: dict, *, source_url: Optional[str] = None) -> Optional[FacebookPost]:
    parsed = parse_cobalt_media_response(data, allow_multi_tunnel=True, source="facebook")
    if not parsed:
        return None

    media_list = [
        FacebookMedia(url=media_url, type=media_type, thumb=thumb)
        for media_url, media_type, thumb in parsed.items
    ]

    return FacebookPost(
        id=hashlib.blake2s(
            json.dumps(data, sort_keys=True, separators=(",", ":"), default=str).encode("utf-8"),
            digest_size=8,
        ).hexdigest(),
        description=_derive_description(data),
        media_list=media_list,
        source_url=source_url,
        use_ytdlp=False,
    )


class FacebookMediaService(CobaltMediaService):
    def __init__(
        self,
        output_dir: str,
        *,
        cobalt_api_url: Optional[str],
        cobalt_api_key: Optional[str],
        fetch_cobalt_data_func: Callable[..., Awaitable[dict | None]],
        retry_async_operation_func: Callable[..., Awaitable[DownloadMetrics | None]],
        youtube_dl_factory: Callable[[dict[str, Any]], Any] = yt_dlp.YoutubeDL,
    ) -> None:
        super().__init__(
            output_dir,
            source="facebook",
            cobalt_api_url=cobalt_api_url,
            cobalt_api_key=cobalt_api_key,
            fetch_cobalt_data_func=fetch_cobalt_data_func,
            retry_async_operation_func=retry_async_operation_func,
            logger=logging,
            download_error_message="Error downloading Facebook media: url=%s error=%s",
        )
        self._output_dir = output_dir
        self._youtube_dl_factory = youtube_dl_factory

    def _extract_ytdlp_info_sync(self, url: str) -> Optional[dict[str, Any]]:
        ydl_opts: dict[str, Any] = {
            "quiet": True,
            "no_warnings": True,
            "noplaylist": True,
            "socket_timeout": 15,
        }
        with self._youtube_dl_factory(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
        if not isinstance(info, dict):
            return None
        if isinstance(info.get("entries"), list) and info["entries"]:
            first = info["entries"][0]
            if isinstance(first, dict):
                return first
        return info

    def _download_with_ytdlp_sync(self, url: str, filename: str) -> DownloadMetrics:
        os.makedirs(self._output_dir, exist_ok=True)
        expected_path = os.path.join(self._output_dir, filename)
        stem, _ = os.path.splitext(expected_path)
        started_at = time.perf_counter()
        ydl_opts: dict[str, Any] = {
            "quiet": True,
            "no_warnings": True,
            "noprogress": True,
            "noplaylist": True,
            "overwrites": True,
            "socket_timeout": 20,
            "retries": 2,
            "fragment_retries": 2,
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
            "merge_output_format": "mp4",
            "outtmpl": f"{stem}.%(ext)s",
        }
        run_ytdlp_download(self._youtube_dl_factory, url, ydl_opts)
        final_path = resolve_downloaded_path(expected_path)
        return DownloadMetrics(
            url=url,
            path=final_path,
            size=os.path.getsize(final_path),
            elapsed=time.perf_counter() - started_at,
            used_multipart=False,
            resumed=False,
        )

    async def download_with_ytdlp(self, url: str, filename: str) -> Optional[DownloadMetrics]:
        try:
            return await asyncio.to_thread(self._download_with_ytdlp_sync, url, filename)
        except Exception as exc:
            logging.error("Error downloading Facebook video via yt-dlp: url=%s error=%s", url, exc)
            return None

    async def download_media(
        self,
        url: str,
        filename: str,
        *,
        user_id: Optional[int] = None,
        chat_id: Optional[int] = None,
        request_id: Optional[str] = None,
        size_hint: Optional[int] = None,
        on_queued=None,
        on_progress=None,
        on_retry=None,
    ) -> Optional[DownloadMetrics]:
        if re.match(FACEBOOK_URL_REGEX, url, re.IGNORECASE):
            return await self.download_with_ytdlp(url, filename)
        return await super().download_media(
            url,
            filename,
            user_id=user_id,
            chat_id=chat_id,
            request_id=request_id,
            size_hint=size_hint,
            on_queued=on_queued,
            on_progress=on_progress,
            on_retry=on_retry,
        )

    async def fetch_post(self, url: str) -> Optional[FacebookPost]:
        normalized_url = strip_facebook_url(url)
        if self._cobalt_api_url and self._fetch_cobalt_data:
            payload = {
                "url": normalized_url,
                "downloadMode": "auto",
                "videoQuality": "1080",
                "alwaysProxy": True,
                "localProcessing": "disabled",
            }
            data = await self._fetch_cobalt_json(payload)
            if data:
                post = parse_facebook_post(data, source_url=normalized_url)
                if post:
                    return post

        try:
            info = await asyncio.to_thread(self._extract_ytdlp_info_sync, normalized_url)
        except Exception as exc:
            logging.warning("Facebook yt-dlp fallback failed: url=%s error=%s", normalized_url, exc)
            return None

        if not info:
            return None

        post_id = str(info.get("id") or "").strip() or hashlib.blake2s(
            normalized_url.encode("utf-8"), digest_size=8
        ).hexdigest()
        description = str(info.get("title") or info.get("description") or "").strip()
        thumb = info.get("thumbnail") if isinstance(info.get("thumbnail"), str) else None
        return FacebookPost(
            id=post_id,
            description=description,
            media_list=[FacebookMedia(url=normalized_url, type="video", thumb=thumb)],
            source_url=normalized_url,
            use_ytdlp=True,
        )
