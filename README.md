# YouTube Agent Engine

An evidence-first operating system for planning, producing, improving, and learning from a YouTube channel.

This project evolves the workflow ideas in [youtube-agent-skill](https://github.com/Jakeschincariol/youtube-agent-skill) into a coordinated system. It is not an unattended publishing bot: the creator stays in control of approvals and publishing.

## Product principles

- Evidence before confidence: distinguish measured data, sourced observations, estimates, and hypotheses.
- One coordinated workflow: research, ideation, scripting, packaging, editing, publishing preparation, and analysis share channel context.
- Channel-specific learning: recommendations improve from actual performance history, not generic viral formulas.
- Human approval: no publishing, replying, or irreversible action without explicit approval.
- Honest capability boundaries: never claim live research, analytics access, or integrations unless configured and verified.

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

## Project status

Foundation phase. See [architecture](docs/ARCHITECTURE.md) and [roadmap](docs/ROADMAP.md).
