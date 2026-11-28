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
            maximum = 100 if field == "ctr" else None
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


def summarize_retention_curve(points: list[dict]) -> dict:
    """Summarize a supplied YouTube retention curve without assigning causes."""
    if not isinstance(points, list):
        raise ValueError("retention points must be an array")
    checked = []
    for index, point in enumerate(points):
        if not isinstance(point, dict):
            raise ValueError(f"retention point {index} must be an object")
        elapsed = point.get("elapsed_video_time_ratio")
        audience = point.get("audience_watch_ratio")
        if isinstance(elapsed, bool) or not isinstance(elapsed, (int, float)) or not 0 <= elapsed <= 1:
            raise ValueError(f"retention point {index}: elapsed_video_time_ratio must be between 0 and 1")
        if isinstance(audience, bool) or not isinstance(audience, (int, float)) or audience < 0:
            raise ValueError(f"retention point {index}: audience_watch_ratio must be nonnegative")
        checked.append(dict(point))
    checked.sort(key=lambda item: item["elapsed_video_time_ratio"])
    drops = []
    for previous, current in zip(checked, checked[1:]):
        drop = previous["audience_watch_ratio"] - current["audience_watch_ratio"]
        if drop > 0:
            drops.append({
                "from_elapsed_ratio": previous["elapsed_video_time_ratio"],
                "to_elapsed_ratio": current["elapsed_video_time_ratio"],
                "absolute_ratio_drop": round(drop, 4),
            })
    largest_drop = max(drops, key=lambda item: item["absolute_ratio_drop"]) if drops else None
    return {
        "point_count": len(checked),
        "largest_observed_drop": largest_drop,
        "drops": drops,
        "notes": [
            "Audience watch ratio can exceed 1 when viewers replay segments.",
            "A drop identifies where the curve falls, not why viewers left.",
        ],
    }
