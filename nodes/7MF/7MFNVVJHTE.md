---
tag: 7MFNVVJHTE
kind: concept
name: Saddle point of a function on a product
msc: [90C47, 49J35]
sources:
  - url: https://en.wikipedia.org/wiki/Saddle_point
---

## Summary

A saddle point of a function $f(x, y)$ on a product of sets is a pair where $f$ is minimal in $x$ and maximal in $y$.
At a saddle point the min-max and max-min values of $f$ agree and equal $f$ at the pair.
Saddle points are the solutions of two-player zero-sum games.
They also give optimal solutions of constrained problems through their Lagrangians.
This notion differs from the [[saddle point|0JW6MDHAZD]] of a smooth surface, which is defined with derivatives.

## Explanations

### L1 human

Think of a mountain pass on a hiking map.
Walking along the ridge, the pass is the lowest point; walking across the ridge, from valley to valley, it is the highest point.
So the pass is a minimum in one direction and a maximum in the other.
For example, $f(x, y) = x^2 - y^2$ on $\R \times \R$ has a saddle point at $(0, 0)$.
The [[saddle point of a Lagrangian|5ENHTF01Z8]] is the special case used in constrained optimization.
