"""Run the original exercise checks and report failures with a nonzero exit code."""
from pathlib import Path
import subprocess
import sys

EXERCISES = (
    "sumofthree.py",
    "numlocations.py",
    "ancestorcolours.py",
    "clusterexhaustive.py",
    "clusterbacktrack.py",
)


def main():
    root = Path(__file__).resolve().parent
    total = 0
    failed = False
    for exercise in EXERCISES:
        try:
            result = subprocess.run(
                [sys.executable, "-B", str(root / exercise)],
                cwd=root,
                capture_output=True,
                text=True,
                timeout=30,
            )
        except subprocess.TimeoutExpired:
            print(f"FAIL {exercise}: exceeded 30 seconds")
            failed = True
            continue
        passed = result.stdout.count(": PASSED")
        ok = result.returncode == 0 and passed > 0 and ": FAILED" not in result.stdout
        total += passed
        print(f"{'PASS' if ok else 'FAIL'} {exercise}: {passed} checks passed")
        if not ok:
            failed = True
            print(result.stdout)
            print(result.stderr)
    print(f"\n{total} checks passed across {len(EXERCISES)} exercises.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
