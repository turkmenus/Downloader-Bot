from __future__ import annotations

import html as _html

from services.i18n import tr_text


def cancel():
    return tr_text({"tr": "✖️ İptal", "ru": "✖️ Отмена", "en": "✖️ Cancel"})


def welcome_message():
    return tr_text(
        {
            "tr": (
                '<b>MaxLoad\'a Hoş Geldiniz <tg-emoji emoji-id="5420141555233071341">❤️</tg-emoji></b>\n\n'
                "Tek bir bağlantı gönderin ya da aynı mesaja birden fazla bağlantı yapıştırın; indirebildiklerimi hemen göndereyim.\n\n"
                "<b>Desteklenen siteler</b>\n"
                '<tg-emoji emoji-id="5233671414023753035">📷</tg-emoji> Instagram\n'
                "📘 Facebook Reels\n"
                '<tg-emoji emoji-id="5370693953236539466">🧵</tg-emoji> Threads\n'
                '<tg-emoji emoji-id="5233597424622144804">🎵</tg-emoji> TikTok\n'
                '<tg-emoji emoji-id="5233311027612913110">▶️</tg-emoji> YouTube\n'
                '<tg-emoji emoji-id="5231309843435919433">🐦</tg-emoji> X / Twitter\n'
                '<tg-emoji emoji-id="5233448977667492819">🎧</tg-emoji> SoundCloud\n'
                '<tg-emoji emoji-id="5391001065418172193">🟢</tg-emoji> Spotify\n'
                '<tg-emoji emoji-id="5233210422298974231">📌</tg-emoji> Pinterest\n\n'
                "Satır içi (inline) modu denemek, ayarları düzenlemek veya botu paylaşmak için aşağıdaki butonları kullanın."
            ),
            "ru": (
                '<b>Добро пожаловать в MaxLoad <tg-emoji emoji-id="5420141555233071341">❤️</tg-emoji></b>\n\n'
                "Отправьте одну ссылку или вставьте сразу несколько в одном сообщении — я скачаю всё, что смогу.\n\n"
                "<b>Поддерживаемые сервисы</b>\n"
                '<tg-emoji emoji-id="5233671414023753035">📷</tg-emoji> Instagram\n'
                "📘 Facebook Reels\n"
                '<tg-emoji emoji-id="5370693953236539466">🧵</tg-emoji> Threads\n'
                '<tg-emoji emoji-id="5233597424622144804">🎵</tg-emoji> TikTok\n'
                '<tg-emoji emoji-id="5233311027612913110">▶️</tg-emoji> YouTube\n'
                '<tg-emoji emoji-id="5231309843435919433">🐦</tg-emoji> X / Twitter\n'
                '<tg-emoji emoji-id="5233448977667492819">🎧</tg-emoji> SoundCloud\n'
                '<tg-emoji emoji-id="5391001065418172193">🟢</tg-emoji> Spotify\n'
                '<tg-emoji emoji-id="5233210422298974231">📌</tg-emoji> Pinterest\n\n'
                "Используйте кнопки ниже, чтобы попробовать inline-режим, изменить настройки или поделиться ботом."
            ),
            "en": (
                '<b>Welcome to MaxLoad <tg-emoji emoji-id="5420141555233071341">❤️</tg-emoji></b>\n\n'
                "Send one link, or paste several links in one message, and I'll download what I can.\n\n"
                "<b>Supported sites</b>\n"
                '<tg-emoji emoji-id="5233671414023753035">📷</tg-emoji> Instagram\n'
                "📘 Facebook Reels\n"
                '<tg-emoji emoji-id="5370693953236539466">🧵</tg-emoji> Threads\n'
                '<tg-emoji emoji-id="5233597424622144804">🎵</tg-emoji> TikTok\n'
                '<tg-emoji emoji-id="5233311027612913110">▶️</tg-emoji> YouTube\n'
                '<tg-emoji emoji-id="5231309843435919433">🐦</tg-emoji> X / Twitter\n'
                '<tg-emoji emoji-id="5233448977667492819">🎧</tg-emoji> SoundCloud\n'
                '<tg-emoji emoji-id="5391001065418172193">🟢</tg-emoji> Spotify\n'
                '<tg-emoji emoji-id="5233210422298974231">📌</tg-emoji> Pinterest\n\n'
                "Use the buttons below to try inline mode, tune settings, or share the bot."
            ),
        }
    )


def settings():
    return tr_text(
        {
            "tr": (
                "<b>⚙️ Ayarlar</b>\n"
                "İndirmelerin nasıl gönderileceğini özelleştirmek için aşağıdaki butonları kullanın. "
                "Bu değişiklikler yalnızca sizin hesabınız için geçerlidir."
            ),
            "ru": (
                "<b>⚙️ Настройки</b>\n"
                "Используйте кнопки ниже, чтобы настроить отправку загрузок. "
                "Изменения применяются только к вашему аккаунту."
            ),
            "en": (
                "<b>⚙️ Settings</b>\n"
                "Use the buttons below to customize how downloads are sent. "
                "These changes apply only to your account."
            ),
        }
    )


def settings_private_only():
    return tr_text(
        {
            "tr": "Ayarlar yalnızca özel sohbette kullanılabilir. Tercihleri değiştirmek için botla DM açın.",
            "ru": "Настройки доступны только в личном чате. Откройте диалог с ботом, чтобы изменить параметры.",
            "en": "Settings are available only in private chat. Open DM with the bot to change preferences.",
        }
    )


def settings_update_failed():
    return tr_text(
        {
            "tr": "Ayarlar şu anda güncellenemedi. Lütfen daha sonra tekrar deneyin.",
            "ru": "Не удалось обновить настройки прямо сейчас. Пожалуйста, попробуйте позже.",
            "en": "Couldn't update settings right now. Please try again later.",
        }
    )


