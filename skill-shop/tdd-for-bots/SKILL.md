---
name: tdd-for-bots
description: Test-first changes to bot.py. Use before you change shoot() or keep().
---
# TDD for bots

1. Write a test in `test_bot.py` for the behaviour you want, for example "with an opponent run-up angle of -25, keep() dives left".
2. Run `python -m pytest -q` and see the test fail.
3. Change `bot.py` until the test passes.
4. Check the bot against the real stadium: `./penalty practice` a few times.

Rules for `bot.py`:
- `shoot(state)` returns `(target, power)`: one of `left-low`, `left-high`, `center-low`, `center-high`, `right-low`, `right-high`, and a power from 0 to 1.
- `keep(state)` returns `left`, `center` or `right`.
- Both must be fast and must never raise an exception: a crash forfeits the match.
