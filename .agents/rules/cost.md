# Rule: Financial Cost Transparency & Model Routing

This rule governs token expenditure, cost tracking, and economic routing across model providers.

---

## 1. Universal Cost Logging Standard

Every analytical step, external API query, or major reasoning session must record its token utilization and estimated financial cost in `state/cost-log.csv`.

### CSV Schema (`state/cost-log.csv`):
```csv
timestamp,phase,model,input_tokens,output_tokens,est_cost_usd,notes
```

- `timestamp`: ISO-8601 UTC timestamp (`YYYY-MM-DDTHH:MM:SSZ`).
- `phase`: Active workflow phase (`phase_1_intake`, `phase_2_research`, `phase_3_options`, `phase_4_redteam`, `phase_5_strategy`, `phase_6_governance`, `phase_r_revision`).
- `model`: Canonical model identifier (`gemini-3.8-flash`, `glm-5.3`, `perplexity-sonar`, `claude-3.7-sonnet`).
- `input_tokens`: Prompt token count.
- `output_tokens`: Completion token count.
- `est_cost_usd`: Calculated cost in USD based on standard blended rates.
- `notes`: Brief 2–5 word description of the operation.

---

## 2. Model Routing Tiers & Cost Optimization

To prevent token waste and excessive runtime costs, the agent applies hierarchical routing:

| Workstream Tier | Recommended Model | Pricing Bracket | Use Cases |
| :--- | :--- | :--- | :--- |
| **Tier 1: High-Speed Scaffolding** | `gemini-3.8-flash` | ~$0.10 / 1M tokens | Intake clarification, parsing briefs, markdown formatting, state logging |
| **Tier 2: Adversarial Red-Team** | `glm-5.3` (via Zcode) | ~$0.50 / 1M tokens | Devil's advocacy, stress-testing unit economics, regulatory audits |
| **Tier 3: Web Grounding & Panel** | Perplexity Pro / Sonar | ~$1.00 / 1M tokens | Fresh telecom industry metrics, competitor pricing checks |

---

## 3. Automated Cost Reporting

The agent must maintain `scripts/cost_summary.py`. When executed:
- Parses `state/cost-log.csv`.
- Aggregates spend by phase and by model.
- Generates a markdown table displaying total input/output tokens, total USD spend, and converted RUB equivalent for presentation in the final contest PDF report.