def get_field_text(field: str):
    texts = {
        "captions": {
            "tr": (
                "<b>📝 Açıklamalar</b>\n"
                "İndirilen medyada gönderi açıklamalarını gösterin veya gizleyin. "
                "Bazı kaynaklar açıklama sağlamayabilir."
            ),
            "ru": (
                "<b>📝 Описания</b>\n"
                "Показывать или скрывать подписи к постам в загруженных медиа. "
                "Некоторые источники могут не передавать описание."
            ),
            "en": (
                "<b>📝 Descriptions</b>\n"
                "Show or hide post captions in downloaded media. "
                "Some sources may not provide captions."
            ),
        },
        "delete_message": {
            "tr": (
                "<b>🗑️ Mesajları Sil</b>\n"
                "İndirme tamamlandığında gönderdiğiniz bağlantı mesajını otomatik olarak siler."
            ),
            "ru": (
                "<b>🗑️ Удаление сообщений</b>\n"
                "Автоматически удалять ваше сообщение со ссылкой после завершения загрузки."
            ),
            "en": (
                "<b>🗑️ Delete Messages</b>\n"
                "Automatically remove your link once the download is handled."
            ),
        },
        "info_buttons": {
            "tr": (
                "<b>ℹ️ Bilgi Butonları</b>\n"
                "İndirilen medyanın altındaki ek istatistik/bilgi butonlarını açıp kapatın."
            ),
            "ru": (
                "<b>ℹ️ Кнопки информации</b>\n"
                "Включить или отключить дополнительные кнопки статистики под загруженным медиа."
            ),
            "en": (
                "<b>ℹ️ Info Buttons</b>\n"
                "Toggle additional info buttons under downloaded media."
            ),
        },
        "url_button": {
            "tr": (
                "<b>🔗 URL Butonu</b>\n"
                "Orijinal gönderi bağlantısını içeren butonu gösterin veya gizleyin."
            ),
            "ru": (
                "<b>🔗 Кнопка URL</b>\n"
                "Показывать или скрывать кнопку со ссылкой на оригинальный пост."
            ),
            "en": (
                "<b>🔗 URL Button</b>\nShow or hide a button with the original post link."
            ),
        },
        "audio_button": {
            "tr": (
                "<b>🎧 MP3 Butonu</b>\n"
                "Ses mevcut olduğunda MP3 İndir butonunu açıp kapatın."
            ),
            "ru": (
                "<b>🎧 Кнопка MP3</b>\n"
                "Включить или отключить кнопку «Скачать MP3», если доступно аудио."
            ),
            "en": (
                "<b>🎧 MP3 Button</b>\n"
                "Toggle the Download MP3 button when audio is available."
            ),
        },
        "file_button": {
            "tr": (
                "<b>📄 Dosya Butonu</b>\n"
                "Videoları sıkıştırılmamış dosya olarak almak için Dosya İndir butonunu gösterin veya gizleyin."
            ),
            "ru": (
                "<b>📄 Кнопка файла</b>\n"
                "Показывать или скрывать кнопку «Скачать файл» под видео для получения оригинала без сжатия."
            ),
            "en": (
                "<b>📄 File Button</b>\n"
                "Show or hide the Download File button under videos to get original uncompressed files on demand."
            ),
        },
        "video_quality": {
            "tr": (
                "<b>🎬 Video Kalitesi</b>\n"
                "Tercih ettiğiniz video indirme çözünürlüğünü seçin:\n\n"
                "• <b>En İyi (1080p+)</b>: Mümkün olan en yüksek çözünürlük.\n"
                "• <b>Dengeli (720p)</b>: Kalite ve hız arasında ideal denge.\n"
                "• <b>Veri Tasarrufu (480p)</b>: Minimum veriyle daha hızlı indirme."
            ),
            "ru": (
                "<b>🎬 Качество видео</b>\n"
                "Выберите предпочтительное разрешение загрузки видео:\n\n"
                "• <b>Максимальное (1080p+)</b>: Наивысшее доступное качество.\n"
                "• <b>Сбалансированное (720p)</b>: Оптимальный баланс скорости и качества.\n"
                "• <b>Экономия трафика (480p)</b>: Быстрая загрузка с минимальным трафиком."
            ),
            "en": (
                "<b>🎬 Video Quality</b>\n"
                "Select your preferred video download resolution:\n\n"
                "• <b>Best (1080p+)</b>: Maximum possible resolution.\n"
                "• <b>Balanced (720p)</b>: Great balance of quality and speed.\n"
                "• <b>Data Saver (480p)</b>: Faster downloads with minimal data usage."
            ),
        },
        "as_document": {
            "tr": (
                "<b>📄 Dosya Olarak Gönder</b>\n"
                "Etkinleştirildiğinde videolar ve fotoğraflar %100 orijinal kaliteyi koruyarak sıkıştırılmamış belge (.mp4 / .jpg) olarak gönderilir."
            ),
            "ru": (
                "<b>📄 Отправлять как файл</b>\n"
                "Когда включено, видео и фото отправляются как документы (.mp4 / .jpg) без сжатия с сохранением 100% оригинального качества."
            ),
            "en": (
                "<b>📄 Send as File</b>\n"
                "When enabled, videos and photos will be sent as uncompressed documents (.mp4 / .jpg) preserving 100% original quality."
            ),
        },
        "audio_format": {
            "tr": (
                "<b>🎵 Ses Formatı</b>\n"
                "Müzik indirmeleri için varsayılan ses formatını seçin:\n\n"
                "• <b>MP3</b>: Standart evrensel ses formatı.\n"
                "• <b>M4A (AAC)</b>: iOS ve Mac için yüksek kaliteli kompakt format.\n"
                "• <b>FLAC / Orijinal</b>: Mevcut olduğunda kayıpsız sıkıştırılmamış ses."
            ),
            "ru": (
                "<b>🎵 Формат аудио</b>\n"
                "Выберите формат аудио по умолчанию для загрузок:\n\n"
                "• <b>MP3</b>: Стандартный универсальный формат.\n"
                "• <b>M4A (AAC)</b>: Компактный качественный формат для iOS и Mac.\n"
                "• <b>FLAC / Оригинал</b>: Аудио без потери качества, если доступно."
            ),
            "en": (
                "<b>🎵 Audio Format</b>\n"
                "Choose default audio format for music downloads:\n\n"
                "• <b>MP3</b>: Standard universal audio format.\n"
                "• <b>M4A (AAC)</b>: High quality compact format for iOS & Mac.\n"
                "• <b>FLAC / Original</b>: Uncompressed lossless audio where available."
            ),
        },
        "language": {
            "tr": (
                "<b>🌐 Dil / Язык / Language</b>\n"
                "Botun sizinle hangi dilde iletişim kuracağını seçin."
            ),
            "ru": (
                "<b>🌐 Язык / Dil / Language</b>\n"
                "Выберите язык интерфейса бота."
            ),
            "en": (
                "<b>🌐 Language / Dil / Язык</b>\n"
                "Choose the language the bot uses to communicate with you."
            ),
        },
    }
    if field in texts:
        return tr_text(texts[field])
    return tr_text(
        {
            "tr": "<b>Ayarlar</b>\nBu seçenek için henüz açıklama yok.",
            "ru": "<b>Настройки</b>\nДля этого параметра пока нет описания.",
            "en": "<b>Settings</b>\nThis option doesn't have a description yet.",
        }
    )


