"""Minimal read-only client for the YouTube Analytics API v2.

OAuth is intentionally handled outside this module. Pass an access token obtained
with the yt-analytics.readonly scope; never use a write-capable YouTube scope here.
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

API_URL = "https://youtubeanalytics.googleapis.com/v2/reports"
READONLY_SCOPE = "https://www.googleapis.com/auth/yt-analytics.readonly"
ALLOWED_METRICS = {
    "views", "engagedViews", "estimatedMinutesWatched", "averageViewDuration",
    "averageViewPercentage", "likes", "comments", "shares", "subscribersGained",
    "subscribersLost", "audienceWatchRatio", "relativeRetentionPerformance",
    "startedWatching", "stoppedWatching", "totalSegmentImpressions",
}
ALLOWED_DIMENSIONS = {"video", "day", "month", "elapsedVideoTimeRatio", "creatorContentType", "insightTrafficSourceType", "insightTrafficSourceDetail"}


class YouTubeAnalyticsError(RuntimeError):
    """Raised when the read-only YouTube Analytics request fails."""


def query_report(access_token: str, start_date: str, end_date: str,
                 metrics: list[str], dimensions: list[str] | None = None,
                 filters: str | None = None, max_results: int = 200) -> dict:
    if not isinstance(access_token, str) or not access_token.strip():
        raise ValueError("A valid OAuth access token is required.")
    for date_value in (start_date, end_date):
        if not isinstance(date_value, str) or not re.fullmatch("[0-9]{4}-[0-9]{2}-[0-9]{2}", date_value):
            raise ValueError("Dates must use YYYY-MM-DD.")
        try:
            datetime.strptime(date_value, "%Y-%m-%d")
        except ValueError as exc:
            raise ValueError("Dates must be valid calendar dates.") from exc
    if start_date > end_date:
        raise ValueError("start_date must not be after end_date.")
    if not isinstance(metrics, list) or not metrics or any(m not in ALLOWED_METRICS for m in metrics):
        raise ValueError("One or more metrics are unsupported or not allowlisted.")
    dimensions = dimensions or []
    if not isinstance(dimensions, list) or any(d not in ALLOWED_DIMENSIONS for d in dimensions):
        raise ValueError("One or more dimensions are not allowlisted.")
    if isinstance(max_results, bool) or not isinstance(max_results, int) or not 1 <= max_results <= 200:
        raise ValueError("max_results must be between 1 and 200.")

    params = {
        "ids": "channel==MINE",
        "startDate": start_date,
        "endDate": end_date,
        "metrics": ",".join(metrics),
        "maxResults": max_results,
    }
    if dimensions:
        params["dimensions"] = ",".join(dimensions)
    if filters:
        if not isinstance(filters, str) or not re.fullmatch("video==[A-Za-z0-9_-]+", filters):
            raise ValueError("Only a single video==VIDEO_ID filter is supported.")
        params["filters"] = filters

    request = Request(
        API_URL + "?" + urlencode(params),
        headers={"Authorization": f"Bearer {access_token}", "Accept": "application/json"},
        method="GET",
    )
    try:
        with urlopen(request, timeout=30) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise YouTubeAnalyticsError(f"YouTube Analytics API returned HTTP {exc.code}: {detail}") from exc
    except (URLError, TimeoutError) as exc:
        raise YouTubeAnalyticsError(f"Could not reach YouTube Analytics API: {exc}") from exc
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise YouTubeAnalyticsError("YouTube Analytics API returned invalid JSON.") from exc

    headers = [column.get("name") for column in payload.get("columnHeaders", [])]
    rows = [dict(zip(headers, row)) for row in payload.get("rows", [])]
    return {
        "kind": "youtube_analytics_api_v2",
        "start_date": start_date,
        "end_date": end_date,
        "dimensions": dimensions,
        "metrics": metrics,
        "rows": rows,
        "row_count": len(rows),
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "source": API_URL,
    }


def fetch_channel_summary(access_token: str, start_date: str, end_date: str) -> dict:
    """Fetch aggregate channel activity for a reporting window."""
    return query_report(
        access_token, start_date, end_date,
        metrics=["views", "estimatedMinutesWatched", "averageViewDuration",
                 "averageViewPercentage", "likes", "comments", "shares",
                 "subscribersGained"],
    )


def fetch_traffic_sources(access_token: str, start_date: str, end_date: str,
                          video_id: str | None = None) -> dict:
    """Fetch channel or single-video traffic-source categories."""
    filters = None
    if video_id is not None:
        if not isinstance(video_id, str) or not re.fullmatch("[A-Za-z0-9_-]+", video_id):
            raise ValueError("video_id is invalid.")
        filters = f"video=={video_id}"
    return query_report(
        access_token, start_date, end_date,
        metrics=["views", "engagedViews", "estimatedMinutesWatched"],
        dimensions=["insightTrafficSourceType"],
        filters=filters,
    )


def fetch_video_performance(access_token: str, video_ids: list[str],
                            start_date: str, end_date: str) -> dict:
    """Fetch metrics for caller-supplied video IDs (one supported report per video)."""
    if not isinstance(video_ids, list) or not video_ids:
        raise ValueError("Provide one or more video IDs.")
    if len(video_ids) > 50 or any(
        not isinstance(video_id, str) or not re.fullmatch("[A-Za-z0-9_-]+", video_id)
        for video_id in video_ids
    ):
        raise ValueError("Provide 1 to 50 valid video IDs.")
    videos = []
    for video_id in video_ids:
        report = query_report(
            access_token, start_date, end_date,
            metrics=["views", "estimatedMinutesWatched", "averageViewDuration",
                     "averageViewPercentage", "likes", "comments", "shares", "subscribersGained"],
            filters=f"video=={video_id}",
        )
        row = report["rows"][0] if report["rows"] else {}
        videos.append({
            "video_id": video_id,
            "title": video_id,
            "views": row.get("views"),
            "watch_time_minutes": row.get("estimatedMinutesWatched"),
            "average_view_duration_seconds": row.get("averageViewDuration"),
            "average_view_percentage": row.get("averageViewPercentage"),
            "likes": row.get("likes"),
            "comments": row.get("comments"),
            "shares": row.get("shares"),
            "subscribers_gained": row.get("subscribersGained"),
            "format": "unspecified",
            "metric_sources": {"analytics_api": report["source"]},
        })
    return {
        "kind": "youtube_analytics_api_v2",
        "start_date": start_date,
        "end_date": end_date,
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "videos": videos,
        "video_count": len(videos),
        "notes": [
            "Video IDs are used as labels; add verified titles and formats before cohort comparison.",
            "CTR is not included in this API request; fetch traffic-source categories separately with fetch_traffic_sources.",
        ],
    }


def fetch_video_retention(access_token: str, video_id: str,
                          start_date: str, end_date: str) -> dict:
    """Fetch the audience-retention curve for exactly one owned video."""
    if not isinstance(video_id, str) or not re.fullmatch("[A-Za-z0-9_-]+", video_id):
        raise ValueError("video_id is invalid.")
    report = query_report(
        access_token, start_date, end_date,
        metrics=["audienceWatchRatio", "relativeRetentionPerformance",
                 "startedWatching", "stoppedWatching", "totalSegmentImpressions"],
        dimensions=["elapsedVideoTimeRatio"],
        filters=f"video=={video_id}",
    )
    report["video_id"] = video_id
    report["retention_curve"] = [
        {
            "elapsed_video_time_ratio": row.get("elapsedVideoTimeRatio"),
            "audience_watch_ratio": row.get("audienceWatchRatio"),
            "relative_retention_performance": row.get("relativeRetentionPerformance"),
            "started_watching": row.get("startedWatching"),
            "stopped_watching": row.get("stoppedWatching"),
            "segment_impressions": row.get("totalSegmentImpressions"),
        }
        for row in report["rows"]
    ]
    return report
