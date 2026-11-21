# TICKET-06: Session State & Manus-Style Resumability

## Goal
Enable uninterrupted strategic continuity across chat restarts and developer sessions through deterministic, file-based task state checkpoints.

## Problem
In conversational LLM interfaces, closing a chat window wipes working memory. Product leads cannot conduct multi-day strategic cycles without painstakingly re-explaining context.

## Scope
- **MUST**:
  - `state/STATE-current-task.md`: Living checkpoint capturing active project, phase, open questions, completed steps, next action, and session resume pointer.
  - `skill:session-resume`: Context bootstrap protocol reading state files upon cold boot in a new chat.
  - Deterministic state schema requiring $<1$ second to parse by an incoming agent session.
- **SHOULD**:
  - Session replay pointer mapping to `demo/session_transcript.jsonl`.
- **COULD**:
  - Automatic git commit on state transition.

## Requirements
1. An agent opening a fresh chat window must be able to restore full situational awareness by reading only `state/STATE-current-task.md` and `docs/STATE.md`.
2. State file must be updated at the conclusion of every analytical phase.
3. Cold-boot status message must be emitted in concise, professional Russian (`sasha` standard).

## Implementation Notes
- Architecture inspired by Manus file-based state management and Claude Code task persistence.
- State files reside in `state/`.

## Acceptance Criteria ("Done when")
- `state/STATE-current-task.md` exists and contains valid task metadata.
- Opening a fresh chat and prompting *"Continue project"* triggers `skill:session-resume` and accurately identifies the current task state.

## References
- https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus — Core reference for file-based state and KV-cache optimization.
- https://gist.github.com/renschni/4fbc70b31bad8dd57f3370239dccd58f — Manus state teardown and agent planning loop.

## Dependencies
TICKET-01, TICKET-03.

## Effort & Risks
- **Effort**: 1.5 person-hours (MUST scope).
- **Risk**: State file becoming stale due to missed updates. *Mitigation*: Rule `.agents/rules/workflow.md` enforces updating state before ending turns.
