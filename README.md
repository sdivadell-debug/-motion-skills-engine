# YouTube Agent Engine

An evidence-first operating system for planning, producing, improving, and learning from a YouTube channel.

This project evolves the workflow ideas in [youtube-agent-skill](https://github.com/Jakeschincariol/youtube-agent-skill) into a coordinated system. It is not an unattended publishing bot: the creator stays in control of approvals and publishing.

## Current MVP

The core provides:
- transparent weighted scoring for video ideas
- explicit evidence status and confidence labels
- channel-normalized competitor outlier analysis using a leave-one-out median baseline
- documented competitor-data provenance and anti-misinterpretation rules
- validation of research claims, source URLs, dates, and metric origins
- a channel profile JSON Schema and dependency-free profile validator
- a multi-stage workflow orchestrator and JSON workspace memory (planning mode)
- offline handlers for profile validation, research evidence checks, supplied competitor analysis, idea scoring, script-outline templates, packaging briefs, editing cues, Shorts shortlist heuristics, metadata drafts, analytics, learning notes, community review, and weekly planning

## Run locally

Requires Python 3.10 or newer.

```bash
python -m pip install -e .
python -m unittest discover -s tests
python -m youtube_agent.cli examples/ideas.json
youtube-competitor-analysis examples/competitor_videos.sample.json

# Optional live collection (requires a YouTube Data API key)
youtube-competitor-fetch "your niche keyword" --channels 5 --videos-per-channel 15 --output competitor-data.json
youtube-competitor-analysis competitor-data.json

# Workflow plan and offline pipeline
youtube-workflow-plan "video topic" --output workflow-plan.json
youtube-pipeline examples/pipeline-input.sample.json --output pipeline-output.json

# Optional AI drafts (requires OPENAI_API_KEY)
youtube-agent-ai script "Video topic" --audience "new viewers" --angle "practical" --output script.json
youtube-agent-ai ideas "home renovation" --audience "DIY beginners"
```

Scoring is a prioritization heuristic, not a prediction of views or virality. Scores are only as reliable as the assessments and evidence supplied.

## Optional AI drafts

An OpenAI-compatible provider can generate script and idea drafts when configured with an environment API key. See [AI provider setup](docs/AI_PROVIDER.md). Draft generation does not publish or take channel actions. The provider accepts JSON object outputs and reports unreadable or invalid responses as errors.

## Competitor research

The core analyzes supplied competitor video records and flags videos that exceed a same-channel median baseline. See [competitor research protocol](docs/COMPETITOR_RESEARCH.md) and the synthetic [sample dataset](examples/competitor_videos.sample.json). An optional official YouTube Data API v3 collector is available when `YOUTUBE_DATA_API_KEY` is configured; it does not scrape YouTube pages. See [API setup and limits](docs/YOUTUBE_API_SETUP.md).

## Core workflow

1. Understand the channel: audience, niche, voice, constraints, goals, and analytics.
2. Research opportunities: audience questions, competitor outliers, search demand, and emerging topics with source links and dates.
3. Score ideas: audience fit, demand evidence, differentiation, production cost, and confidence.
4. Build the package: angle, hooks, script, title/thumbnail pair, description, and chapters.
5. Prepare production: edit decision list, B-roll cues, Shorts candidates, and quality checks.
6. Learn from results: compare outcomes with the channel baseline and update recommendations.

## Skill map

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

Each specialist's operating instructions are in `skills/<skill-id>/SKILL.md`. The skill registry lists the planned status of each component; written skill instructions do not by themselves mean the automation is implemented.

## Project design

See [architecture](docs/ARCHITECTURE.md), [roadmap](docs/ROADMAP.md), and [skill registry](config/skills.json).


## Optional AI workflow review

Set `OPENAI_API_KEY` in your environment and include `ai_review: true` in the JSON payload passed to the workflow pipeline to request an evidence-grounded AI review. The review summarizes the pipeline's supplied results and returns priority actions, risks, recommendation, and evidence gaps. It is opt-in, requires provider access, and does not publish or perform external actions. If no key/provider is available, the review stage is reported as blocked; the rest of the offline workflow remains available.
