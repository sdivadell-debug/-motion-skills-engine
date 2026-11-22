"""CLI for running the implemented offline pipeline stages."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from .pipeline import execute_pipeline

def main() -> int:
    parser = argparse.ArgumentParser(description="Run offline YouTube pipeline stages.")
    parser.add_argument("input", type=Path, help="JSON input payload")
    parser.add_argument("--output", type=Path, default=Path("pipeline-output.json"))
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    result = execute_pipeline(payload)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Pipeline report written: {args.output}")
    print("Offline mode: no model calls, publishing, or external side effects.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
