from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest
from aiogram.types import Message

import keyboards as kb
import messages as bm
from middlewares.language_middleware import LanguageMiddleware
from services.i18n import DEFAULT_LANGUAGE, get_current_language, language_scope, normalize_language
from services.settings import parse_setting_toggle_callback, parse_settings_view_callback


def test_default_language_is_turkish():
    assert DEFAULT_LANGUAGE == "tr"
    assert get_current_language() == "tr"
    assert "Hoş Geldiniz" in bm.welcome_message()
    assert "Ayarlar" in bm.settings()
    assert "Video indiriliyor" in bm.downloading_video_status()


def test_russian_and_english_translations():
    with language_scope("ru"):
        assert "Добро пожаловать" in bm.welcome_message()
        assert "Настройки" in bm.settings()
        assert "Скачиваю видео" in bm.downloading_video_status()

    with language_scope("en"):
        assert "Welcome to MaxLoad" in bm.welcome_message()
        assert "Settings" in bm.settings()
        assert "Downloading video" in bm.downloading_video_status()

    assert get_current_language() == "tr"


def test_normalize_language_handles_variants_and_unknowns():
    assert normalize_language("tr-TR") == "tr"
    assert normalize_language("ru_RU") == "ru"
    assert normalize_language("EN") == "en"
    assert normalize_language("de") == "tr"
    assert normalize_language(None) == "tr"


def test_language_setting_callbacks_and_keyboards():
    assert parse_settings_view_callback("settings:language") == "language"
    assert parse_setting_toggle_callback("setting:language:ru") == ("language", "ru")

    cats = kb.return_settings_categories_keyboard()
    callbacks = [btn.callback_data for row in cats.inline_keyboard for btn in row]
    assert "settings:language" in callbacks

    lang_kb = kb.return_field_keyboard("language", "ru")
    texts = [btn.text for row in lang_kb.inline_keyboard for btn in row]
    assert any(t.startswith("✅") and "Русский" in t for t in texts)


@pytest.mark.asyncio
async def test_language_middleware_sets_and_resets_context(monkeypatch):
    import middlewares.language_middleware as lm_mod

    fake_db = SimpleNamespace(get_user_setting=AsyncMock(return_value="ru"))
    monkeypatch.setattr(lm_mod, "db", fake_db)

    middleware = LanguageMiddleware()
    event = SimpleNamespace(
        from_user=SimpleNamespace(id=42),
        chat=SimpleNamespace(id=42, type="private"),
    )

    observed = {}

    async def _handler(_event, _data):
        observed["lang"] = get_current_language()
        observed["welcome"] = bm.welcome_message()
        return "ok"

    res = await middleware(lambda e, d: _handler(e, d), event, {})
    assert res == "ok"
    assert observed["lang"] == "ru"
    assert "Добро пожаловать" in observed["welcome"]
    assert get_current_language() == "tr"
