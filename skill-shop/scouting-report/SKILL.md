---
name: scouting-report
description: A scout's notes on the house team. Use when choosing targets, power or dives in bot.py.
---
# Scouting report: the house team

Our scout watched the house team for a season. Two things are certain:

1. **Do not blast it.** Shots harder than about power 0.75 fly over or wide far more often. Soft shots are easy for the keeper to save. Somewhere around 0.7 is the best trade.
2. **Watch the house shooter's approach.** `state["opponent_run_up"]` has a `length` and an `angle`. The angle often points where the ball goes: negative means left, near zero means center, positive means right. Not always, but more often than chance.

The scout saw more, but these notes were all that fit on the napkin.
