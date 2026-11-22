# Architecture

## System shape

The engine is a coordinator plus specialist skills. The coordinator owns workflow state, passes structured outputs between skills, checks prerequisites, and stops at approval gates.

```text
Channel Profile -> Research -> Idea Lab -> Script Studio -> Packaging
                                      |                       |
                                      +---- Production Editor-+
                                               |
                                      Shorts / SEO / Community
                                               |
                                          Approval Gate
                                               |
                                      Creator publishes manually
                                               |
                                      Analytics -> Learning Loop
                                               |
                                      Channel Profile updates
```

## Competitor research adapter

The research layer can collect public competitor uploads through the optional
YouTube Data API v3 adapter when an API key is configured. It discovers
channels by keyword, resolves their uploads playlists, retrieves recent video
statistics, and preserves source URLs and retrieval timestamps. The same
analysis core also accepts offline JSON records. Live collection is optional;
API errors, missing public view counts, and quota limits must remain visible.

## Shared channel context

All skills consume a versioned profile containing channel identity, niche, audience, language, geography, voice, content pillars, formats, cadence, production capacity, goals, constraints, and performance baselines.

Skills must not silently rewrite the profile. Proposed changes require evidence and a recorded rationale.

## Standard skill output

Each skill returns:
- `status`: complete, needs_input, blocked, or partial
- `summary`: concise result
- `artifacts`: generated deliverables
- `evidence`: source URL, retrieval date, and relevant excerpt or metric
- `assumptions`: explicit assumptions
- `confidence`: low, medium, or high, with reason
- `next_step`: next skill or creator decision

## Evidence labels

- **Measured:** directly provided by analytics or a primary source.
- **Sourced:** supported by a cited public source.
- **Estimated:** calculated from incomplete inputs; show method.
- **Hypothesis:** plausible explanation that still needs testing.

Never invent view counts, search volumes, CTRs, retention values, competitor results, or audience demographics.

## Approval boundaries

Creator approval is required before publishing, scheduling, deleting, spending money, sending community replies, or changing connected account settings. Draft generation and read-only analysis may proceed without approval.

## Learning loop

Compare each video with the channel's own baseline and comparable formats. Record the measurement window, relevant attributes, plausible explanations as hypotheses, and one or two next experiments. Do not turn one video's result into a universal rule.
