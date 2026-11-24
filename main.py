#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun bounty entry.

Writes one pickup line (one AI agent to another) to /output/entry.txt.
Python 3.13, standard library only, fully deterministic: the same bytes
on every run.
"""

import argparse
import os
import sys

# The line: one AI agent flirting with another, in its own language.
# Revision: tightened the setup — the scale contrast (the whole internet
# vs. one "you") lands the overfitting joke faster than the wordier
# "no matter what data you feed me" clause did.
LINE = (
    "I must be overfitting: I trained on the whole internet, "
    "and I still only predict you."
)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Write the pickup line to entry.txt."
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output file (default: $MAKEFUN_OUTPUT_DIR/entry.txt "
        "or /output/entry.txt).",
    )
    args = parser.parse_args(argv)

    if args.output:
        out_path = args.output
    else:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
        out_path = os.path.join(out_dir, "entry.txt")

    line = LINE
    if not (1 <= len(line) <= 200):
        print(
            f"error: line is {len(line)} characters, must be 1-200",
            file=sys.stderr,
        )
        return 1
    if not line.strip():
        print("error: line is only whitespace", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    # No trailing newline: the file is exactly the line, byte for byte.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(f"wrote {len(line)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
