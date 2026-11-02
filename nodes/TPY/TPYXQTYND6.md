---
tag: TPYXQTYND6
kind: concept
name: Hyers–Ulam stability
msc: [39B82]
sources:
  - url: https://en.wikipedia.org/wiki/Hyers%E2%80%93Ulam%E2%80%93Rassias_stability
---

## Summary

A [[functional equation|SRAN4EKWS0]] is Hyers–Ulam stable if each approximate solution is near an exact one.
Precisely, a function that satisfies it up to an error $\delta$ lies within $K\delta$ of a solution, for a fixed constant $K$.
The notion comes from a question of Ulam on approximate homomorphisms.
[[Hyers' theorem|VFRJ0P2P15]] shows that the Cauchy equation $f(x+y) = f(x) + f(y)$ is stable, with $K = 1$, for maps from a normed space to a Banach space.
Stability results justify replacing an approximate solution by an exact one.

## Explanations

### L1 human

Measurements and computations are never exact, so a function found in practice satisfies an equation only roughly.
Stability says this is harmless: a rough solution is near a true solution.
For example, $f(x) = x + \sin x$ satisfies $f(x + y) = f(x) + f(y)$ up to an error at most $3$, and it stays within distance $1$ of the true solution $x \mapsto x$.
Some equations are not stable, and then a rough solution can drift arbitrarily far from every true one.
