# Competitor Research and Outlier Protocol

## Purpose

Find videos that materially outperform the typical recent videos on their own
channel. A high raw view count alone is not an outlier signal.

## Required input

Each video record must include:
- stable `video_id` and `channel_id`
- non-negative integer `views`
- public source URL
- retrieval date/time

Collect comparable videos from the same channel and a reasonably consistent
time window. Record collection method and any known limitations in the research
notes. Prefer a documented official API or a manually verified public page.
This repository currently accepts supplied records; it does not scrape YouTube
or connect to the YouTube Data API.

## Calculation

For each candidate video, calculate the median views of the other supplied
videos from the same channel (leave-one-out baseline). Then calculate:

`views_multiple = candidate_views / same_channel_median_views`

The default outlier threshold is 2.0x. A channel needs at least three videos
for a candidate to have two comparison videos after excluding itself. If the
baseline is zero, a positive-view candidate is represented as infinite multiple;
interpret that case cautiously and inspect the underlying data.

## Interpretation safeguards

- Compare within a channel first; do not rank channels by raw views.
- Keep retrieval dates and source URLs with every result.
- Do not mix Shorts and long-form videos without explicitly segmenting them.
- Match video age or record it; older videos have had more time to accumulate views.
- Treat outliers as research leads, not proof of why a video succeeded.
- Investigate topic, packaging, format, timing, and audience fit separately.
- Do not infer views, subscribers, CTR, retention, or revenue when not supplied.
- Sample records are synthetic and must never be presented as live findings.

## Current implementation boundary

`youtube_agent.outliers` performs deterministic analysis on supplied records.
Automated discovery, API credentials, pagination, rate-limit handling, and
live collection are not implemented.
