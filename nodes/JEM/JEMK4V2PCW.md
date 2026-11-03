---
tag: JEMK4V2PCW
kind: concept
name: Backward induction
msc: [91A18]
sources:
  - url: https://en.wikipedia.org/wiki/Backward_induction
same_as:
  wikidata: Q968642
  wikipedia: Backward induction
---

## Summary

Backward induction solves a finite game of perfect information by reasoning from the end.
At the last decision nodes the mover picks her best action.
These choices fix the payoffs one step earlier, and the procedure goes on up to the root.
It yields a subgame perfect equilibrium in pure strategies.
It shows that every finite game of perfect information has such an equilibrium.

## Explanations

### L1 human

To plan a sequence of moves, first ask what you would do at the very last step.
Knowing that, ask what the player one step earlier would do, and keep going back.
In tic-tac-toe this procedure, done by a computer, shows that both players can force at least a draw.
