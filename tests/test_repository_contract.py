import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from auditor import audit_repository  # noqa: E402


class RepositoryContractTests(unittest.TestCase):
    def test_auditor_passes(self):
        self.assertEqual([], audit_repository(ROOT))

    def test_seed_participants_are_distinct(self):
        p1 = json.loads((ROOT / "participants/p001/PROFILE.json").read_text(encoding="utf-8"))
        p2 = json.loads((ROOT / "participants/p002/PROFILE.json").read_text(encoding="utf-8"))
        self.assertNotEqual(p1["participant_id"], p2["participant_id"])

    def test_no_workflow_directory_required(self):
        workflows = ROOT / ".github/workflows"
        self.assertFalse(workflows.exists() and any(workflows.iterdir()))

    def test_tjsp_blueprint_has_70_questions(self):
        blueprint = json.loads(
            (ROOT / "competitions/tjsp-escrevente-2025/BLUEPRINT.json").read_text(encoding="utf-8")
        )
        objective = blueprint["objective"]
        self.assertEqual(70, objective["questions"])
        self.assertEqual(70, sum(block["questions"] for block in objective["blocks"]))

    def test_tjsp_elimination_rules_are_explicit(self):
        blueprint = json.loads(
            (ROOT / "competitions/tjsp-escrevente-2025/BLUEPRINT.json").read_text(encoding="utf-8")
        )
        blocks = {block["block_id"]: block for block in blueprint["objective"]["blocks"]}
        self.assertTrue(blocks["B1"]["eliminatory"])
        self.assertTrue(blocks["B2"]["eliminatory"])
        self.assertEqual(0.5, blocks["B1"]["minimum_correct_fraction"])
        self.assertEqual(0.5, blocks["B2"]["minimum_correct_fraction"])
        self.assertFalse(blocks["B3"]["eliminatory"])

    def test_tjsp_weekly_simulation_matches_objective_blueprint(self):
        blueprint = json.loads(
            (ROOT / "competitions/tjsp-escrevente-2025/BLUEPRINT.json").read_text(encoding="utf-8")
        )
        simulation = json.loads(
            (
                ROOT
                / "competitions/tjsp-escrevente-2025/SIMULATION_BLUEPRINT.json"
            ).read_text(encoding="utf-8")
        )

        objective = blueprint["objective"]
        weekly = simulation["weekly_full_objective"]

        self.assertEqual(objective["questions"], weekly["questions"])
        self.assertEqual(objective["alternatives_per_question"], weekly["alternatives_per_question"])
        self.assertEqual(70, sum(section["questions"] for section in weekly["sections"]))

        objective_blocks = {block["block_id"]: block for block in objective["blocks"]}
        simulation_blocks = {block["block_id"]: block for block in weekly["sections"]}
        self.assertEqual(set(objective_blocks), set(simulation_blocks))

        for block_id, expected in objective_blocks.items():
            actual = simulation_blocks[block_id]
            self.assertEqual(expected["questions"], actual["questions"])
            expected_subjects = {
                subject["subject_id"]: subject["questions"]
                for subject in expected["subjects"]
            }
            actual_subjects = {
                subject["subject_id"]: subject["questions"]
                for subject in actual["subjects"]
            }
            self.assertEqual(expected_subjects, actual_subjects)

        self.assertEqual(
            "microdrill",
            simulation["weekly_cycle"]["regular_phase"]["monday_to_saturday"],
        )
        self.assertEqual(
            "weekly_full_objective",
            simulation["weekly_cycle"]["regular_phase"]["sunday"],
        )

    def test_p001_tjsp_enrollment_is_consistent(self):
        config = json.loads(
            (
                ROOT
                / "participants/p001/enrollments/tjsp-escrevente-2025/CONFIG.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual("p001", config["participant_id"])
        self.assertEqual("tjsp-escrevente-2025", config["competition_id"])
        self.assertEqual(
            "p001__tjsp-escrevente-2025",
            config["enrollment_id"],
        )
        self.assertEqual("unknown", config["official_candidate_status"])


if __name__ == "__main__":
    unittest.main()
