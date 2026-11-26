#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge -- make.fun entry.

Writes one original line (at most 200 characters) roasting a fridge
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Why this line, against the house judge's brief: it is unmistakably
about a fridge (the hum, the light); the mocked detail is specific
(all-night humming, a smell left over from 2019); the twist is that
the machine's only "output" after all that work is a light and an old
smell; and it reads well out loud, one breath, setup then punch.

Deterministic: no input, no network, no randomness, no clock. Every run
writes byte-identical output. The program checks the gate itself before
writing: exactly one line, 1-200 characters, not blank.
"""

import os
import sys

LINE = (
    "My fridge hums all night like it pays rent, yet the only thing it "
    "ever produces is a light and a faint smell of 2019."
)


def main():
    text = LINE
    if not text or not text.strip():
        print("gate failed: line is blank", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("gate failed: line must be a single line", file=sys.stderr)
        return 1
    if len(text) < 1 or len(text) > 200:
        print(
            "gate failed: %d characters, must be 1-200" % len(text),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Read the file back and verify what was written is exactly the gated
    # line plus one trailing newline; refuse to report success otherwise.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text + "\n":
        print("gate failed: written file does not match the gated line",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
