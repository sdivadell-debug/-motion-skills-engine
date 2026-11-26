---
name: project-context-handoff
description: Create or refresh a durable, evidence-backed project handoff so a different AI agent or human can resume work without repeating investigation or failed attempts. Use when the user explicitly asks to create, write, update, save, prepare, or finalize a handoff, continuation brief, session checkpoint, or context-transfer document; when pausing work or switching agents/models and asking to preserve state; or when ending a session and asking what the next agent should do. Do not use for a casual status question, standalone summary, plan, retrospective, or progress report unless the user wants a persistent handoff for a successor.
---

# Project Context Handoff

Create a compact continuation brief from project evidence and relevant session context. Optimize for the successor's first useful action, not for a chronological recap.

## Establish scope

1. Honor an explicit output path or filename.
2. Otherwise search the current project root for an existing handoff filename, case-insensitively: `HANDOFF.md`, `handoff.md`, `PROJECT_HANDOFF.md`, or `CONTEXT_HANDOFF.md`.
3. Update the single clear match. If several plausible files exist and choosing one risks overwriting the wrong artifact, ask which one to update. If none exists, create `HANDOFF.md` in the project root.
4. Preserve useful existing facts unless current evidence supersedes them. Do not erase unresolved history merely because it did not arise in the current session.

## Gather evidence

Inspect the project before drafting, using tools available in the host environment:

- Read applicable agent instructions, project documentation, task trackers, plans, and the existing handoff.
- Inspect version-control status, diff summary, current branch, and recent commits when version control exists.
- Read files relevant to active work and inspect tests, build output, issue data, or logs when available.
- Include session facts that may not exist on disk: user-stated goals, decisions and rationale, attempted approaches, errors, pending approvals, and promised follow-ups.
- Run only safe checks needed to resolve material uncertainty. Do not mutate product code, install dependencies, contact external systems, or run destructive commands solely to prepare a handoff.

If tools, version control, tests, or logs are unavailable, continue with the evidence that exists and state the limitation. Never invent missing repository state.

## Classify claims

- Put work under `Done` only when evidence shows it is complete. Name the verifying test, command, artifact, commit, or user confirmation when that detail helps.
- Put modified, uncommitted, partially implemented, unverified, or actively investigated work under `In Progress`.
- Treat a committed change as completed implementation, not automatically as shipped or deployed.
- Label inference or uncertainty explicitly.
- Record the current branch and uncommitted changes when relevant to safe continuation.
- Preserve decisions with their rationale and important constraints.
- Preserve failed attempts with the attempted action, observed result or error, likely cause if known, and a clear retry condition or warning.
- Distinguish a true blocker from a remaining task. A blocker prevents the next action; unfinished work alone is not a blocker.
- Never expose secrets, tokens, credentials, private keys, raw environment values, or unnecessary personal data. Mention only the secret's variable or configuration name when necessary.

## Select the next best step

Choose exactly one immediate action that most reduces risk or advances the goal. Make it executable by naming the target file, component, command, expected result, or acceptance condition when known. Do not use vague actions such as “continue implementation,” “fix remaining issues,” or “review the code.”

If the project is complete, use the next verification, release, review, or monitoring action. If no further action is needed, say so explicitly and name the completion evidence.

## Write the handoff

Use the exact headings and order in [assets/HANDOFF_TEMPLATE.md](assets/HANDOFF_TEMPLATE.md). Keep `Done` and `In Progress` as separate labeled bullets. Replace every template token. Write `None known` for an empty section.

Keep the document self-contained and concise, but prefer enough specificity to prevent rediscovery. Use repository-relative paths where possible. Add commands, test outcomes, issue numbers, commit identifiers, timestamps, or environment names only when they materially help the successor.

## Validate and report

Run `python3 .claude/skills/project-context-handoff/scripts/validate_handoff.py <handoff-path>` when Python and the bundled script are available. Resolve every reported structural error. If the script cannot run, manually confirm:

- all required headings occur once and in order;
- `Done`, `In Progress`, and `Action Item` are present and non-empty;
- no template token remains;
- completed and unverified work are separated;
- decisions include rationale;
- failures prevent repeated mistakes;
- exactly one specific action item remains;
- no sensitive value appears.

Return the handoff path, whether validation passed or was performed manually, and the next action in one sentence. Do not claim that validation proves factual accuracy; it checks structure and completeness only.
