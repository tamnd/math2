---
tag: RDTESNZTKQ
kind: concept
name: Indirect method by shooting
msc: [49M05, 65L10, 49K15]
specializes: [ECT6RNF865]
sources:
  - url: https://en.wikipedia.org/wiki/Shooting_method
---

## Summary

The indirect method by shooting solves an [[optimal control|T3V6ZNAMDN]] problem by first writing the necessary conditions of [[Pontryagin's maximum principle|7RPV2T29CF]] and then solving them numerically.
These conditions form a two-point [[boundary value problem|TM8VQJWGHZ]] for the state and the costate.
The unknown initial costate is found by the [[shooting method|ECT6RNF865]]: one integrates forward from a guess and corrects the guess until the final conditions hold.
The method is very accurate near a good guess, and it is the main alternative to direct methods such as [[direct collocation|T58W34D60G]].

## Explanations

### L1 human

The maximum principle tells you what an optimal trajectory looks like, except for a few unknown numbers at the start.
If you knew the initial costate, you could integrate the equations forward and get the whole optimal path.
So you guess it, integrate, measure how far you miss the required final state, and adjust the guess, as when aiming a cannon.
For instance, take $x' = u$ from $0$ to $1$ in unit time at least cost $\int u^2 / 2$.
The conditions say $u$ is a constant $p$, and shooting finds $p = 1$ after one Newton step.
The hard part in practice is that the miss can depend very sensitively on the guess.
