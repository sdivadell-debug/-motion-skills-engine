"""Transparent, evidence-aware scoring for YouTube video ideas.

This is a prioritization heuristic, not a view-count predictor.
All input scores are creator/research assessments on a 0-10 scale.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any


WEIGHTS = {
    "audience_fit": 0.25,
    "demand_evidence": 0.25,
    "differentiation": 0.20,
    "channel_fit": 0.15,
    "feasibility": 0.15,
}


@dataclass
class Idea:
    title: str
    audience_fit: float
    demand_evidence: float
    differentiation: float
    channel_fit: float
    feasibility: float
    evidence_urls: list[str]
    evidence_notes: str = ""

    def validate(self) -> None:
        if not self.title.strip():
            raise ValueError("Idea title cannot be empty.")
        for key in WEIGHTS:
            value = getattr(self, key)
            if not isinstance(value, (int, float)) or not 0 <= value <= 10:
                raise ValueError(f"{key} must be a number from 0 to 10.")
        if not isinstance(self.evidence_urls, list):
            raise ValueError("evidence_urls must be a list.")
        for url in self.evidence_urls:
            if not isinstance(url, str) or not url.startswith(("https://", "http://")):
                raise ValueError("Every evidence URL must start with http:// or https://.")


def score_idea(idea: Idea) -> dict[str, Any]:
    """Return a weighted score, evidence status, and transparent breakdown."""
    idea.validate()
    weighted = sum(getattr(idea, key) * weight for key, weight in WEIGHTS.items())
    evidence_status = "sourced" if idea.evidence_urls else "unsupported"
    confidence = "medium" if len(idea.evidence_urls) >= 2 else (
        "low" if not idea.evidence_urls else "limited"
    )
    result = asdict(idea)
    result.update({
        "score": round(weighted * 10, 1),
        "score_scale": "0-100",
        "evidence_status": evidence_status,
        "confidence": confidence,
        "weights": WEIGHTS,
        "interpretation": (
            "Prioritization heuristic only; not a prediction of views or virality."
        ),
    })
    return result


def rank_ideas(ideas: list[Idea]) -> list[dict[str, Any]]:
    """Rank ideas by score, then evidence confidence."""
    ranked = [score_idea(idea) for idea in ideas]
    confidence_rank = {"medium": 2, "limited": 1, "low": 0}
    return sorted(
        ranked,
        key=lambda item: (item["score"], confidence_rank[item["confidence"]]),
        reverse=True,
    )
