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
    "00_SYSTEM/CHECKPOINT.md",
    "00_SYSTEM/NEXT_ACTION.md",
    "00_SYSTEM/DECISION_LOG.md",
]

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

    participant_ids: set[str] = set()
    participants_dir = root / "participants"
    if participants_dir.exists():
        for profile in participants_dir.glob("p*/PROFILE.json"):
            try:
                data = _load_json(profile)
            except (json.JSONDecodeError, OSError) as exc:
                errors.append(f"invalid participant profile {profile.relative_to(root)}: {exc}")
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
                errors.append(f"forbidden public profile keys in {profile.relative_to(root)}: {sorted(forbidden)}")

    for path in root.rglob("*.json"):
        if "_template" in path.parts:
            continue
        try:
            _load_json(path)
        except (json.JSONDecodeError, OSError) as exc:
            errors.append(f"invalid json {path.relative_to(root)}: {exc}")

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
                    errors.append(f"event missing keys {path.relative_to(root)}:{number}: {sorted(missing)}")
                pid = event.get("participant_id")
                if participant_ids and pid not in participant_ids:
                    errors.append(f"event references unknown participant {pid}: {path.relative_to(root)}:{number}")

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
