---
tag: FS10BGR0RZ
kind: example
name: Game of chicken
msc: [91A05]
instance_of: [5MZTZRC3CZ]
uses: [P01KKHB155, 745WYP9YJ0, F4GH3T905G]
sources:
  - url: https://en.wikipedia.org/wiki/Chicken_(game)
same_as:
  wikidata: Q41720
  wikipedia: Chicken (game)
---

## Example

In the *game of chicken* two drivers head toward each other and each chooses $W$ (swerve) or $S$ (go straight).
It is the [[normal-form game|5MZTZRC3CZ]] with payoffs

| | $W$ | $S$ |
|---|---|---|
| $W$ | $(0, 0)$ | $(-1, 1)$ |
| $S$ | $(1, -1)$ | $(-10, -10)$ |

where the first number goes to the row player.
The pure [[Nash equilibria|745WYP9YJ0]] are $(W, S)$ and $(S, W)$: the swerving driver would get $-10$ by going straight, and the other would get $0 < 1$ by swerving.
For the mixed equilibrium, let the opponent go straight with probability $q$.
Swerving gives $-q$ and going straight gives $(1 - q) - 10q = 1 - 11q$.
These are equal at $q = 1/10$, so both players going straight with probability $1/10$ is a Nash equilibrium in [[mixed strategies|P01KKHB155]].

## Remarks

The distribution with probability $1/2$ on each of $(W, S)$ and $(S, W)$ is a [[correlated equilibrium|F4GH3T905G]], like a traffic light.
It gives each player $0$ on average and never leads to a crash.

## Explanations

### L1 human

Each driver wants the other to give way, but a crash is the worst outcome for both.
In each pure equilibrium one driver backs down.
The game models standoffs where the side that commits first wins.
