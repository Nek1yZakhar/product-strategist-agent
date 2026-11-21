# TICKET-05: Megafon Demo Project Golden Run

## Goal
Deliver an authentic, end-to-end case study on the official Megafon "Family Connectivity" brief, demonstrating the full strategic cycle from problem statement to ratified decision.

## Problem
A strategic agent without a fully worked, verified demonstration project cannot prove its real-world viability to competition evaluators or demonstrate compliance with scoring rubrics.

## Scope
- **MUST**:
  - `knowledge/projects/demo-megafon/brief.md`: Normalized problem statement.
  - `knowledge/projects/demo-megafon/data/baseline-metrics.md`: Official 5-row metrics table (Gross profit 282->285M ₽, 4k vs 5k active groups, 8k/12k targets, 100k households, 40k multi-SIM, +500 ₽ margin/month).
  - `findings/*.md`: $\ge 5$ verified research findings with YAML frontmatter and live URLs.
  - `output/options.md`: Strategic triad (Status Quo, Shutdown, Value Pivot) with steelman counterarguments.
  - `output/adversarial-review.md`: Red-Team critique from GLM 5.3 / Zcode addressing IoT margin leakage and cannibalization.
  - `output/product-strategy.md`: Full Product Strategy with JTBD and conscious refusals.
  - `output/communication-strategy.md`: Communication Strategy with single-minded message (`sasha` standard).
  - `output/validation-plan.md`: 60-day empirical validation plan with falsification thresholds.
  - `output/ux-journey.md`: Grounded UI/UX journey analysis eliminating the 42% onboarding drop-off.
  - `state/decision-journal.md`: Logged decision record `DEC-2026-MF-01`.
- **SHOULD**:
  - Customer interview guide in `knowledge/projects/demo-megafon/interview-guide.md`.
- **COULD**:
  - Competitor feature comparison matrix in tabular format.

## Requirements
1. Baseline metrics must strictly match ground truth provided in the contest brief.
2. Every external finding must pass `python scripts/verify_citations.py` with HTTP 200.
3. Red-Team critique must be formally acknowledged and incorporated into the final strategy.
4. Promotional claims in the Communication Strategy must strictly match actual technical capabilities.

## Implementation Notes
- Directory: `knowledge/projects/demo-megafon/`.
- Written in Russian for client copy and strategy deliverables, complying with `sasha` communication standards.

## Acceptance Criteria ("Done when")
- All files in `knowledge/projects/demo-megafon/output/` exist and are populated.
- `python scripts/verify_citations.py --project demo-megafon` returns 0 dead and 0 hallucinated links.
- `state/decision-journal.md` contains record `DEC-2026-MF-01` with Zakhar designated as owner.

## References
- https://arxiv.org/abs/2608.24306 — "Who is the Agent to Blame?": Motivates isolating findings to prevent orchestrator error cascades.
- https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus — Context structuring across project materials.

## Dependencies
TICKET-02, TICKET-03, TICKET-04.

## Effort & Risks
- **Effort**: 3.0 person-hours (MUST scope).
- **Risk**: Over-optimistic financial projections. *Mitigation*: Anchor calculations strictly to the +500 ₽ retention margin formula.
