"""Validation helpers for source-backed research notes."""
from __future__ import annotations

from datetime import date
from typing import Any


ALLOWED_EVIDENCE_TYPES = {"measured", "sourced", "estimated", "hypothesis"}


def validate_research_item(item: dict[str, Any]) -> list[str]:
    """Return validation errors; never invent missing sources or dates."""
    errors: list[str] = []
    if not item.get("claim"):
        errors.append("claim is required")
    evidence_type = item.get("evidence_type")
    if evidence_type not in ALLOWED_EVIDENCE_TYPES:
        errors.append(f"evidence_type must be one of {sorted(ALLOWED_EVIDENCE_TYPES)}")
    if evidence_type == "sourced":
        if not str(item.get("source_url", "")).startswith(("https://", "http://")):
            errors.append("sourced claims require a valid source_url")
        if not item.get("retrieved_at"):
            errors.append("sourced claims require retrieved_at")
    if evidence_type == "measured" and not item.get("metric_origin"):
        errors.append("measured claims require metric_origin")
    retrieved_at = item.get("retrieved_at")
    if retrieved_at:
        try:
            date.fromisoformat(retrieved_at)
        except (TypeError, ValueError):
            errors.append("retrieved_at must use YYYY-MM-DD")
    return errors


def research_brief(topic: str, items: list[dict[str, Any]]) -> dict[str, Any]:
    """Build a brief while preserving unsupported claims as explicit gaps."""
    validated = []
    for item in items:
        errors = validate_research_item(item)
        validated.append({**item, "validation_errors": errors})
    return {
        "topic": topic,
        "items": validated,
        "validated_count": sum(not x["validation_errors"] for x in validated),
        "needs_research_count": sum(bool(x["validation_errors"]) for x in validated),
        "rule": "Unverified claims remain gaps; do not turn them into facts.",
    }
