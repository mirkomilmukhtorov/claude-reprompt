# Official Documentation Research Report

**Research snapshot:** 7 November 2026 (Malaysia time). **Evidence standard:** parent-company documentation and official Agent Skills specifications. This report is a point-in-time design basis, not proof of personal account access, benchmark superiority or ongoing availability.

## Executive findings

1. **OpenAI model IDs are not UI nicknames.** The official model catalog lists `gpt-6-astra`, `gpt-6.1-sol`, `gpt-6.1-terra`, and `gpt-6-luna`. The Responses API exposes model-specific `reasoning.effort` values; Astra and 6.1 Sol reject `none`. For supported models, `reasoning.mode` standard/pro is a separate concept. Source: https://developers.openai.com/api/docs/models and https://developers.openai.com/api/docs/guides/reasoning
2. **Current Claude exposes effort separately from its adaptive thinking behavior.** The official current model list includes `claude-fable-5-1`, `claude-opus-5-5`, `claude-sonnet-5-5`, and `claude-haiku-5-5`. Use `output_config.effort`; do not use legacy manual `budget_tokens` with the current 5.x family. Anthropic supports `low`, `medium`, `high`, `xhigh`, and `max` across these listed models; defaults differ. Sources: https://platform.claude.com/docs/en/models/overview , https://platform.claude.com/docs/en/build-with-claude/effort , https://platform.claude.com/docs/en/build-with-claude/extended-thinking
3. **Gemini 4 Argon and 3.8 Flash forbid minimal thinking.** Both support `low`, `medium`, and `high` thinking levels; Argon also forbids `thinking_budget`. The Google sources identify `gemini-4-argon`, `gemini-3.8-flash`, and the economical `gemini-3.5-flash-lite`. These names have API identifiers, but surface-level availability and billing requirements differ. Sources: https://firebase.google.com/docs/ai-logic/models , https://firebase.google.com/docs/ai-logic/thinking and https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/guides/gemini-4-argon
4. **Skills can be portable without host-specific frontmatter.** Agent Skills needs `name` and `description` in `SKILL.md`; OpenAI Codex, Claude Code and Gemini CLI support variations. Host-level tool access, activation and permissions remain separate. Sources: https://agentskills.io/specification , https://code.claude.com/docs/en/skills , https://geminicli.com/docs/cli/skills/ and https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md

## Verified comparison (select dimensions)

| Model/API ID | Provider | Primary official positioning | Effort options | Context / max output (tokens) | Price input/output per 1M tokens* |
|---|---|---|---|---|---|
| `gpt-6-astra` | OpenAI | Highest capability for complex tasks | low medium high xhigh max | 1,050,000 / 128,000 | $10 / $50 |
| `gpt-6.1-sol` | OpenAI | Complex work at lower cost | low medium high xhigh max | 1,050,000 / 128,000 | $2 / $10 |
| `gpt-6.1-terra` | OpenAI | Computer use/writing/scoped fixes | none low medium high xhigh max | 1,050,000 / 128,000 | $1 / $5 |
| `gpt-6-luna` | OpenAI | Bulk and low-latency workloads | none low medium high xhigh max | 1,050,000 / 128,000 | $0.10 / $0.50 |
| `gemini-4-argon` | Google | Deep work/long context | low medium high | 1,048,576 unified input+output; per-segment output limits | Not quoted: Google promotional/endpoint terms require refresh |
| `gemini-3.8-flash` | Google | High-capability fast engineering/agent work | low medium high | 1M / 64K | $0.75 / $3.75 introductory through 2026-12-31 |
| `gemini-3.5-flash-lite` | Google | High-volume cost-sensitive work | minimal low medium high | Not verified for this snapshot | Not verified |
| `claude-fable-5-1` | Anthropic | Most demanding reasoning | low medium high xhigh max | 1M / 128K | $10 / $50 |
| `claude-opus-5-5` | Anthropic | Agentic coding/knowledge work | low medium high xhigh max | 1M / 128K | $4 / $20 |
| `claude-sonnet-5-5` | Anthropic | Balanced speed and capability | low medium high xhigh max | 1M / 128K | $2 / $10 |
| `claude-haiku-5-5` | Anthropic | High volume extraction/routing | low medium high xhigh max | 1M / 128K | From $0.10 / $0.50 |

*Prices are captured model/catalog values, **not all-in transaction costs**. Context-dependent tiers, caching, tools, batching and promotions alter actual charges. OpenAI catalog: https://developers.openai.com/api/docs/models ; Anthropic catalog: https://platform.claude.com/docs/en/models/overview ; Gemini 3.8 price: https://ai.google.dev/gemini-api/docs/latest-model . Do not reuse these tables after provider prices change without re-verifying.

## Prompt technique differences supported by sources

**OpenAI:** State goal, constraints, available inputs and output format clearly; specify observable completion and actual test evidence. Reasoning effort is not a substitute for task clarity. Favor direct results over forcing a private reasoning transcript. Sources: https://developers.openai.com/api/docs/guides/reasoning and https://developers.openai.com/api/docs/guides/prompt-engineering

**Google:** Precise, consistently structured sections and early placement of critical instructions; explicit modality references for images/video/audio; model-specific thinking levels; API migrations may deprecate sampling flags. Sources: https://ai.google.dev/gemini-api/docs/prompting-strategies and https://ai.google.dev/gemini-api/docs/latest-model

**Anthropic:** Clear direct instructions, examples when needed, XML grouping for complex prompts with mixed input types, explicit tool boundaries and scoped work; adaptive effort controls instead of 5.x manual budgets. Sources: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices and https://platform.claude.com/docs/en/build-with-claude/effort

## Selection and reasoning methodology

The routing design excludes inactive or unverifiable IDs, respects provider and explicit model preference, evaluates category/complexity, and compares qualitative fit with price/latency objectives. It avoids false precision and never assigns benchmark accuracy scores without measurements. The actual model recommendation is a starting hypothesis, not a universal objective champion. For hard tasks, compare a suitable mid-tier model with a frontier model using **the same real input dataset and acceptance rubric**. Increase effort only when observed gains outweigh extra cost and latency. See `references/routing-framework.md`, `references/reasoning-modes.md` and `references/evaluation-methodology.md`.

## Limitations and unresolved questions

- Consumer-app plan availability, rate limits and tool permissions were not inspected for any personal account.
- Prices for Argon and Flash-Lite were intentionally left unknown rather than interpreting an unverified or promotional tier as a stable number.
- Multiple Google docs could not be opened directly as HTML because the endpoint served Markdown or redirected, so official Firebase, Google Cloud and indexed Google AI documentation were cross-checked.
- No live API model calls, external code execution agents, latency sampling, or comparative response quality experiments were performed in this release.
- The standalone Python CLI **classifies and wraps** prompts using explicit domain patterns. A running agent using `SKILL.md` performs the requested **semantic** prompt rewrite. This distinction is essential: the CLI is an offline fallback, not an LLM paraphraser.
