#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/teamwork_runner.py
==========================
Standalone Deterministic Team Work & Multi-Agent Task Runner.
Compliant with Solo-Maker Architecture & Zero External Heavy Frameworks (ADR-001).

Manages multi-agent task execution, DAG dependency resolution, file boundary isolation,
and forensic verification across sprint tickets (TICKET-01 to TICKET-11).
"""

import argparse
import asyncio
import csv
import enum
import json
import os
import subprocess
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple


class AgentRole(str, enum.Enum):
    COORDINATOR = "coordinator"
    RESEARCHER = "researcher"
    IMPLEMENTER = "implementer"
    QA_VERIFIER = "qa_verifier"
    RED_TEAM = "red_team"


@dataclass
class TicketTask:
    ticket_id: str
    title: str
    phase: int
    roles: List[AgentRole]
    dependencies: List[str]
    input_files: List[str]
    output_files: List[str]
    verification_cmd: Optional[str] = None
    timeout_sec: int = 180
    description: str = ""


# Canonical Sprint Tickets DAG (TICKET-01 to TICKET-11)
SPRINT_REGISTRY: Dict[str, TicketTask] = {
    "TICKET-01": TicketTask(
        ticket_id="TICKET-01",
        title="Базовый каркас, правила и аудит здоровья",
        phase=1,
        roles=[AgentRole.COORDINATOR, AgentRole.IMPLEMENTER, AgentRole.QA_VERIFIER],
        dependencies=[],
        input_files=[".env.example"],
        output_files=["AGENTS.md", ".gitignore", ".agents/rules/workflow.md", ".agents/rules/evidence.md"],
        verification_cmd="python -c \"import pathlib; assert pathlib.Path('AGENTS.md').exists(); print('TICKET-01: OK')\"",
        description="Scaffolding, AGENTS.md passport (25-40 lines), and 6 rule files."
    ),
    "TICKET-02": TicketTask(
        ticket_id="TICKET-02",
        title="4-слойная изоляция знаний и методология",
        phase=1,
        roles=[AgentRole.COORDINATOR, AgentRole.RESEARCHER, AgentRole.IMPLEMENTER, AgentRole.QA_VERIFIER],
        dependencies=["TICKET-01"],
        input_files=["docs/source/demo_brief_ru.md", "docs/source/task_ru.md"],
        output_files=[
            "knowledge/methodology/evidence-standards.md",
            "knowledge/methodology/strategy-frameworks.md",
            "knowledge/methodology/synthetic-respondents.md"
        ],
        verification_cmd="python -c \"import pathlib; assert pathlib.Path('knowledge/methodology/evidence-standards.md').exists(); print('TICKET-02: OK')\"",
        description="4-layer knowledge isolation: architecture, methodology, projects, state."
    ),
    "TICKET-03": TicketTask(
        ticket_id="TICKET-03",
        title="6-фазный воркфлоу и движок 11 навыков",
        phase=1,
        roles=[AgentRole.COORDINATOR, AgentRole.IMPLEMENTER, AgentRole.QA_VERIFIER],
        dependencies=["TICKET-01", "TICKET-02"],
        input_files=[".agents/rules/workflow.md"],
        output_files=[
            ".agents/skills/strategist/SKILL.md",
            ".agents/skills/research-planner/SKILL.md",
            ".agents/skills/evidence-collector/SKILL.md",
            ".agents/skills/options-generator/SKILL.md"
        ],
        verification_cmd="python -c \"import pathlib; assert len(list(pathlib.Path('.agents/skills').glob('*/SKILL.md'))) == 11; print('TICKET-03: OK')\"",
        description="Suite of 11 modular Anthropic/AgentSkills.io skills."
    ),
    "TICKET-04": TicketTask(
        ticket_id="TICKET-04",
        title="Детерминированные Python CLI скрипты",
        phase=2,
        roles=[AgentRole.COORDINATOR, AgentRole.IMPLEMENTER, AgentRole.QA_VERIFIER],
        dependencies=["TICKET-01"],
        input_files=["knowledge/projects/demo-megafon/"],
        output_files=["scripts/verify_citations.py", "scripts/extract_brief.py", "scripts/cost_summary.py"],
        verification_cmd="python -m py_compile scripts/verify_citations.py scripts/cost_summary.py scripts/extract_brief.py",
        description="Python 3.11+ deterministic stdlib utilities."
    ),
    "TICKET-05": TicketTask(
        ticket_id="TICKET-05",
        title="Демо-кейс МегаФона (Golden Run)",
        phase=3,
        roles=[AgentRole.COORDINATOR, AgentRole.RESEARCHER, AgentRole.IMPLEMENTER, AgentRole.RED_TEAM, AgentRole.QA_VERIFIER],
        dependencies=["TICKET-02", "TICKET-03", "TICKET-04"],
        input_files=["docs/source/demo_brief_ru.md", "knowledge/projects/demo-megafon/source_brief.txt"],
        output_files=[
            "knowledge/projects/demo-megafon/brief.md",
            "knowledge/projects/demo-megafon/data/baseline-metrics.md",
            "knowledge/projects/demo-megafon/output/options.md",
            "knowledge/projects/demo-megafon/output/adversarial-review.md",
            "knowledge/projects/demo-megafon/output/product-strategy.md",
            "knowledge/projects/demo-megafon/output/communication-strategy.md",
            "knowledge/projects/demo-megafon/output/validation-plan.md",
            "knowledge/projects/demo-megafon/output/ux-journey.md"
        ],
        verification_cmd="python -c \"import pathlib; assert all(pathlib.Path(p).exists() for p in ['knowledge/projects/demo-megafon/brief.md', 'knowledge/projects/demo-megafon/data/baseline-metrics.md', 'knowledge/projects/demo-megafon/output/options.md', 'knowledge/projects/demo-megafon/output/adversarial-review.md', 'knowledge/projects/demo-megafon/output/product-strategy.md', 'knowledge/projects/demo-megafon/output/communication-strategy.md', 'knowledge/projects/demo-megafon/output/validation-plan.md', 'knowledge/projects/demo-megafon/output/ux-journey.md']); print('TICKET-05: OK')\"",
        description="End-to-end Megafon Family demonstration run based on 11-page canonical brief."
    ),
    "TICKET-06": TicketTask(
        ticket_id="TICKET-06",
        title="Возобновляемость сессии в стиле Manus",
        phase=3,
        roles=[AgentRole.COORDINATOR, AgentRole.IMPLEMENTER, AgentRole.QA_VERIFIER],
        dependencies=["TICKET-05"],
        input_files=["knowledge/projects/demo-megafon/brief.md"],
        output_files=["state/STATE-current-task.md", "state/decision-journal.md"],
        verification_cmd="python -c \"import pathlib; assert pathlib.Path('state/STATE-current-task.md').exists(); print('TICKET-06: OK')\"",
        description="Session resumption checkpoint pointer for clean chat windows."
    ),
    "TICKET-07": TicketTask(
        ticket_id="TICKET-07",
        title="Субагент верификации ссылок (Anti-Hallucination)",
        phase=2,
        roles=[AgentRole.COORDINATOR, AgentRole.RESEARCHER, AgentRole.QA_VERIFIER],
        dependencies=["TICKET-04"],
        input_files=["knowledge/projects/demo-megafon/findings/", "scripts/verify_citations.py"],
        output_files=["state/citation-report.md"],
        verification_cmd="python scripts/verify_citations.py --url https://habr.com",
        description="Deterministic network verification of URLs against hallucination (arXiv:2504.00317)."
    ),
    "TICKET-08": TicketTask(
        ticket_id="TICKET-08",
        title="Панель респондентов с честной маркировкой",
        phase=2,
        roles=[AgentRole.COORDINATOR, AgentRole.RESEARCHER, AgentRole.IMPLEMENTER, AgentRole.QA_VERIFIER],
        dependencies=["TICKET-02"],
        input_files=["knowledge/methodology/synthetic-respondents.md"],
        output_files=["knowledge/projects/demo-megafon/data/synthetic-panel.md"],
        verification_cmd="python -c \"import pathlib; p = pathlib.Path('knowledge/projects/demo-megafon/data/synthetic-panel.md'); assert p.exists() and 'МЕТОДОЛОГИЧЕСКИЙ ДИСКЛЕЙМЕР' in p.read_text(encoding='utf-8'); print('TICKET-08: OK')\"",
        description="Synthetic user personas with mandatory hypothesis-only disclaimer."
    ),
    "TICKET-09": TicketTask(
        ticket_id="TICKET-09",
        title="Маршрутизация Pro-моделей и Red-Team Zcode",
        phase=3,
        roles=[AgentRole.COORDINATOR, AgentRole.RED_TEAM, AgentRole.QA_VERIFIER],
        dependencies=["TICKET-03", "TICKET-05"],
        input_files=["knowledge/projects/demo-megafon/output/options.md"],
        output_files=["state/cost-log.csv"],
        verification_cmd="python -c \"import pathlib; assert pathlib.Path('state/cost-log.csv').exists() and pathlib.Path('knowledge/projects/demo-megafon/output/adversarial-review.md').exists(); print('TICKET-09: OK')\"",
        description="Dual-engine Red-Team stress test on Zcode GLM 5.3."
    ),
    "TICKET-10": TicketTask(
        ticket_id="TICKET-10",
        title="Запись сессий и 10-минутный видеосценарий",
        phase=4,
        roles=[AgentRole.COORDINATOR, AgentRole.IMPLEMENTER, AgentRole.QA_VERIFIER],
        dependencies=["TICKET-05", "TICKET-06"],
        input_files=["demo/RUNBOOK.md"],
        output_files=["demo/VIDEO-PLAN.md", "demo/session_transcript.jsonl"],
        verification_cmd="python -c \"import pathlib; assert pathlib.Path('demo/VIDEO-PLAN.md').exists(); print('TICKET-10: OK')\"",
        description="10-minute presentation video script and session recording."
    ),
    "TICKET-11": TicketTask(
        ticket_id="TICKET-11",
        title="Конкурсный пакет и матрица трассируемости",
        phase=4,
        roles=[AgentRole.COORDINATOR, AgentRole.IMPLEMENTER, AgentRole.QA_VERIFIER],
        dependencies=["TICKET-05", "TICKET-10"],
        input_files=["docs/source/task_ru.md"],
        output_files=["docs/SUBMISSION.md", "docs/specs/TRACEABILITY.md"],
        verification_cmd="python -c \"import pathlib; assert pathlib.Path('docs/SUBMISSION.md').exists(); print('TICKET-11: OK')\"",
        description="Full contest compliance checklist and traceability matrix."
    ),
}


class TeamworkOrchestrator:
    """Async Orchestrator managing DAG execution, file isolation, and verification."""

    def __init__(self, registry: Dict[str, TicketTask] = SPRINT_REGISTRY):
        self.registry = registry

    def validate_dag(self) -> Tuple[bool, List[str]]:
        """Validate DAG: check that all dependencies exist and there are no cycles."""
        errors = []
        for tid, task in self.registry.items():
            for dep in task.dependencies:
                if dep not in self.registry:
                    errors.append(f"Ticket {tid} references unknown dependency '{dep}'")

        # Cycle detection via DFS
        visited: Set[str] = set()
        rec_stack: Set[str] = set()

        def dfs(node: str) -> bool:
            visited.add(node)
            rec_stack.add(node)
            for dep in self.registry[node].dependencies:
                if dep not in visited:
                    if dfs(dep):
                        return True
                elif dep in rec_stack:
                    errors.append(f"Cycle detected involving {node} -> {dep}")
                    return True
            rec_stack.remove(node)
            return False

        for tid in self.registry:
            if tid not in visited:
                dfs(tid)

        return len(errors) == 0, errors

    def validate_file_isolation(self) -> Tuple[bool, List[str]]:
        """Verify that tasks in the same phase do not write to the same files."""
        conflicts = []
        phase_groups: Dict[int, List[TicketTask]] = {}
        for task in self.registry.values():
            phase_groups.setdefault(task.phase, []).append(task)

        for phase, tasks in phase_groups.items():
            claimed_outputs: Dict[str, str] = {}
            for task in tasks:
                for out in task.output_files:
                    if out in claimed_outputs:
                        conflicts.append(
                            f"File collision in Phase {phase}: '{out}' claimed by {claimed_outputs[out]} and {task.ticket_id}"
                        )
                    else:
                        claimed_outputs[out] = task.ticket_id

        return len(conflicts) == 0, conflicts

    def generate_mermaid_dag(self) -> str:
        """Render a Mermaid flowchart of the ticket dependencies."""
        lines = ["flowchart TD"]
        for tid, task in self.registry.items():
            roles_str = ",".join([r.value[:4] for r in task.roles])
            lines.append(f'  {tid.replace("-", "_")}["{tid}: {task.title}<br/>({roles_str})"]')
            for dep in task.dependencies:
                lines.append(f'  {dep.replace("-", "_")} --> {tid.replace("-", "_")}')
        return "\n".join(lines)

    async def run_ticket(self, ticket_id: str, mode: str = "dry-run") -> bool:
        """Run or dry-run a specific ticket."""
        if ticket_id not in self.registry:
            print(f"[-] Error: Ticket {ticket_id} not found in registry.")
            return False

        task = self.registry[ticket_id]
        print(f"\n=======================================================")
        print(f"[*] Dispatching: {task.ticket_id} — {task.title}")
        print(f"[*] Phase: {task.phase} | Roles: {[r.value for r in task.roles]}")
        print(f"[*] Dependencies: {task.dependencies}")
        print(f"[*] Input Files: {task.input_files}")
        print(f"[*] Output Files: {task.output_files}")
        print(f"[*] Verification Cmd: {task.verification_cmd}")
        print(f"=======================================================")

        if mode == "dry-run":
            print(f"[+] [DRY-RUN] Verification simulated successfully for {ticket_id}.")
            return True

        # Live execution of verification command
        if task.verification_cmd:
            t0 = time.time()
            proc = await asyncio.create_subprocess_shell(
                task.verification_cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await proc.communicate()
            elapsed = time.time() - t0

            if proc.returncode == 0:
                print(f"[+] [SUCCESS] {task.ticket_id} verified in {elapsed:.2f}s:")
                if stdout:
                    print(stdout.decode("utf-8", errors="replace").strip())
                return True
            else:
                print(f"[-] [FAIL] {task.ticket_id} verification failed (exit {proc.returncode}):")
                if stderr:
                    print(stderr.decode("utf-8", errors="replace").strip())
                return False
        else:
            print(f"[*] No verification command specified for {ticket_id}.")
            return True

    async def run_all(self, mode: str = "dry-run") -> bool:
        """Run all tickets respecting dependency order."""
        dag_ok, dag_errors = self.validate_dag()
        if not dag_ok:
            print("[-] DAG Validation failed:")
            for err in dag_errors:
                print(f"    - {err}")
            return False

        iso_ok, iso_errors = self.validate_file_isolation()
        if not iso_ok:
            print("[-] File isolation validation failed:")
            for err in iso_errors:
                print(f"    - {err}")
            return False

        print(f"[+] DAG and File Boundaries are CLEAN. Running {len(self.registry)} tickets ({mode})...")
        success_count = 0
        for tid in self.registry:
            ok = await self.run_ticket(tid, mode=mode)
            if ok:
                success_count += 1
            else:
                print(f"[-] Halting execution on failure of {tid}")
                return False

        print(f"\n[+] Completed {success_count}/{len(self.registry)} tickets successfully.")
        return True


def main():
    parser = argparse.ArgumentParser(
        description="Team Work & Multi-Agent Task Runner for Product Strategist Agent"
    )
    parser.add_argument("--ticket", type=str, help="Specific ticket ID (e.g. TICKET-04)")
    parser.add_argument(
        "--mode", choices=["dry-run", "live"], default="dry-run", help="Execution mode (default: dry-run)"
    )
    parser.add_argument("--validate-all", action="store_true", help="Validate DAG topology and file isolation")
    parser.add_argument("--dag", action="store_true", help="Print Mermaid flowchart DAG")

    args = parser.parse_args()
    orchestrator = TeamworkOrchestrator()

    if args.dag:
        print(orchestrator.generate_mermaid_dag())
        sys.exit(0)

    if args.validate_all:
        dag_ok, dag_errors = orchestrator.validate_dag()
        iso_ok, iso_errors = orchestrator.validate_file_isolation()
        if dag_ok and iso_ok:
            print(f"[+] All 11 tickets valid. 0 cycles, 0 missing dependencies, 0 file boundary collisions.")
            # Verify live check
            asyncio.run(orchestrator.run_all(mode="live"))
            sys.exit(0)
        else:
            for err in dag_errors + iso_errors:
                print(f"[-] {err}")
            sys.exit(1)

    if args.ticket:
        ok = asyncio.run(orchestrator.run_ticket(args.ticket, mode=args.mode))
        sys.exit(0 if ok else 1)

    # Default action
    asyncio.run(orchestrator.run_all(mode=args.mode))


if __name__ == "__main__":
    main()
