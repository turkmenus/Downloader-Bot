from urllib.parse import quote

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from services.i18n import tr_text


def start_keyboard(
    bot_username: str | None = None, ref_user_id: int | None = None
) -> InlineKeyboardMarkup:
    username = bot_username or "MaxLoadBot"
    base_link = f"https://t.me/{username}"

    share_text = tr_text(
        {
            "tr": "Instagram, TikTok, YouTube ve daha fazlası için hızlı medya indirme botu!",
            "ru": "Быстрый бот для скачивания из Instagram, TikTok, YouTube и других сервисов!",
            "en": "Fast downloader bot for Instagram, TikTok, YouTube & more!",
        }
    )
    share_url = (
        f"https://t.me/share/url?url={quote(base_link)}&text={quote(share_text)}"
    )
    add_to_group_url = f"https://t.me/{username}?startgroup=true"

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=tr_text(
                        {
                            "tr": "⚡ Satır içi dene",
                            "ru": "⚡ Попробовать inline",
                            "en": "⚡ Try inline",
                        }
                    ),
                    switch_inline_query_current_chat="",
                ),
                InlineKeyboardButton(
                    text=tr_text(
                        {
                            "tr": "⚙️ Ayarlar",
                            "ru": "⚙️ Настройки",
                            "en": "⚙️ Settings",
                        }
                    ),
                    callback_data="back_to_settings",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=tr_text(
                        {
                            "tr": "🚀 Botu paylaş",
                            "ru": "🚀 Поделиться ботом",
                            "en": "🚀 Share bot",
                        }
                    ),
                    url=share_url,
                ),
                InlineKeyboardButton(
                    text=tr_text(
                        {
                            "tr": "➕ Gruba ekle",
                            "ru": "➕ Добавить в группу",
                            "en": "➕ Add to group",
                        }
                    ),
                    url=add_to_group_url,
                ),
            ],
        ]
    )


def cancel_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="❌ Cancel", callback_data="cancel_action")
    return builder.as_markup()


