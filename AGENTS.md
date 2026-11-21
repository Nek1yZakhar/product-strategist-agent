# AGENTS.md — Domain Passport: Product Strategist Agent

A repository-based AI agent for digital product and communication strategy (MGIMO AI Challenge 2026, track "Стратег Фабрики продуктов" / Megafon Product Factory). Operates directly inside agentic IDEs (AntiGravity, Cursor, Claude Code, Zcode) through structured domain rules, modular skills, and file-based state.

## Model & IDE Subscription Matrix
| Role | Runtime & Engine | Access Mode | Purpose |
| :--- | :--- | :--- | :--- |
| **Primary Strategist** | AntiGravity / Gemini 3.8 Flash | IDE Pro Subscription | Orchestration, research, synthesis, decision logging |
| **Adversarial Red-Team** | Zcode / GLM 5.3 | Zcode Coding Plan / Pro | Steelman objections, cognitive bias audits, stress testing |
| **Triangulation Panel** | Perplexity Pro (Sonnet 5.5 / GPT-6.2) | Web Copilot Panel | External ground-truth discovery and second-opinion validation |

## Core CLI Tooling (Python 3.11+ Stdlib)
- `python scripts/extract_brief.py [pdf_or_text]` — Extract & normalize incoming product briefs.
- `python scripts/verify_citations.py` — Resolve per-claim URLs, detect dead links & hallucinations.
- `python scripts/cost_summary.py` — Aggregate financial token expenditure and compute model costs.

## Environment Variables (.env.example)
- `GEMINI_API_KEY`: Optional Google AI Studio Free-Tier key for standalone Python CLI scripts.
- `GLM_API_KEY`: Optional Zhipu AI trial key for direct CLI API calls.
- Note: Primary operation runs inside AntiGravity IDE & Zcode via active Pro subscriptions without paid API billing.

## System Invariants & Pointers
- **Rules Engine**: Read `.agents/rules/` (`workflow.md`, `evidence.md`, `knowledge.md`, `cost.md`, `research.md`, `deliverables.md`).
- **Active State**: Inspect `state/STATE-current-task.md` and `docs/STATE.md` before taking action.
- **IMMUTABLE GROUND TRUTH**: Files in `docs/source/*.md` are verbatim originals — never modify them.
- **Solo Maker**: Developed exclusively by **Zakhar** (Захар).
