# Integration Playbook: 11 YouTube specialists -> Engine

This playbook maps the external 11-skill YouTube team into the existing engine. It avoids duplicating components and treats the engine as the system of record.

## Mapping

| External specialist | Existing engine stage | Reuse | Upgrade / acceptance check |
|---|---|---|---|
| yt-script | script-studio | hook and outline drafting | Produce 3 opening hooks and a structured script; preserve channel voice and cite research claims |
| yt-package | packaging | title/thumbnail brief | Deliver 3 title-thumbnail pairs, each with one promise and visual concept; avoid misleading packaging |
| yt-edit | production-editor | edit cues | Convert transcript to timestamped cuts, B-roll, overlays and audio notes; never invent timestamps |
| yt-comment | community | comment review | Classify, prioritize, draft replies; flag sensitive/ambiguous cases for creator approval |
| yt-plan | weekly-planner | calendar | Plan workload against stated capacity; balance formats and goals |
| yt-viral | competitor-research | outlier detection | Normalize against same-channel median and disclose sample limitations |
| yt-retention | analytics | retention diagnosis | Identify opening/decline intervals only from supplied retention data; mark hypotheses |
| yt-shorts | shorts-cutter | Shorts selection | Find standalone moments from transcript and produce hook/caption/crop notes |
| yt-seo | seo-publisher | metadata | Generate description, keywords and metadata without keyword stuffing or unsupported claims |
| yt-chapters | seo-publisher | chapter drafts | Draft chapter titles/boundaries from transcript or timecoded source; never fabricate timestamps |
| yt-audit | learning-loop + analytics | improvement review | Prioritize measurable actions and evidence gaps; distinguish measured facts from hypotheses |

## Shared contract

Every stage returns:
- status: complete, partial, needs_input, or blocked
- summary and deliverables
- evidence (URL, retrieval date, metric origin, or transcript timecode)
- assumptions and limitations
- confidence and rationale
- next action

## Pipeline

1. Validate the channel profile and source inputs.
2. Research and validate evidence.
3. Generate and score ideas.
4. Draft scripts and hook alternatives.
5. Generate paired packaging options.
6. Prepare edit decision list and Shorts candidates.
7. Prepare SEO and chapters.
8. Review comments (when provided).
9. Plan weekly workload.
10. Review performance/retention data (when provided).
11. Audit and record learning; propose profile changes, never silently apply them.

## Safety and reliability gates

- No fabricated metrics, transcript passages, citations, or timestamps.
- Clearly label measured, sourced, estimated, and hypothesis claims.
- Human approval before publishing, scheduling, deleting, spending, sending replies, or changing account settings.
- Missing inputs should yield a partial result or explicit request, not invented substitutes.

## Minimum release tests

- Missing channel profile is reported as a blocker or request for input.
- Claims without source/date are flagged.
- Missing timestamps are not invented.
- Packaging pairs avoid conflicting promises.
- Competitor outliers use a comparable same-channel baseline.
- Retention interpretations are limited to provided data.
- Community replies remain drafts.
- Weekly workload respects declared capacity.