def mailing_audience_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(
                text="👤 Private chats only", callback_data="mailing_target:dm"
            )
        ],
        [
            InlineKeyboardButton(
                text="🏘 Groups only", callback_data="mailing_target:groups"
            )
        ],
        [
            InlineKeyboardButton(
                text="🌐 All (DM + Groups)", callback_data="mailing_target:all"
            )
        ],
        [InlineKeyboardButton(text="❌ Cancel", callback_data="cancel_action")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def format_number(value: int) -> str | None:
    if value is None:
        return None
    if value >= 1_000_000_000:
        return f"{value / 1_000_000_000:.1f}B"
    if value >= 1_000_000:
        return f"{value / 1_000_000:.1f}M"
    if value >= 1_000:
        return f"{value / 1_000:.1f}K"
    return str(value)


FIELD_CATEGORY_MAP = {
    "video_quality": "media",
    "as_document": "media",
    "audio_format": "media",
    "captions": "appearance",
    "info_buttons": "appearance",
    "audio_button": "appearance",
    "file_button": "appearance",
    "url_button": "appearance",
    "delete_message": "chat",
    "language": "root",
}


def return_settings_categories_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(
                text=tr_text(
                    {
                        "tr": "🎬 Medya ve Kalite",
                        "ru": "🎬 Медиа и качество",
                        "en": "🎬 Media & Quality",
                    }
                ),
                callback_data="settings_cat:media",
            )
        ],
        [
            InlineKeyboardButton(
                text=tr_text(
                    {
                        "tr": "🎨 Görünüm ve Butonlar",
                        "ru": "🎨 Внешний вид и кнопки",
                        "en": "🎨 Appearance & Buttons",
                    }
                ),
                callback_data="settings_cat:appearance",
            )
        ],
        [
            InlineKeyboardButton(
                text=tr_text(
                    {
                        "tr": "💬 Sohbet ve Temizlik",
                        "ru": "💬 Чат и очистка",
                        "en": "💬 Chat & Clean-up",
                    }
                ),
                callback_data="settings_cat:chat",
            )
        ],
        [
            InlineKeyboardButton(
                text="🌐 Dil / Язык / Language",
                callback_data="settings:language",
            )
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def return_category_settings_keyboard(category: str) -> InlineKeyboardMarkup:
    if category == "media":
        fields = [
            (
                tr_text(
                    {
                        "tr": "🎬 Video Kalitesi",
                        "ru": "🎬 Качество видео",
                        "en": "🎬 Video Quality",
                    }
                ),
                "video_quality",
            ),
            (
                tr_text(
                    {
                        "tr": "📄 Dosya Olarak Gönder",
                        "ru": "📄 Отправлять как файл",
                        "en": "📄 Send as File",
                    }
                ),
                "as_document",
            ),
            (
                tr_text(
                    {
                        "tr": "🎵 Ses Formatı",
                        "ru": "🎵 Формат аудио",
                        "en": "🎵 Audio Format",
                    }
                ),
                "audio_format",
            ),
        ]
    elif category == "appearance":
        fields = [
            (
                tr_text(
                    {
                        "tr": "📝 Açıklamalar",
                        "ru": "📝 Описания",
                        "en": "📝 Descriptions",
                    }
                ),
                "captions",
            ),
            (
                tr_text(
                    {
                        "tr": "ℹ️ Bilgi Butonları",
                        "ru": "ℹ️ Кнопки информации",
                        "en": "ℹ️ Info Buttons",
                    }
                ),
                "info_buttons",
            ),
            (
                tr_text(
                    {
                        "tr": "🎧 MP3 Butonu",
                        "ru": "🎧 Кнопка MP3",
                        "en": "🎧 MP3 Button",
                    }
                ),
                "audio_button",
            ),
            (
                tr_text(
                    {
                        "tr": "📄 Dosya Butonu",
                        "ru": "📄 Кнопка файла",
                        "en": "📄 File Button",
                    }
                ),
                "file_button",
            ),
            (
                tr_text(
                    {
                        "tr": "🔗 URL Butonu",
                        "ru": "🔗 Кнопка URL",
                        "en": "🔗 URL Button",
                    }
                ),
                "url_button",
            ),
        ]
    else:
        fields = [
            (
                tr_text(
                    {
                        "tr": "🗑️ Mesajları Sil",
                        "ru": "🗑️ Удаление сообщений",
                        "en": "🗑️ Delete Messages",
                    }
                ),
                "delete_message",
            ),
        ]

    buttons = [
        [InlineKeyboardButton(text=text, callback_data=f"settings:{field}")]
        for text, field in fields
    ]
    buttons.append(
        [
            InlineKeyboardButton(
                text=tr_text(
                    {
                        "tr": "⬅️ Kategorilere Dön",
                        "ru": "⬅️ Назад к категориям",
                        "en": "⬅️ Back to Categories",
                    }
                ),
                callback_data="back_to_settings",
            )
        ]
    )
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def return_field_keyboard(field: str, value: str | None):
    val = (value or "").strip().lower()
    cat = FIELD_CATEGORY_MAP.get(field, "media")
    back_cb = "back_to_settings" if cat == "root" else f"settings_cat:{cat}"
    back_label = tr_text({"tr": "⬅️ Geri", "ru": "⬅️ Назад", "en": "⬅️ Back"})

    if field == "language":
        current = val or "tr"
        opt_tr = "✅ 🇹🇷 Türkçe" if current == "tr" else "🇹🇷 Türkçe"
        opt_ru = "✅ 🇷🇺 Русский" if current == "ru" else "🇷🇺 Русский"
        opt_en = "✅ 🇬🇧 English" if current == "en" else "🇬🇧 English"
        buttons = [
            [InlineKeyboardButton(text=opt_tr, callback_data="setting:language:tr")],
            [InlineKeyboardButton(text=opt_ru, callback_data="setting:language:ru")],
            [InlineKeyboardButton(text=opt_en, callback_data="setting:language:en")],
            [InlineKeyboardButton(text=back_label, callback_data=back_cb)],
        ]
        return InlineKeyboardMarkup(inline_keyboard=buttons)

    if field == "video_quality":
        current = val or "best"
        lbl_best = tr_text(
            {
                "tr": "🏆 En İyi (1080p+)",
                "ru": "🏆 Максимальное (1080p+)",
                "en": "🏆 Best (1080p+)",
            }
        )
        lbl_bal = tr_text(
            {
                "tr": "⚖️ Dengeli (720p)",
                "ru": "⚖️ Сбалансированное (720p)",
                "en": "⚖️ Balanced (720p)",
            }
        )
        lbl_saver = tr_text(
            {
                "tr": "⚡ Veri Tasarrufu (480p)",
                "ru": "⚡ Экономия (480p)",
                "en": "⚡ Data Saver (480p)",
            }
        )
        opt_best = f"✅ {lbl_best}" if current == "best" else lbl_best
        opt_bal = f"✅ {lbl_bal}" if current == "balanced" else lbl_bal
        opt_saver = f"✅ {lbl_saver}" if current == "saver" else lbl_saver

        buttons = [
            [
                InlineKeyboardButton(
                    text=opt_best, callback_data="setting:video_quality:best"
                )
            ],
            [
                InlineKeyboardButton(
                    text=opt_bal, callback_data="setting:video_quality:balanced"
                )
            ],
            [
                InlineKeyboardButton(
                    text=opt_saver, callback_data="setting:video_quality:saver"
                )
            ],
            [InlineKeyboardButton(text=back_label, callback_data=back_cb)],
        ]
        return InlineKeyboardMarkup(inline_keyboard=buttons)

    if field == "audio_format":
        current = val or "mp3"
        lbl_mp3 = tr_text(
            {
                "tr": "🎧 MP3 Ses",
                "ru": "🎧 MP3 Аудио",
                "en": "🎧 MP3 Audio",
            }
        )
        lbl_m4a = "📱 M4A (AAC)"
        lbl_best = tr_text(
            {
                "tr": "🎼 FLAC / Orijinal",
                "ru": "🎼 FLAC / Оригинал",
                "en": "🎼 FLAC / Original",
            }
        )
        opt_mp3 = f"✅ {lbl_mp3}" if current == "mp3" else lbl_mp3
        opt_m4a = f"✅ {lbl_m4a}" if current == "m4a" else lbl_m4a
        opt_best = f"✅ {lbl_best}" if current == "best" else lbl_best

        buttons = [
            [
                InlineKeyboardButton(
                    text=opt_mp3, callback_data="setting:audio_format:mp3"
                )
            ],
            [
                InlineKeyboardButton(
                    text=opt_m4a, callback_data="setting:audio_format:m4a"
                )
            ],
            [
                InlineKeyboardButton(
                    text=opt_best, callback_data="setting:audio_format:best"
                )
            ],
            [InlineKeyboardButton(text=back_label, callback_data=back_cb)],
        ]
        return InlineKeyboardMarkup(inline_keyboard=buttons)

    is_enabled = val == "on"
    status_text = (
        tr_text(
            {"tr": "🟢 Şu an AÇIK", "ru": "🟢 Сейчас ВКЛ", "en": "🟢 Currently ON"}
        )
        if is_enabled
        else tr_text(
            {"tr": "🔴 Şu an KAPALI", "ru": "🔴 Сейчас ВЫКЛ", "en": "🔴 Currently OFF"}
        )
    )
    next_value = "off" if is_enabled else "on"
    action_text = (
        tr_text({"tr": "🔴 Kapat", "ru": "🔴 Выключить", "en": "🔴 Turn OFF"})
        if is_enabled
        else tr_text({"tr": "🟢 Aç", "ru": "🟢 Включить", "en": "🟢 Turn ON"})
    )

    buttons = [
        [InlineKeyboardButton(text=status_text, callback_data="noop")],
        [
            InlineKeyboardButton(
                text=action_text, callback_data=f"setting:{field}:{next_value}"
            )
        ],
        [InlineKeyboardButton(text=back_label, callback_data=back_cb)],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def return_settings_keyboard():
    return return_settings_categories_keyboard()


def stats_keyboard(current_period: str = "Week", mode: str = "total"):
    period_labels = {
        "Week": tr_text({"tr": "Hafta", "ru": "Неделя", "en": "Week"}),
        "Month": tr_text({"tr": "Ay", "ru": "Месяц", "en": "Month"}),
        "Year": tr_text({"tr": "Yıl", "ru": "Год", "en": "Year"}),
    }
    periods = ["Week", "Month", "Year"]
    period_buttons = [
        InlineKeyboardButton(
            text=(
                f"[{period_labels[period]}]"
                if period == current_period
                else period_labels[period]
            ),
            callback_data=f"stats:{period}:{mode}",
        )
        for period in periods
    ]

    toggle_target = "split" if mode == "total" else "total"
    toggle_label = (
        tr_text(
            {
                "tr": "Görünüm: Platforma göre",
                "ru": "Вид: По платформам",
                "en": "View: By platform",
            }
        )
        if mode == "total"
        else tr_text(
            {
                "tr": "Görünüm: Genel",
                "ru": "Вид: Общий",
                "en": "View: Overall",
            }
        )
    )

    buttons = [
        period_buttons,
        [
            InlineKeyboardButton(
                text=toggle_label,
                callback_data=f"stats:{current_period}:{toggle_target}",
            )
        ],
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)


def admin_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text="🩺 Health", callback_data="admin_ops"),
            InlineKeyboardButton(
                text="📦 Runtime", callback_data="admin_runtime_storage"
            ),
        ],
        [InlineKeyboardButton(text="🔄 Refresh", callback_data="admin_refresh")],
        [
            InlineKeyboardButton(
                text="👥 Check Active Users", callback_data="check_active_users"
            ),
            InlineKeyboardButton(
                text="🏘 Check Groups", callback_data="check_active_groups"
            ),
        ],
        [
            InlineKeyboardButton(
                text="📥 Download History", callback_data="admin_download_history"
            )
        ],
        [InlineKeyboardButton(text="📬 Mailing", callback_data="send_to_all")],
        [
            InlineKeyboardButton(text="📄 View Log", callback_data="download_log"),
            InlineKeyboardButton(text="🗑️ Delete Log", callback_data="delete_log"),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def admin_detail_keyboard(refresh_callback: str):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔄 Refresh", callback_data=refresh_callback)],
            [InlineKeyboardButton(text="⬅️ Back", callback_data="back_to_admin")],
        ]
    )