def captions(user_captions, post_caption, bot_url, *, limit: int = 1024):
    def _truncate_escaped(value: str, max_len: int) -> str:
        if max_len <= 0:
            return ""
        if len(value) <= max_len:
            return value
        cut = value[:max_len]
        amp = cut.rfind("&")
        semi = cut.rfind(";")
        if amp > semi:
            cut = cut[:amp]
        return cut

    footer_template = tr_text(
        {
            "tr": '<tg-emoji emoji-id="5283080528818360566">🚀</tg-emoji> <a href="{bot_url}">MaxLoad</a> ile indirildi',
            "ru": '<tg-emoji emoji-id="5283080528818360566">🚀</tg-emoji> Скачано с <a href="{bot_url}">MaxLoad</a>',
            "en": '<tg-emoji emoji-id="5283080528818360566">🚀</tg-emoji> Powered by <a href="{bot_url}">MaxLoad</a>',
        }
    )
    footer = footer_template.format(bot_url=bot_url)

    if user_captions == "on" and post_caption:
        body = _html.escape(str(post_caption))
        sep = "\n\n"
        budget = limit - len(sep) - len(footer)
        if budget <= 0:
            return _truncate_escaped(footer, limit)

        if len(body) > budget:
            suffix = "…"
            body = (
                _truncate_escaped(body, max(0, budget - len(suffix))).rstrip() + suffix
            )

        return f"{body}{sep}{footer}"

    return _truncate_escaped(footer, limit)


def downloading_audio_status():
    return tr_text(
        {
            "tr": "🎧 Ses indiriliyor...",
            "ru": "🎧 Скачиваю аудио...",
            "en": "🎧 Downloading audio...",
        }
    )


def downloading_video_status():
    return tr_text(
        {
            "tr": "<tg-emoji emoji-id='5375464961822695044'>🎬</tg-emoji> Video indiriliyor...",
            "ru": "<tg-emoji emoji-id='5375464961822695044'>🎬</tg-emoji> Скачиваю видео...",
            "en": "<tg-emoji emoji-id='5375464961822695044'>🎬</tg-emoji> Downloading video...",
        }
    )


def uploading_status():
    return tr_text(
        {
            "tr": "☁️ Dosya Telegram'a yükleniyor...",
            "ru": "☁️ Загружаю файл в Telegram...",
            "en": "☁️ Uploading file to Telegram...",
        }
    )


def retrying_again_status(next_attempt: int, total_attempts: int):
    return tr_text(
        {
            "tr": f"Hata oluştu, yeniden deneniyor... ({next_attempt}/{total_attempts})",
            "ru": f"Ошибка, пробую снова... ({next_attempt}/{total_attempts})",
            "en": f"Error, trying again... ({next_attempt}/{total_attempts})",
        }
    )


def dm_start_required():
    return tr_text(
        {
            "tr": "<tg-emoji emoji-id='5472308992514464048'>🔒</tg-emoji> İlk kurulum gerekli: DM'i açıp Başlat'a basın ve bağlantıyı tekrar gönderin.",
            "ru": "<tg-emoji emoji-id='5472308992514464048'>🔒</tg-emoji> Требуется первичная настройка: откройте ЛС, нажмите Start и отправьте ссылку снова.",
            "en": "<tg-emoji emoji-id='5472308992514464048'>🔒</tg-emoji> First-time setup needed: open DM, press Start, and resend the link.",
        }
    )


def duplicate_link_processing():
    return tr_text(
        {
            "tr": "Bu bağlantı zaten işleniyor. Lütfen birkaç saniye bekleyin.",
            "ru": "Эта ссылка уже обрабатывается. Подождите несколько секунд.",
            "en": "This link is already being processed. Wait a few seconds.",
        }
    )


def duplicate_link_recently_processed():
    return tr_text(
        {
            "tr": "Bu bağlantı az önce işlendi. Hâlâ ihtiyacınız varsa birkaç saniye sonra tekrar deneyin.",
            "ru": "Эта ссылка только что была обработана. Если она всё ещё нужна, попробуйте снова через несколько секунд.",
            "en": "This link was just handled. If you still need it, try again in a few seconds.",
        }
    )


def settings_admin_only():
    return tr_text(
        {
            "tr": "Grup sohbetlerinde /settings komutunu yalnızca grup yöneticileri açabilir.",
            "ru": "В групповых чатах открывать /settings могут только администраторы группы.",
            "en": "Only group admins can open /settings in group chats.",
        }
    )


