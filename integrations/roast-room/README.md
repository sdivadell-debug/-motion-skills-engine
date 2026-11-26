# Roast Room

Official project: https://github.com/nateherkai/roast-room

Roast Room is a Claude Code workflow that convenes AI advisor agents to debate a business decision, score the options, and produce a written verdict plus a downloadable PDF. The default council includes simulations inspired by the public work of Jeff Bezos, Paul Graham, Alex Hormozi, Gary Vaynerchuk, Dan Martell, Gino Wickman, and Warren Buffett. These are AI simulations, not the real people and not endorsements.

## Important distinction

This folder is an integration note and discovery pointer. It does **not** contain a copy of Roast Room, install it, or make it available inside the ordinary Claude.ai chat interface. The upstream repository remains the source of truth. Review its current README, source, dependencies, and licence before cloning or running it.

## Requirements and upstream setup

According to the upstream README:

- Claude Code.
- Node.js 20 or newer.
- Clone the upstream repository and run it from its own folder:

```bash
git clone https://github.com/nateherkai/roast-room.git
cd roast-room
npm start
```

- Keep the local room running, open `http://localhost:4730`, then open Claude Code in that same folder.
- Run `/roast-room` followed by the business decision you want examined. The verdict is shown in Claude Code and the room provides a PDF download.
- The upstream README also documents `/roast-room --quick` for a smaller four-advisor, two-round session, and `/roast-room ask <advisor>` for one advisor.

Do not run installation commands automatically. Inspect the upstream repository and ask the user before installing dependencies, starting local services, or accessing external accounts.

## Usage and cost caution

The upstream README says a full council uses 21 sub-agent runs and can consume a substantial amount of the Claude plan's usage. Prefer `--quick` for an initial test. The optional API mode requires an Anthropic API key and bills the API account; do not enable it unless the user explicitly chooses that mode.

Because this user may be on Claude Free, explain that Roast Room does not increase Claude's allowance and may exhaust the available usage quickly. Do not promise that a full session will fit within the free allowance.

## How Claude should discover this integration

When the user asks about Roast Room, a founder council, or wants a business decision challenged by multiple AI advisors:

1. Read this file.
2. Check the upstream README for current setup instructions: https://github.com/nateherkai/roast-room
3. Explain the requirements and usage trade-offs before setup.
4. Ask for approval before cloning, installing, or running anything.
5. Never claim the tool is installed merely because this note exists.
