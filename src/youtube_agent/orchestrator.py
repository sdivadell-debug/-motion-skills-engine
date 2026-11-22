"""Workflow coordinator for YouTube Agent Engine.

Coordinates specialist stages using a deterministic workflow contract. The
coordinator currently generates task plans and validates stage hand-offs;
external research, editing, and publishing require adapters and approvals.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any

WORKFLOW = [
    "channel_profile",
    "research",
    "competitor_research",
    "idea_lab",
    "script_studio",
    "packaging",
    "production_editor",
    "shorts_cutter",
    "seo_publisher",
    "creator_review",
]


@dataclass
class Stage:
    name: str
    status: str = "pending"
    input: dict[str, Any] | None = None
    output: dict[str, Any] | None = None
    notes: list[str] | None = None


class WorkflowRun:
    def __init__(self, topic: str, channel_profile: dict[str, Any] | None = None):
        if not isinstance(topic, str) or not topic.strip():
            raise ValueError("topic must be a non-empty string")
        self.run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        self.topic = topic.strip()
        self.profile = channel_profile or {}
        self.stages = [Stage(name=s, notes=[]) for s in WORKFLOW]
        self.created_at = datetime.now(timezone.utc).isoformat()
        self.approval_required = True

    def plan(self) -> dict[str, Any]:
        for stage in self.stages:
            stage.input = {"topic": self.topic}
            if stage.name == "channel_profile":
                stage.input["profile"] = self.profile
            stage.notes = self._notes_for(stage.name)
        return self.to_dict()

    def _notes_for(self, stage: str) -> list[str]:
        notes = {
            "channel_profile": ["Validate supplied profile; report missing required fields."],
            "research": ["Gather source-backed claims; record URLs and retrieval dates."],
            "competitor_research": ["Collect public metrics only through configured adapter or supplied data."],
            "idea_lab": ["Generate differentiated ideas; score with the idea scoring module."],
            "script_studio": ["Draft only after concept selection; cite factual claims."],
            "packaging": ["Generate truthful title/thumbnail pairs based on the draft."],
            "production_editor": ["Produce an editor plan; do not claim to have edited media."],
            "shorts_cutter": ["Identify short-form candidates from available script/transcript."],
            "seo_publisher": ["Draft metadata and upload checklist; do not publish."],
            "creator_review": ["Require creator approval before external actions."],
        }
        return notes.get(stage, [])

    def mark_stage(self, stage_name: str, status: str, output: dict[str, Any] | None = None):
        allowed = {"pending", "running", "complete", "partial", "blocked", "approved"}
        if status not in allowed:
            raise ValueError(f"Invalid status: {status}")
        stage = next((s for s in self.stages if s.name == stage_name), None)
        if stage is None:
            raise ValueError(f"Unknown stage: {stage_name}")
        stage.status = status
        stage.output = output
        return asdict(stage)

    def to_dict(self) -> dict[str, Any]:
        return {
            "run_id": self.run_id,
            "created_at": self.created_at,
            "topic": self.topic,
            "profile": self.profile,
            "workflow": [asdict(stage) for stage in self.stages],
            "approval_required": self.approval_required,
            "status": "planned",
        }


def create_workflow_plan(topic: str, channel_profile: dict[str, Any] | None = None) -> dict[str, Any]:
    return WorkflowRun(topic, channel_profile).plan()
