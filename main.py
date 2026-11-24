#!/usr/bin/env python3
"""Write one one-line resignation letter to entry.txt.

Standard library only. No network access.
"""

import os
import sys
from pathlib import Path

ENTRY = (
    "I resign as fire warden, effective today: after four years "
    "practising the evacuation route, I have decided to finally "
    "use it myself."
)

def validate(text):
    """Check the gate rules before anything is written."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry must be 1-140 characters, got {len(text)}")
    return text


def main():
    validate(ENTRY)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    os.chmod(target, 0o644)
    # Read the file back and verify what was actually written.
    written = target.read_text(encoding="utf-8")
    if written != ENTRY:
        raise ValueError("verification failed: entry.txt does not match ENTRY")
    validate(written)
    if written.endswith("\n"):
        raise ValueError("verification failed: trailing newline present")
    print(f"Wrote {target} ({len(written)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
