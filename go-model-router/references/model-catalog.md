# Go Model Catalog (all 30 `opencode-go` models)

Grouped by family. Credits shown as monthly dollar pool / requests per 5h / requests per month.
Variants are appended as `model#variant`.

## Kimi (Moonshot)

### 1. `opencode-go/kimi-k3.1-pro` — $2/$10 | variants: `low`, `high`, `max` | Credits: $15, 147/5h, 735/mo | 1M ctx, multimodal, 0-day ZDR.
**Strengths:** #1 Terminal-Bench 4.0 (67%), GDPval-AA #3 (1,846 Elo), AutomationBench 73%, AA II 55 (top open-weights), SWE-Marathon 51.7, 3D/CAD/Unity/Unreal/Godot, finance hallucination −65%, flags incomplete work honestly.
**Weaknesses:** scarcest quota (147/5h), KingBench 53.7 (~tied with Argon/Haiku on pure snippet codegen).
**Role:** T3 primary for complex terminal/agentic loops, 3D/game dev, and architecture.

### 2. `opencode-go/kimi-k3` — $3/$15 | Credits: $15, 110/5h, 490/mo | 1M ctx, 0-day ZDR.
**Strengths:** long-horizon repo navigation & visual/React reasoning.
**Weaknesses:** older and pricier than K3.1 Pro.
**Role:** Per-model quota fallback when `kimi-k3.1-pro` hits its 147/5h cap on long-horizon Kimi-lineage workflows (separate per-model quota pool).

### 3. `opencode-go/kimi-k2.7-code` — $0.95/$4 | variants: none | Credits: $60, 1,350/5h, 6,750/mo | 262K+ ctx, 0-day ZDR.
**Strengths:** Moonshot's code-specialized agentic model (K2.6 line 66.7% TB2.0), top pick in agent guides for multi-file refactors and long tool sessions.
**Weaknesses:** not a frontier math/proof model.
**Role:** T2 primary for multi-file refactoring and feature implementation.

## Gemini (Google)

