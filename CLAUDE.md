# Instructions for Claude

When working on video editing in this repository, first read `.claude/skills/video-editing/SKILL.md`. Its upstream source is AskEditor/ai-video-editing-skills.

Important: the imported skill instructions alone are not the complete runtime. Check `skills/video-editing/README.md` and verify the companion scripts/assets exist before attempting setup or execution. Do not claim an edit was rendered unless the output file was actually produced and checked.

For this repository's YouTube workflow, preserve the existing evidence-first approach and require the creator's approval before publishing or taking external channel actions.

For official ChatGPT/OpenAI API references in this project, see `integrations/chatgpt/README.md`. This is documentation and links to official resources, not a local copy of ChatGPT.

For the Roast Room multi-advisor business decision workflow, read `integrations/roast-room/README.md` first. This is an integration guide only; do not claim Roast Room is installed or run setup commands without the user's approval.

For MiroFish swarm-based scenario simulations, read `integrations/mirofish/README.md` first and consult the official upstream repository for current setup details. This is a guide only; do not install or run MiroFish, create accounts, or handle API credentials without the user's separate approval.

For cross-model development workflows using Claude Code and Codex CLI, read `integrations/claudex-loop/README.md` first and consult the official upstream project for current installation and security details. This is documentation only; do not install, authenticate, or execute it without the user's separate approval.

When the user asks to pause, switch agents, or preserve project state for a future session, use `.claude/skills/project-context-handoff/SKILL.md` and its template to create or update a root-level `HANDOFF.md`. Base claims on repository and session evidence, distinguish verified work from in-progress work, never include secrets, and leave exactly one actionable next step. This skill is installed in the repository for Claude Code; it does not automatically add persistent context to ordinary Claude.ai chats.

For the ethical freelance video-production workflow, read `.claude/skills/freelance-video-agency/SKILL.md` first. It covers project qualification, ethical/halal-oriented screening, proposals, production QA, privacy, and human approval before client contact, commitments, payment actions, publishing, or delivery. For the recommended agent-driven editing tool, see `integrations/diffusion-studio/README.md`. These files document a workflow; they do not install software or authorize external actions.
