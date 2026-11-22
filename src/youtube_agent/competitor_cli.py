"""Command-line interface for competitor outlier analysis."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from youtube_agent.outliers import analyze_outliers


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze competitor videos against their own channel baselines.")
    parser.add_argument("input", type=Path, help="JSON file containing a top-level 'videos' array")
    parser.add_argument("--threshold", type=float, default=2.0, help="Outlier threshold multiple (default: 2.0)")
    args = parser.parse_args()

    payload = json.loads(args.input.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or not isinstance(payload.get("videos"), list):
        parser.error("input JSON must contain a 'videos' array")
    results = analyze_outliers(payload["videos"], threshold=args.threshold)
    print(json.dumps({
        "threshold": args.threshold,
        "video_count_analyzed": len(results),
        "outliers": [row for row in results if row["is_outlier"]],
        "results": results,
        "notice": "Descriptive analysis of supplied records; not a causal explanation or live YouTube discovery."
    }, ensure_ascii=False, indent=2, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
