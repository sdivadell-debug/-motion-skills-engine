"""Channel-normalized competitor video outlier analysis.

Input data must be collected from a documented source. This module does not
scrape YouTube or claim that sample metrics are live.
"""
from __future__ import annotations

from collections import defaultdict
from datetime import date
import math
from statistics import median
from typing import Any


REQUIRED_VIDEO_FIELDS = ("video_id", "channel_id", "views", "source_url", "retrieved_at")


def _positive_int(value: Any, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{field} must be a non-negative integer")
    return value


def analyze_outliers(videos: list[dict[str, Any]], threshold: float = 2.0) -> list[dict[str, Any]]:
    """Rank videos by views / same-channel median, excluding each video itself.

    Each channel needs at least two other baseline videos. Incomplete or
    malformed records fail loudly rather than silently becoming evidence.
    """
    if not isinstance(threshold, (int, float)) or isinstance(threshold, bool) or not math.isfinite(threshold) or threshold <= 0:
        raise ValueError("threshold must be a positive number")

    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    seen_ids: set[tuple[str, str]] = set()
    for index, item in enumerate(videos):
        if not isinstance(item, dict):
            raise ValueError(f"video at index {index} must be an object")
        missing = [field for field in REQUIRED_VIDEO_FIELDS if field not in item or item[field] in (None, "")]
        if missing:
            raise ValueError(f"video at index {index} is missing: {', '.join(missing)}")
        if not isinstance(item["video_id"], str) or not isinstance(item["channel_id"], str):
            raise ValueError("video_id and channel_id must be strings")
        if not isinstance(item["source_url"], str) or not item["source_url"].startswith(("https://", "http://")):
            raise ValueError("source_url must be an http(s) URL")
        if not isinstance(item["retrieved_at"], str):
            raise ValueError("retrieved_at must be a YYYY-MM-DD date string")
        try:
            date.fromisoformat(item["retrieved_at"][:10])
        except ValueError as exc:
            raise ValueError("retrieved_at must begin with a valid YYYY-MM-DD date") from exc
        _positive_int(item["views"], "views")
        key = (item["channel_id"], item["video_id"])
        if key in seen_ids:
            raise ValueError(f"duplicate video: {key}")
        seen_ids.add(key)
        grouped[item["channel_id"]].append(item)

    results = []
    for channel_id, channel_videos in grouped.items():
        for video in channel_videos:
            baseline_views = [v["views"] for v in channel_videos if v["video_id"] != video["video_id"]]
            if len(baseline_views) < 2:
                continue
            baseline = median(baseline_views)
            baseline_zero = baseline == 0
            multiple = (video["views"] / baseline) if baseline > 0 else (None if video["views"] > 0 else 0.0)
            is_outlier = (video["views"] > 0) if baseline_zero else multiple >= threshold
            results.append({
                "video_id": video["video_id"],
                "channel_id": channel_id,
                "views": video["views"],
                "baseline_median_views": baseline,
                "views_multiple": multiple,
                "is_outlier": is_outlier,
                "baseline_zero": baseline_zero,
                "source_url": video["source_url"],
                "retrieved_at": video["retrieved_at"],
                "interpretation": "descriptive_signal_not_causal_explanation",
            })
    return sorted(results, key=lambda row: float("inf") if row["views_multiple"] is None else row["views_multiple"], reverse=True)
