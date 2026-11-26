# Project Context Handoff

A portable skill for creating an evidence-backed `HANDOFF.md` so a fresh AI session or human contributor can resume a project without repeating investigation.

## Upstream

- Source: https://github.com/r1shul/project-context-handoff-skill
- License: MIT
- Local skill: `.claude/skills/project-context-handoff/`
- Template: `.claude/skills/project-context-handoff/assets/HANDOFF_TEMPLATE.md`
- Validator: `.claude/skills/project-context-handoff/scripts/validate_handoff.py`

## Use it

In a supported Claude Code environment, invoke:

```text
/project-context-handoff
```

Or ask naturally:

```text
Create a project context handoff so another AI agent can continue from here.
```

The skill inspects available project evidence, distinguishes verified completion from in-progress work, preserves decisions and failed attempts, and records one precise next action. By default it creates or updates `HANDOFF.md` at the project root. It avoids writing credentials or secret values.

Validate a generated handoff with:

```bash
python3 .claude/skills/project-context-handoff/scripts/validate_handoff.py HANDOFF.md
```

The validator checks structure and common secret-assignment patterns; it cannot prove that the handoff's factual claims are correct.

## Important scope

This adds the skill files and instructions to this repository. It does not create a live `HANDOFF.md` for the current project, because that file must be generated from the actual working tree and session evidence at the time a handoff is requested. It does not install software globally or configure Claude.ai mobile/web chat. The skill is intended for Claude Code and other Agent Skills-compatible runtimes.

See the upstream repository for changes and compatibility notes: https://github.com/r1shul/project-context-handoff-skill
