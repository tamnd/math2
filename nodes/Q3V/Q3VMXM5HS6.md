---
tag: Q3VMXM5HS6
kind: example
name: Stag hunt
msc: [91A05]
instance_of: [5MZTZRC3CZ]
uses: [P01KKHB155, 745WYP9YJ0]
sources:
  - url: https://en.wikipedia.org/wiki/Stag_hunt
same_as:
  wikidata: Q1025469
  wikipedia: Stag hunt
---

## Example

In the *stag hunt* two hunters each choose $S$ (hunt a stag) or $H$ (hunt a hare).
A stag needs both hunters, while a hare can be caught alone.
It is the [[normal-form game|5MZTZRC3CZ]] with payoffs

| | $S$ | $H$ |
|---|---|---|
| $S$ | $(4, 4)$ | $(0, 3)$ |
| $H$ | $(3, 0)$ | $(3, 3)$ |

where the first number goes to the row player.
$(S, S)$ is a pure [[Nash equilibrium|745WYP9YJ0]], since switching to $H$ drops a payoff from $4$ to $3$.
$(H, H)$ is one too, since switching to $S$ drops a payoff from $3$ to $0$.
If the other hunter plays $S$ with probability $q$, then $S$ gives $4q$ and $H$ gives $3$.
So there is also a mixed equilibrium in which each plays $S$ with probability $3/4$.

## Remarks

$(S, S)$ gives both players more, so it is payoff dominant.
$(H, H)$ is safer: $H$ guarantees $3$ whatever the other does.
In the sense of Harsanyi and Selten, $(H, H)$ is risk dominant here, because $(3 - 0)^2 > (4 - 3)^2$.

## Explanations

### L1 human

Working together pays more, but only if the partner can be trusted.
Going alone pays less but cannot fail.
The game models social cooperation that depends on trust, in contrast with the prisoner's dilemma, where cooperating is never individually best.
