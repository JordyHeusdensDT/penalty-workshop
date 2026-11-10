---
name: penalty-analytics
description: How to analyse penalty match logs to find patterns. Use after you played some matches and want to improve bot.py with evidence.
---
# Penalty analytics

1. Play many practice matches first: `./penalty practice` (you can play 60 per minute). Each finished match writes `logs/<match_id>.json`.
2. A log is `{"kicks": [...]}`. Every kick has `shooter` (`player` or `house`), `target`, `power`, `dive`, `outcome` (`goal`, `saved`, `missed`), `ball_x`, `ball_y` (where the ball went), `sudden_death`, and for house kicks the `run_up`.
3. Load all logs into one table (pandas, or plain Python) and group:
   - your goal rate per power bucket (0.1 wide)
   - the keeper's dive against what you shot in your previous kicks
   - the house target against its run-up angle
   - `ball_x` against `target` per match
   - outcomes in sudden death against regulation time
4. Look for differences larger than chance. Use at least a few hundred kicks per question, because 20 kicks prove nothing.
5. Change one thing in `bot.py`, play 50 matches, and compare the goal rate with the previous version.