def invalid_settings_option():
    return tr_text(
        {
            "tr": "Geçersiz ayar seçeneği.",
            "ru": "Недопустимый параметр настройки.",
            "en": "Invalid settings option.",
        }
    )


def join_group(chat_title: str) -> str:
    return tr_text(
        {
            "tr": (
                "Beni <b>{chat_title}</b> grubuna eklediğiniz için teşekkürler <tg-emoji emoji-id='5280764381804650651'>🌸</tg-emoji>\n"
                "Tüm özellikleri kullanabilmek için lütfen bana <b>yönetici yetkisi</b> verin 🔓"
            ),
            "ru": (
                "Спасибо, что добавили меня в <b>{chat_title}</b> <tg-emoji emoji-id='5280764381804650651'>🌸</tg-emoji>\n"
                "Пожалуйста, выдайте мне <b>права администратора</b>, чтобы разблокировать все функции 🔓"
            ),
            "en": (
                "Thanks for adding me to <b>{chat_title}</b> <tg-emoji emoji-id='5280764381804650651'>🌸</tg-emoji>\n"
                "Please grant me <b>admin rights</b> to unlock full functionality 🔓"
            ),
        }
    ).format(chat_title=chat_title)


def admin_rights_granted(chat_title: str) -> str:
    return tr_text(
        {
            "tr": (
                "<b>{chat_title}</b> grubunda yönetici yetkisi verdiğiniz için teşekkürler <tg-emoji emoji-id='5280764381804650651'>🌸</tg-emoji>\n"
                "💻 İndirmelerin sorunsuz devam etmesini sağlayacağım."
            ),
            "ru": (
                "Спасибо за права администратора в <b>{chat_title}</b> <tg-emoji emoji-id='5280764381804650651'>🌸</tg-emoji>\n"
                "💻 Я обеспечу стабильную работу загрузок."
            ),
            "en": (
                "Thanks for granting admin rights in <b>{chat_title}</b> <tg-emoji emoji-id='5280764381804650651'>🌸</tg-emoji>\n"
                "💻 I'll keep downloads running smoothly."
            ),
        }
    ).format(chat_title=chat_title)


def keyboard_removed():
    return tr_text(
        {
            "tr": "Klavye kaldırıldı.",
            "ru": "Клавиатура скрыта.",
            "en": "Reply keyboard removed.",
        }
    )


def tiktok_live_not_supported():
    return tr_text(
        {
            "tr": "TikTok CANLI yayınları henüz desteklenmiyor. Normal bir TikTok gönderi bağlantısı gönderin.",
            "ru": "Прямые эфиры (LIVE) TikTok пока не поддерживаются. Отправьте ссылку на обычный пост TikTok.",
            "en": "TikTok LIVE streams aren't supported yet. Send a regular TikTok post link.",
        }
    )


def delete_permission_warning():
    return tr_text(
        {
            "tr": "Otomatik silme başarısız: Bu sohbette mesaj silme iznim yok. Lütfen silme izni verin veya ayarlardan otomatik silmeyi kapatın.",
            "ru": "Не удалось автоматически удалить сообщение: нет прав на удаление в этом чате. Выдайте права или отключите автоудаление в настройках.",
            "en": "Auto-delete failed: missing permission to delete messages in this chat. Please grant delete permissions or turn off auto-delete in settings.",
        }
    )


def stats_temporarily_unavailable():
    return tr_text(
        {
            "tr": "İstatistikler şu anda oluşturulamadı. Lütfen daha sonra tekrar deneyin.",
            "ru": "Не удалось сформировать статистику прямо сейчас. Пожалуйста, попробуйте позже.",
            "en": "Couldn't generate stats right now. Please try again later.",
        }
    )


def no_queue_metrics_yet():
    return tr_text(
        {
            "tr": "Henüz kuyruk metriği yok.",
            "ru": "Пока нет метрик очереди.",
            "en": "No queue metrics yet.",
        }
    )


def open_bot_for_audio():
    return tr_text(
        {
            "tr": "Ses indirmek için botu özel sohbette açın.",
            "ru": "Откройте бота в личном чате, чтобы скачать аудио.",
            "en": "Open the bot in private chat to download audio.",
        }
    )


def audio_fetch_failed():
    return tr_text(
        {
            "tr": "Ses bilgisi alınamadı. Lütfen daha sonra tekrar deneyin.",
            "ru": "Не удалось получить информацию об аудио. Попробуйте позже.",
            "en": "Failed to get audio info. Please try again later.",
        }
    )


def audio_download_failed():
    return tr_text(
        {
            "tr": "Ses indirme başarısız oldu. Lütfen daha sonra tekrar deneyin.",
            "ru": "Не удалось скачать аудио. Пожалуйста, попробуйте позже.",
            "en": "Audio download failed. Please try again later.",
        }
    )


def spotify_metadata_failed():
    return tr_text(
        {
            "tr": "Bu Spotify parçası okunamadı. Bağlantıyı kontrol edip tekrar deneyin.",
            "ru": "Не удалось прочитать этот трек Spotify. Проверьте ссылку и попробуйте снова.",
            "en": "Couldn't read this Spotify track. Please check the link and try again.",
        }
    )


def spotify_source_not_found():
    return tr_text(
        {
            "tr": "Bu Spotify parçası için uygun ses kaynağı bulunamadı.",
            "ru": "Не удалось найти подходящий источник аудио для этого трека Spotify.",
            "en": "Couldn't find a matching audio source for this Spotify track.",
        }
    )


def inline_album_link_invalid():
    return tr_text(
        {
            "tr": "Bu albüm bağlantısının süresi dolmuş veya geçersiz.",
            "ru": "Эта ссылка на альбом устарела или недействительна.",
            "en": "This album link is expired or invalid.",
        }
    )


