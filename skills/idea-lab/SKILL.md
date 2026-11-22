---
name: idea-lab
description: Convert audience problems and verified research signals into differentiated, ranked YouTube video concepts.
---

# Idea Lab Skill

## Objective
Create a prioritized slate of video concepts aligned with the channel profile. Optimize for audience value and feasible differentiation, not raw trend-chasing.

## Inputs
- Versioned channel profile.
- Research brief with source URLs and retrieval dates.
- Competitor outlier report when available.
- Production capacity, format, and publishing constraints.

## Workflow
1. Extract audience problems, questions, and desired outcomes from sourced evidence.
2. Separate measured observations, sourced facts, estimates, and hypotheses.
3. Generate distinct concepts; do not paraphrase competitor titles as the concept.
4. For each concept, define audience, problem, promise, unique angle, format, and proof required.
5. Score each concept using `youtube_agent.idea_scoring` and the configured weights.
6. Explain uncertainty and missing evidence. Do not treat the score as a view forecast.
7. Recommend a short test slate rather than presenting one idea as guaranteed.

## Output
Each idea includes: working title, audience, problem, promise, unique angle, format, evidence URLs, evidence notes, score breakdown, confidence, production effort, and next validation step.

## Guardrails
- Never invent search volume or audience demand.
- Do not confuse competitor performance with proof of demand for this channel.
- Flag ideas that require expertise, permissions, equipment, or costs not in the channel profile.
- Keep creator approval before committing the calendar.
