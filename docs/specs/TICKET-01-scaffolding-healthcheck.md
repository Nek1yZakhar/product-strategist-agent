# TICKET-01: Core Repository Scaffolding, Governance Passport & Healthcheck

## Goal
Establish a clean, lean repository-as-agent topology that runs natively inside agentic IDEs without external daemon runtimes.

## Problem
Without an explicit domain passport and governance foundation, agent sessions hallucinate project boundaries, duplicate system rules, or attempt to launch heavy background daemons that break IDE workflows.

## Scope
- **MUST**:
  - Root `AGENTS.md` (Domain Passport, 25–40 lines) defining model allocation, CLI tooling, environment variables, and pointers.
  - Core rules engine in `.agents/rules/` (`workflow.md`, `evidence.md`, `knowledge.md`, `cost.md`, `research.md`, `deliverables.md`).
  - `.env.example` with safe placeholder configuration.
  - `.gitignore` protecting secrets, Python bytecache, and IDE temporary files.
- **SHOULD**:
  - Automated directory sanity check command in Python.
- **COULD**:
  - Pre-commit hook for secret scanning.

## Requirements
1. `AGENTS.md` must not exceed 40 lines and must contain no duplicate global system invariants.
2. `.agents/rules/` must contain 6 distinct markdown rules enforcing workflow, evidence, knowledge isolation, cost accounting, research discipline, and competition deliverables.
3. Git repository must ignore `.env` and Python cache files.
4. All instructions and rules must be written in English for high-density reasoning.

## Implementation Notes
- Files created: `AGENTS.md`, `.env.example`, `.gitignore`, `.agents/rules/*.md`.
- Architecture reference: Follows the "folder agent" pattern where the workspace directory itself represents the agent.

## Acceptance Criteria ("Done when")
- `Test-Path AGENTS.md` returns True.
- Line count of `AGENTS.md` is between 25 and 40 lines.
- All 6 rule files exist in `.agents/rules/`.
- Git status confirms `.env` is ignored when created.

## References
- https://code.claude.com/docs/en/best-practices — Best practices for agent rules vs skills vs hooks and task-tracking discipline.
- https://www.reddit.com/r/ClaudeAI/comments/1q403xw/ — Claude Code as an office automation platform: validating folder-agent design.

## Dependencies
None (Root bootstrap ticket).

## Effort & Risks
- **Effort**: 1.5 person-hours (MUST scope).
- **Risk**: Rule bloat degrading context window. *Mitigation*: Progressive disclosure; keep rules concise ($\le 8\text{ KB}$).
