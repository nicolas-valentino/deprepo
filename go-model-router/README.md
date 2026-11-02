# go-model-router

A deterministic, quota-aware, and privacy-enforced router across all 30 `opencode-go/*` models.

## File Layout

```text
go-model-router/
├── README.md                        # This file
├── SKILL.md                         # Core 16-row Task-Kind Matrix & routing protocol
├── usage.sh                         # Live OpenCode Go quota telemetry & routing_mode calculator
└── references/
    ├── model-catalog.md             # Full 30-model catalog (pricing, variants, quotas, ZDR, roles)
    └── personal-domains.md          # Niches 17–23 (Resume, Tax, Legal, Medical, OpenClaw, Open WebUI)
```

## Overview

`go-model-router` routes coding, research, math, documentation, and personal-assistant tasks exclusively across the 30 models in the `opencode-go` provider using:

1. **Task Kind & Complexity Tier (`T1` / `T2` / `T3`)** — 16 core engineering/research niches in `SKILL.md` plus 7 personal/assistant niches in `references/personal-domains.md`.
2. **Live Account Telemetry (`usage.sh`)** — Queries `https://opencode.ai/zen/go/v1/usage` to inspect 5-hour rolling, weekly, and monthly quota utilization, remaining cycle days, and burn rate.
3. **Credit Pool Tie-Breaking** — When models are within ~5 benchmark points, prefers larger monthly credit pools (`$100` → `$60` → `$30` → `$20` → `$15`) and higher 5-hour request limits.
4. **Per-Model Quota Fallbacks** — Each task row defines an independent fallback model pool to switch to immediately on HTTP 429 or per-model quota exhaustion.
5. **Privacy & Data-Retention Guards** — Enforces 0-day ZDR for sensitive/PII workloads and blocks contributor models that train on data unless explicitly opted into by the user.

## Prerequisites

- **OS / Shell:** macOS or Linux with `bash`, `curl`, `jq`, and `python3`
- **Authentication:** Either:
  - An active `opencode-go` integration configured in OpenCode (`opencode auth export`), or
  - `OPENCODE_GO_API_KEY` exported in the environment.

## Running Live Usage Telemetry (`usage.sh`)

```bash
bash ~/.config/opencode/skills/go-model-router/usage.sh
```

Example output:

```text
Usage snapshot: 5-hour 0.0%, weekly 44.0%, monthly 22.0%, days left 28.6d
Tightest window: weekly (44.0%); routing_mode=downgrade_1_tier (surplus_upgrade=False, end_of_cycle_upgrade=False, running_hot=True)
{"rolling": {"percent": 0.0, ...}, "weekly": {"percent": 44.0, ...}, "monthly": {"percent": 22.0, ...}, "days_left": 28.6, "days_elapsed": 1.4, "fresh_cycle": false, "running_hot": true, "tightest_window": "weekly", "routing_mode": "downgrade_1_tier"}
```

## Deterministic Routing Modes

`usage.sh` computes one of six `routing_mode` states:

| `routing_mode` | Trigger Condition | Tier Adjustment |
|---|---|---|
| `normal` | Default operating range, not running hot | Use the task's intrinsic column (`T1`, `T2`, or `T3`) |
| `surplus_upgrade` | 5h ≤ 20%, weekly ≤ 25%, monthly ≤ 35%, `running_hot=False` | Upgrade 1 tier right (`T1 → T2`, `T2 → T3`) |
| `end_of_cycle_upgrade` | `days_left` ≤ 5, monthly < 70%, 5h < 70%, weekly < 80% | Shift all `T2` and `T3` tasks to `T3` to spend expiring monthly credit |
| `downgrade_1_tier` | 5h ≥ 60%, weekly ≥ 60%, monthly ≥ 70% (outside EoC), or `running_hot=True` | Shift 1 tier left (`T3 → T2`, `T2 → T1`) |
| `downgrade_t1_only` | 5h ≥ 80%, weekly ≥ 80%, or monthly ≥ 85% (outside EoC) | Route all tasks to `T1` (security-critical fixes capped at `T2`) |
| `exhausted_free_only` | Any window ≥ 95% | Use `opencode-go/beam-free` for read/search/summary only; pause implementation |

> **Burn-rate check (`running_hot`):** Set to `true` when `monthly.percent > (days_elapsed / 30.0) * 100 * 1.25`.

## Task Classes & Subagent Dispatch

In Build mode, tasks are dispatched to subagents matched to their routed tier:

