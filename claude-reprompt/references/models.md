# Sonnet and Opus guidance

Reviewed on 2026-11-07. This reference covers Claude Sonnet 5.5 and Claude Opus 5.5. Treat effort defaults, supported modes, and model IDs as version- and surface-specific.

## Choose the target

Preserve the model the user requested. If they ask for a recommendation, Sonnet 5.5 fits speed-sensitive and well-specified work. Consider Opus 5.5 for complex, open-ended work that requires sustained judgment, such as a migration with interacting changes across a large repository. Compare them on representative cases when the choice matters. [Models overview](https://platform.claude.com/docs/en/models/overview), [Sonnet 5.5 release](https://www.anthropic.com/claude-sonnet-5-5)

## Claude Sonnet 5.5

- For well-specified coding with tools, try `medium` effort first. For harder or longer coding, try `high`. The Claude API default is `high`. Reserve `xhigh` and `max` for measured gains. [Calibrate effort](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5#calibrate-effort)
- If Sonnet pauses on routine steps, name the work it should complete independently and when to ask. If it adds scope, name the completion condition and boundaries. For code edits, name a real check and ask for the result or the blocker. [Initiative and scope](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5#steer-initiative-and-scope), [Coding verification](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5#verification-on-coding-tasks)
- **Messages API.** Use adaptive thinking for reasoning-heavy tasks, including decisions that must be returned as JSON. `thinking.type: "between_tools"` skips up-front thinking and works at `high` effort or below. With no tools, it gives the model no initial thinking phase. For reasoning plus JSON, try adaptive thinking, structured outputs, and `high` effort. Treat a `max_tokens` stop as an incomplete attempt. [Thinking modes](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5#running-without-up-front-thinking), [Reasoning with JSON](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5#reasoning-tasks-with-json-output)

## Claude Opus 5.5

- Start at `medium`, the Claude API default. Measure the benefit before raising effort, especially to `xhigh` or `max`. If a run is too slow, try a lower setting before adding prose to constrain thinking. [Calibrate effort](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5#calibrate-effort)
- For long migrations or audits, state the deliverables, repository boundaries, checks, and what counts as done. Keep progress updates brief and tied to meaningful findings. In an unattended integration, use explicit task state to distinguish an interim text-only turn from completion. Bound automatic continuations and stop when user input or permission is required. [Unattended runs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5#unattended-agentic-runs), [Progress updates](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5#user-facing-progress-updates)
- **Messages API.** Opus 5.5 always uses adaptive thinking. Explicitly disabling it returns HTTP 400. Allow room for thinking within `max_tokens` and read response blocks by type. [Opus 5.5 migration guide](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide)

## Apply settings in the right place

| Surface | Where settings belong |
| --- | --- |
| Claude Code | Use the model picker (`/model`) and effort control (`/effort`), or launch with `--model` and `--effort`. Available options depend on the installation and provider. The skill inherits the active session settings. [Claude Code model configuration](https://code.claude.com/docs/en/model-config) |
| Messages API | Set `model` to `claude-sonnet-5-5` or `claude-opus-5-5` on Anthropic's API. Set effort in `output_config.effort` and use only the thinking modes accepted by that version. Check the provider's docs for its ID and supported settings. [Models overview](https://platform.claude.com/docs/en/models/overview), [Thinking](https://platform.claude.com/docs/en/thinking) |
| Claude chat | Use model and thinking controls if the interface offers them. Prompt text can ask for a result or a brief explanation. It cannot set API request fields. |

## Migrate an existing prompt

Start by running the old prompt on the new target. Adjust wording for observed failures and retest settings independently. Effort labels do not imply equal thinking across releases. For older pinned versions, consult the relevant guide before porting defaults, tool rules, or thinking options. [Sonnet 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5), [Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5), [Sonnet 5.5 migration guide](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide), [Opus 5.5 migration guide](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide)