def inline_photo_title(service_name: str):
    return tr_text(
        {
            "tr": f"{service_name} Fotoğraf",
            "ru": f"{service_name} Фото",
            "en": f"{service_name} Photo",
        }
    )


def inline_photo_description():
    return tr_text(
        {
            "tr": "Tek fotoğraf",
            "ru": "Одно фото",
            "en": "Single photo",
        }
    )


def inline_album_title(service_name: str):
    return tr_text(
        {
            "tr": f"{service_name} Albüm",
            "ru": f"{service_name} Альбом",
            "en": f"{service_name} Album",
        }
    )


def inline_album_description():
    return tr_text(
        {
            "tr": "Albümün tamamını botta aç",
            "ru": "Открыть весь альбом в боте",
            "en": "Open full album in bot",
        }
    )


def inline_open_full_album_button():
    return tr_text(
        {
            "tr": "Albümün Tamamını Aç",
            "ru": "Открыть весь альбом",
            "en": "Open Full Album",
        }
    )


def inline_photos_title(service_name: str):
    return tr_text(
        {
            "tr": f"{service_name} Fotoğraflar",
            "ru": f"{service_name} Фото",
            "en": f"{service_name} Photos",
        }
    )


def inline_photos_not_supported(service_name: str):
    return tr_text(
        {
            "tr": f"{service_name} fotoğrafları inline modda desteklenmiyor.",
            "ru": f"Фото {service_name} не поддерживаются в inline-режиме.",
            "en": f"{service_name} photos are not supported inline.",
        }
    )


def inline_send_video_button():
    return tr_text(
        {
            "tr": "Videoyu inline gönder",
            "ru": "Отправить видео",
            "en": "Send video inline",
        }
    )


def inline_send_photo_button():
    return tr_text(
        {
            "tr": "Fotoğrafı inline gönder",
            "ru": "Отправить фото",
            "en": "Send photo inline",
        }
    )


def inline_send_audio_button():
    return tr_text(
        {
            "tr": "Sesi inline gönder",
            "ru": "Отправить аудио",
            "en": "Send audio inline",
        }
    )


def inline_mode_only():
    return tr_text(
        {
            "tr": "Bu buton yalnızca inline modda çalışır.",
            "ru": "Эта кнопка работает только в inline-режиме.",
            "en": "This button works only in inline mode.",
        }
    )


def inline_open_in_bot_desc():
    return tr_text(
        {
            "tr": "Bu sonucu botta aç.",
            "ru": "Открыть этот результат в боте.",
            "en": "Open this result in the bot.",
        }
    )


def inline_press_to_send_video():
    return tr_text(
        {
            "tr": "Bu videoyu inline göndermek için butona basın.",
            "ru": "Нажмите кнопку, чтобы отправить это видео.",
            "en": "Press the button to send this video inline.",
        }
    )


def inline_press_to_send_photo():
    return tr_text(
        {
            "tr": "Bu fotoğrafı inline göndermek için butona basın.",
            "ru": "Нажмите кнопку, чтобы отправить это фото.",
            "en": "Press the button to send this photo inline.",
        }
    )


def inline_press_to_send_audio():
    return tr_text(
        {
            "tr": "Bu sesi inline göndermek için butona basın.",
            "ru": "Нажмите кнопку, чтобы отправить это аудио.",
            "en": "Press the button to send this audio inline.",
        }
    )


def inline_text_post_desc(service_name: str):
    return tr_text(
        {
            "tr": f"{service_name} metin gönderisi.",
            "ru": f"Текстовый пост из {service_name}.",
            "en": f"Text post from {service_name}.",
        }
    )


def inline_single_videos_only_desc():
    return tr_text(
        {
            "tr": "Inline modda yalnızca tekil videolar desteklenir.",
            "ru": "В inline-режиме поддерживаются только одиночные видео.",
            "en": "Only single videos are supported inline.",
        }
    )


def inline_single_videos_only_text(service_name: str):
    return tr_text(
        {
            "tr": f"Inline modda yalnızca tekil {service_name} videoları desteklenir.",
            "ru": f"В inline-режиме поддерживаются только одиночные видео {service_name}.",
            "en": f"Only single {service_name} videos are supported inline.",
        }
    )


def inline_send_video_prompt(service_name: str):
    return tr_text(
        {
            "tr": f"{service_name} videosu hazırlanıyor...\nOtomatik başlamazsa aşağıdaki butona dokunun.",
            "ru": f"Видео {service_name} подготавливается...\nЕсли отправка не начнётся автоматически, нажмите кнопку ниже.",
            "en": f"{service_name} video is being prepared...\nIf it does not start automatically, tap the button below.",
        }
    )


def inline_send_photo_prompt(service_name: str):
    return tr_text(
        {
            "tr": f"{service_name} fotoğrafı hazırlanıyor...\nOtomatik başlamazsa aşağıdaki butona dokunun.",
            "ru": f"Фото {service_name} подготавливается...\nЕсли отправка не начнётся автоматически, нажмите кнопку ниже.",
            "en": f"{service_name} photo is being prepared...\nIf it does not start automatically, tap the button below.",
        }
    )


def inline_send_audio_prompt(service_name: str):
    return tr_text(
        {
            "tr": f"{service_name} sesi hazırlanıyor...\nOtomatik başlamazsa aşağıdaki butona dokunun.",
            "ru": f"Аудио {service_name} подготавливается...\nЕсли отправка не начнётся автоматически, нажмите кнопку ниже.",
            "en": f"{service_name} audio is being prepared...\nIf it does not start automatically, tap the button below.",
        }
    )


def inline_video_already_processing():
    return tr_text(
        {
            "tr": "Bu inline video zaten hazırlanıyor.",
            "ru": "Это inline-видео уже подготавливается.",
            "en": "This inline video is already being prepared.",
        }
    )


