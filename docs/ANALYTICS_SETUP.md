# YouTube Analytics setup (read-only)

## What this integration does
The optional adapter in `src/youtube_agent/youtube_analytics_api.py` calls YouTube Analytics API v2 for supplied video IDs (it does not enumerate channel uploads) and retrieves:
- per-video views, watch time, average view duration, average view percentage, likes, comments, shares, and subscribers gained;
- an individual video's audience-retention curve.

It does not publish or modify channel content.

## Google authorization
1. Create/select a Google Cloud project and enable **YouTube Analytics API**.
2. Configure an OAuth client appropriate to the app that will run the workflow.
3. Obtain user consent using only this scope:

   `https://www.googleapis.com/auth/yt-analytics.readonly`

4. Supply the short-lived access token to the adapter from a secure runtime/secret manager. Do not put tokens in source files, commits, logs, screenshots, or chat.
5. The adapter only accepts a token at call time; this repository does not implement the OAuth consent screen, token refresh, or token storage.

Google does not support service-account or device authorization flows for the YouTube Analytics API. Use a supported OAuth flow for the actual application type. Review Google's current authorization guide before deployment.

## CTR and traffic sources limitations
- The YouTube Analytics API v2 metric list used by this project does not provide YouTube Studio's video-thumbnail impressions CTR. Import CTR from a verified YouTube Studio export when needed; record its source and date.
- Traffic-source breakdowns are not currently fetched by the adapter. Do not infer them. Add a separate supported report only after checking the current API report compatibility tables.
- No revenue metrics are requested.

## Example (Python)
```python
from youtube_agent.youtube_analytics_api import (
    fetch_video_performance,
    fetch_video_retention,
)

# Read the token from your secret manager/environment in the calling application.
token = obtain_access_token_securely()
video_ids = ["VIDEO_ID_1", "VIDEO_ID_2"]  # supplied by the channel owner
performance = fetch_video_performance(token, video_ids, "2026-01-01", "2026-01-31")
retention = fetch_video_retention(token, "VIDEO_ID", "2026-01-01", "2026-01-31")
```

## Verification
Run the unit tests with:

```bash
python -m unittest discover -s tests
```

A successful mock test does not prove live Google OAuth or API access. Verify those separately after configuring credentials and granting consent.
