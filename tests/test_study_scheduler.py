"""Synthetic scheduler tests plus read-only canonical baseline checks when present."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from study_scheduler import (build_report, classify, load_feedback,
                             official_weights, plan_next_10)


class ShadowSchedulerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads(
            (ROOT / "competitions/tjsp-escrevente-2025/STUDY_TOPIC_CATALOG.json")
            .read_text(encoding="utf-8"))
        cls.blueprint = json.loads(
            (ROOT / "competitions/tjsp-escrevente-2025/BLUEPRINT.json")
            .read_text(encoding="utf-8"))

    def make_root(self):
        tmp = tempfile.TemporaryDirectory()
        root = Path(tmp.name)
        base = root / "competitions/tjsp-escrevente-2025"
        base.mkdir(parents=True)
        (base / "BLUEPRINT.json").write_text(json.dumps(self.blueprint), encoding="utf-8")
        (base / "STUDY_TOPIC_CATALOG.json").write_text(json.dumps(self.catalog), encoding="utf-8")
        return tmp, root

    def write(self, root, participant, filename, row):
        folder = (root / "participants" / participant /
                  "enrollments/tjsp-escrevente-2025/session_feedback")
        folder.mkdir(parents=True, exist_ok=True)
        (folder / filename).write_text(json.dumps(row), encoding="utf-8")

    @staticmethod
    def block(pid, bid, qs, session="chat-a", fid=None, day="2026-11-05"):
        return {"record_type": "block_review", "feedback_id": fid or f"{session}:{bid}",
                "session_id": session, "block_id": bid, "participant_id": pid,
                "competition_id": "tjsp-escrevente-2025",
                "enrollment_id": f"{pid}__tjsp-escrevente-2025",
                "occurred_at": day,
                "scope": {"first_main_question": int(bid[1:]) * 10 if bid[1:].isdigit() else 1},
                "score": {"total": len(qs), "correct": sum(q["correct"] for q in qs),
                          "incorrect": sum(not q["correct"] for q in qs)},
                "questions": qs}

    def report(self, root, pid="p001"):
        return build_report(root, pid, "tjsp-escrevente-2025", "2026-11-06")

    def test_official_weights_and_catalog(self):
        w = official_weights(self.blueprint)
        self.assertEqual(16/70, w["portugues"])
        self.assertEqual(30/70, w["direito"])
        self.assertEqual(9/70, w["informatica"])
        self.assertAlmostEqual(1, sum(w.values()))
        ids = [x["id"] for x in self.catalog["topics"]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertGreaterEqual(len(ids), 40)

    def test_known_legacy_topic_mapping_and_unknown(self):
        expected = [
            ("cp_312_paragrafo_3_peculato", "direito-penal", "dp.peculato"),
            ("cpp_366_vs_367", "direito-processual-penal", "dpp.citacao"),
            ("cpc_335_i_219_224", "direito-processual-civil", "dpc.conciliacao"),
            ("outlook_para_cc_cco", "informatica", "inf.email"),
            ("excel_referencias_mistas", "informatica", "inf.excel"),
            ("lbi_13146_art3", "atualidades_pcd", "ac.pcd"),
        ]
        for label, subject, topic in expected:
            with self.subTest(label=label):
                self.assertEqual(topic, classify(label, subject, self.catalog))
        self.assertIsNone(classify("tema_inexistente", "portugues", self.catalog))
        self.assertIsNone(classify("cf_500", "direito-constitucional", self.catalog))
        self.assertIsNone(classify("cp_312", "portugues", self.catalog))

    def test_parallel_sessions_same_q_number_are_distinct(self):
        t, root = self.make_root()
        try:
            q = {"question_number": 1, "subject": "direito-penal",
                 "subtopic": "cp_312_peculato", "correct": True, "confidence": "firm"}
            self.write(root, "p001", "a.json", self.block("p001", "b01", [q], session="chat-a"))
            self.write(root, "p001", "b.json", self.block("p001", "b01", [q], session="chat-b"))
            r = self.report(root)
            self.assertEqual(2, r["question_level_records"])
            self.assertEqual(2, next(x for x in r["topics"]
                                     if x["topic_id"] == "dp.peculato")["questions"])
        finally:
            t.cleanup()

    def test_replay_idempotent(self):
        t, root = self.make_root()
        try:
            q = {"subject":"portugues","subtopic":"concordancia_verbal",
                 "correct":True,"confidence":"firm"}
            row = self.block("p001", "b01", [q])
            self.write(root, "p001", "a.json", row)
            self.write(root, "p001", "b.json", row)
            self.assertEqual(1, self.report(root)["question_level_records"])
        finally:
            t.cleanup()

    def test_conflicting_id_or_logical_key_fails_closed(self):
        for same_id in (True, False):
            t, root = self.make_root()
            try:
                q = {"subject":"portugues","subtopic":"concordancia_verbal",
                     "correct":True,"confidence":"firm"}
                self.write(root, "p001", "a.json",
                           self.block("p001", "b01", [q], fid="one"))
                self.write(root, "p001", "b.json",
                           self.block("p001", "b01", [{**q, "correct": False}],
                                      fid="one" if same_id else "two"))
                self.assertEqual(0, self.report(root)["question_level_records"])
            finally:
                t.cleanup()

    def test_score_inconsistency_fails_closed(self):
        t, root = self.make_root()
        try:
            q = {"subject":"portugues","subtopic":"concordancia_verbal","correct":True}
            row = self.block("p001", "b01", [q])
            row["score"]["correct"] = 0
            self.write(root,"p001","a.json",row)
            self.assertEqual(0,self.report(root)["question_level_records"])
        finally:
            t.cleanup()

    def test_pending_correction_does_not_silently_count_old_evidence(self):
        t, root = self.make_root()
        try:
            q = {"subject":"portugues","subtopic":"concordancia_verbal","correct":True}
            self.write(root,"p001","a.json",self.block("p001","b01",[q],fid="original"))
            correction = {"participant_id":"p001","competition_id":"tjsp-escrevente-2025",
                          "enrollment_id":"p001__tjsp-escrevente-2025",
                          "record_type":"correction","supersedes_feedback_id":"original"}
            self.write(root,"p001","correction.json",correction)
            r = self.report(root)
            self.assertEqual(0,r["question_level_records"])
            self.assertTrue(any("reconciliation" in msg for msg in r["warnings"]))
        finally:
            t.cleanup()

    def test_participant_isolation(self):
        t, root = self.make_root()
        try:
            q = {"subject":"portugues","subtopic":"concordancia_verbal","correct":False}
            self.write(root,"p002","only-p002.json",self.block("p002","b01",[q]))
            self.assertEqual(0,self.report(root,"p001")["question_level_records"])
            self.assertEqual(1,self.report(root,"p002")["question_level_records"])
        finally:
            t.cleanup()

    def test_two_firm_answers_not_mastered_or_immediately_due(self):
        t, root = self.make_root()
        try:
            q = {"subject":"direito-penal","subtopic":"cp_312_peculato",
                 "correct":True,"confidence":"firm"}
            self.write(root,"p001","a.json",self.block("p001","b01",[q,q]))
            r = self.report(root)
            item = next(x for x in r["topics"] if x["topic_id"] == "dp.peculato")
            self.assertEqual("LOCAL_FIRM_NEEDS_DELAYED_TRANSFER",item["state"])
            self.assertEqual("cooldown",item["lane"])
        finally:
            t.cleanup()

    def test_other_chat_cannot_fake_spaced_retention(self):
        t, root = self.make_root()
        try:
            q = {"subject":"direito-penal","subtopic":"cp_312_peculato",
                 "correct":True,"confidence":"firm"}
            other = {"subject":"informatica","subtopic":"excel_referencias",
                     "correct":True,"confidence":"firm"}
            self.write(root,"p001","a.json",
                       self.block("p001","b01",[q,q],session="chat-a",day="2026-10-20"))
            self.write(root,"p001","b.json",
                       self.block("p001","b01",[other]*21,session="chat-b"))
            item = next(x for x in self.report(root)["topics"]
                        if x["topic_id"] == "dp.peculato")
            self.assertEqual(0,item["same_session_questions_since_last"])
            self.assertEqual("cooldown",item["lane"])
        finally:
            t.cleanup()

    def test_due_retention_requires_elapsed_days_and_same_session_gap(self):
        t, root = self.make_root()
        try:
            q = {"subject":"direito-penal","subtopic":"cp_312_peculato",
                 "correct":True,"confidence":"firm"}
            other = {"subject":"informatica","subtopic":"excel_referencias",
                     "correct":True,"confidence":"firm"}
            self.write(root,"p001","a.json",
                       self.block("p001","b01",[q,q],day="2026-10-20"))
            self.write(root,"p001","b.json",
                       self.block("p001","b02",[other]*21,day="2026-11-05"))
            item = next(x for x in self.report(root)["topics"]
                        if x["topic_id"] == "dp.peculato")
            self.assertEqual("maintain",item["lane"])
        finally:
            t.cleanup()

    def test_lane_distribution_fallback_and_unique_suggestions(self):
        t, root = self.make_root()
        try:
            q = {"subject":"informatica","subtopic":"outlook_para_cc_cco",
                 "correct":False,"confidence":"firm"}
            self.write(root,"p001","a.json",self.block("p001","b01",[q,q]))
            r = self.report(root)
            plan = r["proposed_next_10"]
            self.assertEqual(6,sum(x["preferred_lane"]=="explore" for x in plan))
            self.assertEqual(3,sum(x["preferred_lane"]=="remediate" for x in plan))
            self.assertEqual(1,sum(x["preferred_lane"]=="maintain" for x in plan))
            chosen = [x["topic_id"] for x in plan if "topic_id" in x]
            self.assertEqual(len(chosen),len(set(chosen)))
            self.assertTrue(all(x.get("status") == "SUGGESTED_NOT_RESERVED"
                                for x in plan if "topic_id" in x))
            self.assertEqual("DISABLED",r["activation"])
        finally:
            t.cleanup()

    def test_checkpoints_use_valid_main_questions_only(self):
        t, root = self.make_root()
        try:
            q = {"subject":"portugues","subtopic":"concordancia_verbal",
                 "correct":True,"confidence":"firm"}
            for i in range(6):
                self.write(root,"p001",f"{i}.json",
                           self.block("p001",f"b{i+1:02}",[q]*10))
            self.write(root,"p001","review.json",
                       {"participant_id":"p001","competition_id":"tjsp-escrevente-2025",
                        "enrollment_id":"p001__tjsp-escrevente-2025",
                        "record_type":"active_review","score":{"total":100}})
            r = self.report(root)
            self.assertEqual(60,r["question_level_records"])
            self.assertEqual(50,r["latest_full_50_checkpoint"])
            self.assertEqual(100,r["next_50_checkpoint"])
        finally:
            t.cleanup()

    def test_real_canonical_p001_baseline_when_available(self):
        folder = (ROOT / "participants/p001/enrollments/tjsp-escrevente-2025"
                  / "session_feedback")
        if not folder.exists():
            self.skipTest("full GitHub checkout unavailable in isolated test directory")
        blocks, warnings = load_feedback(ROOT,"p001","tjsp-escrevente-2025")
        baseline = [b for b in blocks
                    if b.get("session_id") == "chatgpt-20261009-p001-tjsp-adaptive-01"
                    and b.get("block_id") in {
                        "b01-q01-q10", "b02-q11-q20", "b03-q21-q30",
                        "b04-q31-q40", "b05-q41-q50", "b06-q51-q60"}]
        self.assertEqual(6,len(baseline),warnings)
        self.assertEqual(60,sum(len(b["questions"]) for b in baseline))
        self.assertEqual(48,sum(b["score"]["correct"] for b in baseline))


if __name__ == "__main__":
    unittest.main()
