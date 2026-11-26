# Agency — 21-agent team coordination for Ethical Video Studio

## Upstream project
- Repository: https://github.com/christag/agency
- License: GNU Affero General Public License v3.0 (AGPL-3.0). Read the upstream LICENSE before modifying, hosting, or distributing a modified network-accessible version. This guide does not copy the upstream application.
- Python requirement: 3.11+
- Project type: local dashboard and coordination layer, not an agent model or autonomous worker by itself.
- Upstream README states it manages 21 agents across three groups in its own production setup. This is a report about the upstream author's setup, not a ready-made 21-person video-agency team.

## What it does
Agency provides a unified dashboard for agents that run through supported integrations such as Claude Code, Codex, Gemini, Aider, Goose, OpenCode, Pi, custom scripts, and SDK agents. Agents have persistent identities and histories. They can write observations and proposals; the owner can approve, defer, or reject proposals, and approved decisions can be dispatched to configured agents.

The dashboard includes agent status, activity, groups, a proposal/decision pipeline, logs, and scheduled dispatch. The dispatch scheduler uses host operating system timer facilities. Its documentation describes a 15-minute default heartbeat and configurable daily run limits.

Important: Agency is a coordination dashboard, not a complete autonomous workforce. Each worker needs a separately configured execution tool, model/provider access, role instructions, and permissions.

## Proposed 21-agent organization

The 21 positions below are a proposed roster for this user's freelance video-production agency. They are not built-in employees supplied by the upstream project. Start with a small pilot and activate roles gradually.

| # | Department | Role | Core responsibility |
|---:|---|---|---|
| 1 | Leadership | CEO / Owner | User; strategy and final approvals |
| 2 | Leadership | COO | Daily coordination, priorities, workload and reports |
| 3 | Sales | Market Researcher | Find suitable public freelance opportunities |
| 4 | Sales | Lead Qualifier | Assess client fit, budget signals and brief clarity |
| 5 | Sales | Proposal Writer | Draft tailored proposals and scope |
| 6 | Sales | Client Brief Analyst | Convert approved client briefs into requirements |
| 7 | Creative | Creative Director | Creative direction and visual treatment |
| 8 | Creative | Scriptwriter | Scripts, hooks and narration drafts |
| 9 | Creative | Storyboard Planner | Shot lists, scene plans and B-roll suggestions |
| 10 | Production | Senior Video Editor | Editing plan and primary assembly |
| 11 | Production | Short-form Editor | Reels, Shorts and TikTok versions |
| 12 | Production | Long-form Editor | YouTube and documentary edits |
| 13 | Production | Motion Designer | Titles, transitions and motion graphics |
| 14 | Production | Graphic Designer | Thumbnails and supporting graphics |
| 15 | Production | Caption Specialist | Arabic captions, timing and subtitle QA |
| 16 | Production | Audio Specialist | Dialogue cleanup, levels and licensed music checks |
| 17 | Production | Asset Researcher | Find rights-cleared footage, images and sound |
| 18 | Quality | Visual QA Reviewer | Framing, pacing, consistency and export checks |
| 19 | Quality | Language QA Reviewer | Spelling, Arabic wording and subtitle accuracy |
| 20 | Quality | Rights & Policy Reviewer | Usage rights, client fit and ethical screening |
| 21 | Operations | Finance & Admin Analyst | Track approved estimates, costs and invoices; no payments |

The user remains the real CEO and final decision-maker. AI role labels do not imply human-level judgment or guaranteed quality.

## COO daily operating routine
The COO should prepare (not silently execute) a daily report containing:
1. Team health: last activity, failed runs, and agents needing attention.
2. Project status: each active project, owner, due date, blockers, and next step.
3. Sales pipeline: newly discovered public opportunities and fit rationale.
4. Production status: drafts awaiting QA, revisions, and deliverables awaiting user review.
5. Cost report: model/provider usage where available, estimated spend, and budget warnings.
6. Risks: rights questions, privacy concerns, scope changes, suspicious requests, and ethical/halal flags.
7. Decisions required: a short list of explicit choices for the user.

