---
name: competitor-research
description: Discover relevant YouTube channels and identify videos that outperform their own channel baseline using documented public metrics.
---

# Competitor Research Skill

## Objective

Produce a small, evidence-backed competitor landscape and a ranked set of video outliers. The goal is to discover repeatable audience opportunities, not copy creators or promise virality.

## Inputs

- Channel profile: niche, target audience, language, geography, content formats.
- One or more discovery keywords.
- Optional competitor channel IDs or supplied video records.
- Optional API key configured through `YOUTUBE_DATA_API_KEY`; never request or print the secret in chat.

## Workflow

1. Confirm the keyword matches the channel's niche and audience.
2. If the official API adapter is configured, discover candidate channels and collect recent public uploads. Otherwise, accept user-supplied records or clearly label research as unavailable.
3. Preserve channel ID, video ID, title, publication time, view count, source URL, and retrieval timestamp.
4. Exclude records without public view counts; report how many were skipped.
5. Segment Shorts and long-form before comparing when format metadata is available. Do not silently mix unlike formats.
6. Compare each candidate with the median views of other supplied videos from the same channel. Use the leave-one-out baseline implemented by `youtube_agent.outliers`.
7. Rank outliers, but treat them as leads for qualitative review.
8. Inspect the title, topic, audience promise, structure, and publication context before suggesting an adaptation.
9. Return source links, retrieval dates, sample size, data gaps, and limitations.

## Output contract

Return:
- `status`: complete, partial, needs_input, or blocked
- `channels`: channel IDs, names, and links
- `outliers`: video title, URL, views, same-channel median, multiple, and publication date
- `method`: source, retrieval timestamp, sample size, threshold
- `caveats`: missing metrics, format comparability, sample limitations
- `opportunities`: audience problem and differentiated angle to test

## Non-negotiable rules

- Never fabricate views, subscribers, CTR, retention, revenue, or search demand.
- Never present public view counts as private analytics.
- Never claim the API search result is a complete competitor census.
- Do not infer causation from a high views multiple.
- Do not recommend copying a competitor's script, branding, or thumbnail.
- Do not publish or schedule anything. Creator approval is required for external actions.