def downloads_admin_keyboard(
    can_cleanup: bool = True, refresh_callback: str = "admin_downloads"
):
    buttons = [
        [InlineKeyboardButton(text="🔄 Refresh", callback_data=refresh_callback)]
    ]
    if can_cleanup:
        buttons.append(
            [
                InlineKeyboardButton(
                    text="🧹 Clean downloads", callback_data="admin_cleanup_downloads"
                )
            ]
        )
    buttons.append([InlineKeyboardButton(text="⬅️ Back", callback_data="back_to_admin")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def return_back_to_admin_keyboard():
    back_button = [[InlineKeyboardButton(text="⬅️ Back", callback_data="back_to_admin")]]
    return InlineKeyboardMarkup(inline_keyboard=back_button)


def return_back_to_history_keyboard() -> InlineKeyboardMarkup:
    back_button = [[InlineKeyboardButton(text="⬅️ Back", callback_data="admin_download_history")]]
    return InlineKeyboardMarkup(inline_keyboard=back_button)


def start_private_chat_keyboard(bot_username: str):
    url = f"https://t.me/{bot_username}?start=from_group"
    button = [
        [
            InlineKeyboardButton(
                text=tr_text(
                    {
                        "tr": "💬 Bot sohbetini aç",
                        "ru": "💬 Открыть чат с ботом",
                        "en": "💬 Open bot chat",
                    }
                ),
                url=url,
            )
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=button)


def return_audio_download_keyboard(platform, url):
    audio_button = [
        [
            InlineKeyboardButton(
                text=tr_text(
                    {
                        "tr": "🎧 MP3 İndir",
                        "ru": "🎧 Скачать MP3",
                        "en": "🎧 Download MP3",
                    }
                ),
                callback_data=f"{platform}_audio_{url}",
            )
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=audio_button)


def inline_send_video_keyboard(token: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=tr_text(
                        {
                            "tr": "Videoyu inline gönder",
                            "ru": "Отправить видео",
                            "en": "Send video inline",
                        }
                    ),
                    callback_data=f"inline:tiktok:{token}",
                )
            ]
        ]
    )


def inline_send_media_keyboard(text: str, callback_data: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=text, callback_data=callback_data)]]
    )


