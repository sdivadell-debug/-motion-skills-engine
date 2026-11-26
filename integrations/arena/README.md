# Arena Skill integration

Upstream: https://github.com/Jakeschincariol/arena-skill  
Upstream license: MIT (see upstream LICENSE). This repository includes the upstream skill and its supporting files under `.claude/skills/arena/`.

## What it does

Arena is a Claude Code skill that runs a single-elimination tournament of sub-agents on one task. Each competitor receives the same task plus a different strategy card. Competitors attack and defend solutions, and Claude judges each match against the written rubric. The surviving answer is returned for the user to review; Arena does not prove that the winner is correct.

## Recommended use

- Everyday tasks: `/arena --quick` (16 competitors, 91 sub-agent calls).
- Important tasks only: `/arena --agents 100` (100 competitors, 595 sub-agent calls).
- Smaller custom run: `/arena --agents 8` or another supported count.
- The skill defaults to 100 if no size flag is supplied. Explicitly choose `--quick` to control usage.

## Requirements and limitations

- Requires Claude Code with the Agent/sub-agent tool and Python 3.8 or newer.
- It is not a directly executable feature in the ordinary Claude.ai mobile app.
- Agents use the configured Claude model; 100 agents are not 100 independent model providers.
- The skill is free and MIT-licensed, but model usage is not free. A 100-agent tournament is estimated at 595 sub-agent calls; 16 agents at 91. Actual token charges/usage depend on task size and provider plan.
- Sub-agents write run artifacts under `.arena/`. The upstream instructions say the skill does not directly edit project files; applying any proposed code changes remains the user's choice.
- Results are comparative, not guaranteed correct. Verify important claims and test code independently.

## Safety and approvals

Use `--quick` by default. Before any large run, review the estimated calls and obtain explicit user approval. Keep Claude Code permission prompts enabled; do not switch to accept-edits mode automatically. Do not send client messages, publish content, make purchases, transfer funds, or deliver client work based only on an Arena winner. Require the repository owner's approval for external actions and review all outputs for lawful, ethical, rights-cleared work.

## Included files

- `.claude/skills/arena/SKILL.md` — orchestration instructions.
- `.claude/skills/arena/bracket.py` — tournament state machine.
- `.claude/skills/arena/strategies.json` — strategy cards.
- `.claude/skills/arena/rubric.md` — judging rubric.

This is a source integration, not an installation into Claude Code. Follow the upstream installation instructions for the environment where Claude Code runs.
