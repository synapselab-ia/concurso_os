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
