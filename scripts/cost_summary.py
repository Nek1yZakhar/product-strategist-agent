#!/usr/bin/env python3
"""
scripts/cost_summary.py — Financial Token Accounting & Cost Reporter
Part of the Product Strategist Agent (MGIMO AI Challenge 2026).

Parses state/cost-log.csv, aggregates token consumption across models and phases,
computes estimated expenditure in USD and RUB, and outputs a formatted markdown
summary table for inclusion in contest reports and executive briefs.
"""

import argparse
import csv
import sys
from pathlib import Path


USD_TO_RUB_EXCHANGE_RATE = 95.0


def parse_cost_log(csv_path: Path) -> list[dict]:
    """Parses state/cost-log.csv safely."""
    records = []
    if not csv_path.exists():
        return records

    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                records.append({
                    "timestamp": row.get("timestamp", "").strip(),
                    "phase": row.get("phase", "unknown").strip(),
                    "model": row.get("model", "unknown").strip(),
                    "input_tokens": int(row.get("input_tokens", 0)),
                    "output_tokens": int(row.get("output_tokens", 0)),
                    "est_cost_usd": float(row.get("est_cost_usd", 0.0)),
                    "notes": row.get("notes", "").strip(),
                })
            except (ValueError, TypeError):
                continue
    return records


def generate_cost_report(records: list[dict]) -> str:
    """Generates structured markdown cost report."""
    if not records:
        return "No cost records found in `state/cost-log.csv`."

    total_input_tokens = sum(r["input_tokens"] for r in records)
    total_output_tokens = sum(r["output_tokens"] for r in records)
    total_tokens = total_input_tokens + total_output_tokens
    total_usd = sum(r["est_cost_usd"] for r in records)
    total_rub = total_usd * USD_TO_RUB_EXCHANGE_RATE

    # Grouping by phase
    phase_stats = {}
    for r in records:
        p = r["phase"]
        if p not in phase_stats:
            phase_stats[p] = {"in": 0, "out": 0, "cost": 0.0, "calls": 0}
        phase_stats[p]["in"] += r["input_tokens"]
        phase_stats[p]["out"] += r["output_tokens"]
        phase_stats[p]["cost"] += r["est_cost_usd"]
        phase_stats[p]["calls"] += 1

    # Grouping by model
    model_stats = {}
    for r in records:
        m = r["model"]
        if m not in model_stats:
            model_stats[m] = {"in": 0, "out": 0, "cost": 0.0, "calls": 0}
        model_stats[m]["in"] += r["input_tokens"]
        model_stats[m]["out"] += r["output_tokens"]
        model_stats[m]["cost"] += r["est_cost_usd"]
        model_stats[m]["calls"] += 1

    lines = []
    lines.append("### Financial Expenditure & Token Accounting Summary")
    lines.append(f"**Exchange Rate Anchor**: $1 = {USD_TO_RUB_EXCHANGE_RATE:.2f} ₽ | **Total Operations Logged**: {len(records)}\n")

    lines.append("#### 1. Aggregate Financial Totals")
    lines.append("| Total Input Tokens | Total Output Tokens | Total Combined Tokens | Total Spend (USD) | Total Spend (RUB) |")
    lines.append("| :---: | :---: | :---: | :---: | :---: |")
    lines.append(f"| {total_input_tokens:,} | {total_output_tokens:,} | {total_tokens:,} | **${total_usd:.4f}** | **{total_rub:.2f} ₽** |\n")

    lines.append("#### 2. Expenditure by Analytical Phase")
    lines.append("| Workflow Phase | Operations | Input Tokens | Output Tokens | Est. Cost (USD) | Est. Cost (RUB) |")
    lines.append("| :--- | :---: | :---: | :---: | :---: | :---: |")
    for phase, s in sorted(phase_stats.items()):
        p_rub = s["cost"] * USD_TO_RUB_EXCHANGE_RATE
        lines.append(f"| `{phase}` | {s['calls']} | {s['in']:,} | {s['out']:,} | ${s['cost']:.4f} | {p_rub:.2f} ₽ |")
    lines.append("")

    lines.append("#### 3. Expenditure by Model Engine")
    lines.append("| Model Identifier | Invocations | Input Tokens | Output Tokens | Est. Cost (USD) | Share of Budget |")
    lines.append("| :--- | :---: | :---: | :---: | :---: | :---: |")
    for model, s in sorted(model_stats.items()):
        share = (s["cost"] / total_usd * 100.0) if total_usd > 0 else 0.0
        lines.append(f"| `{model}` | {s['calls']} | {s['in']:,} | {s['out']:,} | ${s['cost']:.4f} | {share:.1f}% |")

    lines.append("\n> [!NOTE]")
    lines.append("> Token expenditure is tracked strictly in accordance with contest criteria for economic efficiency.")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Financial Token Accounting & Cost Reporter")
    parser.add_argument("--csv", default="state/cost-log.csv", help="Path to cost-log.csv")
    parser.add_argument("--rub-rate", type=float, default=95.0, help="USD to RUB conversion rate")

    args = parser.parse_args()

    global USD_TO_RUB_EXCHANGE_RATE
    USD_TO_RUB_EXCHANGE_RATE = args.rub_rate

    repo_root = Path(__file__).resolve().parent.parent
    csv_path = repo_root / args.csv

    records = parse_cost_log(csv_path)
    report = generate_cost_report(records)
    print(report)


if __name__ == "__main__":
    main()

