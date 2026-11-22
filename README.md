# YouTube Agent Engine

An evidence-first operating system for planning, producing, improving, and learning from a YouTube channel.

This project evolves the workflow ideas in [youtube-agent-skill](https://github.com/Jakeschincariol/youtube-agent-skill) into a coordinated system. It is not an unattended publishing bot: the creator stays in control of approvals and publishing.

## Current MVP

The first working core provides:
- transparent weighted scoring for video ideas
- explicit evidence status and confidence labels
- channel-normalized competitor outlier analysis using a leave-one-out median baseline
- documented competitor-data provenance and anti-misinterpretation rules
- validation of research claims, source URLs, dates, and metric origins
- a channel profile JSON Schema
- unit tests for scoring and evidence rules

## Run locally

Requires Python 3.10 or newer. No runtime third-party dependencies.

```bash
python -m pip install -e .
python -m unittest discover -s tests
python -m youtube_agent.cli examples/ideas.json
youtube-competitor-analysis examples/competitor_videos.sample.json

# Optional live collection (requires a YouTube Data API key)
youtube-competitor-fetch "your niche keyword" --channels 5 --videos-per-channel 15 --output competitor-data.json
youtube-competitor-analysis competitor-data.json
```

The ranking score is a prioritization heuristic, not a prediction of views or virality. Scores are only as reliable as the assessments and evidence supplied.

## Competitor outlier analysis

The current research core can analyze supplied competitor video records and flag videos that exceed a same-channel median baseline. See [competitor research protocol](docs/COMPETITOR_RESEARCH.md) and the clearly synthetic [sample dataset](examples/competitor_videos.sample.json). An optional official YouTube Data API v3 collector is now available when `YOUTUBE_DATA_API_KEY` is configured; it is not a web scraper. See [API setup and limits](docs/YOUTUBE_API_SETUP.md).

## Core workflow

1. Understand the channel: audience, niche, voice, constraints, goals, and analytics.
2. Research opportunities: audience questions, competitor outliers, search demand, and emerging topics with source links and dates.
3. Score ideas: audience fit, demand evidence, differentiation, production cost, and confidence.
4. Build the package: angle, hooks, script, title/thumbnail pair, description, and chapters.
5. Prepare production: edit decision list, B-roll cues, Shorts candidates, and quality checks.
6. Learn from results: compare outcomes with the channel baseline and update recommendations.

## Initial skill map

| Skill | Responsibility |
|---|---|
| channel-profile | Maintain channel context, voice, goals, and constraints |
| research | Gather and cite current topic and competitor evidence |
| competitor-research | Discover channels and rank same-channel video outliers |
| idea-lab | Generate, score, and prioritize video opportunities |
| script-studio | Develop hooks, structure, and spoken scripts |
| packaging | Optimize title and thumbnail as one promise |
| production-editor | Turn transcripts into edit decisions and asset cues |
| shorts-cutter | Identify standalone short-form moments |
| seo-publisher | Prepare descriptions, chapters, and metadata |
| community | Classify comments and draft on-brand replies |
| analytics | Diagnose retention, CTR, and performance against baseline |
| learning-loop | Convert verified outcomes into channel-specific guidance |
| weekly-planner | Turn priorities and capacity into a schedule |

## Trust and data rules

Every research claim should carry a source URL and retrieval date. Every metric should carry its origin and time range. Missing data must be marked as missing; estimates must be labeled. Correlations must not be presented as proven causes.

## Skill instructions

Each specialist's operating instructions are in `skills/<skill-id>/SKILL.md`. The skill registry lists the planned status of each component; a written skill contract does not by itself mean its automation is implemented.

## Project design

See [architecture](docs/ARCHITECTURE.md), [roadmap](docs/ROADMAP.md), and [skill registry](config/skills.json).
