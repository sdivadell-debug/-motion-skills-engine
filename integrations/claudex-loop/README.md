# Claudex Loop — Cross-model planning, building, and review

Official upstream project: https://github.com/chaseai-yt/claudex-loop

## What it does

Claudex Loop is a set of skills for coordinating Claude Code and OpenAI Codex CLI. It supports a cross-provider software workflow:

1. The current host gathers requirements and writes a plan with acceptance checks.
2. The other provider independently reviews the plan and returns evidence-backed findings.
3. The coordinator revises the plan until it is approved, blocked, or the review-round limit is reached.
4. The selected builder implements the approved plan.
5. The other provider inspects the resulting changes and proof checks.

The repository also includes Claudex Route for task/model recommendations and one-off handoffs. Route is separate from the full Loop workflow.

## Important distinction

This is primarily a developer workflow for Claude Code and Codex CLI. It is not a feature that automatically adds a second model to the ordinary Claude.ai mobile/web chat. Both command-line tools need to be installed and authenticated for the full cross-provider workflow.

## Requirements described upstream

- Claude Code CLI, installed and authenticated
- OpenAI Codex CLI, installed and authenticated
- Python 3.10 or newer for the shared adapter
- Access to the models configured in each CLI; model availability depends on the user's accounts and configuration

The upstream README currently describes plugin installation for Claude Code and manual skill installation for Codex or Claude Code. Exact commands, compatibility, supported models, and security controls may change, so consult the official repository before installation:

https://github.com/chaseai-yt/claudex-loop

## Cost, permissions, and safety

- The workflow uses the user's Claude and Codex account limits; it does not create free model quota or bypass provider limits.
- Cross-provider review and repeated rounds can consume additional usage.
- Review does not guarantee correctness. Inspect evidence, diffs, and test results.
- Keep API keys and authentication material out of this repository.
- Read upstream permission boundaries and runtime documentation before running it on important projects.
- Do not run installation, authentication, delegated commands, or code changes without the user's explicit approval for that step.

## Instructions for Claude in this repository

When the user asks about Claudex Loop, read this guide and then check the official upstream README and runtime/security documentation for current details. Explain that both CLIs and their account access are required for the full workflow. Do not claim it is installed or configured based on this guide.

This file is documentation only. It does not clone, install, configure, or execute Claudex Loop.