Suggested cadence:
- Morning: prepare workload and opportunity summary.
- During the day: check project blockers and scheduled task results.
- End of day: summarize completed work, pending approvals, failures, and costs.

The COO must not send messages, submit proposals, negotiate, accept contracts, promise deadlines, spend money, publish content, or deliver files. It prepares recommendations for the user.

## Recommended groups in Agency
Create three separate groups to keep responsibilities and permissions understandable:
- Growth & Client Research — roles 3–6.
- Creative Production — roles 7–17.
- Quality & Operations — roles 18–21, with the COO coordinating across groups.

The CEO/Owner role is the user outside the autonomous agent roster. This gives 21 AI positions plus the human owner.

## Safe rollout plan
1. Install and test Agency locally before importing real client data.
2. Begin with only three agents: COO, Sales Researcher, and QA Reviewer.
3. Use sample/public-domain footage and a dummy project.
4. Configure read-only research and local file access narrowly.
5. Review every observation and proposal manually.
6. Add production roles only after the pilot is stable.
7. Increase scheduling limits slowly and review logs and costs daily.

## Critical execution and permission warning
The upstream dispatch documentation says its Claude Code integration can invoke Claude Code with the --dangerously-skip-permissions flag and its Codex integration can invoke Codex with the --yolo flag. These flags can bypass normal interactive permission checks. Therefore:
- Do not enable unattended dispatch for these integrations in a real client workspace.
- Do not give agents broad filesystem, browser, email, social-account, shell, or payment access.
- Use isolated test directories and least-privilege credentials.
- Keep external communication, client uploads, purchases, publishing, contracts, and final delivery behind explicit human approval.
- If safe approval controls cannot be enforced for a particular integration, do not connect that integration to sensitive work.

## Ethical and halal-oriented screening
This is an operational checklist, not a fatwa or a guarantee of permissibility. Screen each client, brief, asset, and intended use. Flag or reject work promoting gambling/betting, alcohol, pornography, fraud, deceptive claims, interest-based lending, or other content the user has instructed the agency to avoid. Pause uncertain cases for review by a trusted qualified scholar.

Use client-owned, public-domain, or properly licensed footage, music, fonts, images, sound effects, and voices. Do not fabricate testimonials, impersonate people, mislead viewers, or make unsupported claims.

## Privacy and cost
- Do not commit client personal data, raw footage, contracts, credentials, API keys, or payment information to Git.
- Do not upload confidential assets to cloud AI providers without informed client permission.
- Cloud model/API usage can incur separate costs; Agency itself does not make model usage free.
- Set low daily run limits and conservative timeouts for the pilot. Review logs and provider billing.
- Store secrets outside this repository using the operating system's secure credential facilities.

## Compatibility and setup notes
The upstream project documents Python 3.11+, FastAPI, Jinja2, and a file-based Markdown/YAML data store; it states that a database and Docker are not required. Follow the upstream installation and deployment docs for the current platform. Dispatch automation is documented for Linux (systemd) and macOS (launchd); Windows scheduling requires manual Task Scheduler setup according to the dispatch guide.

This is a desktop/server-style local dashboard, not an Android-native app. Running it on a computer and accessing its local dashboard from a phone may be possible on a suitably configured network, but that is not the same as native Android support.

## Status in this repository
This file and the companion skill are planning/configuration guidance only. The Agency application has not been downloaded, installed, configured, connected to providers, or run. No agents have been created or activated and no client data has been imported.

## Upstream documentation
- https://github.com/christag/agency
- https://github.com/christag/agency/blob/master/kb/getting-started.md
- https://github.com/christag/agency/blob/master/kb/dispatch.md
- https://github.com/christag/agency/blob/master/kb/agent-identity.md
- https://github.com/christag/agency/blob/master/LICENSE
