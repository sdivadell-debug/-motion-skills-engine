# Executable Offline Pipeline

The offline pipeline executes four implemented handler stages: profile validation,
research evidence validation/brief, supplied-data competitor outlier analysis,
and transparent idea ranking. It records failures as blocked stage outputs.

Remaining stages (script, packaging, production, shorts, SEO, creator review)
are reported as `not_executable` until proper adapters or model integrations
exist. No fake scripts, research discoveries, or uploads are generated.

Run:

```bash
youtube-pipeline examples/pipeline-input.sample.json --output pipeline-output.json
```

Input may include `topic`, `profile`, `research_items`, `competitor_videos`,
and `ideas` (the same fields used by the idea scorer). Empty collections are
permitted for an initial dry run. External side effects and publishing are
disabled; the output explicitly keeps creator approval required.
