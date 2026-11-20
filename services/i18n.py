from __future__ import annotations

from contextlib import contextmanager
from contextvars import ContextVar
from typing import Final, Iterator, Mapping

DEFAULT_LANGUAGE: Final[str] = "tr"
SUPPORTED_LANGUAGES: Final[tuple[str, ...]] = ("tr", "ru", "en")
SUPPORTED_LANGUAGE_SET: Final[frozenset[str]] = frozenset(SUPPORTED_LANGUAGES)

_current_language: ContextVar[str] = ContextVar("current_language", default=DEFAULT_LANGUAGE)


def normalize_language(language: str | None) -> str:
    if not isinstance(language, str):
        return DEFAULT_LANGUAGE
    normalized = language.strip().lower()
    if normalized in SUPPORTED_LANGUAGE_SET:
        return normalized
    short = normalized.split("-", 1)[0].split("_", 1)[0]
    if short in SUPPORTED_LANGUAGE_SET:
        return short
    return DEFAULT_LANGUAGE


def get_current_language() -> str:
    return normalize_language(_current_language.get())


def set_current_language(language: str | None):
    return _current_language.set(normalize_language(language))


def reset_current_language(token) -> None:
    _current_language.reset(token)


@contextmanager
def language_scope(language: str | None) -> Iterator[str]:
    normalized = normalize_language(language)
    token = _current_language.set(normalized)
    try:
        yield normalized
    finally:
        _current_language.reset(token)


def tr_text(translations: Mapping[str, str], language: str | None = None) -> str:
    lang = normalize_language(language) if language is not None else get_current_language()
    if lang in translations:
        return translations[lang]
    if DEFAULT_LANGUAGE in translations:
        return translations[DEFAULT_LANGUAGE]
    if "en" in translations:
        return translations["en"]
    return next(iter(translations.values()))
