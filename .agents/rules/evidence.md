# Rule: Evidence Standards, Citation Integrity & Synthetic Honesty

This rule enforces strict epistemic standards across all data collection, research, and analysis tasks within the repository.

---

## 1. Per-Claim Citation Invariant & Frontmatter Standard

Every factual claim derived from external sources (reports, articles, datasets, regulatory docs) must be recorded in an isolated findings markdown file in `knowledge/projects/<project>/findings/<slug>.md`.

### Mandatory Findings Frontmatter Schema:
```yaml
---
claim: "Exact, unambiguous factual claim stated in a single sentence"
source_url: "https://example.com/verified-report-link"
verified: pending | verified | dead | hallucinated
confidence: fact | hypothesis | assumption
date_checked: "YYYY-MM-DD"
author: "Authoritative Organization / Source Name"
data_period: "Reporting period (e.g., 2025-Q4)"
---

### Context & Supporting Excerpt
Direct quotation or data extract supporting the claim.

### Methodological Triangulation
Comparison against at least one secondary source or historical baseline.
```

---

## 2. Citation Verification Policy & Anti-Hallucination Guardrails

- **Academic Grounding**: Recent scientific benchmarks document a 3–13% rate of hallucinated URLs in autonomous research outputs ([arXiv:2504.00317](https://arxiv.org/abs/2504.00317)), with 84.7% of downstream report errors tracing directly to unverified orchestrator claims ([arXiv:2608.24306](https://arxiv.org/abs/2608.24306)).
- **Mandatory Tooling**: Agents must run `python scripts/verify_citations.py` on all findings.
- **Status Classification**:
  - `verified`: HTTP status 200 returned, page content verified.
  - `dead`: HTTP 404 / 410 or domain unreachable.
  - `hallucinated`: URL does not exist or points to fabricated domain.
- Any finding marked `dead` or `hallucinated` is immediately disqualified from serving as a foundation for strategic choices.

---

## 3. Strict Epistemic Labeling (Fact vs. Hypothesis vs. Assumption)

Every strategic proposition and metric projection must carry an explicit classification:
1. **Fact [FACT]**: Empirically documented metric, historical company record, or verified third-party audit with live source link.
2. **Hypothesis [HYPOTHESIS]**: Plausible causal proposition that can be verified or falsified by empirical testing (e.g., "Bundling multi-SIM reduces monthly churn by 0.4pp").
3. **Assumption [ASSUMPTION]**: Unverified baseline premise required for computational modeling (e.g., "Average household size remains stable at 2.4 persons").

---

## 4. Synthetic Respondents & AI Persona Policy

- **Scientific Reality**: Synthetic respondents and LLM personas fail to provide valid statistical evidence of real consumer willingness-to-pay or market demand ([Chen, Zhu, & Zheng, arXiv:2507.04438](https://arxiv.org/abs/2507.04438); Verasight 2026 Midterm Validation Study: RMSE 8.3 percentage points against actual behavior).
- **Mandatory Honesty Standard**:
  - LLM-simulated respondents are permitted **EXCLUSIVELY for hypothesis generation, qualitative interview guide preparation, and cognitive blind-spot exploration**.
  - Synthetic respondent outputs must **NEVER** be cited as market demand proof, customer validation, or willingness-to-pay metrics.
  - Every synthetic persona document must begin with the following verbatim disclaimer:
    > `[METHODOLOGICAL DISCLAIMER: This persona output is generated via synthetic LLM simulation and serves exclusively for qualitative hypothesis generation and blind-spot identification. It does NOT constitute empirical evidence of consumer demand, behavior, or purchasing intent (arXiv:2507.04438).]`

