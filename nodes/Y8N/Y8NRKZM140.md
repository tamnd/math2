---
tag: Y8NRKZM140
kind: definition
name: Subgame perfect equilibrium
msc: [91A18, 91A11]
defines: HE8K9M4EXN
uses: [4Y8AF9H9HA, P01KKHB155, 745WYP9YJ0, JEMK4V2PCW]
sources:
  - url: https://en.wikipedia.org/wiki/Subgame_perfect_equilibrium
---

## Definition

Let $\Gamma$ be a finite [[extensive-form game|4Y8AF9H9HA]].
A decision node $x$ is the root of a *subgame* if the following hold.

1. The information set of $x$ is $\set{x}$.
2. Every information set that contains a successor of $x$ contains only successors of $x$.

The subgame is the part of $\Gamma$ consisting of $x$ and its successors, with the inherited data.
A profile of behavior [[strategies|P01KKHB155]] of $\Gamma$ is a *subgame perfect equilibrium* if its restriction to every subgame is a [[Nash equilibrium|745WYP9YJ0]] of that subgame.

## Remarks

The whole game is a subgame, so a subgame perfect equilibrium is a Nash equilibrium.
In a finite game of perfect information every node is the root of a subgame, and [[backward induction|JEMK4V2PCW]] gives a pure subgame perfect equilibrium.
Example: in the entry game, player 1 chooses Out, ending with $(0, 2)$, or In; then player 2 chooses Fight, $(-1, -1)$, or Accommodate, $(1, 1)$.
The profile (In, Accommodate) is subgame perfect: Accommodate is best in the subgame after In, and then In gives player 1 $1 > 0$.
Non-example: (Out, Fight) is a Nash equilibrium, since player 2's choice does not matter once player 1 stays out.
It is not subgame perfect, because in the subgame after In, Fight gives player 2 $-1 < 1$.
