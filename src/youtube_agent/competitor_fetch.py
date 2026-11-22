"""Fetch public competitor channel metrics through YouTube Data API v3."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from youtube_agent.youtube_api import YouTubeDataAPI


def main() -> int:
    parser = argparse.ArgumentParser(description="Collect public recent-video metrics for keyword-discovered channels.")
    parser.add_argument("query", help="Niche or competitor keyword")
    parser.add_argument("--channels", type=int, default=5, help="Number of channels to inspect (1-10)")
    parser.add_argument("--videos-per-channel", type=int, default=15, help="Recent uploads per channel (3-50)")
    parser.add_argument("--output", type=Path, default=Path("competitor-data.json"))
    args = parser.parse_args()
    result = YouTubeDataAPI().collect_competitor_videos(
        args.query, max_channels=args.channels, videos_per_channel=args.videos_per_channel
    )
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved {len(result['videos'])} public video records to {args.output}")
    print(f"Channels: {len(result['channels'])}; skipped videos without public view counts: {result['skipped_private_metrics']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
