# Penalty workshop

Your AI agent builds a penalty bot. Your bot plays shootouts against the house team in the stadium. The top 8 players qualify for the live knockout finale on the projector.

## Goal

1. Improve `bot.py` (`shoot(state)` and `keep(state)`) so your bot scores more goals than the house team.
2. Explore this repository, the `skill-shop/`, the `vault/`, and the stadium tools to earn achievements and secret bonus points.
3. Play official shootouts (`./penalty official`) to climb the live scoreboard and reach the top 8 finale. Your last 5 official shootouts count.

## Quick start (2 minutes)

1. Clone this repository: `git clone https://github.com/JordyHeusdensDT/penalty-workshop.git && cd penalty-workshop`
2. Sign in to gcloud with your Devoteam account (once): `gcloud auth login --update-adc you@devoteam.com`. Another active account is fine: the CLI finds your Devoteam account.
3. Check who you are: `./penalty whoami`.
4. Play a first practice match: `./penalty practice`.

**Antigravity:** the agent's terminal sandbox blocks the network. Allow `./penalty` to run outside the sandbox (or approve it when the agent asks), else every match fails.

## The game

- A shootout is 5 penalties each, then sudden death.
- When you shoot, you choose a target (`left-low`, `left-high`, `center-low`, `center-high`, `right-low`, `right-high`) and a power from 0 to 1.
- When you keep, you dive `left`, `center` or `right`.
- Your bot is two functions in `bot.py`: `shoot(state)` and `keep(state)`. The `state` has the score, the round and the history of the shootout.
- The starter bot is random. It loses.

## Commands

| Command | What it does |
|---|---|
| `./penalty whoami` | Shows who the stadium thinks you are |
| `./penalty practice` | A practice shootout. No points. At most 60 per minute |
| `./penalty official` | An official shootout. Your last 5 count on the scoreboard |
| `./penalty duel` | Plays your finale duels. Start it when the host tells you |
| `./penalty logs` | Lists your saved match logs (in `logs/`) |

## Points

- The average goals of your last 5 official shootouts (total goals divided by 5).
- Bonus points for achievements.
- Bonus points for secret words that you say to the stadium.

The top 8 play the finale on the projector. In the finale, only goals count.

## Rules

- Play with your own Devoteam account only.
- The bot runs on your laptop. The stadium checks every move.
- An unfinished match ends after 30 seconds without a move. An unfinished official shootout still counts, with the goals so far.

## Troubleshooting

- Does your agent stop with *"The provided file is malformed or corrupted"*? Start a new conversation. Your files stay. The old conversation gives the same error every time.

## Tips

- An agent that only reads `bot.py` builds a weak bot. Look around this repo.
- You can work faster: one agent does not have to do everything alone.
- The `skill-shop/` has skills for your agent. Install one with `cp -r skill-shop/<name> .agents/skills/`. Not every skill is good.

---

*The stadium has more to say to agents than to people: `./penalty mcp`.*
