# TICKET-07: Anti-Hallucination & Citation Verification Subagent

## Goal
Eliminate fabricated URLs and phantom citations from strategic research reports through deterministic HTTP resolution and automated claim quarantining.

## Problem
Empirical benchmarks show 3–13% of URLs in AI research reports are hallucinations (arXiv:2504.00317; arXiv:2607.00738). Relying on dead or fabricated links destroys credibility in competition evaluation.

## Scope
- **MUST**:
  - Deterministic URL resolver (`scripts/verify_citations.py`) executing HTTP HEAD/GET probes.
  - Classification engine: `verified` (HTTP 200/WAF), `dead` (HTTP 404/DNS failure), `hallucinated` (dummy/synthetic domains).
  - Quarantine protocol: Any finding not marked `verified` is blocked from informing strategic options.
  - Audit table generation formatted in GitHub-flavored markdown.
- **SHOULD**:
  - `--update` flag to rewrite YAML frontmatter automatically in `findings/*.md`.
- **COULD**:
  - Extraction and fuzzy-matching of page titles to detect domain parking pages.

## Requirements
1. Verification must execute via standard Python libraries without external API keys.
2. Detection heuristics must catch common synthetic domains (`example.com`, `fake.org`, `test.local`).
3. Results must be documented in a publication-grade markdown table with HTTP status codes and diagnostic notes.

## Implementation Notes
- Core script: `scripts/verify_citations.py`.
- Integrates with `skill:citation-verifier`.

## Acceptance Criteria ("Done when")
- `python scripts/verify_citations.py --project demo-megafon` audits all project findings.
- Synthetic dummy URL passed via `--url https://example.com/fake` returns status `hallucinated`.
- Active domain passed via `--url https://habr.com` returns status `verified`.

## References
- https://arxiv.org/abs/2607.00738 — "Phantom References": Hallucinated citations surviving peer review and agent evaluation.
- https://arxiv.org/abs/2608.24306 — "Who is the Agent to Blame?": Error propagation from orchestrator evidence collection.

## Dependencies
TICKET-04 (CLI Tooling).

## Effort & Risks
- **Effort**: 2.0 person-hours (MUST scope).
- **Risk**: Corporate firewalls or bot protections returning HTTP 403. *Mitigation*: Code treats HTTP 403 on valid registered domains as `verified (Domain active / WAF protected)` to prevent false alarms.
