"""Dependency-free validation for the channel profile contract."""
from __future__ import annotations

from datetime import date
from typing import Any
from urllib.parse import urlparse

REQUIRED = {"channel_name", "niche", "primary_audience", "language", "voice"}
ALLOWED = {
    "channel_name", "channel_url", "niche", "primary_audience", "language",
    "geography", "content_pillars", "formats", "publishing_capacity_per_week",
    "goals", "constraints", "voice", "performance_baseline",
}
LIST_FIELDS = {"content_pillars", "formats", "goals", "constraints"}


def validate_channel_profile(profile: dict[str, Any]) -> list[str]:
    """Return all detected validation errors without mutating the profile."""
    errors: list[str] = []
    if not isinstance(profile, dict):
        return ["profile must be an object"]
    missing = sorted(REQUIRED - profile.keys())
    errors.extend(f"missing required field: {key}" for key in missing)
    errors.extend(f"unknown field: {key}" for key in sorted(profile.keys() - ALLOWED))

    for key in ("channel_name", "niche", "primary_audience"):
        if key in profile and (not isinstance(profile[key], str) or not profile[key].strip()):
            errors.append(f"{key} must be a non-empty string")
    if "language" in profile and (not isinstance(profile["language"], str) or len(profile["language"]) < 2):
        errors.append("language must be a string of at least 2 characters")
    if "channel_url" in profile:
        parsed = urlparse(profile["channel_url"]) if isinstance(profile["channel_url"], str) else None
        if not parsed or parsed.scheme not in {"http", "https"} or not parsed.netloc:
            errors.append("channel_url must be a valid http(s) URL")
    for key in LIST_FIELDS:
        if key in profile and (
            not isinstance(profile[key], list)
            or any(not isinstance(value, str) for value in profile[key])
        ):
            errors.append(f"{key} must be an array of strings")
    if "publishing_capacity_per_week" in profile:
        value = profile["publishing_capacity_per_week"]
        if isinstance(value, bool) or not isinstance(value, (int, float)) or value < 0:
            errors.append("publishing_capacity_per_week must be a non-negative number")

    if "voice" in profile:
        voice = profile["voice"]
        if not isinstance(voice, dict):
            errors.append("voice must be an object")
        else:
            if not isinstance(voice.get("tone"), str) or not voice.get("tone", "").strip():
                errors.append("voice.tone is required and must be a non-empty string")
            unknown_voice = set(voice) - {"tone", "preferred_phrases", "avoid", "pacing"}
            errors.extend(f"unknown voice field: {key}" for key in sorted(unknown_voice))
            for key in ("preferred_phrases", "avoid"):
                if key in voice and (
                    not isinstance(voice[key], list)
                    or any(not isinstance(value, str) for value in voice[key])
                ):
                    errors.append(f"voice.{key} must be an array of strings")
            if "pacing" in voice and not isinstance(voice["pacing"], str):
                errors.append("voice.pacing must be a string")

    if "performance_baseline" in profile:
        baseline = profile["performance_baseline"]
        if not isinstance(baseline, dict):
            errors.append("performance_baseline must be an object")
        else:
            for key in ("source", "period_start", "period_end"):
                if not isinstance(baseline.get(key), str) or not baseline.get(key).strip():
                    errors.append(f"performance_baseline.{key} is required")
            dates = {}
            for key in ("period_start", "period_end"):
                if key in baseline:
                    try:
                        dates[key] = date.fromisoformat(baseline[key])
                    except (TypeError, ValueError):
                        errors.append(f"performance_baseline.{key} must use YYYY-MM-DD")
            if len(dates) == 2 and dates["period_start"] > dates["period_end"]:
                errors.append("performance_baseline.period_start must not be after period_end")
            metrics = baseline.get("metrics", {})
            if not isinstance(metrics, dict) or any(
                not isinstance(value, (int, float)) or isinstance(value, bool)
                for value in metrics.values()
            ):
                errors.append("performance_baseline.metrics must map names to numbers")

    return errors
