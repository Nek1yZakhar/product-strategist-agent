# TICKET-02: 4-Layer Knowledge Isolation & Methodology Standards

## Goal
Enforce strict separation between permanent instructions, strategic methodology, project-specific materials, and runtime state to prevent cognitive cross-contamination.

## Problem
Standard conversational agents overwrite methodology with project data or lose track of foundational rules during long sessions, causing context drift and unpredictable outputs.

## Scope
- **MUST**:
  - Form directory tree: `knowledge/methodology/` and `knowledge/projects/`.
  - `knowledge/methodology/evidence-standards.md` detailing the Fact vs Hypothesis vs Assumption taxonomy.
  - `knowledge/methodology/strategy-frameworks.md` standardizing Product Strategy, Communication Strategy, and Options Triad.
  - `knowledge/methodology/synthetic-respondents.md` defining strict guardrails for synthetic personas.
  - Strategy templates in `knowledge/methodology/templates/` (`product-strategy.md`, `communication-strategy.md`, `validation-plan.md`).
  - Red-Team prompt template in `knowledge/methodology/red-team/adversarial-review-prompt.md`.
- **SHOULD**:
  - Retraction notice schema for superseded findings.
- **COULD**:
  - Automated linter for markdown templates.

## Requirements
1. Permanent instructions must never be written into `knowledge/projects/`.
2. All empirical claims must follow the YAML frontmatter schema (`claim`, `source_url`, `verified`, `confidence`, `date_checked`).
3. Synthetic respondents must be strictly labeled as qualitative hypothesis generation (arXiv:2607.26348).
4. Raw competition source texts in `docs/source/` must remain immutable.

## Implementation Notes
- Methodology files reside in `knowledge/methodology/`.
- Project instances reside in `knowledge/projects/<project-name>/`.
- Template schemas provide plug-and-play structure for `strategy-writer` skill.

## Acceptance Criteria ("Done when")
- All files in `knowledge/methodology/` exist and contain verified template structures.
- Running regex check on `knowledge/methodology/evidence-standards.md` confirms presence of arXiv:2504.00317, arXiv:2608.24306, and arXiv:2607.26348.
- Templates in `knowledge/methodology/templates/` can be rendered without syntax errors.

## References
- https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus — File-based knowledge and context engineering.
- https://gist.github.com/renschni/4fbc70b31bad8dd57f3370239dccd58f — Manus architecture teardown: memory management and knowledge retrieval.
- https://arxiv.org/abs/2607.26348 — "When Synthetic Users Fail": grounding for synthetic respondent honesty standard.

## Dependencies
TICKET-01 (Repository Scaffolding).

## Effort & Risks
- **Effort**: 2.0 person-hours (MUST scope).
- **Risk**: Over-complicating template headers. *Mitigation*: Use standard GFM markdown with minimal YAML blocks.
