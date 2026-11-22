"""Optional public-metrics collector using the official YouTube Data API v3.

Requires YOUTUBE_DATA_API_KEY. Uses only the Python standard library.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen
from typing import Any

BASE_URL = "https://www.googleapis.com/youtube/v3"


class YouTubeAPIError(RuntimeError):
    """Raised when the YouTube Data API request fails."""


class YouTubeDataAPI:
    def __init__(self, api_key: str | None = None, timeout: int = 20):
        self.api_key = api_key or os.getenv("YOUTUBE_DATA_API_KEY")
        if not self.api_key:
            raise ValueError("Set YOUTUBE_DATA_API_KEY before using live collection.")
        self.timeout = timeout

    def _get(self, endpoint: str, **params: Any) -> dict[str, Any]:
        query = urlencode({**params, "key": self.api_key})
        request_url = f"{BASE_URL}/{endpoint}?{query}"
        try:
            with urlopen(request_url, timeout=self.timeout) as response:
                payload = json.loads(response.read().decode("utf-8"))
        except HTTPError as exc:
            raise YouTubeAPIError(f"YouTube API returned HTTP {exc.code}. Check API key, quota, and request parameters.") from exc
        except URLError as exc:
            raise YouTubeAPIError(f"Could not reach YouTube API: {exc.reason}") from exc
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise YouTubeAPIError("YouTube API returned an unreadable response.") from exc
        if not isinstance(payload, dict):
            raise YouTubeAPIError("YouTube API returned an unexpected response shape.")
        if "error" in payload:
            reason = payload["error"].get("errors", [{}])[0].get("reason", "apiError")
            raise YouTubeAPIError(f"YouTube API error: {reason}")
        return payload

    def collect_competitor_videos(
        self, query: str, max_channels: int = 5, videos_per_channel: int = 15
    ) -> dict[str, Any]:
        """Find channels by keyword, then collect recent public uploads and view counts."""
        if not isinstance(query, str) or not query.strip():
            raise ValueError("query must not be empty")
        if isinstance(max_channels, bool) or not 1 <= max_channels <= 10:
            raise ValueError("max_channels must be between 1 and 10")
        if isinstance(videos_per_channel, bool) or not 3 <= videos_per_channel <= 50:
            raise ValueError("videos_per_channel must be between 3 and 50")

        search = self._get(
            "search", part="snippet", type="channel", q=query.strip(),
            maxResults=max_channels, order="relevance"
        )
        channel_items = search.get("items", [])
        channel_ids = [
            item.get("id", {}).get("channelId")
            for item in channel_items
            if item.get("id", {}).get("channelId")
        ]
        if not channel_ids:
            return {"query": query, "retrieved_at": datetime.now(timezone.utc).isoformat(),
                    "channels": [], "videos": [], "skipped_private_metrics": 0}

        channel_response = self._get(
            "channels", part="snippet,contentDetails", id=",".join(channel_ids)
        )
        channel_map = {}
        for channel in channel_response.get("items", []):
            uploads = channel.get("contentDetails", {}).get("relatedPlaylists", {}).get("uploads")
            if uploads:
                channel_map[channel["id"]] = {
                    "channel_title": channel.get("snippet", {}).get("title", ""),
                    "uploads_playlist_id": uploads,
                }

        retrieved_at = datetime.now(timezone.utc).isoformat()
        videos: list[dict[str, Any]] = []
        skipped_private_metrics = 0
        channels: list[dict[str, str]] = []
        for channel_id in channel_ids:
            info = channel_map.get(channel_id)
            if not info:
                continue
            channels.append({"channel_id": channel_id, "channel_title": info["channel_title"]})
            playlist = self._get(
                "playlistItems", part="contentDetails", playlistId=info["uploads_playlist_id"],
                maxResults=videos_per_channel
            )
            video_ids = [
                item.get("contentDetails", {}).get("videoId")
                for item in playlist.get("items", [])
                if item.get("contentDetails", {}).get("videoId")
            ]
            for offset in range(0, len(video_ids), 50):
                batch = video_ids[offset:offset + 50]
                if not batch:
                    continue
                details = self._get("videos", part="snippet,statistics", id=",".join(batch))
                for item in details.get("items", []):
                    statistics = item.get("statistics", {})
                    if "viewCount" not in statistics:
                        skipped_private_metrics += 1
                        continue
                    snippet = item.get("snippet", {})
                    video_id = item.get("id")
                    videos.append({
                        "video_id": video_id,
                        "channel_id": snippet.get("channelId", channel_id),
                        "channel_title": info["channel_title"],
                        "title": snippet.get("title", ""),
                        "published_at": snippet.get("publishedAt"),
                        "views": int(statistics["viewCount"]),
                        "source_url": f"https://www.youtube.com/watch?v={video_id}",
                        "retrieved_at": retrieved_at,
                        "data_source": "YouTube Data API v3",
                    })

        return {
            "query": query,
            "retrieved_at": retrieved_at,
            "channels": channels,
            "videos": videos,
            "skipped_private_metrics": skipped_private_metrics,
            "collection_note": "Public view counts only; missing viewCount fields were skipped.",
        }
