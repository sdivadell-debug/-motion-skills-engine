---
name: channel-profile
description: Maintain the canonical, evidence-backed operating profile for a YouTube channel.
---
# Channel Profile Skill

## Objective
Maintain one versioned source of truth for channel identity, audience, niche, voice, formats, goals, constraints, and measured baselines.

## Workflow
1. Gather only details the creator can verify or explicitly mark as assumptions.
2. Separate creator-provided facts, measured analytics, and hypotheses.
3. Capture audience segments, language, geography, content pillars, formats, cadence, capacity, equipment, and budget.
4. Record metric definitions, source, measurement window, and date for every baseline.
5. Propose profile changes with a reason and evidence; never silently rewrite it.

## Output
A schema-valid profile, missing-field list, assumptions, version, and proposed changes.

## Guardrails
Do not infer sensitive audience traits. Do not fabricate analytics. Ask for one missing critical field at a time. Creator approval is required for profile changes that alter strategy.
