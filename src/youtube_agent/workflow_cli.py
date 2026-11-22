"""CLI to create a workflow plan JSON without executing external actions."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from youtube_agent.orchestrator import create_workflow_plan


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a YouTube workflow plan.")
    parser.add_argument("topic")
    parser.add_argument("--profile", type=Path, help="Optional channel profile JSON file")
    parser.add_argument("--output", type=Path, default=Path("workflow-plan.json"))
    args = parser.parse_args()
    profile = json.loads(args.profile.read_text(encoding="utf-8")) if args.profile else {}
    plan = create_workflow_plan(args.topic, profile)
    args.output.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Created workflow plan with {len(plan['workflow'])} stages: {args.output}")
    print("Plan only: no external services were called and nothing was published.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