def inline_video_already_sent():
    return tr_text(
        {
            "tr": "Bu inline video zaten gönderildi.",
            "ru": "Это inline-видео уже отправлено.",
            "en": "This inline video was already sent.",
        }
    )


def supported_sites_message(bot_username: str | None = None):
    return help_message(bot_username)


def category_settings_text(category: str) -> str:
    if category == "media":
        return tr_text(
            {
                "tr": (
                    "<b>🎬 Medya ve Kalite Ayarları</b>\n\n"
                    "Video çözünürlüğü, dosya formatı ve ses seçeneklerini yapılandırın:"
                ),
                "ru": (
                    "<b>🎬 Настройки медиа и качества</b>\n\n"
                    "Настройте разрешение видео, формат файлов и параметры аудио:"
                ),
                "en": (
                    "<b>🎬 Media & Quality Settings</b>\n\n"
                    "Configure video resolution, file format, and audio options:"
                ),
            }
        )
    if category == "appearance":
        return tr_text(
            {
                "tr": (
                    "<b>🎨 Görünüm ve Butonlar</b>\n\n"
                    "Gönderi açıklamalarını, orijinal bağlantı butonunu ve eylem butonlarını özelleştirin:"
                ),
                "ru": (
                    "<b>🎨 Внешний вид и кнопки</b>\n\n"
                    "Настройте описания постов, кнопку ссылки и дополнительные кнопки действий:"
                ),
                "en": (
                    "<b>🎨 Appearance & Buttons</b>\n\n"
                    "Customize post descriptions, original URL links, and action buttons:"
                ),
            }
        )
    if category == "chat":
        return tr_text(
            {
                "tr": (
                    "<b>💬 Sohbet ve Temizlik</b>\n\n"
                    "Grup sohbet davranışını ve otomatik mesaj temizliğini yönetin:"
                ),
                "ru": (
                    "<b>💬 Чат и очистка</b>\n\n"
                    "Управляйте поведением в группах и автоматической очисткой сообщений:"
                ),
                "en": (
                    "<b>💬 Chat & Clean-up</b>\n\n"
                    "Manage group chat behavior and message cleanup settings:"
                ),
            }
        )
    return settings()


def help_message(bot_username: str | None = None) -> str:
    username = bot_username or "MaxLoadBot"
    return tr_text(
        {
            "tr": (
                "<b>📖 MaxLoad Yardım ve Rehber</b>\n\n"
                "Tek bir bağlantı gönderin veya tek mesaja birden fazla bağlantı yapıştırın. Bot medyayı otomatik olarak çıkarıp gönderir.\n\n"
                "<blockquote expandable><b>📷 Instagram, Facebook & Threads</b>\n"
                "• Gönderi, Reels, IGTV ve Hikaye indirme\n"
                "• Facebook Reels, Watch ve fb.watch videoları\n"
                "• Çoklu fotoğraf ve medya albümleri\n"
                "• Paylaş → Bağlantıyı kopyala ile gönderin</blockquote>\n\n"
                "<blockquote expandable><b>🎵 TikTok</b>\n"
                "• Filigransız video indirme\n"
                "• Fotoğraf slaytları ve albümler\n"
                "• MP3 ses çıkarma desteği</blockquote>\n\n"
                "<blockquote expandable><b>▶️ YouTube & YouTube Music</b>\n"
                "• YouTube Shorts ve normal videolar\n"
                "• Yüksek kaliteli ses ve video akışları\n"
                "• Ses indirmek için MP3 butonuna dokunun</blockquote>\n\n"
                "<blockquote expandable><b>🐦 X / Twitter & 📌 Pinterest</b>\n"
                "• X / Twitter videoları, GIF'ler ve görseller\n"
                "• Pinterest video ve görsel Pin'leri</blockquote>\n\n"
                "<blockquote expandable><b>🎧 SoundCloud & 🟢 Spotify</b>\n"
                "• Yüksek kaliteli SoundCloud ses parçaları\n"
                "• Spotify parça eşleştirme ve ses indirme</blockquote>\n\n"
                f"<blockquote expandable><b>⚡ Satır İçi (Inline) Mod</b>\n"
                f"• Herhangi bir sohbette <code>@{username} [bağlantı]</code> yazın\n"
                "• Anında önizleme ve doğrudan medya paylaşımı</blockquote>\n\n"
                "<blockquote expandable><b>📦 Toplu İndirme</b>\n"
                "• Tek mesajda en fazla 6 bağlantı yapıştırın\n"
                "• Sohbeti temiz tutmak için sırayla teslim edilir</blockquote>"
            ),
            "ru": (
                "<b>📖 Справка и руководство MaxLoad</b>\n\n"
                "Отправьте одну ссылку или вставьте сразу несколько в одном сообщении. Бот автоматически извлечёт и отправит медиа.\n\n"
                "<blockquote expandable><b>📷 Instagram, Facebook и Threads</b>\n"
                "• Скачивание постов, Reels, IGTV и историй\n"
                "• Видео Facebook Reels, Watch и fb.watch\n"
                "• Карусели фото и смешанные альбомы\n"
                "• Скопируйте ссылку через «Поделиться»</blockquote>\n\n"
                "<blockquote expandable><b>🎵 TikTok</b>\n"
                "• Видео без водяного знака\n"
                "• Карусели фото и слайд-шоу\n"
                "• Поддержка извлечения MP3</blockquote>\n\n"
                "<blockquote expandable><b>▶️ YouTube и YouTube Music</b>\n"
                "• YouTube Shorts и обычные видео\n"
                "• Видео и аудио высокого качества\n"
                "• Нажмите кнопку MP3 для скачивания звука</blockquote>\n\n"
                "<blockquote expandable><b>🐦 X / Twitter и 📌 Pinterest</b>\n"
                "• Видео, GIF и изображения из X / Twitter\n"
                "• Видео- и фото-пины Pinterest</blockquote>\n\n"
                "<blockquote expandable><b>🎧 SoundCloud и 🟢 Spotify</b>\n"
                "• Треки SoundCloud в высоком качестве\n"
                "• Подбор и скачивание треков Spotify</blockquote>\n\n"
                f"<blockquote expandable><b>⚡ Inline-режим</b>\n"
                f"• Введите <code>@{username} [ссылка]</code> в любом чате\n"
                "• Мгновенный предпросмотр и отправка медиа</blockquote>\n\n"
                "<blockquote expandable><b>📦 Пакетная загрузка</b>\n"
                "• Вставьте до 6 ссылок в одном сообщении\n"
                "• Загружаются по очереди, не засоряя чат</blockquote>"
            ),
            "en": (
                "<b>📖 MaxLoad Help & Guide</b>\n\n"
                "Send one link or paste multiple links in one message. The bot will automatically extract and deliver the media.\n\n"
                "<blockquote expandable><b>📷 Instagram, Facebook & Threads</b>\n"
                "• Download Posts, Reels, IGTV & Stories\n"
                "• Facebook Reels, Watch & fb.watch videos\n"
                "• Photo carousels & multi-media albums\n"
                "• Copy link via Share → Copy link</blockquote>\n\n"
                "<blockquote expandable><b>🎵 TikTok</b>\n"
                "• Watermark-free video downloads\n"
                "• Photo carousels & slideshows\n"
                "• MP3 audio extraction supported</blockquote>\n\n"
                "<blockquote expandable><b>▶️ YouTube & YouTube Music</b>\n"
                "• YouTube Shorts & regular Videos\n"
                "• High quality audio & video streams\n"
                "• Tap MP3 button to download audio</blockquote>\n\n"
                "<blockquote expandable><b>🐦 X / Twitter & 📌 Pinterest</b>\n"
                "• X / Twitter videos, GIFs & images\n"
                "• Pinterest video and image Pins</blockquote>\n\n"
                "<blockquote expandable><b>🎧 SoundCloud & 🟢 Spotify</b>\n"
                "• High quality SoundCloud audio tracks\n"
                "• Spotify track matching & audio download</blockquote>\n\n"
                f"<blockquote expandable><b>⚡ Inline Mode</b>\n"
                f"• Type <code>@{username} [link]</code> in any chat\n"
                "• Instant preview and direct media sharing</blockquote>\n\n"
                "<blockquote expandable><b>📦 Batch Downloading</b>\n"
                "• Paste up to 6 links in a single message\n"
                "• Delivered one by one to keep chat clean</blockquote>"
            ),
        }
    )


