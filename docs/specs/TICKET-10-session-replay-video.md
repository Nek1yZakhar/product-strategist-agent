# TICKET-10: Session Replay & 10-Minute Video Script Engine

## Goal
Deliver a complete demonstration package including an end-to-end scenario runbook, reference session transcript, and second-by-second video screenplay mapped to the 10-minute contest limit.

## Problem
Competition entries often lose points on implementation and presentation quality due to disorganized demo videos that exceed time limits, skip critical requirements, or rely on slow live API calls that bore evaluators.

## Scope
- **MUST**:
  - `demo/RUNBOOK.md`: Step-by-step walkthrough covering the 6 phases from vague request to resumed session.
  - `demo/VIDEO-PLAN.md`: Second-by-second screenplay (00:00 to 09:50) with Russian voiceover script and visual focus cues covering all 4 contest criteria.
  - `demo/session_transcript.jsonl`: Reference session recording formatted for terminal replay utilities.
- **SHOULD**:
  - Paced replay timing configuration to simulate real-time agent typing without dead air.
- **COULD**:
  - Asciinema `.cast` recording file for embedding interactive terminal replays.

## Requirements
1. Total video screenplay runtime must strictly not exceed 10 minutes (600 seconds).
2. The script must explicitly cover:
   - Initial vague request and intake clarification.
   - Evidence gathering and deterministic URL verification.
   - Options formulation (including Status Quo and Shutdown).
   - Adversarial Red-Team audit by GLM 5.3.
   - Product Strategy, Communication Strategy, and Validation Plan.
   - Simulated break and session resumption in a fresh chat window.
   - Final cost accounting report.
3. Voiceover copy must be written in professional Russian (`sasha` standard).

## Implementation Notes
- Files reside in `demo/`.
- Designed for compatibility with `BenLirio/claude-session-replay` and `es617/claude-replay`.

## Acceptance Criteria ("Done when")
- `demo/RUNBOOK.md` provides clear copy-paste commands for every phase.
- `demo/VIDEO-PLAN.md` has timestamps from 00:00 to 09:50 without gaps.
- `demo/session_transcript.jsonl` exists and is valid JSONL.

## References
- https://github.com/BenLirio/claude-session-replay — Pure-Python session JSONL to self-contained HTML replay.
- https://github.com/es617/claude-replay — Paced multi-IDE replay tool.
- https://asciinema.org/ and https://github.com/asciinema/asciinema — Asciinema headless recording standard.

## Dependencies
TICKET-05 (Demo Case Study), TICKET-06 (Session Resumability).

## Effort & Risks
- **Effort**: 2.0 person-hours (MUST scope).
- **Risk**: Video running over the 10-minute contest limit. *Mitigation*: Script time-boxed to 09:50 with 10-second safety buffer.
