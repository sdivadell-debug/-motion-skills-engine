# Workflow Orchestrator

The orchestrator provides a structured plan for a multi-stage YouTube workflow:

1. Channel profile
2. Research
3. Competitor research
4. Idea lab
5. Script studio
6. Packaging
7. Production editor
8. Shorts cutter
9. SEO publisher
10. Creator review

It stores a plan with explicit stage status and handoff inputs. The current
orchestrator creates plans and accepts stage-status updates; it does **not**
automatically invoke the external specialist skills, browser research, video
editing, or YouTube publishing. These integrations require additional adapters.

## Create a plan

```bash
youtube-workflow-plan "topic or working title" --output plan.json
```

Optional profile file:

```bash
youtube-workflow-plan "topic" --profile channel-profile.json --output plan.json
```

## Workspace memory

`ChannelMemory` stores channel profile, research notes, idea history, and
experiments in a JSON file. It is local to the user's execution environment and
is not a remote shared database. Keep secrets out of memory. Back up and protect
the file as any other project data.

## Approval boundaries

Creator review is an explicit workflow stage. This plan does not publish,
schedule, post comments, upload assets, or make account changes.
