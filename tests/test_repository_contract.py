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


if __name__ == "__main__":
    unittest.main()
