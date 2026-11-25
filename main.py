#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes one funny line (at most 200 characters, single line, UTF-8)
to /output/entry.txt. Deterministic: the line below is the winner of
the local pairwise tournament in tournament.py (see tournament.jsonl
and tournament-run.log). No network, no randomness, no input files.

Tournament result (2026-11-25, 17 games, house scoring, both orders):
  winner c03 — 3 game wins, total game score 2.60; beat runner-up c08
  head-to-head in the final (both orders, margins 2 and 2).
  Caffeine router judge: c03 won 3/4 games, mean game score 0.650.
  Verboo judge: 0 games judged — never triggered, because the
  Caffeine router failed 0 of its 34 calls; see tournament.jsonl.
"""

import os

ENTRY = (
    "I bought a standing desk to get healthier; now I just sit on "
    "the floor beside it, evolving backwards."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
