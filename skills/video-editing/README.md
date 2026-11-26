# Video Editing Skill — upstream package note

This folder contains the upstream Claude skill instructions from AskEditor.

- Upstream repository: https://github.com/AskEditor/ai-video-editing-skills
- Upstream skill file: https://github.com/AskEditor/ai-video-editing-skills/blob/main/SKILL.md
- License: MIT (see LICENSE)
- Imported source: AskEditor/ai-video-editing-skills, branch main
- Purpose: local editing of talking-head videos, including pause/retake removal, word-timed captions, B-roll, color looks, music, sound effects, motion graphics, and vertical social formats.

## Important: full runtime package is not vendored here

The upstream skill expects its companion files (such as `setup.sh`, effect scripts, assets, and Python modules) to sit beside `SKILL.md`. This repository currently stores the skill instructions and provenance, not the complete 277-file runtime package. Do not run its setup commands from this folder until the full upstream repository has been cloned into this folder or otherwise installed.

To install the complete runtime package, clone the upstream repository into this folder (or a separate local skill folder), then run the setup instructions in its upstream README. Review the scripts before running them.

## Claude discovery

Claude Code should discover the project skill at `.claude/skills/video-editing/SKILL.md`. The same instruction file is also kept at `skills/video-editing/SKILL.md` for this project's own skill layout.

If Claude does not automatically load it, ask: "Read `.claude/skills/video-editing/SKILL.md` and follow it for this video-editing task. First check whether the complete AskEditor runtime package is installed; do not run setup until its companion files are present."
