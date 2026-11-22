# Executable Offline Pipeline

The pipeline executes available deterministic handlers in sequence:

1. Profile validation
2. Research evidence validation/brief
3. Supplied-data competitor outlier analysis
4. Idea scoring
5. Script outline template
6. Packaging directions
7. Transcript edit cue plan
8. Shorts excerpt shortlist (length heuristic)
9. Metadata draft
10. Performance analytics (median comparison)
11. Optional hypothesis/learning record
12. Comment review classification
13. Capacity-limited weekly task planning
14. Creator approval gate

Some outputs are templates or simple heuristics rather than model-generated
content. The pipeline labels unavailable/optional stages and blocked inputs.
It does not fabricate live research, transcripts, or metrics.

## Run

```bash
youtube-pipeline examples/pipeline-input.sample.json --output pipeline-output.json
```

Input keys can include `topic`, `profile`, `research_items`,
`competitor_videos`, `ideas`, `audience`, `angle`,
`duration_minutes`, `transcript_segments`, `description_facts`,
`keywords`, `performance_videos`, `observation`, `hypothesis`,
`next_test`, `evidence`, `comments`, `tasks`, and `weekly_capacity`.

Empty collections are permitted for an initial dry run. External side effects,
publishing, upload, comment replies, and scheduling are disabled. Creator review
is required. Do not include API keys or private credentials in input files.
