---
tag: TGM10N59RR
kind: example
name: Blotto game
msc: [91A05]
instance_of: [8PC5CFGMAD]
uses: [5MZTZRC3CZ, 745WYP9YJ0]
sources:
  - url: https://en.wikipedia.org/wiki/Blotto_game
same_as:
  wikidata: Q1280481
  wikipedia: Blotto game
---

## Example

In a *Blotto game* two players each split a fixed number of soldiers among $k$ battlefields at the same time.
Each battlefield is won by the player who sent more soldiers to it, and it is a tie if both sent the same number.
A player's payoff is the number of battlefields she wins minus the number she loses.
So the payoffs add up to $0$, and this is a [[zero-sum game|8PC5CFGMAD]] in [[normal form|5MZTZRC3CZ]].

Take $k = 3$ battlefields and $2$ indivisible soldiers for each player.
Each player has six pure strategies: the three permutations of $(2, 0, 0)$ and the three permutations of $(1, 1, 0)$.
Play $(1, 1, 0)$ against each of the six:

- against $(1, 1, 0)$, $(1, 0, 1)$, $(0, 1, 1)$ the payoff is $0$;
- against $(2, 0, 0)$: lose, win, tie, so $0$; against $(0, 2, 0)$: win, lose, tie, so $0$;
- against $(0, 0, 2)$: win, win, lose, so $1$.

So $(1, 1, 0)$ never gets less than $0$.
The game is symmetric, so its value is $0$, and $(1, 1, 0)$ is an optimal strategy for each player.
Hence the profile where both play $(1, 1, 0)$ is a pure [[Nash equilibrium|745WYP9YJ0]].

## Remarks

The game goes back to Émile Borel.
In larger versions, with many soldiers and battlefields, there is usually no pure equilibrium, and the optimal mixed strategies are hard to describe.

## Explanations

### L1 human

Two generals divide their troops among several fronts, and each front goes to the side with more troops there.
Putting everything on one front wins it for sure but loses the others.
In the small game above, spreading the troops thinly over two fronts is the safe choice.
