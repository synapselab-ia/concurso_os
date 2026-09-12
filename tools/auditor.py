from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "AGENTS.md",
    "PROJECT_CONTROL.md",
    "00_SYSTEM/START_HERE.md",
    "00_SYSTEM/PROJECT_SPEC.md",
    "00_SYSTEM/ARCHITECTURE.md",
    "00_SYSTEM/DATA_MODEL.md",
    "00_SYSTEM/CONTINUITY_PROTOCOL.md",
    "00_SYSTEM/PRACTICE_PROTOCOL.md",
    "00_SYSTEM/SIMULATION_PROTOCOL.md",
    "00_SYSTEM/CHECKPOINT.md",
    "00_SYSTEM/NEXT_ACTION.md",
    "00_SYSTEM/DECISION_LOG.md",
]

REQUIRED_COMPETITION_FILES = {
    "COMPETITION.json",
    "BLUEPRINT.json",
    "SOURCES.json",
    "COMPETENCY_MAP.json",
}

FORBIDDEN_PUBLIC_PROFILE_KEYS = {
    "cpf", "email", "phone", "telefone", "address", "endereco",
    "password", "senha", "health", "saude", "bank", "bank_account"
}


def _load_json(path: Path):
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def audit_repository(root: Path = ROOT) -> list[str]:
    errors: list[str] = []

    for relative in REQUIRED:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")

    workflow_dir = root / ".github" / "workflows"
    if workflow_dir.exists() and any(workflow_dir.iterdir()):
        errors.append("GitHub Actions are disabled during the production phase")

    # Parse all non-template JSON once. Structural checks below may safely reuse it.
    json_data: dict[Path, object] = {}
    for path in root.rglob("*.json"):
        if "_template" in path.parts:
            continue
        try:
            json_data[path] = _load_json(path)
        except (json.JSONDecodeError, OSError) as exc:
            errors.append(f"invalid json {path.relative_to(root)}: {exc}")

    participant_ids: set[str] = set()
    participants_dir = root / "participants"
    if participants_dir.exists():
        for profile in participants_dir.glob("p*/PROFILE.json"):
            data = json_data.get(profile)
            if not isinstance(data, dict):
                continue
            pid = data.get("participant_id")
            if not isinstance(pid, str) or not pid.startswith("p"):
                errors.append(f"invalid participant_id in {profile.relative_to(root)}")
            elif pid in participant_ids:
                errors.append(f"duplicate participant_id: {pid}")
            else:
                participant_ids.add(pid)
            forbidden = FORBIDDEN_PUBLIC_PROFILE_KEYS.intersection(k.lower() for k in data)
            if forbidden:
                errors.append(
                    f"forbidden public profile keys in {profile.relative_to(root)}: {sorted(forbidden)}"
                )

    # Reusable competency catalog.
    competency_ids: set[str] = set()
    catalog_dir = root / "knowledge" / "competencies"
    if catalog_dir.exists():
        for catalog in catalog_dir.glob("*.json"):
            data = json_data.get(catalog)
            if not isinstance(data, dict):
                continue
            items = data.get("competencies", [])
            if not isinstance(items, list):
                errors.append(f"invalid competency catalog list: {catalog.relative_to(root)}")
                continue
            for item in items:
                cid = item.get("competency_id") if isinstance(item, dict) else None
                if not isinstance(cid, str) or not cid:
                    errors.append(f"invalid competency in {catalog.relative_to(root)}")
                elif cid in competency_ids:
                    errors.append(f"duplicate competency_id: {cid}")
                else:
                    competency_ids.add(cid)

    competition_ids: set[str] = set()
    competitions_dir = root / "competitions"
    if competitions_dir.exists():
        for competition_dir in competitions_dir.iterdir():
            if not competition_dir.is_dir() or competition_dir.name.startswith("_"):
                continue

            missing_files = [
                filename for filename in REQUIRED_COMPETITION_FILES
                if not (competition_dir / filename).is_file()
            ]
            for filename in sorted(missing_files):
                errors.append(
                    f"competition {competition_dir.name} missing required file: {filename}"
                )

            competition_path = competition_dir / "COMPETITION.json"
            competition = json_data.get(competition_path)
            if not isinstance(competition, dict):
                continue

            competition_id = competition.get("competition_id")
            if not isinstance(competition_id, str) or not competition_id:
                errors.append(f"invalid competition_id in {competition_path.relative_to(root)}")
                continue
            if competition_id != competition_dir.name:
                errors.append(
                    f"competition directory/id mismatch: {competition_dir.name} != {competition_id}"
                )
            if competition_id in competition_ids:
                errors.append(f"duplicate competition_id: {competition_id}")
            competition_ids.add(competition_id)

            blueprint_path = competition_dir / "BLUEPRINT.json"
            blueprint = json_data.get(blueprint_path)
            if isinstance(blueprint, dict):
                objective = blueprint.get("objective")
                if isinstance(objective, dict):
                    questions = objective.get("questions")
                    blocks = objective.get("blocks", [])
                    if isinstance(questions, int) and isinstance(blocks, list):
                        block_total = sum(
                            block.get("questions", 0)
                            for block in blocks
                            if isinstance(block, dict) and isinstance(block.get("questions"), int)
                        )
                        if block_total != questions:
                            errors.append(
                                f"blueprint block total mismatch in {blueprint_path.relative_to(root)}: "
                                f"{block_total} != {questions}"
                            )
                        for block in blocks:
                            if not isinstance(block, dict):
                                continue
                            subjects = block.get("subjects", [])
                            block_questions = block.get("questions")
                            if isinstance(subjects, list) and isinstance(block_questions, int):
                                subject_total = sum(
                                    subject.get("questions", 0)
                                    for subject in subjects
                                    if isinstance(subject, dict)
                                    and isinstance(subject.get("questions"), int)
                                )
                                if subject_total != block_questions:
                                    errors.append(
                                        f"blueprint subject total mismatch in block "
                                        f"{block.get('block_id')}: {subject_total} != {block_questions}"
                                    )

            sources_path = competition_dir / "SOURCES.json"
            sources = json_data.get(sources_path)
            source_ids: set[str] = set()
            if isinstance(sources, dict):
                for source in sources.get("sources", []):
                    sid = source.get("source_id") if isinstance(source, dict) else None
                    if isinstance(sid, str):
                        if sid in source_ids:
                            errors.append(f"duplicate source_id in {sources_path.relative_to(root)}: {sid}")
                        source_ids.add(sid)
                for source_ref in competition.get("source_refs", []):
                    if source_ref not in source_ids:
                        errors.append(
                            f"competition references unknown source {source_ref}: "
                            f"{competition_path.relative_to(root)}"
                        )

            mapping_path = competition_dir / "COMPETENCY_MAP.json"
            mapping = json_data.get(mapping_path)
            if isinstance(mapping, dict):
                mapped_ids: set[str] = set()
                for item in mapping.get("mappings", []):
                    cid = item.get("competency_id") if isinstance(item, dict) else None
                    if not isinstance(cid, str):
                        errors.append(f"invalid competency mapping in {mapping_path.relative_to(root)}")
                        continue
                    if cid in mapped_ids:
                        errors.append(
                            f"duplicate competency mapping in {mapping_path.relative_to(root)}: {cid}"
                        )
                    mapped_ids.add(cid)
                    if competency_ids and cid not in competency_ids:
                        errors.append(
                            f"competition maps unknown competency {cid}: {mapping_path.relative_to(root)}"
                        )

            baseline_path = competition_dir / "BASELINE_PLAN.json"
            baseline = json_data.get(baseline_path)
            if isinstance(baseline, dict):
                ids: list[str] = []
                stage_1 = baseline.get("stage_1")
                if isinstance(stage_1, dict):
                    ids.extend(stage_1.get("competency_ids", []))
                writing_screen = baseline.get("writing_screen")
                if isinstance(writing_screen, dict):
                    ids.extend(writing_screen.get("competency_ids", []))
                for cid in ids:
                    if competency_ids and cid not in competency_ids:
                        errors.append(
                            f"baseline references unknown competency {cid}: {baseline_path.relative_to(root)}"
                        )

    enrollment_ids: set[str] = set()
    if participants_dir.exists():
        for config in participants_dir.glob("p*/enrollments/*/CONFIG.json"):
            data = json_data.get(config)
            if not isinstance(data, dict):
                continue
            enrollment_id = data.get("enrollment_id")
            pid = data.get("participant_id")
            competition_id = data.get("competition_id")
            if not isinstance(enrollment_id, str) or not enrollment_id:
                errors.append(f"invalid enrollment_id in {config.relative_to(root)}")
            elif enrollment_id in enrollment_ids:
                errors.append(f"duplicate enrollment_id: {enrollment_id}")
            else:
                enrollment_ids.add(enrollment_id)
            if participant_ids and pid not in participant_ids:
                errors.append(f"enrollment references unknown participant {pid}: {config.relative_to(root)}")
            if competition_ids and competition_id not in competition_ids:
                errors.append(
                    f"enrollment references unknown competition {competition_id}: {config.relative_to(root)}"
                )
            expected_id = f"{pid}__{competition_id}"
            if isinstance(enrollment_id, str) and enrollment_id != expected_id:
                errors.append(
                    f"enrollment_id mismatch in {config.relative_to(root)}: "
                    f"{enrollment_id} != {expected_id}"
                )

    required_event_keys = {
        "schema_version", "event_id", "event_type", "occurred_at",
        "participant_id", "competition_id", "enrollment_id",
        "competency_ids", "payload", "provenance"
    }
    for path in root.rglob("*.jsonl"):
        with path.open("r", encoding="utf-8") as fh:
            for number, line in enumerate(fh, 1):
                if not line.strip():
                    continue
                try:
                    event = json.loads(line)
                except json.JSONDecodeError as exc:
                    errors.append(f"invalid jsonl {path.relative_to(root)}:{number}: {exc}")
                    continue
                missing = required_event_keys.difference(event)
                if missing:
                    errors.append(
                        f"event missing keys {path.relative_to(root)}:{number}: {sorted(missing)}"
                    )
                pid = event.get("participant_id")
                competition_id = event.get("competition_id")
                enrollment_id = event.get("enrollment_id")
                if participant_ids and pid not in participant_ids:
                    errors.append(
                        f"event references unknown participant {pid}: {path.relative_to(root)}:{number}"
                    )
                if competition_ids and competition_id not in competition_ids:
                    errors.append(
                        f"event references unknown competition {competition_id}: "
                        f"{path.relative_to(root)}:{number}"
                    )
                if enrollment_ids and enrollment_id not in enrollment_ids:
                    errors.append(
                        f"event references unknown enrollment {enrollment_id}: "
                        f"{path.relative_to(root)}:{number}"
                    )
                for cid in event.get("competency_ids", []):
                    if competency_ids and cid not in competency_ids:
                        errors.append(
                            f"event references unknown competency {cid}: {path.relative_to(root)}:{number}"
                        )

    return errors


def main() -> int:
    errors = audit_repository()
    if errors:
        print("AUDIT FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("AUDIT PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
