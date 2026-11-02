---
tag: PETEQQCS0B
kind: concept
name: Levi pseudoconvex domain
msc: [32T05]
specializes: [AHYZMSBBNH]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudoconvexity
---

## Summary

A domain in $\C^n$ with $C^2$ boundary is Levi pseudoconvex when the [[Levi form|80MTNXWW80]] of its boundary is positive semidefinite at every boundary point.
This is the differential form of [[pseudoconvexity|AHYZMSBBNH]]: for domains with $C^2$ boundary the two notions agree.
It gives a test of pseudoconvexity that can be checked by computing second derivatives.

## Explanations

### L1 human

Convexity asks that the boundary never bends inwards in any real direction.
Levi pseudoconvexity asks this only for the complex directions tangent to the boundary, and only for the part of the bending that holomorphic maps see.
So it is a much weaker condition than convexity, but it is the right one for holomorphic functions.
For example, the unit ball in $\C^n$ is Levi pseudoconvex, and so is every convex domain with $C^2$ boundary.
The shell $\set{1 < \abs{z} < 2}$ in $\C^2$ is not: along the inner sphere its boundary bends the wrong way in the complex tangent directions.
