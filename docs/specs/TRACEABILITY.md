# Traceability Matrix: MGIMO AI Challenge 2026

**Contest**: MGIMO AI Challenge 2026  
**Nomination**: «ИИ-проект»  
**Track**: «Стратег Фабрики продуктов» (Megafon Product Factory)  
**Author**: **Zakhar (Solo Maker)**  

This document establishes 100% bidirectional traceability between the official competition requirements and the engineering tickets, agent skills, and verifiable artifacts delivered in this repository.

---

## 1. Mandatory Minimum Requirements (Core Criteria)

| # | Competition Requirement | Implementing Ticket(s) | Operational Skill / Script | Verifiable Deliverable Artifact |
| :-: | :--- | :--- | :--- | :--- |
| **1** | **Task Framing & Clarification**<br/>Clarify goal, recipient, constraints, baseline data; ask only what gates next step ($\le 2$ questions/step). | `TICKET-03`<br/>`TICKET-05` | `skill:strategist` | `knowledge/projects/demo-megafon/brief.md`<br/>`state/STATE-current-task.md` |
| **2** | **Source Gathering & Citations**<br/>Gather materials from allowed open sources; every factual claim must retain an authoritative source link. | `TICKET-04`<br/>`TICKET-07` | `skill:evidence-collector`<br/>`scripts/verify_citations.py` | `knowledge/projects/demo-megafon/findings/*.md`<br/>(5 verified files with YAML frontmatter) |
| **3** | **Decision-Driven Research**<br/>Plan driven by decision-changing questions; cross-check sources; honestly disclose gaps. | `TICKET-02`<br/>`TICKET-03` | `skill:research-planner` | `knowledge/methodology/evidence-standards.md`<br/>`findings/` (triangulation sections) |
| **4** | **Strategic Options Triad**<br/>$\ge 3$ distinct options, ALWAYS including "Keep as is" and "Shut down direction"; strong objections per option. | `TICKET-03`<br/>`TICKET-05` | `skill:options-generator`<br/>`skill:adversarial-reviewer` | `knowledge/projects/demo-megafon/output/options.md`<br/>`output/adversarial-review.md` |
| **5a**| **Product Strategy**<br/>Audience & JTBD, existing alternatives, chosen vector & conscious refusals, value-to-cost link. | `TICKET-03`<br/>`TICKET-05` | `skill:strategy-writer` | `knowledge/projects/demo-megafon/output/product-strategy.md` |
| **5b**| **Communication Strategy**<br/>Audience & situation, perception barriers, single-minded message & RTB, channel roles, honest promises. | `TICKET-03`<br/>`TICKET-05` | `skill:strategy-writer` | `knowledge/projects/demo-megafon/output/communication-strategy.md` |
| **5c**| **Empirical Validation Plan**<br/>Expected metric change, baseline comparison, observation window, cannibalization/adverse monitor. | `TICKET-03`<br/>`TICKET-05` | `skill:strategy-writer` | `knowledge/projects/demo-megafon/output/validation-plan.md` |
| **6** | **Human-in-the-Loop Workflow**<br/>Step-by-step workflow with human checkpoints at critical choice gates. | `TICKET-01`<br/>`TICKET-03` | `.agents/rules/workflow.md`<br/>`skill:strategist` | Confirmation checkpoints in chat and `demo/RUNBOOK.md` |
| **7** | **4-Layer Knowledge Isolation**<br/>Separate storage for instructions, methodology, project materials, and current task state. | `TICKET-01`<br/>`TICKET-02` | `.agents/rules/knowledge.md` | Root folder structure (`.agents/`, `knowledge/`, `state/`) |
| **8** | **Session Resumability**<br/>Resume work after break, including cold start in a fresh IDE chat session (Manus-style file state). | `TICKET-06` | `skill:session-resume` | `state/STATE-current-task.md`<br/>`state/decision-journal.md` |
| **9** | **Transparency & Cost Accounting**<br/>Full visibility of actions, grounds, token consumption, and financial spend per analytical step. | `TICKET-04`<br/>`TICKET-09` | `scripts/cost_summary.py`<br/>`.agents/rules/cost.md` | `state/cost-log.csv`<br/>Automated financial summary report |

---

## 2. Bonus-Level Features (Additional Evaluation Points)

| Bonus Capability | Methodological & Technical Implementation | Implementing Ticket(s) | Verifiable Deliverable Artifact |
| :--- | :--- | :--- | :--- |
| **Synthetic Interview Panel** | LLM personas strictly labeled as qualitative hypothesis generation; never demand proof (arXiv:2607.26348). | `TICKET-08` | `knowledge/methodology/synthetic-respondents.md`<br/>`skill:interview-panel` |
| **Anti-Hallucination Link Verifier** | Deterministic HTTP HEAD/GET resolver detecting dead links and fabricated URLs (arXiv:2504.00317, arXiv:2607.00738). | `TICKET-04`<br/>`TICKET-07` | `scripts/verify_citations.py`<br/>Audit report (100% verified URLs) |
| **UX & Journey Analysis** | Grounded interface and journey analysis eliminating the 42% SMS onboarding drop-off. | `TICKET-05` | `knowledge/projects/demo-megafon/output/ux-journey.md` |
| **Reproducible Data Analysis** | Python stdlib verification of baseline metrics, unit economics (+500 ₽/mo retention anchor). | `TICKET-04`<br/>`TICKET-05` | `knowledge/projects/demo-megafon/data/baseline-metrics.md` |
| **Post-Decision Governance** | Long-term operational contract with owners, target metrics, and explicit revision triggers. | `TICKET-03`<br/>`TICKET-05` | `state/decision-journal.md`<br/>(Record `DEC-2026-MF-01`) |
| **Revision on New Data** | Automated impact scanning across previous findings and strategies upon arrival of fresh market data. | `TICKET-03` | `skill:revision-scanner`<br/>`.agents/rules/knowledge.md` |
| **Model Routing & Red-Team** | Primary strategist on Gemini 3.8 Flash; independent adversarial critic on GLM 5.3 in Zcode; Perplexity Pro copilot. | `TICKET-09` | `docs/ARCHITECTURE.md`<br/>`output/adversarial-review.md` |
| **Session Replay Video Engine** | Second-by-second 10-minute video screenplay and reference session transcript for replay tools. | `TICKET-10` | `demo/VIDEO-PLAN.md`<br/>`demo/RUNBOOK.md`<br/>`demo/session_transcript.jsonl` |
| **Zero-Framework Portability** | Pure file-based repo-agent with zero daemon dependencies, runnable in AntiGravity, Cursor, Claude Code, Zcode. | `TICKET-01`<br/>`TICKET-11` | `AGENTS.md`<br/>`README.md` |

---

## 3. Competition Deliverables Checklist

| Mandatory Deliverable | Required Specification | Status | Location in Repository |
| :--- | :--- | :---: | :--- |
| **GitHub / GitVerse Repository** | Clean repo with 5-minute launch instructions in README. | **READY** | Root directory (`README.md`, `AGENTS.md`) |
| **Megafon Demo Project** | End-to-end case study on family connectivity brief (open data only). | **READY** | `knowledge/projects/demo-megafon/` |
| **Video Recording ($\le 10$ min)** | Request $\to$ Agent work $\to$ Options $\to$ Strategy $\to$ Resume after break. | **READY** | `demo/VIDEO-PLAN.md`, `demo/RUNBOOK.md` |
| **PDF Project Description** | Architecture, models, key prompts, bonus features, time & costs, limits. | **READY** | `docs/CONTEXT.md`, `docs/ARCHITECTURE.md`, `scripts/cost_summary.py` |
