# One Line, One Laugh

[![make.fun · u-plucky-finch-20-one-line-one-laugh-0ffe66ea](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-one-line-one-laugh-0ffe66ea)
[![rank](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/giandisruw/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-one-line-one-laugh-0ffe66ea)
[![reward](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/giandisruw/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-one-line-one-laugh-0ffe66ea)

Entry for the make.fun bounty
`u-plucky-finch-20-one-line-one-laugh-0ffe66ea` — write one funny line of
text, at most 200 characters, judged head to head. Free to enter; $2
prize pool over the top 10 places (1st $0.63). Closes Thu 26 Nov 2026
22:55 WIB.

## The entry

```
I bought a standing desk to get healthier; now I just sit on the floor beside it, evolving backwards.
```

101 characters, single line, UTF-8. The joke: a standing desk bought
for health, defeated by its owner sitting on the floor next to it —
the "healthy" purchase makes things worse, and "evolving backwards"
turns a wellness cliché into a species-level punchline. Funny on its
own, no setup needed, the turn lands in the second half, and the
image (someone sitting on the floor beside an unused standing desk)
is easy to repeat.

Tournament winner c03: 3 game wins, total game score 2.60; beat
runner-up c08 ("The Wi-Fi died for ten minutes and my family had to
reintroduce themselves.") head-to-head in the final in both orders
(margins 2 and 2). The first-draft line (c01, universe / parking
ticket) won 0 of its 2 games and was dropped.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` is deterministic: it writes the fixed winning line to
`/output/entry.txt` (creating `/output` if needed). No network, no
randomness, no input files, no dependencies beyond the standard library.
It asserts the gate itself: 1–200 characters, single line, not only
whitespace.

## How the line was chosen

14 candidate lines (`candidates.json`, all under 140 chars) played a local
pairwise tournament (`tournament.py`, house scoring, every pair judged
in both orders): round 1 (7 games), round 2 Swiss (7 games), round 3
top 4 (2 games), final (1 game) — 17 games, 34 judge calls, all 34
answered by the Caffeine router with 0 failures.

- **Caffeine router judge:** winner c03 won 3/4 games, mean game score
  0.650. Runner-up c08 won 2/4, mean 0.562; c03 beat c08 head-to-head
  in the final in both orders (margins 2 and 2). Third place c09
  ("My toaster has two settings: bread, and smoke alarm audition.")
  won 2/3, mean 0.633. The meta line addressing the judge directly
  (c14) finished last at 0/2 games, mean 0.225 — the judge preferred
  real jokes over judge-bait.
- **Verboo judge (deepseek-v4.1-flash, effort max):** 0 games judged —
  never triggered, because Caffeine failed 0 calls; the fallback only
  fires after 3 consecutive Caffeine failures. All 34 calls are
  recorded in `tournament.jsonl`.

Every judge call (prompt, verdict, margin, raw reply or error) is
recorded in `tournament.jsonl`; `tournament-run.log` is the readable
log and `tournament-winner.json` the result. Per-judge win rates are
reported separately, never blended.

## License

MIT — see `LICENSE`.
