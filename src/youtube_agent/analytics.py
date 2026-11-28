"""Evidence-first analysis of supplied YouTube video analytics."""
from __future__ import annotations

from collections import defaultdict
from statistics import median
from typing import Any

METRIC_FIELDS = (
    "views", "impressions", "ctr", "average_view_duration_seconds",
    "average_view_percentage", "watch_time_minutes", "likes", "comments",
    "shares", "subscribers_gained",
)


def _number(value: Any, field: str, index: int, *, minimum: float = 0,
            maximum: float | None = None) -> float | None:
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"video {index}: {field} must be numeric when supplied")
    if value < minimum or (maximum is not None and value > maximum):
        bound = f" between {minimum} and {maximum}" if maximum is not None else f" >= {minimum}"
        raise ValueError(f"video {index}: {field} must be{bound}")
    return float(value)


def analyze_performance(videos: list[dict], min_comparison_sample: int = 3) -> dict:
    """Compare videos only within declared comparable cohorts.

    Expected optional fields include format (long_form/shorts/live), age_window_days,
    impressions, ctr (percentage, usually exported from Studio), average_view_duration_seconds,
    average_view_percentage, watch_time_minutes, likes, comments, shares,
    subscribers_gained, retention_curve, traffic_sources, and metric_sources.
    """
    if not isinstance(videos, list):
        raise ValueError("videos must be an array")
    if isinstance(min_comparison_sample, bool) or not isinstance(min_comparison_sample, int) or min_comparison_sample < 2:
        raise ValueError("min_comparison_sample must be an integer >= 2")

    checked = []
    for i, original in enumerate(videos):
        if not isinstance(original, dict):
            raise ValueError(f"video {i} must be object")
        video = dict(original)
        if not isinstance(video.get("title"), str) or not video["title"].strip():
            fallback = video.get("video_id")
            if not isinstance(fallback, str) or not fallback.strip():
                raise ValueError(f"video {i} needs a non-empty title or video_id")
            video["title"] = fallback
        if video.get("views") is None:
            raise ValueError(f"video {i} missing views")
        for field in METRIC_FIELDS:
            maximum = 100 if field in ("ctr", "average_view_percentage") else None
            video[field] = _number(video.get(field), field, i, maximum=maximum)
        video["format"] = str(video.get("format") or "unspecified").lower()
        age = video.get("age_window_days", "unspecified")
        video["age_window_days"] = age
        video["missing_metrics"] = [field for field in METRIC_FIELDS if video.get(field) is None]
        checked.append(video)

    if not checked:
        return {
            "video_count": 0, "median_views": None, "videos": [],
            "cohort_baselines": [], "notes": ["No analytics data supplied."],
        }

    cohorts: dict[tuple[str, Any], list[dict]] = defaultdict(list)
    for video in checked:
        cohorts[(video["format"], video["age_window_days"])].append(video)

    cohort_baselines = []
    for (video_format, age_window), members in cohorts.items():
        row = {
            "format": video_format,
            "age_window_days": age_window,
            "sample_size": len(members),
            "comparable": len(members) >= min_comparison_sample,
            "metrics": {},
        }
        if row["comparable"]:
            for field in METRIC_FIELDS:
                values = [v[field] for v in members if v[field] is not None]
                if values:
                    row["metrics"][field] = median(values)
        cohort_baselines.append(row)

        for video in members:
            comparisons = {}
            for field, baseline in row["metrics"].items():
                value = video.get(field)
                if value is not None:
                    comparisons[field] = {
                        "value": value,
                        "cohort_median": baseline,
                        "difference": round(value - baseline, 3),
                        "multiple": round(value / baseline, 3) if baseline else None,
                    }
            video["cohort_comparable"] = row["comparable"]
            video["comparisons"] = comparisons
            video["views_vs_median"] = comparisons.get("views", {}).get("multiple")

    all_views = [v["views"] for v in checked if v["views"] is not None]
    notes = [
        "Comparisons use only the same declared format and age_window_days.",
        "A cohort needs at least the configured sample size; otherwise no cohort baseline is reported.",
        "CTR must come from a creator-provided Studio export or other verified source; it is not fabricated from public views.",
        "Correlation is not causation. Treat explanations as hypotheses and test one change at a time.",
    ]
    if any(v["format"] == "unspecified" for v in checked):
        notes.append("Some videos have no format label; they are grouped as unspecified.")
    if any(v.get("ctr") is None for v in checked):
        notes.append("CTR is missing for one or more videos.")
    if any(v.get("average_view_percentage") is None for v in checked):
        notes.append("Average view percentage is missing for one or more videos.")

    return {
        "video_count": len(checked),
        "median_views": median(all_views) if all_views else None,
        "cohort_baselines": cohort_baselines,
        "videos": checked,
        "notes": notes,
    }
