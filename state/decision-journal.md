# Strategic Decision Journal

This journal records formal product and communication decisions, their rationale, assigned owners, tracking metrics, and explicit revision triggers.

---

## Log Schema

| Field | Description |
| :--- | :--- |
| **Decision ID** | Unique identifier (e.g., `DEC-2026-MF-01`) |
| **Timestamp** | ISO-8601 UTC timestamp |
| **Project** | Target project (e.g., `demo-megafon`) |
| **Options Weighed** | List of evaluated options (incl. Status Quo and Shutdown) |
| **Selected Option** | Winning strategic direction |
| **Core Rationale** | Key justification linking user value to unit economics |
| **Accepted Counterarguments** | Legitimate risks identified by red-team and how they are mitigated |
| **Owner** | Responsible manager (Zakhar) |
| **Primary Metric** | Key KPI & target threshold |
| **Revision Trigger** | Condition that mandates reopening the decision |

---

## Decision Records

### [DEC-2026-MF-01] Ratification of Megafon Family 2.0 Strategic Pivot
- **Timestamp**: `2026-11-22T02:07:00Z`
- **Project**: `demo-megafon`
- **Options Weighed**:
  1. *Option A (Status Quo)*: Inertial optimization, maintain current mechanics, accept plan deficit (-20%).
  2. *Option B (Shutdown)*: Terminate direction, migrate groups to mono-tariffs, risk -10M ₽ margin loss.
  3. *Option C (Value Pivot)*: Relaunch as "Digital Family Security & Smart-Device Hub".
- **Selected Option**: **Option C (Value Pivot: «МегаФон Семья 2.0 — Цифровая Защита»)**
- **Core Rationale**:
  - Unlocks 40 000 multi-SIM subscriber pool and 100 000 pilot households without entering a margin-destroying price war.
  - Leverages verified retention anchor (+500 ₽ gross profit per extra month of group life) by reducing monthly churn from 1.8% to 1.1%.
  - Targets doubling active groups from 4,000 to 8,000 by year-end and generating +20 млн ₽ incremental gross profit.
- **Accepted Counterarguments & Mitigations (GLM 5.3 Red-Team Audit)**:
  1. *Margin leakage on IoT*: Capped device data traffic and set fixed 99 ₽/mo fee for smart watches instead of free unlimited tier.
  2. *Cannibalization of VIP lines*: Enforced group ARPA minimum threshold of 1,650 ₽.
  3. *Anti-fraud & privacy*: Replaced raw SMS codes with asynchronous secure in-app Push confirmation.
- **Owner**: **Захар (Zakhar, Solo Maker)**
- **Primary Metric**: **8 000 active family groups / 12 000 connected groups** by year-end; ARPA $\ge 1\,650$ ₽.
- **Revision Triggers**:
  - If 60-day cohort net active groups grow by $< 1\,000$ groups.
  - If overall cohort gross profit decreases by $> 5$ млн ₽ due to unforeseen cannibalization.
  - If competitor (MTS/Beeline) introduces free universal family sharing nationwide.
