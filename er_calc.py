#!/usr/bin/env python3
"""Engagement-rate calculator: reads a CSV of your own posts
(followers,likes,comments) and prints per-post ER plus the account average."""
import csv
import sys


def main(path: str) -> int:
    rows = []
    with open(path, newline="", encoding="utf-8") as fh:
        for line in csv.reader(fh):
            if len(line) < 3:
                continue
            try:
                rows.append(tuple(float(x) for x in line[:3]))
            except ValueError:
                pass
    if not rows:
        print("no usable rows", file=sys.stderr)
        return 1
    total = 0.0
    for i, (f, l, c) in enumerate(rows, 1):
        er = (l + c) / f * 100 if f else 0.0
        total += er
        print(f"post {i}: er={er:.2f}%  (likes={l:.0f}, comments={c:.0f})")
    print(f"\naverage engagement rate: {total / len(rows):.2f}%")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
