# Rule: Contest Deliverables & Traceability Matrix

This matrix provides 100% bidirectional traceability between the official MGIMO AI Challenge 2026 task requirements and repository components.

---

## Traceability Matrix

| Contest Requirement | Implementation in Repository | Primary Skill / Script | Verifiable Artifact |
| :--- | :--- | :--- | :--- |
| **1. Task Framing** | Intake loop with $\le 2$ questions/turn, clarifying goal, recipient, constraints, data. | `skill:strategist` | `knowledge/projects/demo-megafon/brief.md` |
| **2. Material Collection** | External source gathering with per-claim links, anti-hallucination URL verification. | `skill:evidence-collector`, `skill:citation-verifier` | `knowledge/projects/demo-megafon/findings/*.md`, `scripts/verify_citations.py` |
| **3. Decision Research** | Research driven by decision questions, source cross-checking, honest gap disclosure. | `skill:research-planner` | `knowledge/methodology/evidence-standards.md`, research findings |
| **4. Strategic Options** | $\ge 3$ distinct options, ALWAYS including Status Quo and Shutdown, with steelman counterarguments. | `skill:options-generator`, `skill:adversarial-reviewer` | `knowledge/projects/demo-megafon/output/options.md`, red-team reviews |
| **5a. Product Strategy** | Audience, JTBD, alternatives, chosen vector & conscious refusals, value-cost link. | `skill:strategy-writer` | `knowledge/projects/demo-megafon/output/product-strategy.md` |
| **5b. Communication Strategy**| Audience, purchase situation, perception barriers, core message, channel matrix. | `skill:strategy-writer` | `knowledge/projects/demo-megafon/output/communication-strategy.md` |
| **5c. Validation Plan** | Expected changes, comparison baseline, observation window, adverse effect monitoring. | `skill:strategy-writer` | `knowledge/projects/demo-megafon/output/validation-plan.md` |
| **6. Human-in-the-Loop** | Explicit confirmation gates at intake, options selection, and strategy sign-off. | `.agents/rules/workflow.md` | Session checkpoints & runbook |
| **7. 4-Layer Separation** | Strict separation: Instructions vs Methodology vs Projects vs State. | `.agents/rules/knowledge.md` | Repository folder hierarchy |
| **8. Session Resumability** | Full state checkpointing and restoration in a fresh IDE chat window. | `skill:session-resume` | `state/STATE-current-task.md` |
| **9. Cost Transparency** | Logging of model, tokens, and estimated financial costs per step. | `.agents/rules/cost.md`, `scripts/cost_summary.py` | `state/cost-log.csv`, cost report |
| **10. Synthetic Respondents** | Persona exploration strictly labeled as hypothesis generation (arXiv:2507.04438). | `skill:interview-panel` | `knowledge/methodology/synthetic-respondents.md` |
| **11. Decision Support** | Structured decision register with owners, metrics, staleness and revision conditions. | `skill:decision-journal` | `state/decision-journal.md` |
| **12. Revision on New Data** | Automatic detection of affected conclusions, delta updates, audit logging. | `skill:revision-scanner` | Revised findings & decision journal logs |
| **13. Video & Submission Pack** | <=10 min video script, step-by-step runbook, PDF structure and contest checklist. | `demo/RUNBOOK.md`, `demo/VIDEO-PLAN.md` | `docs/SUBMISSION.md` |

