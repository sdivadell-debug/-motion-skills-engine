"""Simple JSON-file workspace memory for channel workflow runs."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class ChannelMemory:
    def __init__(self, path: str | Path):
        self.path = Path(path)

    def load(self) -> dict[str, Any]:
        if not self.path.exists():
            return {"channel_profile": {}, "research_notes": [], "idea_history": [], "experiments": []}
        payload = json.loads(self.path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("memory file must contain a JSON object")
        for key in ("channel_profile", "research_notes", "idea_history", "experiments"):
            payload.setdefault(key, {} if key == "channel_profile" else [])
        return payload

    def save(self, payload: dict[str, Any]) -> None:
        if not isinstance(payload, dict):
            raise ValueError("memory must be a JSON object")
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temp_path = self.path.with_suffix(self.path.suffix + ".tmp")
        temp_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        temp_path.replace(self.path)

    def append_record(self, section: str, record: dict[str, Any]) -> dict[str, Any]:
        allowed = {"research_notes", "idea_history", "experiments"}
        if section not in allowed:
            raise ValueError("appendable section must be research_notes, idea_history, or experiments")
        if not isinstance(record, dict):
            raise ValueError("record must be an object")
        data = self.load()
        data[section].append(record)
        self.save(data)
        return data

    def update_profile(self, profile: dict[str, Any]) -> None:
        if not isinstance(profile, dict):
            raise ValueError("profile must be an object")
        data = self.load()
        data["channel_profile"] = profile
        self.save(data)
