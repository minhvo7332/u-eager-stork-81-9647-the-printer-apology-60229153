#!/usr/bin/env python3
"""The Printer Apology — program/v1 entry.

Writes one line to /output/entry.txt: an apology note from an office
printer to the people who keep jamming it, feeding it cheap paper and
swearing at it. Deterministic: the same line on every run, no network,
no model calls, no input read.
"""

import os
import sys

# The apology line (118 characters, within the 120-character limit).
# Scored against the judge brief in a 30-candidate bake-off
# (candidates.txt): a genuine apology from the printer, real printer
# truth (cheap paper, a staple, swearing), a fresh angle (the printer
# "ate" the report instead of merely jamming), second-person "your"
# so the reader is a character in the joke, and the punch lands at
# the end ("your swearing is now in my error log").
LINE = (
    "I'm sorry I ate your report. The paper was cheap, the staple was "
    "a surprise, and your swearing is now in my error log."
)


def main() -> int:
    if not (1 <= len(LINE) <= 120):
        print(f"entry line is {len(LINE)} chars, must be 1-120", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry line is blank", file=sys.stderr)
        return 1

    # The grader collects /output/entry.txt as another user, so the file
    # must be readable by everyone (mode 0644) and its directory 0755.
    os.umask(0o022)
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(LINE)
    except OSError:
        # Fallback for local runs where /output is not writable.
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(LINE)
    os.chmod(out_path, 0o644)
    try:
        os.chmod(out_dir, 0o755)
    except OSError:
        pass
    print(f"wrote {len(LINE)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
