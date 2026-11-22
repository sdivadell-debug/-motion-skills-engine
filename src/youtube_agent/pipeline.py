"""Executable offline pipeline handlers; no model or network calls are implied."""
from __future__ import annotations

from typing import Any
from .profile import validate_channel_profile
from .research import research_brief
from .outliers import analyze_outliers
from .idea_scoring import Idea, rank_ideas

HANDLERS = {
    "channel_profile": lambda data: {"errors": validate_channel_profile(data.get("profile", {})), "valid": not validate_channel_profile(data.get("profile", {}))},
    "research": lambda data: research_brief(data.get("topic", ""), data.get("research_items", [])),
    "competitor_research": lambda data: {"results": analyze_outliers(data.get("competitor_videos", [])), "notice": "Analyzes supplied data only; no live discovery."},
    "idea_lab": lambda data: {"ranked_ideas": rank_ideas([Idea(**item) for item in data.get("ideas", [])])},
}


def execute_pipeline(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise ValueError("input payload must be a JSON object")
    topic = payload.get("topic")
    if not isinstance(topic, str) or not topic.strip():
        raise ValueError("topic must be a non-empty string")
    results = {"topic": topic, "stages": {}, "external_actions": "disabled"}
    for stage in ("channel_profile", "research", "competitor_research", "idea_lab"):
        handler = HANDLERS[stage]
        try:
            result = handler(payload)
            results["stages"][stage] = {"status": "complete", "result": result}
        except (ValueError, TypeError, KeyError) as exc:
            results["stages"][stage] = {"status": "blocked", "error": str(exc)}
    for stage in ("script_studio", "packaging", "production_editor", "shorts_cutter", "seo_publisher", "creator_review"):
        results["stages"][stage] = {
            "status": "not_executable",
            "note": "Instruction-only or model-dependent stage; no handler configured. No content was fabricated."
        }
    results["approval_required"] = True
    results["publishing"] = "disabled"
    return results
