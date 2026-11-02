---
name: go-model-router
description: Route coding, research, and writing tasks across all 30 opencode-go models by task kind, T1/T2/T3 class, live Go usage, and usage-credit tie-breaks; run usage.sh for live quotas and routing_mode; read references/personal-domains.md for resume, tax, legal, medical, OpenClaw, and Open WebUI tasks
---

# Go Model Router

Scope: OpenCode Go (`opencode-go/*`) only. Never query or route to other providers.
See `references/model-catalog.md` for the full 30-model catalog and `references/personal-domains.md` for niches 17–23.

## Deterministic Routing Protocol

Run `bash ~/.config/opencode/skills/go-model-router/usage.sh` and read its `routing_mode` output:

- `normal`: select the column matching the task's intrinsic class (`T1`, `T2`, or `T3`) in the Task-Kind Matrix below.
- `surplus_upgrade` (5h ≤ 20%, weekly ≤ 25%, monthly ≤ 35%, not running hot): shift boundary `T1 → T2` and `T2 → T3` (max 1 column right).
- `end_of_cycle_upgrade` (`days_left` known ≤ 5, monthly < 70%, 5h < 70%, weekly < 80%): shift **all** `T2` and `T3` tasks to the `T3` column so expiring monthly credit is spent before reset.
- `downgrade_1_tier` (5h ≥ 60% or weekly ≥ 60% or [monthly ≥ 70% outside end-of-cycle] or `running_hot`): shift `T3 → T2` and `T2 → T1` (1 column left).
- `downgrade_t1_only` (5h ≥ 80% or weekly ≥ 80% or [monthly ≥ 85% outside end-of-cycle]): use the `T1` column for all tasks except security-critical fixes (capped at `T2`).
- `exhausted_free_only` (any window ≥ 95%): use `opencode-go/beam-free` for read/search/summary tasks only; for implementation tasks, **stop and ask the user or wait for the 5-hour reset**.

## Core 16-Row Task-Kind Matrix (`T1` | `T2` | `T3` | `Per-Model Quota Fallback`)

