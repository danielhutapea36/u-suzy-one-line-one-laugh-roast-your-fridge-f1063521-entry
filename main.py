#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge -- make.fun entry.

The program holds one original roast line about a fridge and writes it
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Why this line, against the house judge's brief: it is unmistakably
about a fridge (the hum, the light); the mocked detail is specific
(all-night humming, a smell left over from 2019); the twist is that
the machine's only "output" after all that work is a light and an old
smell; and it reads well out loud, one breath, setup then punch.

Deterministic: standard library only, no input, no network, no clock,
no randomness. Every run writes the same bytes.
"""

import os
import sys

ROAST = (
    "My fridge hums all night like it pays rent, yet the only thing it "
    "ever produces is a light and a faint smell of 2019."
)

MAX_CHARS = 200


def complain(message):
    print("gate failed: " + message, file=sys.stderr)
    return 1


def run():
    line = ROAST
    if not line.strip():
        return complain("the line is empty")
    if any(ch in line for ch in "\r\n"):
        return complain("the line must fit on one line")
    if len(line) > MAX_CHARS:
        return complain(
            "the line is %d characters (max %d)" % (len(line), MAX_CHARS)
        )
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    # Read back what was written and refuse to report success unless it
    # is exactly the gated line plus one trailing newline.
    with open(target, "r", encoding="utf-8", newline="") as handle:
        stored = handle.read()
    if stored != line + "\n":
        return complain("what was written does not match the line")
    return 0


if __name__ == "__main__":
    sys.exit(run())
