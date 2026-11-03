---
tag: 3GQQBDYHWT
kind: example
name: Battle of the sexes
msc: [91A05]
instance_of: [5MZTZRC3CZ]
uses: [P01KKHB155, 745WYP9YJ0]
sources:
  - url: https://en.wikipedia.org/wiki/Battle_of_the_sexes_(game_theory)
same_as:
  wikidata: Q1187614
  wikipedia: Battle of the sexes (game theory)
---

## Example

In the *battle of the sexes* two players want to spend the evening together but prefer different events, $O$ (opera) and $F$ (football).
It is the [[normal-form game|5MZTZRC3CZ]] with payoffs

| | $O$ | $F$ |
|---|---|---|
| $O$ | $(2, 1)$ | $(0, 0)$ |
| $F$ | $(0, 0)$ | $(1, 2)$ |

where the first number goes to the row player.
$(O, O)$ and $(F, F)$ are pure [[Nash equilibria|745WYP9YJ0]]: a single deviation drops the deviator's payoff to $0$.
There is also a mixed equilibrium.
Let the row player play $O$ with probability $p$ and the column player with probability $q$.
The column player is indifferent when $p \cdot 1 = (1 - p) \cdot 2$, that is $p = 2/3$.
The row player is indifferent when $2q = 1 - q$, that is $q = 1/3$.
At these [[mixed strategies|P01KKHB155]] each player gets $2/3$, less than in either pure equilibrium.

## Explanations

### L1 human

Both players most want to meet, but each prefers a different place.
There are two good outcomes, and the game alone does not say which one will happen.
It is a standard example of a coordination problem with a conflict of interest.
