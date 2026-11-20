import asyncio
import datetime
import io
import threading
import time
from collections import defaultdict
from typing import List

import matplotlib.pyplot as plt
from aiogram import types
from aiogram.exceptions import TelegramAPIError, TelegramBadRequest
from aiogram.types import BufferedInputFile, InputMediaPhoto
from matplotlib.ticker import MaxNLocator

import keyboards as kb
import messages as bm
from app_context import db
from services.i18n import get_current_language, tr_text
from services.logger import logger as logging
from services.storage.db import StatsSnapshot
from services.stats.constants import SERVICE_ORDER, SERVICE_COLORS, SERVICE_EMOJI, VALID_STATS_PERIODS, VALID_STATS_MODES

_STATS_CACHE_TTL_SECONDS = 60.0
_stats_snapshot_cache: dict[str, tuple[float, StatsSnapshot]] = {}
_stats_chart_cache: dict[tuple[str, str, str], tuple[float, bytes]] = {}
_stats_chart_warmup_tasks: dict[str, asyncio.Task[None]] = {}
_stats_render_lock = threading.Lock()


def _prepare_series(data: dict[str, int]) -> List[tuple[datetime.datetime, int]]:
    series = []
    for date_str, count in data.items():
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        series.append((dt, count))
    series.sort(key=lambda item: item[0])
    return series


