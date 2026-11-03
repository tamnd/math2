---
tag: 6B2MN8JJRP
kind: definition
name: Game theory
msc: [91A10, 91A12]
defines: J8A9GBFSTY
uses: [5MZTZRC3CZ, 4Y8AF9H9HA]
sources:
  - url: https://en.wikipedia.org/wiki/Game_theory
---

## Definition

A *game* is a model of strategic interaction made of the following data.

1. A set of players.
2. For each player, a set of available choices.
3. A rule that assigns an outcome to each combination of choices.
4. For each player, a preference over the outcomes, usually given by a real-valued payoff function.

*Game theory* is the mathematical study of games and of solution concepts, which single out combinations of choices as reasonable predictions of play.
In *noncooperative* game theory the players choose independently; in *cooperative* game theory groups of players may make binding agreements.

## Remarks

There are two basic formal models.
In a [[normal-form game|5MZTZRC3CZ]] all players choose once and at the same time.
In an [[extensive-form game|4Y8AF9H9HA]] moves happen in order on a game tree.
Example: rock-paper-scissors has two players, three choices each, and payoffs $1$ for a win, $-1$ for a loss and $0$ for a tie; this fills all four clauses.
Non-example: a single person choosing the shortest route on an empty road faces an optimisation problem, not a game.
There is only one decision maker, while clause 1 asks for several interacting players.
