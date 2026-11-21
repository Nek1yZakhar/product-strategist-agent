# TICKET-03: 6-Phase Strategic Workflow & Skills Engine

## Goal
Implement a modular suite of 11 agent skills that guide a product manager from a vague initial idea to an empirically justified strategy with human-in-the-loop checkpoints.

## Problem
Unstructured LLM prompts produce superficial, ungrounded advice, skip stakeholder alignment gates, and fail to generate viable negative options like project shutdown.

## Scope
- **MUST**:
  - Create 11 specialized skills in `.agents/skills/*/SKILL.md`:
    1. `strategist`: Intake loop (clarification budget: $\le 2$ questions/step).
    2. `research-planner`: Decision-relevant inquiry planning.
    3. `evidence-collector`: Gathering findings with YAML frontmatter.
    4. `citation-verifier`: Interface to deterministic link checker.
    5. `options-generator`: Mandatory triad (Status Quo, Shutdown, Value Leap).
    6. `adversarial-reviewer`: Red-Team review prompt formulation.
    7. `interview-panel`: Qualitative persona simulation with honesty disclaimers.
    8. `strategy-writer`: Production of Product Strategy, Comms Strategy, Validation Plan.
    9. `decision-journal`: Formal logging of ratified decisions.
    10. `revision-scanner`: Impact detection upon arrival of fresh market data.
    11. `session-resume`: Context bootstrap in fresh IDE chat windows.
- **SHOULD**:
  - YAML frontmatter with `name` and `description` for all skills conforming to Anthropic standard.
- **COULD**:
  - Interactive skill creator utility.

## Requirements
1. Intake clarification in `strategist` must enforce a strict budget of at most 1–2 questions per turn.
2. `options-generator` must always produce at least 3 distinct options, including "Keep as is" and "Shut down direction", each equipped with steelman counterarguments.
3. Conversational copy directed to the user must follow the Russian `sasha` communication standard.
4. Internal skill instructions must remain in English.

## Implementation Notes
- Folder structure follows Anthropic / AgentSkills.io convention (`.agents/skills/<name>/SKILL.md`).
- Step-by-step Mermaid sequence diagrams included in primary skills.

## Acceptance Criteria ("Done when")
- Exactly 11 `SKILL.md` files exist across `.agents/skills/`.
- Each `SKILL.md` starts with valid YAML frontmatter containing `name` and `description`.
- Running an intake query triggers the $\le 2$ question clarification gate.

## References
- https://github.com/anthropics/skills — Official Anthropic Agent Skills specification and folder format.
- https://agentskills.io — Cross-agent skills interoperability standard.
- https://github.com/travisvn/awesome-claude-skills — Curated skills patterns and structures.

## Dependencies
TICKET-01, TICKET-02.

## Effort & Risks
- **Effort**: 2.5 person-hours (MUST scope).
- **Risk**: Verbose skill runbooks exceeding context limits. *Mitigation*: Concise instructions with explicit state pointers.