| Class | Role | Subagent | Typical Credit Pool / Models |
|---|---|---|---|
| `T1` | Cheap / Fast / High-Credit | `exec-cheap` | `glm-5.3-flash`, `minimax-m3.1-flash`, `qwen3.8-flash`, `hy3`, `claude-haiku-5-5`, `gpt-6-luna`, `mimo-v2.6-flash`, `beam-free` |
| `T2` | Cheapest Adequate Standard | `exec-mid` | `deepseek-v4.1-flash`, `longcat-2.0`, `kimi-k2.7-code`, `glm-5.3`, `glm-5.2`, `hy4-preview`, `qwen3.7-plus`, `step-5-preview`, `mimo-v2.6-pro` |
| `T3` | Complex / Frontier / High-Stakes | `exec-premium` | `gemini-4-argon`, `kimi-k3.1-pro`, `deepseek-v4-pro`, `qwen3.8-max`, `grok-4.7` |

If a subagent encounters an HTTP 429 or quota error, switch once to the row's **Per-Model Quota Fallback** (or drop one tier `T3 → T2 → T1`) rather than retrying the exhausted model.

## Coverage Across 23 Task Niches

- **Core Engineering & Research (`SKILL.md`, Rows 1–16):**
  1. Autonomous terminal & CLI build/test loops
  2. Repo-level bug fixing & issue resolution (SWE)
  3. Greenfield feature & app codegen from specs
  4. Multi-file refactoring & architecture cleanup
  5. Backend services, APIs & database logic
  6. Web frontend, React/UI & interactive 3D/games
  7. Unit, integration & E2E test authoring
  8. Code review, security audit & vuln discovery
  9. Long-context repo comprehension (256K–1M tokens)
  10. Deep log/trace root-cause & 1M-ctx reasoning
  11. Formal math, algorithms & scientific computing
  12. Structured JSON/schema & config/script generation
  13. Technical documentation, specs & changelogs
  14. Internet research & search-augmented synthesis
  15. Multilingual / i18n / localization engineering
  16. Non-interactive batch codemods / scout swarms
- **Personal & Assistant Domains (`references/personal-domains.md`, Rows 17–23):**
  17. Resume writing, cover letters & LinkedIn
  18. Tax planning & financial modeling (with second-pass `deepseek-v4-pro#max` arithmetic verification)
  19. Legal consultation & contract analysis
  20. Medical consultations & clinical scribing
  21. OpenClaw basic (reminders, heartbeats, home commands)
  22. OpenClaw complex (multi-step Home Assistant & browser/file automation)
  23. Open WebUI (self-hosted everyday chat)

## Privacy & Retention Tiers (`references/model-catalog.md`)

- **0-Day ZDR (Default for code, PII, tax, legal, medical, and home telemetry):**
  `gemini-4-argon`, `kimi-k3.1-pro`, `kimi-k3`, `kimi-k2.7-code`, `glm-5.3`, `glm-5.2`, `glm-5.3-flash`, `longcat-2.0`, `qwen3.8-max`, `qwen3.7-plus`, `qwen3.8-flash`, `minimax-m3.1-flash`, `minimax-m3`, `mimo-v2.6-pro`, `mimo-v2.5-pro`, `mimo-v2.6-flash`, `mimo-v2.5`, `step-5-preview`, `hy4-preview`, `hy3` (plus `deepseek-v4.1-flash` and `deepseek-v4-pro` once post-Oct 31, 2026 ZDR renewal is verified in the OpenCode Console).
- **30-Day Retention (Requires explicit user opt-in for sensitive PII/PHI):**
  `grok-4.7`, `gpt-6-luna`, `gpt-5.6-luna`, `claude-haiku-5-5`, `beam-free`.
- **Contributor / Trains on Data (Blocked unless user explicitly opts in for public/synthetic data):**
  `muse-spark-1.3-contributor`, `muse-spark-1.2-contributor`, `iceman-contributor-free`.

## How to Run Routed Models in Build Mode

When you switch from Plan to Build mode with a routed plan, there are two ways to use the recommended models:

### Option A — Automatic Subagent Dispatch (recommended)
The Build agent (`longcat-2.0`) acts as an orchestrator and automatically spawns subagents with the exact routed model for each task. Just press `Tab` and type your build prompt:
1. Press `Tab` to switch to Build mode.
2. Type `apply this change`, `implement task 1`, or `/implement <plan-path>`.
3. The Build agent dispatches each task via `subagent(agent=..., model="<Recommended model>")`.

### Option B — Manual TUI Session Model Switch
Switch your main session to the recommended model and run tasks directly:
1. Press `Tab` to switch to Build mode.
2. Press `Ctrl+X` then `m` (or type `/models`) to open the model picker.
3. Select the recommended model (e.g., `claude-haiku-5-5`).
4. Press `Ctrl+T` to cycle the variant (e.g., `#low`).
5. Type `apply this change directly`.

> **Tip:** Option A is recommended because it preserves the Build orchestrator's ability to run independent tasks in parallel and handle per-model quota fallbacks automatically.
