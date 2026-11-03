---
tag: 1YER21VF5Q
kind: example
name: Prisoner's dilemma
msc: [91A05, 91A10]
instance_of: [5MZTZRC3CZ]
uses: [9BF72YM075, 745WYP9YJ0]
sources:
  - url: https://en.wikipedia.org/wiki/Prisoner%27s_dilemma
same_as:
  wikidata: Q41693
  wikipedia: Prisoner's dilemma
---

## Example

The *prisoner's dilemma* is the two-player [[normal-form game|5MZTZRC3CZ]] with strategies $C$ (cooperate) and $D$ (defect) for each player and payoffs

| | $C$ | $D$ |
|---|---|---|
| $C$ | $(3, 3)$ | $(0, 5)$ |
| $D$ | $(5, 0)$ | $(1, 1)$ |

where the first number goes to the row player.
For the row player, $D$ gives $5 > 3$ against $C$ and $1 > 0$ against $D$.
So $D$ [[strictly dominates|9BF72YM075]] $C$, and by symmetry the same holds for the column player.
Hence $(D, D)$ is the unique [[Nash equilibrium|745WYP9YJ0]], with payoffs $(1, 1)$.
Yet $(C, C)$ gives both players $3 > 1$.

## Remarks

Any payoffs with $T > R > P > S$ give the same structure, where $T$ is the temptation $5$, $R$ the reward $3$, $P$ the punishment $1$ and $S$ the sucker's payoff $0$.
The game shows that individually rational choices can lead to an outcome that is worse for everyone.
When the game is repeated indefinitely, cooperation can be sustained by threats of future punishment.

## Explanations

### L1 human

Two suspects are questioned separately.
Each is better off confessing, whatever the other does.
But if both stay silent, both get a lighter sentence than if both confess.
