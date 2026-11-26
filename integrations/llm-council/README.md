# LLM Council — multi-perspective decision review

A documented option for reviewing important decisions with several independent AI perspectives.

## Upstream project

- Repository: https://github.com/aiwithremy/claude-skills-llm-council
- Review the upstream README, LICENSE, supported Claude environment, and current installation instructions before adopting or copying any upstream files.
- This repository contains our own workflow guide and custom skill instructions; it does not vendor or install the upstream implementation.

## How the council works

The upstream concept uses five Claude-based reviewer roles, followed by cross-review and a final synthesis. These are role prompts/personas, not necessarily five different underlying AI models or five independent sources of truth.

Our recommended roles for this project:

1. **Skeptic / risk reviewer** — finds weak assumptions, failure modes, legal, ethical, privacy, and cost risks.
2. **First-principles analyst** — reconstructs the problem from goals, constraints, and evidence.
3. **Growth strategist** — identifies opportunities, differentiation, and realistic ways to scale.
4. **Outside observer** — challenges internal bias and checks how a customer would perceive the proposal.
5. **Operator** — converts the strongest ideas into a practical sequence, resources, and measurable checks.

The chair then compares disagreements, distinguishes evidence from assumptions, and produces a recommendation with confidence and unresolved questions.

## Good uses

- Choosing which freelance creative service to offer.
- Evaluating a video-editing proposal, pricing structure, or workflow.
- Comparing production tools and automation designs.
- Reviewing a client brief for scope, feasibility, rights, and risks.
- Prioritizing the next improvement to the YouTube/video-production engine.

## Required output format

Every council report should include:
- Decision question and constraints.
- Short summary of each of the five perspectives.
- Points of agreement and disagreement.
- Evidence, assumptions, and unknowns clearly separated.
- Ethical/halal-oriented screening flags where relevant (not a fatwa).
- Recommended decision, alternatives, confidence, and reasons.
- Three practical next actions, with one clearly identified first action.

## Cost and reliability

- Multi-agent reviews can consume substantially more model usage than a single response. Start with a short review and reserve full cross-review for consequential decisions.
- Five role prompts do not guarantee five independent opinions; shared model/provider bias may remain.
- Treat the output as decision support, not verified fact, professional legal/financial advice, or religious ruling. Verify important claims independently.
- For time-sensitive research, require current sources and dates; do not let agents invent citations.

## Safety and approval

The council may draft recommendations, but it must not independently contact clients, send proposals, accept contracts, spend money, publish content, access client accounts, or deliver files. Require explicit user approval before external actions.

For this user's freelance content work, reject or flag projects involving gambling/betting, alcohol promotion, pornography, fraud, deceptive claims, interest-based lending, stolen media, or unlicensed assets. Ambiguous religious cases should be referred to a trusted qualified scholar rather than declared permissible.

## Integration status

This is a guide only. No upstream package has been installed, no API credentials have been configured, and no agents have been run. See the custom skill at `.claude/skills/llm-council/SKILL.md`.

## Upstream

https://github.com/aiwithremy/claude-skills-llm-council
