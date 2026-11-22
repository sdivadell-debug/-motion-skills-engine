# Optional AI provider integration

AI-assisted draft commands use an OpenAI-compatible Chat Completions endpoint. No API key is stored in repository files.

Set environment variables in your local environment:
- `OPENAI_API_KEY` (required)
- `YOUTUBE_AGENT_MODEL` (optional, default `gpt-4o-mini`)
- `OPENAI_API_BASE` (optional endpoint override)

Examples:
```bash
youtube-agent-ai script "Video topic" --audience "new viewers" --angle "practical" --output script.json
youtube-agent-ai ideas "home renovation" --audience "DIY beginners"
```

These commands produce drafts only. They do not upload, publish, message, or modify a channel. Verify research claims and outputs before use. Endpoint overrides are intended for trusted compatible providers.