| # | Task Kind | T1 (Cheap / High-Credit) | T2 (Cheapest Adequate Standard) | T3 (Complex / End-of-Cycle Premium) | Per-Model Quota Fallback (Independent Pool) |
|---|---|---|---|---|---|
| 1 | Autonomous terminal & CLI build/test loops | `glm-5.3-flash#high` | `hy4-preview#high` ($30, 1,350/5h, blind-eval #1) | `kimi-k3.1-pro#max` (TB4.0 67% #1) | `glm-5.3#high` → `kimi-k3` |
| 2 | Repo-level bug fixing & issue resolution (SWE) | `minimax-m3.1-flash#high` | `deepseek-v4.1-flash#high` ($100, 43.3k/5h, DeepSWE 77%) | `gemini-4-argon#high` (DeepSWE 77.9% SOTA, $30) | `gpt-5.6-luna` (BenchLM Coding #13) |
| 3 | Greenfield feature & app codegen from specs | `minimax-m3.1-flash#high` (Vibe 73.9%) | `glm-5.3#high` (KingBench 3 91.25% #1, token-efficient) | `gemini-4-argon#high` (Vibe Code 91.9% #1) | `glm-5.2` ($60, 4× GLM-5.3 credits) |
| 4 | Multi-file refactoring & architecture cleanup | `glm-5.3-flash#high` | `kimi-k2.7-code` ($60, 1,350/5h) | `gemini-4-argon#high` | `glm-5.2` → `qwen3.7-plus#high` |
| 5 | Backend services, APIs & database logic | `hy3` ($60, 4,300/5h, `Hy-Backend`) | `longcat-2.0` ($60, 11,400/5h, SWE-Pro 59.5) | `kimi-k3.1-pro#high` | `qwen3.7-plus#high` ($60, 4,300/5h) |
| 6 | Web frontend, React/UI & interactive 3D/games | `minimax-m3.1-flash#high` | `glm-5.3#high` (web UI #2) / `step-5-preview#high` (3D/canvas/SVG, 228 tok/s) | `kimi-k3.1-pro#max` (multimodal game engines/CAD) | `glm-5.2` (web) / `gemini-4-argon#high` |
| 7 | Unit, integration & E2E test authoring | `claude-haiku-5-5#medium` (≤100K ctx, 3,850/5h) | `claude-haiku-5-5#high` (KingBench 54.2% ≈ K3.1 Pro) | `glm-5.3#high` | `gpt-6-luna#high` (>100K ctx test files, 4,230/5h) |
| 8 | Code review, security audit & vuln discovery | `claude-haiku-5-5#high` (diff review) | `glm-5.3#high` (CyberGym 84.5%) | `gemini-4-argon#high` (20-lang vuln & pentest SOTA) | `grok-4.7#high` (HackerBench dual-use safety) |
| 9 | Long-context repo comprehension (256K–1M tok) | `gpt-6-luna#low` (1.05M ctx) | `longcat-2.0` (1M native, Hierarchical Indexing, $0.006 cache) | `gemini-4-argon#high` (1M in / 1M out) | `minimax-m3#thinking` ($60) → `mimo-v2.6-pro` |
| 10 | Deep log/trace root-cause & 1M-ctx reasoning | `qwen3.8-flash#xhigh` ($30, 5,400/5h) | `mimo-v2.6-pro` ($15, 3,250/5h, wins 5/8 vs DS Flash) | `kimi-k3.1-pro#max` | `mimo-v2.5-pro` (identical 3,250/5h pool) |
| 11 | Formal math, algorithms & scientific computing | `hy3` (STEM/Olympiad, $60) | `longcat-2.0` (IMO 81.8, GPQA 88.9, $60) | `deepseek-v4-pro#max` (GSM8K 95.1%, MATH 88.7%) | `step-5-preview#high` |
| 12 | Structured JSON/schema & config/script generation | `glm-5.3-flash#low` ($60, 6,320/5h) | `glm-5.2` ($60, 880/5h, elite schema adherence) | `glm-5.3#high` | `gpt-6-luna#medium` |
| 13 | Technical documentation, specs & changelogs | `claude-haiku-5-5#low` | `longcat-2.0` (WritingBench 83.8, IFEval 90.0) | `grok-4.7#high` (GDPval 1,695 Elo decks/docs) | `gemini-4-argon#medium` |
| 14 | Internet research & search-augmented synthesis | `gpt-6-luna#low` (page ingestion) | `longcat-2.0` (BrowseComp 79.9, RWSearch 78.8) | `gemini-4-argon#high` (Vals #1) / `grok-4.7#high` (live X/web) | `kimi-k3.1-pro#high` (low hallucination) |
| 15 | Multilingual / i18n / localization engineering | `qwen3.8-flash#medium` ($30, 5,400/5h) | `longcat-2.0` (SWE-Multilingual 77.3) / `qwen3.7-plus#high` | `qwen3.8-max#xhigh` (multilingual flagship) | `gemini-4-argon#high` |
| 16 | Non-interactive batch codemods / scout swarms | `mimo-v2.6-flash` (batch, 30.1k/5h) / `beam-free#low` (read scout) | `mimo-v2.5` (parallel batch twin, 30.1k/5h) / `claude-haiku-5-5#low` (swarm) | `deepseek-v4.1-flash#high` ($100, 43.3k/5h) | `muse-spark-1.3-contributor` → `muse-spark-1.2-contributor` → `iceman-contributor-free` (**opt-in public data only`) |

## Tie-Break, Privacy, and Execution Dispatch Rules

- **Credit tie-break:** When models are within ~5 benchmark points for a task, pick the higher monthly dollar pool, then higher 5-hour request count. Never let a tie-break push private work onto contributor models (`muse-spark-*`, `iceman-contributor-free`) or push interactive turns onto `mimo-v2.6-flash`/`mimo-v2.5` (3s TTFT).
- **Mandatory subagent dispatch:** In Build mode, if the active session model is not already the task's `Recommended model`, you MUST dispatch the task via `subagent(agent="exec-cheap" | "exec-mid" | "exec-premium", model="<Recommended model from table>")` rather than editing files directly in the parent session. Exception: the user explicitly says "run directly" or "do it in the main session". Always finish Build execution with a summary table: `Task ID | Planned Model | Actual Model Used | Result`.

- **Fallback on rate-limit / quota error:** If a subagent returns HTTP 429 or a quota error, switch once to the row's Per-Model Quota Fallback column (or drop one tier `T3 → T2 → T1`) and retry. Never retry the exhausted model. Report the actual model used for every task.

## Quota-semantics note (empirical, 2026-10-31)

One tiny `opencode run` on `glm-5.3-flash#low` ($60 pool) and one on `gpt-6-luna#low` ($15 pool) left the endpoint unchanged (5h 0.0%, weekly 40.0%, monthly 20.0% before and after). Percentages are coarse-grained and/or delayed — they do not move per single request and show no per-model split. Treat `usage.sh` thresholds as account-level signals and rely on the Per-Model Quota Fallback column + one-shot fallback/drop rule on HTTP 429 / quota errors.

## How to Execute Routed Plans in Build Mode

When the user switches from Plan to Build mode and asks to apply/implement a planned task, there are two execution paths:

### Path A — Automatic Subagent Dispatch (recommended)
The Build agent dispatches each task to a subagent with the exact routed model. No manual model switching needed.
1. Press `Tab` to switch from `plan` to `build`.
2. Type a prompt like `apply this change`, `implement task 1`, or `/implement <plan-path>`.
3. The Build agent spawns `subagent(agent="exec-cheap" | "exec-mid" | "exec-premium", model="<Recommended model>")` for each task.

### Path B — Manual TUI Model Switch (run directly in main session)
The user manually changes the active session model and runs the task directly without a subagent.
1. Press `Tab` to switch from `plan` to `build`.
2. Press `Ctrl+X` then `m` (or type `/models`) to open the model picker.
3. Select `<model-name>` (e.g., `claude-haiku-5-5`).
4. Press `Ctrl+T` to cycle the variant to the recommended `#variant` (e.g., `#low`).
5. Type `apply this change directly` — the task now runs on the selected model in the main session.
