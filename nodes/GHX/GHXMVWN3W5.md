---
tag: GHXMVWN3W5
kind: concept
name: Nielsen fixed-point theory
msc: [55M20, 54H25]
sources:
  - url: https://en.wikipedia.org/wiki/Fixed-point_theorem
---

## Summary

Nielsen fixed-point theory studies the least number of fixed points among all maps homotopic to a given self-map $f$ of a space.
It sorts the fixed points of $f$ into classes, using paths and their images, and counts the classes that cannot be removed by a homotopy.
This count is the Nielsen number $N(f)$.
It is a homotopy invariant and a lower bound for the number of fixed points of every map homotopic to $f$.
It refines the [[Lefschetz number|ZSYCA4EGEZ]], which can only show that at least one fixed point exists.

## Explanations

### L1 human

The Lefschetz number can show that a map must have a fixed point, but not how many.
Nielsen theory sorts the fixed points into groups.
Two fixed points are in the same group if the map carries some path joining them to a path that can be deformed back to it.
During this deformation the two ends stay fixed.
Groups with a nonzero total weight can never be removed, so their number is a guaranteed minimum.
The map $z \mapsto z^3$ on the unit circle has two fixed points, $1$ and $-1$, in two essential classes.
So every map homotopic to it has at least two fixed points.
