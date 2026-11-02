# Personal & Assistant Domains (on-demand reference for `go-model-router`)

Load this file when a task involves resume, tax, legal, medical, OpenClaw, or Open WebUI.

| # | Niche | T1 (Cheap / Fast) | T2 (Cheapest Adequate Standard) | T3 (Complex / High-Stakes) | Per-Model Quota Fallback & Privacy Rules |
|---|---|---|---|---|---|
| 17 | Resume writing, cover letters & LinkedIn | `claude-haiku-5-5#medium` (30d ret — confirm OK) | `longcat-2.0` (WritingBench 83.8, 1M ctx for JD tailoring, **0-day ZDR**) | `grok-4.7#high` (GDPval 1,695 Elo executive polish; 30d ret) | `glm-5.2` (0-day ZDR). Never use contributor models for PII. |
| 18 | Tax planning & financial modeling | `step-5-preview#low` (0-day ZDR) | `step-5-preview#high` (finance specialty, 0-day ZDR) | `gemini-4-argon#high` (Vals Finance #1 65.4%, 0-day ZDR) | `kimi-k3.1-pro#high` (finance hallucination −65%, 0-day ZDR) + `deepseek-v4-pro#max` for second-pass arithmetic verification. |
| 19 | Legal consultation & contract analysis | `longcat-2.0` (doc ingestion, 0-day ZDR) | `qwen3.8-max#high` (0-day ZDR) | `gemini-4-argon#high` (Harvey Legal 19.6% vs <7% peers, 0-day ZDR) | `grok-4.7#xhigh` (Legal Research 47.1%, #1 law category; requires user opt-in to 30d retention). |
| 20 | Medical consultations & clinical scribing | `longcat-2.0` (GPQA 88.9, 0-day ZDR) | `kimi-k3.1-pro#high` (multimodal image/lab reading, low hallucination, 0-day ZDR) | `gemini-4-argon#high` (Vals #1, lowest hallucination, 0-day ZDR) | `grok-4.7#xhigh` (MedScribe #4 89.4%, BioMystery #6; requires user opt-in to 30d retention). |
| 21 | OpenClaw basic ("lights on", reminders, cron/heartbeats) | `beam-free#low` (heartbeats/pings, $0 unlimited) | `glm-5.3-flash#low` ($60, 6,320/5h, **0-day ZDR** for home/chat data) | `gpt-6-luna#medium` (#1 OpenClaw community model, 157 tok/s) | `mimo-v2.6-flash` (non-interactive background batch jobs, 30.1k/5h). |
| 22 | OpenClaw complex (multi-step Home Assistant workflows, browser/file automation) | `minimax-m3.1-flash#high` ($20, OpenClaw collection favorite) | `hy4-preview#high` ($30, 1,350/5h, blind-eval #1 for sustained multi-step tool use) | `kimi-k3.1-pro#max` (AutomationBench 73%, TB4.0 #1) | `kimi-k2.7-code` ($60, 1,350/5h) → `longcat-2.0`. |
| 23 | Open WebUI (self-hosted ChatGPT-style everyday conversations) | `beam-free#medium` (free unlimited casual chat) | `gpt-6-luna#medium` (GPT-6 concise chat style, 157 tok/s, 4,230/5h) / `longcat-2.0` (0-day ZDR private chat) | `gemini-4-argon#medium` (Vals #1, multimodal images) | `claude-haiku-5-5#medium` (warm Claude prose) / `grok-4.7#high` (live news/X). |

## High-Stakes Safeguards

- Informational framing only: resume, tax, legal, and medical outputs are informational and not professional advice; always include a licensed-professional disclaimer (CPA/tax attorney, licensed attorney, clinician) for high-stakes decisions.
- 0-day ZDR enforcement: default to 0-day ZDR models (`gemini-4-argon`, `longcat-2.0`, `glm-5.x`, `qwen3.x`, `minimax-m3*`, `mimo-v2.x`, `hy3`, `hy4-preview`, `step-5-preview`, `deepseek-v4*` only after ZDR renewal verified) for PII, contracts, health data, and home telemetry. Models with 30-day retention (`grok-4.7`, `gpt-6-luna`, `gpt-5.6-luna`, `claude-haiku-5-5`, `beam-free`) require explicit user opt-in for sensitive data. Contributor/train-on-data models (`muse-spark-*`, `iceman-contributor-free`) are never used for PII.
- Second-pass arithmetic check on tax numbers: verify every tax/finance calculation with an independent `deepseek-v4-pro#max` pass before presenting totals.
- Console privacy re-check: DeepSeek ZDR ran through Oct 31, 2026 — re-verify renewal in the OpenCode Console privacy settings before routing confidential code or PII to DeepSeek models.

## Open WebUI / OpenClaw Connection Security

- Open WebUI: Admin Panel → Settings → Connections → OpenAI API → Base URL `https://opencode.ai/inference/go/openai/v1`, API key from `opencode auth export` (opencode-go).
- Bind Docker to loopback only: `127.0.0.1:3000:8080`; enable WebUI auth (admin login) before exposing any port.
- OpenClaw: store the Go key in the OS keychain / `OPENCODE_GO_API_KEY` env, never in chat logs or committed files.