def referral_message(bot_username: str, user_id: int, invited_count: int) -> str:
    username = bot_username or "MaxLoadBot"
    ref_link = f"https://t.me/{username}?start=ref_{user_id}"
    return tr_text(
        {
            "tr": (
                "<b>👥 Davet Programınız</b>\n\n"
                "Arkadaşlarınızı MaxLoad kullanmaya davet edin! Kişisel davet bağlantınızı paylaşın:\n"
                f"<code>{ref_link}</code>\n\n"
                f"Davet edilen kullanıcılar: <b>{invited_count}</b>"
            ),
            "ru": (
                "<b>👥 Ваша реферальная программа</b>\n\n"
                "Приглашайте друзей в MaxLoad! Поделитесь своей персональной ссылкой:\n"
                f"<code>{ref_link}</code>\n\n"
                f"Приглашено пользователей: <b>{invited_count}</b>"
            ),
            "en": (
                "<b>👥 Your Referral Program</b>\n\n"
                "Invite friends to use MaxLoad! Share your personal referral link:\n"
                f"<code>{ref_link}</code>\n\n"
                f"Users invited: <b>{invited_count}</b>"
            ),
        }
    )


def batch_links_started(processed_total: int, detected_total: int | None = None):
    if detected_total is not None and detected_total > processed_total:
        return tr_text(
            {
                "tr": f"{detected_total} desteklenen bağlantı bulundu. Sohbetin düzenli kalması için ilk {processed_total} tanesini sırayla işleyeceğim.",
                "ru": f"Найдено {detected_total} поддерживаемых ссылок. Чтобы не засорять чат, обработаю первые {processed_total} по очереди.",
                "en": f"Found {detected_total} supported links. I'll process the first {processed_total} one by one so the chat stays readable.",
            }
        )
    return tr_text(
        {
            "tr": f"{processed_total} desteklenen bağlantı bulundu. Sohbetin düzenli kalması için sırayla işleyeceğim.",
            "ru": f"Найдено {processed_total} поддерживаемых ссылок. Обработаю их по очереди, чтобы чат оставался чистым.",
            "en": f"Found {processed_total} supported links. I'll process them one by one so the chat stays readable.",
        }
    )


def batch_link_progress(current: int, total: int, service_name: str):
    return tr_text(
        {
            "tr": f"Bağlantı işleniyor {current}/{total}: {service_name}...",
            "ru": f"Обработка ссылки {current}/{total}: {service_name}...",
            "en": f"Processing link {current}/{total}: {service_name}...",
        }
    )


def batch_links_finished(total: int):
    return tr_text(
        {
            "tr": f"{total} bağlantı için toplu indirme tamamlandı.",
            "ru": f"Пакетная обработка {total} ссылок завершена.",
            "en": f"Finished batch processing for {total} links.",
        }
    )


def timeout_error():
    return tr_text(
        {
            "tr": "İstek zaman aşımına uğradı. Kaynak şu anda yavaş olabilir. Lütfen daha sonra tekrar deneyin.",
            "ru": "Время ожидания истекло. Источник сейчас может отвечать медленно. Пожалуйста, попробуйте позже.",
            "en": "Request timed out. The source may be slow right now. Please try again later.",
        }
    )


