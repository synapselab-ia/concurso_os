from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from auditor import audit_repository

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    errors = audit_repository(ROOT)
    if errors:
        print("AUDIT FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("AUDIT PASSED")
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py", "-v"],
        cwd=ROOT,
        check=False,
    )
    if result.returncode != 0:
        return result.returncode
    print("VERIFY PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