def return_user_info_keyboard(nickname, followers, videos, likes, url):
    builder = InlineKeyboardBuilder()

    builder.row(InlineKeyboardButton(text=nickname, url=url))

    row1 = []
    if followers is not None:
        row1.append(
            InlineKeyboardButton(
                text=f"👥 {format_number(followers)}",
                callback_data=f"followers_{format_number(followers)}",
            )
        )
    if videos is not None:
        row1.append(
            InlineKeyboardButton(
                text=f"🎬 {format_number(videos)}",
                callback_data=f"videos_{format_number(videos)}",
            )
        )
    if likes is not None:
        row1.append(
            InlineKeyboardButton(
                text=f"❤️ {format_number(likes)}",
                callback_data=f"likes_{format_number(likes)}",
            )
        )

    if row1:
        builder.row(*row1)

    return builder.as_markup()


def return_video_info_keyboard(
    views,
    likes,
    comments,
    shares,
    music_play_url,
    video_url,
    user_settings,
    audio_callback_data: str | None = None,
    file_callback_data: str | None = None,
):
    builder = InlineKeyboardBuilder()

    if user_settings["info_buttons"] == "on":
        row1 = []
        if views is not None:
            formatted_views = format_number(views)
            row1.append(
                InlineKeyboardButton(
                    text=f"👁 {formatted_views}",
                    callback_data=f"views_{formatted_views}",
                )
            )
        if likes is not None:
            formatted_likes = format_number(likes)
            row1.append(
                InlineKeyboardButton(
                    text=f"❤️ {formatted_likes}",
                    callback_data=f"likes_{formatted_likes}",
                )
            )
        if comments is not None:
            formatted_comments = format_number(comments)
            row1.append(
                InlineKeyboardButton(
                    text=f"💬 {formatted_comments}",
                    callback_data=f"comments_{formatted_comments}",
                )
            )
        if shares is not None:
            formatted_shares = format_number(shares)
            row1.append(
                InlineKeyboardButton(
                    text=f"🔁 {formatted_shares}",
                    callback_data=f"shares_{formatted_shares}",
                )
            )

        if row1:
            builder.row(*row1)

    if user_settings.get("audio_button") == "on" and audio_callback_data:
        builder.row(
            InlineKeyboardButton(
                text=tr_text(
                    {
                        "tr": "🎧 MP3 İndir",
                        "ru": "🎧 Скачать MP3",
                        "en": "🎧 Download MP3",
                    }
                ),
                callback_data=audio_callback_data,
            )
        )

    if (
        user_settings.get("file_button") == "on"
        and user_settings.get("as_document") != "on"
        and file_callback_data
    ):
        builder.row(
            InlineKeyboardButton(
                text=tr_text(
                    {
                        "tr": "📄 Dosya İndir",
                        "ru": "📄 Скачать файл",
                        "en": "📄 Download File",
                    }
                ),
                callback_data=file_callback_data,
            )
        )

    if user_settings["url_button"] == "on" and video_url:
        builder.row(InlineKeyboardButton(text="🔗 URL", url=video_url))

    return builder.as_markup()


