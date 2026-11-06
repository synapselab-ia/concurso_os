"""Read-only syllabus coverage and weighted round-robin microdrill planner.

SHADOW ONLY: never writes feedback, reserves topics, or activates for live chats.
Requires a coherent local checkout of one Git commit for a trustworthy snapshot.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

LAW = ("direito-penal", "direito-processual-penal", "direito-processual-civil",
       "direito-constitucional", "direito-administrativo", "legislacao-interna")
GROUPS = {**{s: "direito" for s in LAW},
          **{s: s for s in ("portugues", "informatica", "matematica",
                            "atualidades_pcd", "raciocinio-logico")}}
SLOTS = ("explore", "remediate", "explore", "explore", "remediate",
         "explore", "maintain", "explore", "remediate", "explore")
FIRM = ("firm", "sem_duvida")


def official_weights(blueprint: dict) -> dict[str, float]:
    """Use BLUEPRINT, never inferred frequencies for individual branches of Direito."""
    objective = blueprint["objective"]
    n = objective["questions"]
    mapping = {"current_affairs_lbi": "atualidades_pcd",
               "mathematics": "matematica", "informatics": "informatica",
               "logic": "raciocinio-logico"}
    weights = {}
    for block in objective["blocks"]:
        if block["block_id"] == "B1":
            weights["portugues"] = block["questions"] / n
        elif block["block_id"] == "B2":
            weights["direito"] = block["questions"] / n
        elif block["block_id"] == "B3":
            for subject in block["subjects"]:
                weights[mapping[subject["subject_id"]]] = subject["questions"] / n
    if set(weights) != {"portugues", "direito", "atualidades_pcd", "matematica",
                        "informatica", "raciocinio-logico"} or abs(sum(weights.values()) - 1) > 1e-9:
        raise ValueError("BLUEPRINT groups do not sum to one")
    return weights


def classify(subtopic: object, subject: object, catalog: dict) -> str | None:
    """Map observed labels only when one matching topic is unambiguous."""
    if not isinstance(subtopic, str) or not isinstance(subject, str):
        return None
    candidates = []
    source = subtopic.lower()
    for entry in catalog["topics"]:
        if entry["subject"] != subject:
            continue
        matches = [a for a in entry["aliases"]
                   if re.search(r"(?<![a-z0-9])" + re.escape(a.lower()) + r"(?=$|[_-])", source)]
        if matches:
            longest = max(matches, key=len)
            candidates.append((int(source.startswith(longest)), len(longest), entry["id"]))
    if not candidates:
        return None
    candidates.sort(reverse=True)
    if len(candidates) > 1 and candidates[0][:2] == candidates[1][:2]:
        return None
    return candidates[0][2]


def _date(value: object) -> date | None:
    try:
        return date.fromisoformat(value[:10]) if isinstance(value, str) else None
    except ValueError:
        return None


def load_feedback(root: Path, participant_id: str, competition_id: str) -> tuple[list[dict], list[str]]:
    """Read valid question-level blocks, excluding uncertain/corrected evidence.

    Legacy score-only reviews and active reviews are never counted as questions.
    Same local question number in different session IDs is never a collision.
    """
    folder = (root / "participants" / participant_id / "enrollments" /
              competition_id / "session_feedback")
    if not folder.is_dir():
        return [], ["No persisted session_feedback directory for enrollment"]
    by_id, by_key, invalid, corrected, warnings = {}, {}, set(), set(), []
    for path in sorted(folder.glob("*.json")):
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            warnings.append(f"Invalid JSON {path.name}: {exc}")
            continue
        if (record.get("participant_id") != participant_id or
            record.get("competition_id") != competition_id or
            record.get("enrollment_id") != f"{participant_id}__{competition_id}"):
            warnings.append(f"Excluded identity mismatch: {path.name}")
            continue
        kind = record.get("record_type", "block_review" if record.get("block_id") else "other")
        if kind == "correction":
            if isinstance(record.get("supersedes_feedback_id"), str):
                corrected.add(record["supersedes_feedback_id"])
            warnings.append(f"Manual correction reconciliation required: {path.name}")
            continue
        if kind != "block_review" or not isinstance(record.get("questions"), list):
            continue
        fid, sid, bid = (record.get(x) for x in ("feedback_id", "session_id", "block_id"))
        if any(not isinstance(x, str) or not x for x in (fid, sid, bid)):
            warnings.append(f"Missing stable keys: {path.name}")
            continue
        key = (sid, bid)
        if key in by_key and by_key[key] != fid:
            invalid.update((fid, by_key[key]))
            warnings.append(f"Conflicting session/block: {path.name}")
            continue
        if fid in by_id:
            if by_id[fid] != record:
                invalid.add(fid)
                warnings.append(f"Conflicting feedback_id: {fid}")
            continue
        qs, score = record["questions"], record.get("score", {})
        correct = sum(isinstance(q, dict) and q.get("correct") is True for q in qs)
        if (score.get("total") != len(qs) or
            any(not isinstance(q, dict) or not isinstance(q.get("correct"), bool) for q in qs) or
            ("correct" in score and score["correct"] != correct) or
            ("incorrect" in score and score["incorrect"] != len(qs) - correct)):
            warnings.append(f"Excluded inconsistent score: {path.name}")
            continue
        by_id[fid], by_key[key] = record, fid

    for fid in corrected:
        if fid not in by_id:
            warnings.append(f"Correction target absent: {fid}")
        else:
            invalid.add(fid)
            warnings.append(f"Corrected block withheld pending reconciliation: {fid}")
    result = [r for fid, r in by_id.items() if fid not in invalid]
    result.sort(key=lambda r: (r["session_id"],
                               r.get("scope", {}).get("first_main_question", 0), r["block_id"]))
    # Reject duplicate question keys *within* a session; a new chat's Q01 is independent.
    question_keys, bad_blocks = set(), set()
    for record in result:
        for q in record["questions"]:
            number = q.get("question_number")
            if number is not None:
                key = record["session_id"], str(number)
                if key in question_keys:
                    bad_blocks.add(record["feedback_id"])
                    warnings.append(f"Overlapping local question in {record['feedback_id']}")
                question_keys.add(key)
    return [r for r in result if r["feedback_id"] not in bad_blocks], warnings


def plan_next_10(report: dict) -> list[dict]:
    """Select 10 non-repeating *suggestions*. No reservation or live-chat mutation."""
    selected, counts, branches = set(), Counter(), Counter()
    weights = report["official_group_weights"]
    proposed = []
    for index, requested in enumerate(SLOTS, 1):
        lane = requested
        eligible = [t for t in report["topics"]
                    if t["lane"] == lane and t["topic_id"] not in selected]
        if not eligible and lane != "explore":
            lane = "explore"
            eligible = [t for t in report["topics"]
                        if t["lane"] == lane and t["topic_id"] not in selected]
        if not eligible:
            proposed.append({"slot": index, "preferred_lane": requested,
                             "result": "NO_ELIGIBLE_TOPIC"})
            continue

        def rank(t):
            group = t["exam_group"]
            return (weights[group] * index - counts[group], -branches[t["subject"]],
                    t["high_confidence_errors"] if lane == "remediate" else 0,
                    t["errors"] if lane == "remediate" else 0,
                    -t["questions"], t["topic_id"])

        choice = max(eligible, key=rank)
        selected.add(choice["topic_id"])
        counts[choice["exam_group"]] += 1
        branches[choice["subject"]] += 1
        proposed.append({"slot": index, "preferred_lane": requested,
                         "actual_lane": lane, "topic_id": choice["topic_id"],
                         "subject": choice["subject"], "status": "SUGGESTED_NOT_RESERVED"})
    return proposed


def build_report(root: Path, participant_id: str, competition_id: str,
                 as_of: str, source_commit_sha: str | None = None) -> dict:
    """Produce an ephemeral report; no filesystem writes, no implied mastery."""
    base = root / "competitions" / competition_id
    catalog = json.loads((base / "STUDY_TOPIC_CATALOG.json").read_text(encoding="utf-8"))
    blueprint = json.loads((base / "BLUEPRINT.json").read_text(encoding="utf-8"))
    weights = official_weights(blueprint)
    blocks, warnings = load_feedback(root, participant_id, competition_id)
    history, sessions, events = defaultdict(list), defaultdict(list), []
    for block in blocks:
        for q in block["questions"]:
            subject, raw = q.get("subject", q.get("subject_id")), q.get("subtopic", q.get("topic"))
            topic = classify(raw, subject, catalog)
            event = {"subject": subject, "topic": topic, "correct": q["correct"],
                     "firm": q.get("confidence") in FIRM,
                     "session": block["session_id"], "day": block.get("occurred_at"),
                     "local_index": len(sessions[block["session_id"]])}
            sessions[block["session_id"]].append(event)
            events.append(event)
            if topic:
                history[topic].append(event)
    today = _date(as_of)
    if today is None:
        raise ValueError("as_of must be an ISO date YYYY-MM-DD")
    topics = []
    for t in catalog["topics"]:
        entries = history[t["id"]]
        errors = sum(not e["correct"] for e in entries)
        uncertain = sum(e["correct"] and not e["firm"] for e in entries)
        confident_errors = sum(not e["correct"] and e["firm"] for e in entries)
        tail = 0
        for e in reversed(entries):
            if e["correct"] and e["firm"]:
                tail += 1
            else:
                break
        last = entries[-1] if entries else None
        gap = (len(sessions[last["session"]]) - 1 - last["local_index"]) if last else None
        last_day = _date(last["day"]) if last else None
        days = (today - last_day).days if last_day else None
        delayed = bool(tail >= 2 and gap is not None and gap >= 20
                       and days is not None and days >= 7)
        if not entries:
            state, lane = "UNSEEN", "explore"
        elif tail >= 2:
            state, lane = "LOCAL_FIRM_NEEDS_DELAYED_TRANSFER", "maintain" if delayed else "cooldown"
        elif errors or uncertain:
            state, lane = "NEEDS_REMEDIATION", "remediate" if gap is not None and gap >= 2 else "cooldown"
        else:
            state, lane = ("ASSESSED_NOT_MASTERED",
                           "maintain" if days is not None and days >= 7
                           and gap is not None and gap >= 20 else "cooldown")
        group = GROUPS[t["subject"]]
        difficulty = (round(min(5, 1 + 4 * (errors + .5 * uncertain + .5 * confident_errors) /
                                len(entries)), 2) if entries else None)
        topics.append({"topic_id": t["id"], "subject": t["subject"], "label": t["label"],
                       "exam_group": group, "official_group_share": round(weights[group], 5),
                       "exam_topic_probability": None, "questions": len(entries),
                       "errors": errors, "uncertain_correct": uncertain,
                       "high_confidence_errors": confident_errors, "firm_tail": tail,
                       "difficulty_evidence_score_1_to_5": difficulty,
                       "difficulty_confidence": "insufficient" if len(entries) < 3 else "limited",
                       "state": state, "lane": lane,
                       "same_session_questions_since_last": gap, "days_since_last": days})
    result = {"mode": "SHADOW_READ_ONLY", "activation": "DISABLED",
              "source_commit_sha": source_commit_sha, "as_of": as_of,
              "participant_id": participant_id, "competition_id": competition_id,
              "blocks_read": len(blocks), "question_level_records": len(events),
              "correct": sum(e["correct"] for e in events),
              "mapped_to_catalog": sum(e["topic"] is not None for e in events),
              "unmapped": sum(e["topic"] is None for e in events),
              "latest_full_50_checkpoint": len(events) // 50 * 50,
              "next_50_checkpoint": (len(events) // 50 + 1) * 50,
              "official_group_weights": weights,
              "warnings": warnings, "topics": topics,
              "limitations": ["Broad-topic coverage is not full syllabus mastery",
                              "Only persisted blocks counted; live chats invisible",
                              "Cross-session ordering and retention interval not inferred",
                              "Corrections require manual reconciliation",
                              "Historical VUNESP topic frequencies not invented"]}
    result["proposed_next_10"] = plan_next_10(result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Shadow-only coverage and study planning")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--participant-id", required=True)
    parser.add_argument("--competition-id", default="tjsp-escrevente-2025")
    parser.add_argument("--as-of", required=True, help="YYYY-MM-DD, for reproducibility")
    parser.add_argument("--source-commit-sha", help="Observed Git snapshot SHA, if known")
    args = parser.parse_args()
    result = build_report(args.root, args.participant_id, args.competition_id,
                          args.as_of, args.source_commit_sha)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
