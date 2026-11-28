---
name: analytics
description: Analyze verified YouTube channel and video performance, compare like-for-like formats and age windows, diagnose retention patterns, and propose measurable experiments without inventing metrics.
---

# YouTube Analytics Skill

## Objective
Turn verified channel analytics into careful, useful decisions. Separate measured facts, comparisons, hypotheses, and recommendations. Never promise views or virality.

## Data sources and permissions
- Prefer the official YouTube Analytics API v2 for private channel metrics after the owner explicitly completes Google OAuth consent.
- Request only `https://www.googleapis.com/auth/yt-analytics.readonly`. Never request upload, manage, delete, or write scopes for analytics.
- Use `channel==MINE`; do not query another creator's private analytics.
- The API adapter is `src/youtube_agent/youtube_analytics_api.py`. It accepts an access token supplied by a secure caller; do not print, log, commit, or ask the user to paste access/refresh tokens into chat.
- The API exposes views, watch time, average view duration/percentage, engagement and per-video audience-retention reports, subject to report compatibility and data availability.
- YouTube Studio impressions click-through rate (CTR) is not included in the API v2 metric set documented for this project. Accept CTR only from a verified Studio export or user-supplied report, label its source, and never derive it from views.
- Do not request monetary/revenue metrics. They are outside this skill's scope.

## Required inputs
- Reporting start and end dates.
- Video ID and title where available.
- Format: `shorts`, `long_form`, or `live`.
- Video age at measurement, or a consistent `age_window_days` cohort.
- Metric origin and retrieval/export date.

## Workflow
1. Validate date range, source, metric origin, format, and reporting window.
2. Fetch read-only per-video metrics when OAuth is configured; otherwise analyze supplied CSV/JSON/Studio exports and clearly state that no live connection was made.
3. Keep Shorts, long-form, and live videos in separate cohorts. Compare only similar publication-age windows; do not compare lifetime totals with first-7-day results.
4. Review views, impressions/CTR when supplied, watch time, average view duration, average view percentage, likes, comments, shares, and subscribers gained only when present.
5. For a selected video, inspect the audience-retention curve using elapsed video time, audience watch ratio, and relative retention performance when available. Use `summarize_retention_curve` to locate the steepest observed drop; do not claim it explains why viewers left.
6. Fetch channel or single-video traffic-source categories with `fetch_traffic_sources` when authorized. Explain that the API returns supported source categories, not necessarily every detailed referrer.
7. Build cohort baselines using the median. Require at least three comparable videos by default; mark smaller cohorts as insufficient rather than drawing a strong conclusion.
8. Identify observable patterns (for example, a retention drop at a timestamp) separately from possible explanations (hypotheses).
9. Recommend one or two measurable experiments with a metric, comparison window, and success criterion. Do not claim an experiment caused an outcome without suitable evidence.
10. Produce a weekly or monthly summary only from dated data covering the stated period.

## Output contract
Return:
- reporting window, retrieval date, source, and permission mode
- a metric table with units and missing-data markers
- separate format/age cohort baselines and sample sizes
- strongest observations and confidence level
- retention timestamps or curve findings when available
- CTR/traffic-source provenance, or an explicit unavailable marker
- hypotheses, alternative explanations, and data gaps
- one or two experiments with measurable success criteria

## Safety and accuracy guardrails
- Never invent views, impressions, CTR, retention, watch time, traffic sources, subscribers, or revenue.
- Never infer private CTR or retention from public view counts.
- Never mix Shorts and long-form baselines.
- Do not present correlation as causation or a small sample as a reliable trend.
- Do not expose OAuth credentials or store them in repository files.
- Read-only analysis only. Do not publish, schedule, edit, delete, reply, spend, or change channel settings.
- Require explicit owner approval before any external action, even if another tool offers it.
