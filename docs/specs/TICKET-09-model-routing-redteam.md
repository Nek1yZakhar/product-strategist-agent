# TICKET-09: Model Routing, Pro Subscriptions & Dual-Provider Red-Team Architecture

## Goal
Implement a multi-model cognitive topology that leverages active IDE Pro subscriptions for zero-token-billing execution and independent red-team critique via GLM 5.3 in Zcode.

## Problem
Single-model systems suffer from severe confirmation bias, validating their own assumptions. Furthermore, reliance on developer API keys creates credit card billing friction, whereas professional makers operate via flat-rate Pro subscriptions in specialized IDEs.

## Scope
- **MUST**:
  - Architecture specification in `docs/ARCHITECTURE.md` detailing IDE Pro subscription access (AntiGravity IDE for Gemini Flash; Zcode for GLM 5.3; Perplexity Pro web panel for research).
  - Red-Team review prompt in `knowledge/methodology/red-team/adversarial-review-prompt.md`.
  - Operational skill `.agents/skills/adversarial-reviewer/SKILL.md`.
  - Financial token ledger in `state/cost-log.csv` and summary reporter `scripts/cost_summary.py` tracking token economy for contest transparency.
  - Optional Free-Tier Google AI Studio API key support in `.env.example` for headless CLI scripts.
- **SHOULD**:
  - File-based review request format (`red-team-review-request.md`) for air-gapped Zcode sessions.
- **COULD**:
  - Direct API client fallback for GLM 5.3 via Zhipu AI platform if key is provided.

## Requirements
1. Red-Team review must be conducted by an independent model family (GLM 5.3 via Zcode) to prevent cognitive echo.
2. The agent must never mandate paid API billing when IDE subscription sessions are active.
3. Every analytical session must log token consumption in `state/cost-log.csv` regardless of whether inference was executed under a subscription or an API key.

## Implementation Notes
- Gemini 3.8 Flash provides fast, low-latency orchestration (~1M token context).
- GLM 5.3 acts as a hostile CFO and Principal Product Reviewer.
- Perplexity Pro serves as a second-opinion verification panel.

## Acceptance Criteria ("Done when")
- `docs/ARCHITECTURE.md` documents the Pro-subscription allocation matrix.
- `knowledge/projects/demo-megafon/output/adversarial-review.md` contains an unsparing red-team critique from GLM 5.3.
- Running `python scripts/cost_summary.py` outputs token and cost breakdowns across models.

## References
- https://code.claude.com/docs/en/best-practices — Model and subagent allocation best practices.
- https://github.com/dzhng/deep-research — Multi-stage research and review pattern.

## Dependencies
TICKET-01, TICKET-03, TICKET-04.

## Effort & Risks
- **Effort**: 2.0 person-hours (MUST scope).
- **Risk**: Red-Team review producing overly generic criticism. *Mitigation*: Prompt enforces explicit mathematical critique of unit economics and IoT margin leakage.
