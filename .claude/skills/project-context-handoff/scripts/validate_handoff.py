#!/usr/bin/env python3
"""Validate the structure and basic completeness of a project handoff."""

from __future__ import annotations

import re
import sys
from pathlib import Path


HEADINGS = (
    "# Project Context Handoff",
    "## Goal",
    "## Current Status",
    "## Decisions Made",
    "## Blockers & Failed Attempts",
    "## Next Best Step",
)
TEMPLATE_TOKEN = re.compile(r"\{\{[A-Z][A-Z0-9_]*\}\}")
STATUS_LINE = re.compile(r"^- \*\*(Done|In Progress):\*\*\s*(.+)$", re.MULTILINE)
ACTION_LINE = re.compile(r"^\*\*Action Item:\*\*\s*(.+)$", re.MULTILINE)
SECRET_ASSIGNMENT = re.compile(
    r"(?i)\b(?:api[_-]?key|access[_-]?token|auth[_-]?token|password|passwd|private[_-]?key|client[_-]?secret)\b\s*[:=]\s*[^\s`]+"
)


def section_body(text: str, heading: str) -> str:
    start = text.find(heading) + len(heading)
    end_candidates = [text.find(other, start) for other in HEADINGS if text.find(other, start) >= 0]
    end = min(end_candidates, default=len(text))
    return text[start:end].strip()


def validate(path: Path) -> list[str]:
    if not path.is_file():
        return [f"File not found: {path}"]

    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"Cannot read {path}: {exc}"]

    errors: list[str] = []
    positions: list[int] = []
    for heading in HEADINGS:
        count = sum(1 for line in text.splitlines() if line.strip() == heading)
        if count != 1:
            errors.append(f"Expected heading exactly once: {heading} (found {count})")
        positions.append(text.find(heading))

    if all(position >= 0 for position in positions) and positions != sorted(positions):
        errors.append("Headings are not in the required order")

    for heading in HEADINGS[1:]:
        if text.find(heading) >= 0 and not section_body(text, heading):
            errors.append(f"Empty section: {heading}")

    statuses = {name: value.strip() for name, value in STATUS_LINE.findall(text)}
    for name in ("Done", "In Progress"):
        if not statuses.get(name):
            errors.append(f"Missing or empty **{name}:** status")

    actions = [action.strip() for action in ACTION_LINE.findall(text) if action.strip()]
    if len(actions) != 1:
        errors.append(f"Expected exactly one non-empty **Action Item:** (found {len(actions)})")

    if TEMPLATE_TOKEN.search(text):
        errors.append("Unresolved template token found")
    if SECRET_ASSIGNMENT.search(text):
        errors.append("Possible secret value found; redact it and keep only the variable name")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_handoff.py <handoff.md>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    errors = validate(path)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Structurally valid handoff: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
