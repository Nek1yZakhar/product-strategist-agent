# TICKET-08: Synthetic Interview Panel with Mandatory Honesty Labeling

## Goal
Implement exploratory user research personas while strictly enforcing scientific honesty guardrails that prevent treating synthetic LLM outputs as empirical demand evidence.

## Problem
AI products frequently present simulated LLM user interviews as proof of market demand, despite scientific proof that LLMs exhibit extreme compliance bias and fail to simulate true price sensitivity (arXiv:2607.26348, Verasight 2026).

## Scope
- **MUST**:
  - Methodology guidelines in `knowledge/methodology/synthetic-respondents.md`.
  - Operational skill `.agents/skills/interview-panel/SKILL.md`.
  - Mandatory prominent disclaimer banner on all persona outputs:
    `[METHODOLOGICAL DISCLAIMER: Synthetic simulation for hypothesis generation ONLY; NOT empirical demand evidence (arXiv:2607.26348)]`.
  - Real customer qualitative interview guide generation based on uncovered blind spots.
- **SHOULD**:
  - Demographic archetype diversity (e.g., Head of Household, Digital Native Teen, Elderly Relative).
- **COULD**:
  - Pew Research "silicon samples" digital twin framing for persona calibration.

## Requirements
1. Synthetic personas must never generate quantitative demand forecasts or willingness-to-pay (WTP) figures.
2. Every synthetic interview file must begin with the verbatim disclaimer banner.
3. Personas must focus on uncovering latent anxiety, privacy friction, and onboarding objections.

## Implementation Notes
- Governed by `.agents/rules/evidence.md`.
- Executed via `skill:interview-panel`.

## Acceptance Criteria ("Done when")
- `knowledge/methodology/synthetic-respondents.md` contains strict permitted vs. prohibited use cases.
- Generated persona documents contain the verbatim disclaimer banner in line 1.
- No synthetic persona file contains simulated quantitative market sizing or WTP numbers.

## References
- https://arxiv.org/abs/2607.26348 — Chen, Zhu, Zheng (2026), "When Synthetic Users Fail": Benchmark proving LLM agents fail at individual consumer modeling and inflate segment gaps.
- https://www.verasight.io/reports/synthetic-polls-vs-real-surveys-2026-midterms — Verasight 2026: Out-of-sample test showing synthetic polls missed by RMSE 8.3 pp.
- https://www.pewresearch.org/data-labs/2026/09/30/methodology-silicon-samples/ — Pew Research: Methodologically honest silicon samples standards.

## Dependencies
TICKET-02, TICKET-03.

## Effort & Risks
- **Effort**: 1.5 person-hours (MUST scope).
- **Risk**: Stakeholders misinterpreting persona dialogue as validated customer demand. *Mitigation*: Uncompromising prominent warning banner.