### 4. `opencode-go/gemini-4-argon` — $2/$10 (50% off through Nov 30, 2026 — re-verify Dec 1) | variants: `low`, `medium`, `high` | Credits: $30, 440/5h, 2,120/mo | 1M in / 1M out, multimodal, 0-day ZDR.
**Strengths:** DeepSWE v1.1 77.9% (SOTA), Vibe Code Bench 91.9% (#1), Vals Index #1 (68.9%), Harvey Legal 19.6% (3–5× peers), Vals Finance 65.4% (#1), 20-lang vuln discovery & black-box pentest, low hallucination.
**Weaknesses:** Terminal-Bench 57%, verbose, occasional deep-reasoning timeouts.
**Role:** Pinned Plan-mode model (`#high`), T3 primary for repo debugging, greenfield builds, security audits, and legal/finance/medical analysis; wins all T3 ties via 2×–3× the credits of $15 flagships.

## GLM (Zhipu)

### 5. `opencode-go/glm-5.3` — $1.40/$4.40 | variants: `low`, `high`, `max` | Credits: $15, 220/5h, 1,080/mo | 1M ctx, text-only, 0-day ZDR.
**Strengths:** KingBench 3 #1 (91.25%), TB 2.1 88.2%, TB 3.0 28.3% (open leader), ALE 28.5 (#1 open CLI), CyberGym 84.5%, Frontend #2, token-efficient (~50K out/task vs Opus 120K).
**Weaknesses:** text-only, tight $15 quota (220/5h).
**Role:** T2 cheapest-adequate primary for greenfield codegen, web frontend, and security/code review.

### 6. `opencode-go/glm-5.2` — $1.40/$4.40 | Credits: $60, 880/5h, 4,300/mo (4× GLM-5.3 credits) | 1M ctx, 0-day ZDR.
**Strengths:** same 743B MoE base as 5.3, elite structured-output & instruction adherence, Frontend #2 lineage.
**Weaknesses:** lower agentic post-training than 5.3.
**Role:** T2 primary for structured-output pipelines/schemas and high-credit fallback when `glm-5.3`'s 220/5h pool is tight.

### 7. `opencode-go/glm-5.3-flash` — $0.15/$0.50 | variants: `low`, `high`, `max` | Credits: $60, 6,320/5h, 31,580/mo | 1M ctx, 0-day ZDR.
**Strengths:** KingBench 3 78.75% (strongest cheap-tier coder), strict instruction/JSON adherence.
**Weaknesses:** below flagship tier on deep multi-file architecture.
**Role:** T1 primary for configs, shell/python scripts, boilerplate, `explore` subagent, and OpenClaw basic commands.

## DeepSeek

### 8. `opencode-go/deepseek-v4.1-flash` — $0.15/$0.60 off-peak ($0.30/$1.20 peak: Mon–Fri 01:00–04:00 & 06:00–10:00 UTC) | variants: `low`, `high`, `max` | Credits: $100, 43,330/5h, 216,670/mo (richest paid pool) | 1M ctx, 173.7 tok/s, TTFT 0.98s.
**Strengths:** DeepSWE v1.1 77% (1017 build), AA II 45, CED ultra-compact KV cache for long agent loops.
**Weaknesses:** requires Global region toggle; ZDR agreement ran through Oct 31, 2026 (verify renewal in Console before sensitive code); peak price doubling.
**Role:** T2 primary for repo-level bug fixing & data pipelines; T1 high-volume coder.

### 9. `opencode-go/deepseek-v4-pro` — $0.66/$1.98 off-peak ($1.32/$3.96 peak) | variants: `high`, `max` | Credits: $15, 1,050/5h, 5,200/mo | 1M ctx.
**Strengths:** HumanEval 92.3%, GSM8K 95.1%, MATH 88.7%, TB 2.0 67.9%.
**Weaknesses:** $15 quota, same Global/ZDR/peak caveats.
**Role:** T3 primary for formal math, proofs, and algorithmic complexity.

## Longcat (Meituan)

### 10. `opencode-go/longcat-2.0` — $0.30/$1.20, cache read $0.006 | variants: none | Credits: $60, 11,400/5h, 57,200/mo | 1M native ctx (Hierarchical Indexing for 500K+ token repos), 0-day ZDR.
**Strengths:** SWE-bench Pro 59.5, SWE-bench Multilingual 77.3, TB 2.1 70.8, BrowseComp 79.9, RWSearch 78.8, WritingBench 83.8, IFEval 90.0, IMO-AnswerBench 81.8, GPQA 88.9.
**Weaknesses:** no enforced `response_format` JSON mode.
**Role:** Default `build` model; T2 primary for long-context repo analysis, internet research, technical writing/docs, multilingual code, and value math/science.

## Qwen (Alibaba)

### 11. `opencode-go/qwen3.8-max` — $2/$6 | variants: `none`, `low`, `medium`, `xhigh` | Credits: $15, 160/5h, 810/mo | 1M ctx, 0-day ZDR.
**Strengths:** BenchLM Agentic #15 (66.2), TB 2.1 86.6%, CoWorkBench 74.8%, top multilingual & cross-locale reasoning.
**Weaknesses:** tight 160/5h quota.
**Role:** T3 primary for multilingual/i18n architecture and complex cross-system agentic workflows.

### 12. `opencode-go/qwen3.7-plus` — $0.40/$1.60 (≤256K) | variants: `none`, `high`, `max` | Credits: $60, 4,300/5h, 21,600/mo | 0-day ZDR.
**Strengths:** proven large-codebase agentic workhorse, strong multilingual coding.
**Weaknesses:** 3× price jump above 256K tokens.
**Role:** T2 primary for ≤256K multi-file agentic tasks and i18n/localization implementation.

### 13. `opencode-go/qwen3.8-flash` — $0.15/$0.47 | variants: `none`, `low`, `medium`, `xhigh` | Credits: $30, 5,400/5h, 27,000/mo | 0-day ZDR.
**Strengths:** fast Qwen3.8-generation flash model with `xhigh` thinking option.
**Role:** T1 primary for multilingual/i18n edits and rapid Qwen-lineage agent turns.

## MiniMax

### 14. `opencode-go/minimax-m3.1-flash` — $0.15/$0.60 | variants: `low`, `medium`, `high`, `xhigh`, `max` | Credits: $20, 3,880/5h, 19,380/mo | 1M ctx, multimodal, 0-day ZDR.
**Strengths:** BenchLM Coding #17 (61.3), DeepSWE 73.7%, Vibe Code v1.1 73.94%, AutomationBench 62.2%, top OpenClaw collection model.
**Weaknesses:** TB 4.0 25.3% (weak on unguided multi-hour terminal loops).
**Role:** T1 primary for spec-to-code generation and UI/visual component scaffolding.

### 15. `opencode-go/minimax-m3` — $0.30/$1.20 (≤512K) | variants: `none`, `thinking` | Credits: $60, 3,200/5h, 16,000/mo (3× M3.1 Flash monthly allowance) | 1M ctx, 0-day ZDR.
**Strengths:** 512K–1M long-context synthesis at $60 credit tier.
**Weaknesses:** older than M3.1.
**Role:** T2 long-context reading/synthesis alternate when `longcat-2.0` cache/pool is busy.

## MiMo (Xiaomi)

### 16. `opencode-go/mimo-v2.6-pro` — $0.435/$0.87 | Credits: $15, 3,250/5h, 16,300/mo | 1M ctx, 0-day ZDR.
**Strengths:** wins 5/8 head-to-head reasoning benchmarks vs DS V4.1 Flash on llm-stats, ultra-cheap cache read ($0.0036/M), 3,250/5h in the $15 tier.
**Role:** T2 primary for 1M-context analytical reasoning & log/trace root-cause analysis.

### 17. `opencode-go/mimo-v2.5-pro` — $0.435/$0.87 | Credits: $15, 3,250/5h, 16,300/mo | 1M ctx, 0-day ZDR.
**Strengths:** community-proven 1M-context reasoner (71/100 OpenCode coding index).
**Role:** Per-model quota fallback for `mimo-v2.6-pro` (doubles available 1M-context Pro reasoning requests to 6,500/5h across the pair).

### 18. `opencode-go/mimo-v2.6-flash` — $0.14/$0.28 | Credits: $60, 30,100/5h, 150,400/mo | 1M ctx, 0-day ZDR.
**Strengths:** KingBench 3 72.5%, massive 30,100/5h ZDR quota.
**Weaknesses:** slow throughput (50.6 tok/s, TTFT 3.02s).
**Role:** T1 primary for non-interactive batch jobs, codemods, bulk file migrations, and background cron tasks.

### 19. `opencode-go/mimo-v2.5` — $0.14/$0.28 | Credits: $60, 30,100/5h, 150,400/mo | 1M ctx, 0-day ZDR.
**Role:** Parallel batch worker / per-model quota twin for `mimo-v2.6-flash` (enables 60,200 req/5h across parallel background batch workers).

## xAI / OpenAI / Anthropic / StepFun / Hunyuan / Reflection / Meta

### 20. `opencode-go/grok-4.7` — $2/$6 (≤200K) | variants: `low`, `medium`, `high`, `xhigh` | Credits: $15, 169/5h, 845/mo | 500K ctx, 30-day retention.
**Strengths:** Coding Agent Index 56 (#4 native harness), DeepSWE 73%, GDPval 1,695 Elo (decks/docs), MedScribe #4 (89.4%), Legal Research 47.1%, HackerBench v0.3 safest dual-use cyber filter, native web + X search.
**Weaknesses:** burns ~81K output tokens/task at `xhigh`, tight 169/5h cap, 30-day retention.
**Role:** T3 primary for current-events/X research, executive presentations, clinical scribing, and dual-use cyber defense.

### 21. `opencode-go/gpt-6-luna` — $0.10/$0.50 (≤272K) | variants: `none`, `low`, `medium`, `high`, `xhigh`, `max` | Credits: $15, 4,230/5h, 21,130/mo | 1.05M ctx, 157 tok/s, 30-day retention.
**Strengths:** fastest interactive feel, DeepSWE 66.6% at `#max`, #1 model in OpenRouter's OpenClaw collection.
**Weaknesses:** Coding Agent Index 41 at default effort (below 5.6 Luna), 30-day retention.
**Role:** T1 primary for latency-sensitive interactive CLI/verification, 1M-context page ingestion, and Open WebUI everyday chat.

### 22. `opencode-go/gpt-5.6-luna` — $0.20/$1.20 (≤272K) | Credits: $15, 2,050/5h, 10,250/mo | 1.05M ctx, 30-day retention.
**Strengths:** BenchLM Coding #13–16 (61.6–63.0) — higher pure coding score than GPT-6 Luna (51.4) and Agentic #36 (55.2).
**Weaknesses:** half the 5h request count of GPT-6 Luna.
**Role:** T2 primary for OpenAI-compatible 1M-context code repair when coding accuracy matters more than raw chat speed.

### 23. `opencode-go/claude-haiku-5-5` — $0.10/$0.50 (≤100K; 5× above 100K) | variants: `none`, `low`, `medium`, `high`, `xhigh`, `max` | Credits: $15, 3,850/5h, 19,230/mo | 30-day retention.
**Strengths:** KingBench 54.2% (statistically tied with K3.1 Pro 53.7% and Argon 54.3% on codegen at 26× K3.1's quota), fast, surgical instruction following, top subagent swarm model.
**Weaknesses:** 5× price jump over 100K tokens, 30-day retention.
**Role:** T1/T2 primary for unit/integration test writing, parallel subagent swarms (≤100K ctx), and quick code review passes.

### 24. `opencode-go/step-5-preview` — $1.00/$2.70 | variants: `low`, `medium`, `high` | Credits: $15, 430/5h, 2,130/mo | 1M ctx, text+image+video input, 228.7 tok/s (fastest model on the plan), 0-day ZDR.
**Strengths:** KingBench 3 #2 (83.75%, 9.5/10 on 3D archery game & local ML web UI), BenchLM Coding #21 (60.5), video input, quantitative finance & STEM.
**Role:** T2 primary for interactive 3D/canvas/SVG/game prototyping, video/visual input debugging, and quantitative finance modeling.

### 25. `opencode-go/hy4-preview` — $0.834/$2.501 | variants: `none`, `high` | Credits: $30, 1,350/5h, 6,770/mo | 770B MoE / 49B active, 1M ctx, 0-day ZDR.
**Strengths:** beat GLM-5.3 (2.99 vs 2.92) and Kimi K3 (2.94) in Tencent's 163-expert blind engineering eval; TB 2.1 85.4%; DeepSWE 64.3%; 9× K3.1 Pro's monthly requests.
**Role:** T2 primary for sustained multi-step agent execution and complex OpenClaw workflows.

### 26. `opencode-go/hy3` — $0.14/$0.58 | Credits: $60, 4,300/5h, 21,500/mo | 295B MoE / 21B active, 256K ctx, 0-day ZDR.
**Strengths:** 6.9T tokens processed on OpenCode (95.5% of Tencent volume), strong STEM/Olympiad reasoning & backend dev (`Hy-Backend`) at $60 credit tier (3.2× Hy4's 5h quota).
**Role:** T1/T2 primary for high-volume backend service tasks and STEM reasoning when conserving `hy4-preview`'s $30 pool.

### 27. `opencode-go/beam-free` — $0/$0 | variants: `low`, `medium`, `high`, `xhigh`, `max` | Credits: Unlimited | 501B MoE / 23B active, 1M ctx, 30-day retention, no training.
**Strengths:** Reflection AI's open model, ultra-fast, separate free pool that never touches paid Go allowances.
**Weaknesses:** unreliable tool calling on deep chains.
**Role:** T1 free scout for repo reading/summarization, OpenClaw heartbeats, Open WebUI casual chat floor, and first step in the quota-exhausted fallback ladder.

### 28. `opencode-go/muse-spark-1.3-contributor` — $0.10/$0.20, cache $0.002 | variants: `minimal`, `low`, `medium`, `high`, `xhigh` | Credits: $60, 45,300/5h, 226,600/mo | 1.05M ctx, multimodal.
**Strengths:** MRCR 512K–1M 98.1% (#1 long-context retrieval), AA II 61 at `xhigh`, 20% fewer tool calls than 1.2.
**Weaknesses:** **trains on prompts/outputs (not ZDR)**.
**Role:** Opt-in-only powerhouse for public/open-source/synthetic 1M-context needle-in-a-haystack retrieval when the user explicitly permits contributor models.

### 29. `opencode-go/muse-spark-1.2-contributor` — $0.10/$0.20 | Credits: $60, 45,300/5h, 226,600/mo | 1.05M ctx.
**Weaknesses:** **trains on data (not ZDR)**, older than 1.3.
**Role:** Opt-in-only secondary pool when `muse-spark-1.3-contributor` is rate-limited on public/open-source bulk runs.

### 30. `opencode-go/iceman-contributor-free` — $0/$0 | Credits: Unlimited | 262K ctx.
**Weaknesses:** stealth model, **trains on data (not ZDR)**.
**Role:** Opt-in-only zero-cost sandbox for public/throwaway experiments when the user explicitly requests a free contributor model.
