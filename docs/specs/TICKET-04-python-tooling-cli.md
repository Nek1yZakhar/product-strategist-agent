# TICKET-04: Deterministic Python Tooling & CLI Utilities

## Goal
Provide zero-dependency, pure Python 3.11+ standard library CLI tools for brief extraction, URL citation verification, and token cost accounting.

## Problem
Relying on LLMs for deterministic tasks (checking HTTP status codes, parsing CSV ledgers, extracting PDF text) leads to hallucinations, hidden costs, and unrepeatable results.

## Scope
- **MUST**:
  - `scripts/verify_citations.py`: Resolves URLs via HTTP HEAD/GET, detects dead/hallucinated links, audits YAML frontmatter in `findings/*.md`, supports `--update`.
  - `scripts/extract_brief.py`: Normalizes PDF/text briefs into `knowledge/projects/<project>/brief.md`.
  - `scripts/cost_summary.py`: Aggregates `state/cost-log.csv` into markdown tables with USD and RUB totals.
  - Zero non-standard dependencies (runs on pure Python 3.11+ stdlib; optional `pypdf` for binary PDF extraction).
- **SHOULD**:
  - Robust error handling for network timeouts and SSL certificate validation.
- **COULD**:
  - Parallel asynchronous HTTP checks for bulk URL lists (>50 links).

## Requirements
1. `scripts/verify_citations.py` must handle HTTP redirects, timeouts, and anti-bot WAF responses gracefully.
2. `scripts/cost_summary.py` must calculate metrics grouped by analytical phase and by model engine.
3. All scripts must compile cleanly with `python -m py_compile`.
4. All CLI tools must provide `--help` flags with usage instructions.

## Implementation Notes
- Uses `urllib.request`, `ssl`, `csv`, `re`, `argparse`, `pathlib`.
- Fixed currency anchor: $1 USD = 95.00 RUB.

## Acceptance Criteria ("Done when")
- `python -m py_compile scripts/*.py` exits with code 0.
- `python scripts/verify_citations.py --help` outputs valid options.
- `python scripts/cost_summary.py` parses `state/cost-log.csv` and outputs formatted markdown tables.

## References
- https://arxiv.org/abs/2607.00738 — "Phantom References": academic motivation for deterministic URL resolution checks.
- https://github.com/langchain-ai/open_deep_research — Reference pattern for deterministic tool integration in research pipelines.

## Dependencies
TICKET-01 (Repository Structure).

## Effort & Risks
- **Effort**: 2.0 person-hours (MUST scope).
- **Risk**: External sites blocking HEAD requests with HTTP 403. *Mitigation*: Fallback to GET request with streaming cutoff and browser User-Agent header.
