# Live Competitor Collection

## Setup

1. Enable **YouTube Data API v3** in a Google Cloud project.
2. Create an API key and restrict it to the YouTube Data API where possible.
3. Set the environment variable `YOUTUBE_DATA_API_KEY`; never commit the key.

macOS/Linux:
```bash
export YOUTUBE_DATA_API_KEY="YOUR_API_KEY"
```

PowerShell:
```powershell
$env:YOUTUBE_DATA_API_KEY="YOUR_API_KEY"
```

## Collection method

The collector searches for channels matching a keyword, resolves each channel's
uploads playlist, retrieves recent upload IDs, then fetches public video
statistics. It preserves channel IDs, titles, publication timestamps, source
URLs, and retrieval timestamps. Records without a public `viewCount` are
skipped and counted.

This uses the official YouTube Data API v3 endpoints:
- `search.list`: https://developers.google.com/youtube/data/reference/rest/v3/search/list
- `channels.list`: https://developers.google.com/youtube/data/reference/rest/v3/channels/list
- `playlistItems.list`: https://developers.google.com/youtube/data/reference/rest/v3/playlistItems/list
- `videos.list`: https://developers.google.com/youtube/data/reference/rest/v3/videos/list

## Limits

- Search results are keyword discovery, not a complete census of competitors.
- Public view counts are snapshots and continue changing.
- The API key must have the API enabled and available quota.
- This collector does not access private analytics such as CTR, retention, or revenue.
- Shorts and long-form videos are not automatically separated; segment them before interpreting baselines.
- Use the saved `retrieved_at` timestamp when comparing snapshots.

The collector is optional. Offline analysis with supplied JSON remains supported.