def _stats_keyboard_legacy_bottom(current_period: str = "Week", mode: str = "total"):
    periods = ["Week", "Month", "Year"]
    period_buttons = [
        InlineKeyboardButton(
            text=f"{'· ' if period == current_period else ''}{period}",
            callback_data=f"stats:{period}:{mode}",
        )
        for period in periods
    ]

    toggle_target = "split" if mode == "total" else "total"
    toggle_label = f"Split view: {'On' if mode == 'split' else 'Off'}"

    buttons = [
        period_buttons,
        [
            InlineKeyboardButton(
                text=toggle_label,
                callback_data=f"stats:{current_period}:{toggle_target}",
            )
        ],
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)


def guest_help_keyboard(bot_username: str | None = None) -> InlineKeyboardMarkup:
    username = bot_username or "MaxLoadBot"
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=tr_text(
                        {
                            "tr": "💬 Botta Aç (DM)",
                            "ru": "💬 Открыть в боте (ЛС)",
                            "en": "💬 Open in Bot (DM)",
                        }
                    ),
                    url=f"https://t.me/{username}",
                ),
                InlineKeyboardButton(
                    text=tr_text(
                        {
                            "tr": "➕ Gruba Ekle",
                            "ru": "➕ Добавить в группу",
                            "en": "➕ Add to Group",
                        }
                    ),
                    url=f"https://t.me/{username}?startgroup=true",
                ),
            ]
        ]
    )
