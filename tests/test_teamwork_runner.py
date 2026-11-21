#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tests/test_teamwork_runner.py
=============================
Unit tests for the Teamwork & Multi-Agent Task Runner.
"""

import sys
import unittest
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.teamwork_runner import TeamworkOrchestrator, SPRINT_REGISTRY, AgentRole


class TestTeamworkRunner(unittest.TestCase):
    def setUp(self):
        self.orchestrator = TeamworkOrchestrator()

    def test_registry_has_all_11_tickets(self):
        """Verify that all 11 sprint tickets are registered."""
        self.assertEqual(len(SPRINT_REGISTRY), 11)
        for i in range(1, 12):
            tid = f"TICKET-{i:02d}"
            self.assertIn(tid, SPRINT_REGISTRY)

    def test_dag_acyclic_and_valid(self):
        """Verify that the DAG has no cycles and no missing dependencies."""
        is_valid, errors = self.orchestrator.validate_dag()
        self.assertTrue(is_valid, f"DAG has errors: {errors}")
        self.assertEqual(len(errors), 0)

    def test_file_boundary_isolation(self):
        """Verify that tasks in the same phase have no file collision."""
        is_valid, conflicts = self.orchestrator.validate_file_isolation()
        self.assertTrue(is_valid, f"File boundary collision detected: {conflicts}")
        self.assertEqual(len(conflicts), 0)

    def test_mermaid_generation(self):
        """Verify that Mermaid flowchart is generated and contains all tickets."""
        mermaid = self.orchestrator.generate_mermaid_dag()
        self.assertTrue(mermaid.startswith("flowchart TD"))
        for tid in SPRINT_REGISTRY:
            self.assertIn(tid.replace("-", "_"), mermaid)

    def test_roles_assignment(self):
        """Verify that each ticket has a Coordinator and at least one worker/verifier."""
        for tid, task in SPRINT_REGISTRY.items():
            self.assertIn(
                AgentRole.COORDINATOR,
                task.roles,
                f"Ticket {tid} must have a Coordinator role"
            )
            self.assertGreaterEqual(
                len(task.roles), 2,
                f"Ticket {tid} must have at least 2 roles for teamwork"
            )


if __name__ == "__main__":
    unittest.main()
