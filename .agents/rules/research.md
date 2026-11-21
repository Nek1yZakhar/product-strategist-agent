# Rule: Decision-Relevant Research & Triangulation

This rule governs how research questions are decomposed, hypotheses tested, and empirical blind spots managed.

---

## 1. Decision-Driven Inquiry

Research within the repository is strictly subordinate to business decisions:
- **No Vanity Research**: Gathering general macroeconomic or academic trivia that does not change the probability distribution of strategic options is prohibited.
- **Decision-Relevance Test**: Before any web search or literature review query is formed, the agent must identify:
  1. Which strategic option (A, B, or C) would be validated or disqualified by the answer?
  2. What threshold metric (e.g., CAC, churn rate, ARPU) flips the decision?

---

## 2. Source Triangulation Standard

For core market estimates (market size, segment penetrations, competitor shares):
- A single source is insufficient. The agent must seek at least **two independent sources** (e.g., official telecom operator disclosures + third-party regulatory or analytics agency like Roskomnadzor, TelecomDaily, TAdviser).
- When estimates diverge significantly, the agent must document the spread as an interval (e.g., "penetration estimated between 18% and 24%") rather than averaging them into a false precision.

---

## 3. Honest Epistemic Gap Disclosure

When data cannot be obtained from open public sources or available tables:
- **Never Synthesize Fake Data**: Fabricating numbers or pretending a synthetic estimate is empirical data is strictly forbidden.
- **Explicit Gap Logging**: The agent must formally record:
  - What data is missing (e.g., "Internal multi-SIM churn rates for competitor Y").
  - Why it is unobtainable (proprietary commercial secret).
  - The risk / contingency protocol (proxy metric or sensitivity boundary used instead).

