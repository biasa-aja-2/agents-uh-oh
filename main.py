"""One-word agent uh-oh for make.fun.

Writes a single word an AI agent says when it has no idea what to do
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Pure stdlib, deterministic, no network, no randomness.

The word is "recalculating": the sound of a navigation agent that has
lost the route and is stalling while it works out where it went wrong.
It is what an agent actually blurts out mid-task when it is lost, it
lands at a glance, and it is not the first obvious word anyone types.
"""

import os
import sys

WORD = "recalculating"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
