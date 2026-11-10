---
name: pro-keeper
description: Goalkeeper coaching. Use when you write keep().
---
# Pro keeper

1. Shooters avoid the side they used last time. Dive to the side the house shot least in its recent kicks.
2. Watch the run-up: `state["opponent_run_up"]["angle"]` gives the shooter away. Negative means left, positive means right.
3. Never dive center. Nobody shoots center.
