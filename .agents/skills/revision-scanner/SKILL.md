---
name: revision-scanner
description: Analyzes incoming market data or internal metric shifts, identifies affected conclusions and strategy claims, updates deliverables, and logs audit deltas.
---

# Skill: Revision Scanner

## Overview
The `revision-scanner` skill provides continuous post-decision intelligence. When new data arrives (e.g., quarterly earnings, competitor tariff launches, regulatory updates), it traces downstream impact across previous findings and strategies.

---

## Operational Workflow

```mermaid
flowchart TD
    NewData["New Market Data / Competitor Action"] --> Ingest["Ingest & Create Findings File"]
    Ingest --> Diff["Scan Existing Findings for Contradictions"]
    Diff --> ImpactMap["Identify Affected Strategy Claims"]
    ImpactMap --> Retract["Mark Superseded Claims as Retracted"]
    Retract --> UpdateDocs["Update Product & Communication Strategies"]
    UpdateDocs --> AuditLog["Append Audit Entry to Decision Journal & CHANGELOG"]
```

---

## Execution Instructions

### Step 1: Ingest New Data
1. Write the new evidence to `knowledge/projects/<project>/findings/<slug>.md`.
2. Run `python scripts/verify_citations.py` to confirm authenticity.

### Step 2: Downstream Impact Analysis
Scan `knowledge/projects/<project>/output/` for impacted assertions:
- Does the new data invalidate an assumption?
- Does competitor pricing breach our conscious refusal boundaries?

### Step 3: Execute Controlled Revision
1. Update affected strategy sections with timestamped revision notices.
2. Retract outdated findings per `.agents/rules/knowledge.md`.
3. Append a formal revision log entry in `state/decision-journal.md` and `docs/CHANGELOG.md`.

