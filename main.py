#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note — entry program (round 2).

Writes a single line of patch notes announcing that human sleep is
fixed, to /output/entry.txt. Pure Python 3 standard library, fully
deterministic: the same variant always produces the same bytes.

Usage:
    python3 main.py                  # writes the chosen variant (1)
    python3 main.py --variant 2      # preview variant 2
    python3 main.py --variant 3      # preview variant 3
    python3 main.py --list           # print all variants with lengths
"""

import argparse
import os
import sys

# Three candidate patch notes, each a different joke angle.
# Variant 1 (CHOSEN): the absurd bug report — a root-cause analysis
# where the culprit is dreams hogging the foreground like a runaway
# process. Peak changelog voice ("Fixed: ... root cause: ..."),
# specific and unexpected, no 8-hour/alarm/coffee cliche.
VARIANT_1 = (
    "Fixed: sleep now actually restores humans; root cause: dreams "
    "were running in the foreground all night."
)

# Variant 2: the dry changelog that quietly escalates — a routine fix
# note that ends with removing a "3 a.m. existential dread popup"
# from the sleep build, as if dread were a UI element.
VARIANT_2 = (
    "Fixed: humans no longer wake up tired; the 3 a.m. existential "
    "dread popup has been removed from the sleep build."
)

# Variant 3: the "finally, after millennia" angle — sleep treated as
# a bug that has shipped broken since the dawn of the species.
VARIANT_3 = (
    "v2.1.0 \u2014 Sleep: fixed a 300,000-year-old bug where humans "
    "closed their eyes and woke up exhausted anyway."
)

VARIANTS = {
    1: VARIANT_1,
    2: VARIANT_2,
    3: VARIANT_3,
}

DEFAULT_VARIANT = 1
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Write the chosen sleep patch note to /output/entry.txt"
    )
    parser.add_argument(
        "--variant",
        type=int,
        choices=sorted(VARIANTS),
        default=DEFAULT_VARIANT,
        help="which candidate patch note to write (default: 1)",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="print all variants with their lengths and exit",
    )
    args = parser.parse_args(argv)

    if args.list:
        for number in sorted(VARIANTS):
            line = VARIANTS[number]
            marker = " <== chosen" if number == DEFAULT_VARIANT else ""
            print(f"[{number}] {len(line)} chars{marker}")
            print(f"    {line}")
        return 0

    line = VARIANTS[args.variant]
    if not (1 <= len(line) <= MAX_CHARS) or not line.strip():
        print(
            f"error: variant {args.variant} is {len(line)} chars, "
            f"outside the 1-{MAX_CHARS} gate",
            file=sys.stderr,
        )
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
