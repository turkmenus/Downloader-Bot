from __future__ import annotations

from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.enums import ChatType
from aiogram.types import CallbackQuery, InlineQuery, Message

from app_context import db
from services.i18n import DEFAULT_LANGUAGE, normalize_language, reset_current_language, set_current_language


def _resolve_language_target_id(event: Any) -> int | None:
    if isinstance(event, Message):
        chat = getattr(event, "chat", None)
        chat_type = getattr(chat, "type", None)
        if chat and chat_type not in {ChatType.PRIVATE, "private", None}:
            return getattr(chat, "id", None)
        user = getattr(event, "from_user", None)
        return getattr(user, "id", None)

    if isinstance(event, CallbackQuery):
        msg = getattr(event, "message", None)
        chat = getattr(msg, "chat", None)
        chat_type = getattr(chat, "type", None)
        if chat and chat_type not in {ChatType.PRIVATE, "private", None}:
            return getattr(chat, "id", None)
        user = getattr(event, "from_user", None)
        return getattr(user, "id", None)

    if isinstance(event, InlineQuery):
        user = getattr(event, "from_user", None)
        return getattr(user, "id", None)

    user = getattr(event, "guest_bot_caller_user", None) or getattr(event, "from_user", None)
    return getattr(user, "id", None)


class LanguageMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Any, Dict[str, Any]], Awaitable[Any]],
        event: Any,
        data: Dict[str, Any],
    ) -> Any:
        target_id = _resolve_language_target_id(event)
        lang = DEFAULT_LANGUAGE
        if target_id is not None:
            getter = getattr(db, "get_user_setting", None)
            if callable(getter):
                try:
                    raw_lang = await getter(user_id=target_id, field="language")
                    if raw_lang:
                        lang = normalize_language(raw_lang)
                except Exception:
                    lang = DEFAULT_LANGUAGE

        token = set_current_language(lang)
        try:
            return await handler(event, data)
        finally:
            reset_current_language(token)