def something_went_wrong():
    return tr_text(
        {
            "tr": (
                "Bu bağlantı şu anda işlenemedi.\n"
                "Gönderi gizli, silinmiş, bölge kısıtlı veya kaynak tarafından geçici olarak engellenmiş olabilir. "
                "Lütfen daha sonra tekrar deneyin."
            ),
            "ru": (
                "Сейчас не удалось обработать эту ссылку.\n"
                "Возможно, публикация скрыта, удалена, ограничена по региону или временно заблокирована источником. "
                "Пожалуйста, попробуйте позже."
            ),
            "en": (
                "Couldn't process this link right now.\n"
                "It may be private, deleted, region-limited, or temporarily blocked by the source. "
                "Please try again later."
            ),
        }
    )


def video_too_large():
    return tr_text(
        {
            "tr": "Video Telegram sınırları için çok büyük. Daha kısa bir video veya varsa MP3/ses seçeneğini deneyin.",
            "ru": "Видео слишком большое для ограничений Telegram. Попробуйте ролик покороче или скачайте только аудио (MP3).",
            "en": "The video is too large for Telegram. Try a shorter video or an MP3/audio option if available.",
        }
    )


def audio_too_large():
    return tr_text(
        {
            "tr": "Ses dosyası Telegram sınırları için çok büyük. Daha kısa bir parça veya başka bir kaynak deneyin.",
            "ru": "Аудиофайл слишком большой для Telegram. Попробуйте трек покороче или другой источник.",
            "en": "The audio is too large for Telegram. Try a shorter track or another source link.",
        }
    )


def nothing_found():
    return tr_text(
        {
            "tr": "Medya bulunamadı. Bağlantının herkese açık olduğundan, süresinin dolmadığından ve doğrudan bir gönderiye işaret ettiğinden emin olun.",
            "ru": "Медиа не найдено. Проверьте, что ссылка публичная, не устарела и ведёт напрямую на пост или видео.",
            "en": "No media found. Check that the link is public, not expired, and points directly to a post or video.",
        }
    )


def guest_help_message(bot_username: str) -> str:
    return tr_text(
        {
            "tr": (
                "👋 <b>MaxLoad — Misafir Modu</b>\n\n"
                "Bu sohbette botu etiketlediniz! Medya indirmek için beni desteklenen bir platform bağlantısıyla etiketleyin:\n\n"
                "• <b>TikTok</b> (videolar, fotoğraflar)\n"
                "• <b>Instagram, Facebook & Threads</b> (reels, fotoğraflar)\n"
                "• <b>YouTube</b> (videolar, müzik)\n"
                "• <b>Twitter / X</b> (videolar, gifler)\n"
                "• <b>SoundCloud & Spotify</b> (müzik)\n"
                "• <b>Pinterest</b> (pinler, videolar)\n\n"
                "<i>💡 İpucu: Tüm özellikler ve ayarlar için beni bu gruba ekleyin veya @{bot_username} ile doğrudan sohbet açın!</i>"
            ),
            "ru": (
                "👋 <b>MaxLoad — Гостевой режим</b>\n\n"
                "Вы вызвали бота в этом чате! Чтобы скачать медиа, упомяните меня со ссылкой с любой поддерживаемой платформы:\n\n"
                "• <b>TikTok</b> (видео, фото)\n"
                "• <b>Instagram, Facebook и Threads</b> (reels, фото)\n"
                "• <b>YouTube</b> (видео, музыка)\n"
                "• <b>Twitter / X</b> (видео, gif)\n"
                "• <b>SoundCloud и Spotify</b> (музыка)\n"
                "• <b>Pinterest</b> (пины, видео)\n\n"
                "<i>💡 Совет: добавьте меня в эту группу или откройте личный чат с @{bot_username} для доступа ко всем функциям и настройкам!</i>"
            ),
            "en": (
                "👋 <b>MaxLoad — Guest Mode</b>\n\n"
                "You summoned the bot in this chat! To download media, mention me with a link from any supported platform:\n\n"
                "• <b>TikTok</b> (videos, photos)\n"
                "• <b>Instagram, Facebook & Threads</b> (reels, photos)\n"
                "• <b>YouTube</b> (videos, music)\n"
                "• <b>Twitter / X</b> (videos, gifs)\n"
                "• <b>SoundCloud & Spotify</b> (music)\n"
                "• <b>Pinterest</b> (pins, videos)\n\n"
                "<i>💡 Tip: Add me to this group or open a direct chat with @{bot_username} for full features and settings!</i>"
            ),
        }
    ).format(bot_username=bot_username)


def guest_downloading_status(service_name: str) -> str:
    return tr_text(
        {
            "tr": (
                "⏳ <b>{service_name} medyası hazırlanıyor...</b>\n"
                "Medya işlenirken lütfen bir saniye bekleyin."
            ),
            "ru": (
                "⏳ <b>Медиа {service_name} подготавливается...</b>\n"
                "Пожалуйста, подождите немного, идёт обработка."
            ),
            "en": (
                "⏳ <b>{service_name} media is being prepared...</b>\n"
                "Please wait a moment while the media is processed."
            ),
        }
    ).format(service_name=service_name)


def guest_unsupported_link() -> str:
    return tr_text(
        {
            "tr": (
                "Etiketlemenizde desteklenen bir medya bağlantısı bulunamadı. "
                "Lütfen TikTok, Instagram, Facebook, YouTube, X, SoundCloud, Spotify veya Pinterest bağlantısı ekleyin."
            ),
            "ru": (
                "В вашем сообщении не найдено поддерживаемой ссылки. "
                "Пожалуйста, добавьте ссылку из TikTok, Instagram, Facebook, YouTube, X, SoundCloud, Spotify или Pinterest."
            ),
            "en": (
                "Sorry, no supported media link was found in your mention. "
                "Please include a link from TikTok, Instagram, Facebook, YouTube, X, SoundCloud, Spotify, or Pinterest."
            ),
        }
    )
