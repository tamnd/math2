---
tag: 4AMAKVEQBG
kind: definition
name: Backward induction
msc: [91A18]
defines: JEMK4V2PCW
uses: [4Y8AF9H9HA, P01KKHB155]
sources:
  - url: https://en.wikipedia.org/wiki/Backward_induction
---

## Definition

Let $\Gamma$ be a finite [[extensive-form game|4Y8AF9H9HA]] of perfect information without chance nodes.
*Backward induction* assigns an action to every decision node and a payoff vector to every node, as follows.

1. A terminal node gets its own payoff vector.
2. Let $v$ be a decision node of player $i$ whose children all have payoff vectors. At $v$, choose an action whose child has the largest $i$-th coordinate.
3. Give $v$ the payoff vector of that child.

The chosen actions form a pure [[strategy|P01KKHB155]] profile.

## Remarks

Every decision node gets an action, because the tree is finite and the procedure works from the leaves to the root.
With chance nodes one gives each chance node the expected payoff vector of its children.
The resulting profile is a subgame perfect equilibrium.
The existence of a pure equilibrium in finite games of perfect information is often called Kuhn's theorem, and related ideas go back to Zermelo's work on chess.
If no player has the same payoff at two different terminal nodes, the result is unique.
Example: in the entry game, player 2 compares Fight, with payoff $-1$, and Accommodate, with payoff $1$, and chooses Accommodate.
The node In then gets $(1, 1)$, and player 1 compares $1$ with $0$ for Out and chooses In.
Non-example: the profile (Out, Fight) is not produced by the procedure, because clause 2 rules out Fight at player 2's node.
With imperfect information the procedure does not apply directly, since a player at an information set may not know at which node she is.
