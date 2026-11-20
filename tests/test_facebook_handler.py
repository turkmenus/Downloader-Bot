from types import SimpleNamespace

import pytest

from handlers import facebook
from services.platforms.facebook_media import strip_facebook_url
from utils.download_manager import DownloadMetrics


def test_strip_facebook_url_normalizes_reels_and_preserves_v():
    assert (
        strip_facebook_url("https://www.facebook.com/reels/123456789/?mibextid=xyz#frag")
        == "https://www.facebook.com/reel/123456789/"
    )
    assert (
        strip_facebook_url("https://www.facebook.com/watch/?v=998877&mibextid=xyz")
        == "https://www.facebook.com/watch/?v=998877"
    )


def test_parse_facebook_post_tunnel():
    payload = {
        "status": "tunnel",
        "url": "http://cobalt:9000/tunnel?id=abc",
        "filename": "facebook_123.mp4",
    }
    post = facebook.parse_facebook_post(payload)
    assert post is not None
    assert post.use_ytdlp is False
    assert post.media_list[0].type == "video"
    assert post.media_list[0].url == "http://cobalt:9000/tunnel?id=abc"


@pytest.mark.asyncio
async def test_facebook_service_fetch_post_uses_cobalt_first(monkeypatch, tmp_path):
    captured = {}

    async def fake_fetch_cobalt_data(base_url, api_key, request_payload, **kwargs):
        captured["base_url"] = base_url
        captured["api_key"] = api_key
        captured["payload"] = request_payload
        captured["kwargs"] = kwargs
        return {"status": "tunnel", "url": "http://cobalt:9000/tunnel?id=1", "filename": "fb.mp4"}

    monkeypatch.setattr(facebook, "COBALT_API_URL", "http://cobalt:9000")
    monkeypatch.setattr(facebook, "COBALT_API_KEY", "test-key")
    monkeypatch.setattr(facebook, "fetch_cobalt_data", fake_fetch_cobalt_data)

    service = facebook.FacebookService(output_dir=str(tmp_path))
    post = await service.fetch_post("https://www.facebook.com/reels/12345/?mibextid=test")

    assert post is not None
    assert post.use_ytdlp is False
    assert captured["payload"]["url"] == "https://www.facebook.com/reel/12345/"
    assert captured["kwargs"]["source"] == "facebook"


@pytest.mark.asyncio
async def test_facebook_service_falls_back_to_ytdlp_when_cobalt_fails(tmp_path):
    async def fake_fetch_cobalt_data(*_args, **_kwargs):
        return None

    class FakeYDL:
        def __init__(self, _opts):
            pass

        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return False

        def extract_info(self, url, download=False):
            assert download is False
            return {
                "id": "12345",
                "title": "Sample Facebook Reel",
                "thumbnail": "https://cdn.example.com/thumb.jpg",
            }

    service = facebook.FacebookMediaService(
        output_dir=str(tmp_path),
        cobalt_api_url="http://cobalt:9000",
        cobalt_api_key="test-key",
        fetch_cobalt_data_func=fake_fetch_cobalt_data,
        retry_async_operation_func=lambda fn, **_kw: fn(),
        youtube_dl_factory=FakeYDL,
    )
    post = await service.fetch_post("https://www.facebook.com/reel/12345/")

    assert post is not None
    assert post.use_ytdlp is True
    assert post.id == "12345"
    assert post.description == "Sample Facebook Reel"
    assert post.media_list[0].url == "https://www.facebook.com/reel/12345/"
    assert post.media_list[0].thumb == "https://cdn.example.com/thumb.jpg"


@pytest.mark.asyncio
async def test_facebook_service_download_media_routes_facebook_url_to_ytdlp(monkeypatch, tmp_path):
    async def fake_fetch_cobalt_data(*_args, **_kwargs):
        return None

    service = facebook.FacebookMediaService(
        output_dir=str(tmp_path),
        cobalt_api_url="http://cobalt:9000",
        cobalt_api_key="test-key",
        fetch_cobalt_data_func=fake_fetch_cobalt_data,
        retry_async_operation_func=lambda fn, **_kw: fn(),
    )

    called = {}

    async def fake_ytdlp_download(url, filename):
        called["url"] = url
        called["filename"] = filename
        out = tmp_path / filename
        out.write_bytes(b"mp4")
        return DownloadMetrics(url=url, path=str(out), size=3, elapsed=0.01, used_multipart=False, resumed=False)

    monkeypatch.setattr(service, "download_with_ytdlp", fake_ytdlp_download)
    metrics = await service.download_media("https://www.facebook.com/reel/12345/", "fb.mp4")

    assert metrics is not None
    assert called == {"url": "https://www.facebook.com/reel/12345/", "filename": "fb.mp4"}
