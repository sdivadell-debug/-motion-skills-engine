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

For structured multi-perspective decision reviews, read `.claude/skills/llm-council/SKILL.md` and `integrations/llm-council/README.md`. Use five clearly labeled perspectives, distinguish evidence from assumptions, and disclose when these are role-based analyses rather than separate model calls. This is decision support only; require explicit approval before external actions.

For the proposed Team-X AI-agent company setup, read integrations/team-x/README.md and .claude/skills/ethical-video-agency-operations/SKILL.md. Start with a small agency team, keep costs and permissions limited, apply ethical/halal-oriented screening, protect client data, and require explicit user approval before any external/client-facing action. These are planning documents only; Team-X is not installed or configured by this repository.

For the proposed 21-agent Agency coordination system, read integrations/agency-21/README.md and .claude/skills/agency-21-agent-coo/SKILL.md. Agency is a coordination dashboard, not an autonomous 21-worker runtime. Follow the COO reporting, ethical screening, human approval, privacy, and budget rules. Do not enable unattended dispatch for integrations that use permission-bypass flags. These files are guidance only; Agency is not installed or running.

For multi-agent solution tournaments, read `integrations/arena/README.md` and `.claude/skills/arena/SKILL.md` first. Prefer `--quick` (16 agents) for routine use; a 100-agent run is estimated at 595 sub-agent calls and must not be launched without explicit approval. Keep permission prompts enabled and independently verify winning outputs. Arena requires Claude Code and Python 3.8+; it is not directly runnable in the ordinary Claude.ai mobile app.
For client-specific scroll-driven landing pages and scrollytelling, read `.claude/skills/scrollytelling/SKILL.md` and `integrations/scrollytelling/README.md`. Treat this as an industry-agnostic workflow: choose the visual subject, story, and technology from each client's brief; 3D is optional, not a default. Follow accessibility, performance, asset-rights, QA, privacy, and approval requirements.