def _decimate_series(
        dates: List[datetime.datetime],
        counts: List[int],
        max_points: int,
) -> tuple[list[datetime.datetime], list[int]]:
    if len(dates) <= max_points:
        return dates, counts

    step = max(1, len(dates) // max_points)
    sampled_dates = dates[::step]
    sampled_counts = counts[::step]

    if sampled_dates[-1] != dates[-1]:
        sampled_dates.append(dates[-1])
        sampled_counts.append(counts[-1])

    return sampled_dates, sampled_counts


def _prepare_series_for_period(data: dict[str, int], period: str) -> tuple[list[datetime.datetime], list[int]]:
    return _build_series_for_period(data, period)


def _shift_month(dt: datetime.datetime, months: int) -> datetime.datetime:
    month_index = (dt.year * 12 + (dt.month - 1)) + months
    year = month_index // 12
    month = (month_index % 12) + 1
    return datetime.datetime(year, month, 1)


def _build_period_axis(period: str) -> list[datetime.datetime]:
    today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    if period == "Week":
        return [today - datetime.timedelta(days=offset) for offset in range(6, -1, -1)]
    if period == "Month":
        return [today - datetime.timedelta(days=offset) for offset in range(29, -1, -1)]

    month_start = today.replace(day=1)
    return [_shift_month(month_start, -offset) for offset in range(11, -1, -1)]


def _aggregate_monthly(data: dict[str, int]) -> dict[datetime.datetime, int]:
    monthly: dict[datetime.datetime, int] = defaultdict(int)
    for date_str, count in data.items():
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        monthly[datetime.datetime(dt.year, dt.month, 1)] += count
    return monthly


def _decimate_dates(dates: list[datetime.datetime], max_points: int) -> list[datetime.datetime]:
    if len(dates) <= max_points:
        return dates
    step = max(1, len(dates) // max_points)
    sampled = dates[::step]
    if sampled[-1] != dates[-1]:
        sampled.append(dates[-1])
    return sampled


def _build_series_for_period(data: dict[str, int], period: str) -> tuple[list[datetime.datetime], list[int]]:
    axis_dates = _build_period_axis(period)
    if period == "Year":
        monthly = _aggregate_monthly(data)
        return axis_dates, [monthly.get(dt, 0) for dt in axis_dates]

    daily = {
        datetime.datetime.strptime(date_str, "%Y-%m-%d"): count for date_str, count in data.items()
    }
    return axis_dates, [daily.get(dt, 0) for dt in axis_dates]


def _format_stats_bucket(period: str, bucket: datetime.datetime) -> str:
    if period == "Year":
        return bucket.strftime("%b %Y")
    return bucket.strftime("%b %d")


def _stats_bucket_name(period: str, lang: str | None = None) -> str:
    if period == "Year":
        return tr_text({"tr": "ay", "ru": "месяц", "en": "month"}, lang)
    return tr_text({"tr": "gün", "ru": "день", "en": "day"}, lang)


def _stats_period_label(period: str, lang: str | None = None) -> str:
    labels = {
        "Week": {"tr": "Haftalık", "ru": "Неделя", "en": "Week"},
        "Month": {"tr": "Aylık", "ru": "Месяц", "en": "Month"},
        "Year": {"tr": "Yıllık", "ru": "Год", "en": "Year"},
    }
    if period in labels:
        return tr_text(labels[period], lang)
    return period


def _is_cache_fresh(timestamp: float, ttl_seconds: float = _STATS_CACHE_TTL_SECONDS) -> bool:
    return time.monotonic() - timestamp <= ttl_seconds


def _clear_chart_cache_for_period(period: str) -> None:
    stale_keys = [key for key in _stats_chart_cache if key[0] == period]
    for key in stale_keys:
        _stats_chart_cache.pop(key, None)


def _schedule_stats_chart_warmup(period: str, snapshot: StatsSnapshot) -> None:
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        return

    existing = _stats_chart_warmup_tasks.get(period)
    if existing and not existing.done():
        return

    async def _warmup() -> None:
        try:
            await asyncio.gather(
                asyncio.to_thread(render_stats_chart, snapshot, period, "total"),
                asyncio.to_thread(render_stats_chart, snapshot, period, "split"),
            )
        finally:
            _stats_chart_warmup_tasks.pop(period, None)

    _stats_chart_warmup_tasks[period] = loop.create_task(
        _warmup(),
        name=f"stats-chart-warmup-{period.lower()}",
    )


async def fetch_stats_snapshot(period: str) -> StatsSnapshot:
    cached = _stats_snapshot_cache.get(period)
    if cached and _is_cache_fresh(cached[0]):
        return cached[1]

    snapshot = await db.get_download_stats(period)
    _stats_snapshot_cache[period] = (time.monotonic(), snapshot)
    _clear_chart_cache_for_period(period)
    _schedule_stats_chart_warmup(period, snapshot)
    return snapshot


def render_stats_chart(snapshot: StatsSnapshot, period: str, mode: str, language: str | None = None) -> bytes:
    lang = language or get_current_language()
    cache_key = (period, mode, lang)
    cached = _stats_chart_cache.get(cache_key)
    if cached and _is_cache_fresh(cached[0]):
        return cached[1]

    with _stats_render_lock:
        cached = _stats_chart_cache.get(cache_key)
        if cached and _is_cache_fresh(cached[0]):
            return cached[1]

        total_dates, total_counts = _build_series_for_period(snapshot.totals_by_date, period)
        plt.style.use("dark_background")
        fig, ax = plt.subplots(figsize=(11, 6), facecolor="#08111F")
        fig.subplots_adjust(left=0.08, right=0.97, bottom=0.16, top=0.74)
        ax.set_facecolor("#0F1B2D")

        def _plot_series(
            dates: list[datetime.datetime],
            counts: list[int],
            color: str,
            label: str,
            *,
            annotate_last: bool = False,
            fill_alpha: float = 0.16,
            marker_size: int = 0,
        ) -> None:
            ax.plot(dates, counts, color=color, linewidth=2.4, label=label, solid_capstyle="round")
            if fill_alpha > 0:
                ax.fill_between(dates, counts, color=color, alpha=fill_alpha)
            if marker_size:
                ax.scatter(dates, counts, color=color, s=marker_size, zorder=3)
            if annotate_last and dates and counts:
                ax.scatter(dates[-1], counts[-1], color="#F59E0B", s=54, zorder=4)
                ax.annotate(
                    str(counts[-1]),
                    (dates[-1], counts[-1]),
                    textcoords="offset points",
                    xytext=(0, 10),
                    ha="center",
                    color="#FBBF24",
                    fontsize=10,
                    fontweight="bold",
                )

        bucket_name = _stats_bucket_name(period, lang)
        period_label = _stats_period_label(period, lang)
        peak_count = max(total_counts) if total_counts else 0
        peak_bucket = _format_stats_bucket(period, total_dates[total_counts.index(peak_count)]) if total_dates else "-"
        average_value = snapshot.total_downloads / len(total_counts) if total_counts else 0.0
        mode_label = (
            tr_text({"tr": "Genel aktivite", "ru": "Общая активность", "en": "Overall activity"}, lang)
            if mode == "total"
            else tr_text({"tr": "Platform karşılaştırması", "ru": "Сравнение платформ", "en": "Platform comparison"}, lang)
        )

        fig.text(
            0.08,
            0.92,
            tr_text({"tr": "İndirme Özeti", "ru": "Обзор загрузок", "en": "Downloads Overview"}, lang),
            color="#F8FAFC",
            fontsize=20,
            fontweight="bold",
            ha="left",
        )
        fig.text(
            0.08,
            0.875,
            f"{period_label} | {mode_label}",
            color="#94A3B8",
            fontsize=11,
            ha="left",
        )

        chip_style = dict(boxstyle="round,pad=0.45", facecolor="#0D1728", edgecolor="#22324A", linewidth=1.0)
        chip_positions = [0.66, 0.81, 0.96]
        chip_titles = [
            tr_text({"tr": "Toplam", "ru": "Всего", "en": "Total"}, lang),
            tr_text({"tr": f"Zirve {bucket_name}", "ru": f"Пик ({bucket_name})", "en": f"Peak {bucket_name}"}, lang),
            tr_text({"tr": "Ortalama", "ru": "Среднее", "en": "Average"}, lang),
        ]
        chip_values = [str(snapshot.total_downloads), f"{peak_bucket} | {peak_count}", f"{average_value:.1f} / {bucket_name}"]
        for x_pos, title, value in zip(chip_positions, chip_titles, chip_values):
            fig.text(
                x_pos,
                0.81,
                f"{title}\n{value}",
                color="#E2E8F0",
                fontsize=10.0,
                ha="right",
                va="top",
                linespacing=1.45,
                bbox=chip_style,
            )

        if mode == "split":
            plotted_any = False
            for idx, service in enumerate(SERVICE_ORDER):
                service_data = snapshot.by_service.get(service)
                if not service_data:
                    continue
                dates, counts = _build_series_for_period(service_data, period)
                if not any(counts):
                    continue
                _plot_series(
                    dates,
                    counts,
                    SERVICE_COLORS[idx % len(SERVICE_COLORS)],
                    service,
                    fill_alpha=0.08,
                )
                plotted_any = True

            if plotted_any:
                legend = ax.legend(
                    facecolor="#0D1728",
                    edgecolor="#22324A",
                    labelcolor="#F8FAFC",
                    fontsize=9,
                    ncol=2,
                    loc="upper left",
                    bbox_to_anchor=(0.0, 1.02),
                )
                legend.get_frame().set_alpha(0.95)
            else:
                _plot_series(
                    total_dates,
                    total_counts,
                    "#6C5DD3",
                    tr_text({"tr": "İndirmeler", "ru": "Загрузки", "en": "Downloads"}, lang),
                    marker_size=18,
                )
        else:
            _plot_series(
                total_dates,
                total_counts,
                "#38BDF8",
                tr_text({"tr": "İndirmeler", "ru": "Загрузки", "en": "Downloads"}, lang),
                annotate_last=True,
                marker_size=22,
                fill_alpha=0.18,
            )

        if snapshot.total_downloads <= 0:
            ax.text(
                0.5,
                0.5,
                tr_text(
                    {
                        "tr": "Bu dönem için henüz indirme yok",
                        "ru": "За этот период загрузок ещё нет",
                        "en": "No downloads yet for this period",
                    },
                    lang,
                ),
                transform=ax.transAxes,
                ha="center",
                va="center",
                color="#94A3B8",
                fontsize=14,
                bbox=dict(boxstyle="round,pad=0.6", facecolor="#0D1728", edgecolor="#22324A"),
            )

        ax.set_xlabel(tr_text({"tr": "Tarih", "ru": "Дата", "en": "Date"}, lang), fontsize=11, color="#94A3B8", labelpad=12)
        ax.set_ylabel(tr_text({"tr": "İndirmeler", "ru": "Загрузки", "en": "Downloads"}, lang), fontsize=11, color="#94A3B8", labelpad=10)
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        if total_dates:
            ax.set_xlim(total_dates[0], total_dates[-1])

        if period == "Year":
            import matplotlib.dates as mdates

            ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
            ax.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
        elif period == "Week":
            ax.set_xticks(total_dates)
            ax.set_xticklabels([dt.strftime("%a") for dt in total_dates])
        else:
            visible_dates = _decimate_dates(total_dates, 8)
            ax.set_xticks(visible_dates)
            ax.set_xticklabels([dt.strftime("%b %d") for dt in visible_dates], rotation=20, ha="right")

        ax.grid(axis="y", color="#22324A", linestyle="--", linewidth=0.8, alpha=0.75)
        ax.grid(axis="x", color="#142033", linestyle="-", linewidth=0.5, alpha=0.2)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color("#2B3B52")
        ax.spines["bottom"].set_color("#2B3B52")
        ax.tick_params(axis="x", colors="#CBD5E1", labelsize=10)
        ax.tick_params(axis="y", colors="#CBD5E1", labelsize=10)
        ax.set_ylim(bottom=0)
        ax.margins(x=0.02)

        output = io.BytesIO()
        fig.savefig(output, format="png", bbox_inches="tight", facecolor=fig.get_facecolor())
        plt.close(fig)
        chart_bytes = output.getvalue()
        _stats_chart_cache[cache_key] = (time.monotonic(), chart_bytes)
        return chart_bytes


def build_stats_caption(period: str, snapshot: StatsSnapshot, mode: str = "total", language: str | None = None) -> str:
    lang = language or get_current_language()
    period_label = _stats_period_label(period, lang)
    header = tr_text(
        {
            "tr": f"<b>{period_label} İstatistikleri</b>",
            "ru": f"<b>Статистика: {period_label}</b>",
            "en": f"<b>Statistics for {period}</b>",
        },
        lang,
    )
    if snapshot.total_downloads <= 0:
        empty_text = tr_text(
            {
                "tr": "Bu dönem için henüz indirme kaydedilmedi.",
                "ru": "За этот период загрузок ещё не зафиксировано.",
                "en": "No downloads recorded for this period yet.",
            },
            lang,
        )
        return f"{header}\n\n{empty_text}"

    dates, counts = _build_series_for_period(snapshot.totals_by_date, period)
    peak_index = max(range(len(counts)), key=counts.__getitem__)
    peak_bucket = _format_stats_bucket(period, dates[peak_index])
    peak_count = counts[peak_index]
    bucket_name = _stats_bucket_name(period, lang)
    average = snapshot.total_downloads / len(counts) if counts else 0.0

    lines = [
        header,
        "",
        tr_text(
            {
                "tr": f"Toplam indirme: <b>{snapshot.total_downloads}</b>",
                "ru": f"Всего загрузок: <b>{snapshot.total_downloads}</b>",
                "en": f"Total downloads: <b>{snapshot.total_downloads}</b>",
            },
            lang,
        ),
        tr_text(
            {
                "tr": f"En yoğun {bucket_name}: <b>{peak_bucket}</b> - <b>{peak_count}</b>",
                "ru": f"Пик за {bucket_name}: <b>{peak_bucket}</b> - <b>{peak_count}</b>",
                "en": f"Peak {bucket_name}: <b>{peak_bucket}</b> - <b>{peak_count}</b>",
            },
            lang,
        ),
        tr_text(
            {
                "tr": f"{bucket_name.capitalize()} başına ortalama: <b>{average:.1f}</b>",
                "ru": f"В среднем за {bucket_name}: <b>{average:.1f}</b>",
                "en": f"Average per {bucket_name}: <b>{average:.1f}</b>",
            },
            lang,
        ),
    ]

    if mode == "split" and snapshot.service_totals:
        top_services = sorted(
            snapshot.service_totals.items(),
            key=lambda item: (-item[1], SERVICE_ORDER.index(item[0]) if item[0] in SERVICE_ORDER else len(SERVICE_ORDER)),
        )[:3]
        if top_services:
            lines.extend(
                [
                    "",
                    tr_text(
                        {
                            "tr": "<b>En popüler platformlar</b>",
                            "ru": "<b>Топ платформ</b>",
                            "en": "<b>Top platforms</b>",
                        },
                        lang,
                    ),
                ]
            )
            for service, count in top_services:
                share = (count / snapshot.total_downloads) * 100 if snapshot.total_downloads else 0.0
                emoji = SERVICE_EMOJI.get(service, "")
                prefix = f"{emoji} " if emoji else ""
                lines.append(f"{prefix}{service}: <b>{count}</b> ({share:.0f}%)")

    return "\n".join(lines)


async def _render_stats(period: str, mode: str) -> tuple[bytes, str]:
    snapshot = await fetch_stats_snapshot(period)
    chart_bytes = await asyncio.to_thread(render_stats_chart, snapshot, period, mode)
    caption = build_stats_caption(period, snapshot, mode)
    return chart_bytes, caption


def _build_stats_photo(chart_bytes: bytes, period: str, mode: str) -> BufferedInputFile:
    return BufferedInputFile(chart_bytes, filename=f"stats_{period.lower()}_{mode}.png")


async def _send_stats_photo(target_message: types.Message, period: str, mode: str, chart_bytes: bytes, caption: str) -> None:
    await target_message.answer_photo(
        _build_stats_photo(chart_bytes, period, mode),
        caption=caption,
        parse_mode="HTML",
        reply_markup=kb.stats_keyboard(period, mode),
    )


async def _edit_stats_message(call: types.CallbackQuery, period: str, mode: str, chart_bytes: bytes, caption: str) -> None:
    media = InputMediaPhoto(
        media=_build_stats_photo(chart_bytes, period, mode),
        caption=caption,
        parse_mode="HTML",
    )
    try:
        await call.message.edit_media(media=media, reply_markup=kb.stats_keyboard(period, mode))
    except (TelegramBadRequest, TelegramAPIError) as error:
        logging.warning(
            "Stats edit_media failed; falling back to send/delete: period=%s mode=%s error=%s",
            period,
            mode,
            error,
        )
        await _send_stats_photo(call.message, period, mode, chart_bytes, caption)
        try:
            await call.message.delete()
        except TelegramAPIError:
            logging.warning("Failed to delete stale stats message after fallback")


async def _handle_stats_update(call: types.CallbackQuery, period: str, mode: str) -> None:
    if period not in VALID_STATS_PERIODS or mode not in VALID_STATS_MODES:
        await call.answer()
        return

    try:
        chart_bytes, caption = await _render_stats(period, mode)
        await _edit_stats_message(call, period, mode, chart_bytes, caption)
        await call.answer()
    except Exception:
        logging.exception("Error updating /stats: period=%s mode=%s", period, mode)
        await call.answer(bm.stats_temporarily_unavailable(), show_alert=True)
