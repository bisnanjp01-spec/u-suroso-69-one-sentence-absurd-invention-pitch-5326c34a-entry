#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence (at most 220 characters) pitching a ridiculous
invention that fixes a tiny everyday annoyance, to /output/entry.txt.

The pitch names the invention, the tiny annoyance it fixes, and its
silly mechanism, in one clean sentence: a doormat that runs a job
interview at the front door, so muddy shoes get a performance review
instead of a free wipe. The run is fully deterministic: the same
sentence on every run, with no network, no randomness, and no dependence
on the clock or the environment beyond the output directory.
"""

import os

PITCH = (
    "The BouncerMat is a doormat that interviews every guest with three "
    "questions before they may wipe their feet, turning away muddy shoes "
    "with a polite but devastating performance review."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    text = PITCH.strip()
    if not 1 <= len(text) <= 220:
        raise SystemExit(f"pitch must be 1-220 characters, got {len(text)}")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("pitch must be exactly one sentence")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
