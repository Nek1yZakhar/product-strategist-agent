# Rule: Knowledge Isolation & Repository Architecture

This rule defines the strict boundaries between instructional layers, methodologies, project-specific materials, and real-time state files.

---

## 1. The Four-Layer Separation Principle

The repository enforces strict cognitive and storage separation across four distinct directories:

| Layer | Directory | Lifecycle & Mutability | Purpose |
| :--- | :--- | :--- | :--- |
| **Layer 1: Instructions** | `AGENTS.md`, `.agents/rules/`, `.agents/skills/` | Permanent, immutable during run | Operational governance, agent capabilities, workflow contracts |
| **Layer 2: Methodology** | `knowledge/methodology/` | Evolving, validated standards | Strategy frameworks, evidence policies, prompt templates |
| **Layer 3: Project Materials**| `knowledge/projects/<project>/` | Project-scoped, incremental | Incoming briefs, extracted data, research findings, final strategies |
| **Layer 4: Current State** | `state/`, `docs/STATE.md` | Ephemeral, frequently updated | Resumable task pointers, decision logs, financial cost tracking |

Cross-contamination between layers is strictly prohibited. For example:
- Never write task-specific data into `.agents/rules/`.
- Never record runtime checkpoints in `knowledge/methodology/`.
- Never mutate raw source files in `docs/source/`.

---

## 2. Ground Truth Immutability (`docs/source/`)

- Files located in `docs/source/` (`task_ru.md`, `demo_brief_ru.md`) represent immutable ground truth provided by the contest organizers and client stakeholders.
- Agents are strictly forbidden from modifying, truncating, or refactoring files in `docs/source/`.
- Extracted summaries and normalized briefs must be written into `knowledge/projects/<project>/brief.md`.

---

## 3. Retraction & Outdated Entry Protocol

- When fresh evidence invalidates an earlier finding or assumption, the original file in `knowledge/projects/<project>/findings/` must NOT be silently deleted or overwritten without trace.
- The agent must:
  1. Update the frontmatter field `confidence` to `retracted`.
  2. Add a `Retraction Notice` section explaining the superseding evidence and timestamp.
  3. Log the change in `state/decision-journal.md` and `docs/CHANGELOG.md`.

