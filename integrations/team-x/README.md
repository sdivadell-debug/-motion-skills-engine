# Team-X — AI company operating system

## Official project
- Upstream: https://github.com/Git-Rocky-Stack/Team-X
- Official site: https://team-x.app/
- Downloads: https://team-x.app/download/
- License: MIT (verify the current upstream LICENSE and release checksum before installing).
- This repository stores our agency setup plan and operating rules. It does not contain the Team-X desktop application or install it.

## What Team-X provides
The upstream project describes a local-first desktop application for managing AI-agent organizations. Its current v3.5.0 documentation describes:
- 57 curated role specifications (55 hireable roles plus two system roles).
- Six organizational levels and editable reporting lines.
- Goals, projects, tickets, schedules, employee messaging, and all-hands meetings.
- File vault, generated deliverables, audit log, backups, and usage/cost telemetry.
- Nine provider options, including Ollama for local models and optional cloud providers.
- Privacy tiers, per-employee tool permissions, and budget/authority approvals.

These are upstream product claims; confirm current version and feature availability in release notes before relying on them.

## Proposed company: ethical freelance video-production agency

Start with a small team. Do not hire all 57 roles at once; active agents can consume compute and/or model usage.

| Role | Responsibility | Initial authority |
|---|---|---|
| CEO / Owner | Strategic priorities and final decisions | Human owner retains final approval |
| COO | Break work into projects, tickets, and schedules | Assign internal tasks only |
| Sales Researcher | Find suitable public freelance opportunities and prepare lead notes | Research and draft only |
| Proposal Writer | Prepare tailored proposals and scope statements | Draft only; user sends |
| Creative Director | Translate briefs into creative direction and shot lists | Internal planning |
| Scriptwriter | Draft scripts and hooks | Draft; user reviews |
| Video Editor | Assist with editing plans, captions, pacing, and production tasks | Work on approved assets only |
| Motion Designer | Prepare graphics and animation concepts | Work on approved assets only |
| QA Reviewer | Check spelling, timing, audio, framing, rights, and deliverable requirements | Flag issues; no external delivery |
| Finance / Admin | Track approved quotes, expenses, and invoices | Recordkeeping only; no payments |

Add roles gradually as workload proves the need. One agent may cover more than one role during the pilot.

## Suggested pilot workflow
1. Create one company workspace named Ethical Video Studio.
2. Add the CEO/owner and COO roles first.
3. Add Sales Researcher, Proposal Writer, Creative Director, Video Editor, and QA Reviewer only when needed.
4. Create one test project using sample or public-domain footage, not confidential client material.
5. Assign tickets with a clear brief, owner, deadline, output format, and acceptance checklist.
6. Review agent output and usage/cost telemetry after each run.
7. Only after the workflow is reliable, consider using it for real client projects.

## Ethical and halal-oriented policy
This is an operating policy, not a fatwa or a guarantee that every project is halal. Review each client, brief, asset, and intended use. Reject or flag work promoting gambling/betting, alcohol, pornography, fraud, deceptive advertising, interest-based lending, or other clearly impermissible content. Refer uncertain religious cases to a trusted qualified scholar.

Use only client-owned, public-domain, or properly licensed footage, music, fonts, images, sound effects, and voices. Do not fabricate testimonials, impersonate people, mislead viewers, or claim results that cannot be substantiated.

## Human approval gates
Agents may research, plan, draft, edit approved source material, and prepare reports. They must not independently:
- Send cold outreach, DMs, emails, or proposals.
- Negotiate, accept contracts, or promise deadlines.
- Spend money, purchase subscriptions, or make payments.
- Upload client assets to external services without informed permission.
- Publish content or access a client's social accounts.
- Deliver final files or close a client project.

Require explicit approval from the user for each external/client-facing action.

## Privacy, security, and cost
- Team-X is a desktop app for Windows, macOS, and Linux; it does not run as a native Android app.
- Current upstream download instructions list Electron 44, Node.js 22+, and pnpm 9+ for source builds. Use official installers for ordinary desktop installation.
- The app is described as local-first and supports Ollama for local model inference. Cloud providers are optional and may incur separate API charges.
- Configure privacy tiers deliberately. Prefer local processing for confidential client content where hardware allows; otherwise obtain informed permission before cloud processing.
- Store provider credentials only through the app's supported OS keychain integration. Never commit secrets to this GitHub repository.
- Start with conservative budgets, limited tool permissions, and a small number of agents. Review cost telemetry regularly.
- Verify release checksums and read current release notes before installing.

## Status
Documented in this repository only. Team-X has not been downloaded, installed, configured, connected to a model provider, or run. No employee has been activated and no client data has been imported.

## Upstream links
- https://github.com/Git-Rocky-Stack/Team-X
- https://team-x.app/
- https://team-x.app/download/
