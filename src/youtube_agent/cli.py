"""Command-line entry point for ranking video ideas from JSON."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .idea_scoring import Idea, rank_ideas


def main() -> int:
    parser = argparse.ArgumentParser(description="Rank YouTube video ideas transparently.")
    parser.add_argument("input", help="Path to a JSON file containing an array of ideas.")
    parser.add_argument("--output", help="Optional path for the ranked JSON output.")
    args = parser.parse_args()

    raw = json.loads(Path(args.input).read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        parser.error("Input JSON must be an array of idea objects.")

    ideas = [Idea(**item) for item in raw]
    result = rank_ideas(ideas)
    rendered = json.dumps(result, indent=2, ensure_ascii=False)
    if args.output:
        Path(args.output).write_text(rendered + "\\n", encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
