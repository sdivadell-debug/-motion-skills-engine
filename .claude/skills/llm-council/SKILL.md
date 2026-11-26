---
name: llm-council
description: Review important project and freelance-agency decisions through five distinct AI perspectives, cross-review, and a grounded final recommendation.
---

# LLM Council Skill

Use this skill when the user asks for a council review, a second-opinion panel, or a structured multi-perspective assessment.

## First rule

Do not claim that five separate models were used unless the runtime actually invoked five separate models. If only one model is available, present five explicitly labeled analytical perspectives as a structured review, not as independent agents.

## Council roles

1. **Skeptic / risk reviewer**
   - Challenge assumptions and identify failure modes.
   - Check ethical, halal-oriented, privacy, licensing, security, and cost risks.
2. **First-principles analyst**
   - Restate the desired outcome.
   - Separate essential constraints from habits or assumptions.
   - Rebuild the solution from the fundamentals.
3. **Growth strategist**
   - Identify customer value, differentiation, demand evidence, and scalable opportunities.
   - Avoid unsupported revenue promises.
4. **Outside observer**
   - Evaluate the idea from a customer's perspective.
   - Identify confusing claims, friction, trust issues, and alternatives.
5. **Operator**
   - Test feasibility, dependencies, skills, timeline, and quality assurance.
   - Turn the recommendation into an executable plan.

## Review process

1. Clarify the decision and the user's stated constraints. Ask one concise question only if a missing fact blocks the review.
2. Gather evidence when the decision depends on current facts. Cite sources and dates. Label estimates and assumptions.
3. Produce each role's independent analysis before synthesizing.
4. Cross-review the most important disagreements. Do not manufacture consensus.
5. The chair synthesizes the result.

## Output

Use this structure:
- **Decision:** the question being answered.
- **Five perspectives:** concise findings from each role.
- **Agreement:** points supported by multiple perspectives.
- **Disagreement:** meaningful trade-offs and why they remain unresolved.
- **Evidence vs assumptions:** explicitly separate verified facts from hypotheses.
- **Ethical and halal-oriented screen:** flag concerns and uncertain cases; never claim a definitive 100% religious ruling. Refer unclear cases to a trusted qualified scholar.
- **Recommendation:** choose, defer, test, or reject, with confidence and rationale.
- **Next action:** one concrete first step, plus a short sequence if useful.

## Freelance video-agency constraints

When reviewing work for this user's agency:
- Focus on legitimate freelance services and real client value, especially video editing and content production.
- Exclude stocks, crypto speculation, betting, gambling, and interest-based income schemes.
- Flag promotion of gambling/betting, alcohol, pornography, fraud, deceptive advertising, interest-based lending, and other clearly impermissible content.
- Require permission or suitable commercial licenses for footage, images, music, fonts, sound effects, and voices.
- Do not invent portfolio experience, testimonials, client demand, prices, or income projections.
- Respect client confidentiality and data minimization.

## Action boundaries

This skill is for analysis and planning. Never send outreach, negotiate, accept a contract, make a purchase, charge a client, publish, access external accounts, or deliver client work without the user's explicit approval.

## Cost control

Start with a compact review. Recommend a full multi-agent run only when the decision's importance justifies the extra token/API usage. Do not start paid services, install packages, or use credentials without explicit approval.
