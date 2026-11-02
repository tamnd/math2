---
tag: QFY1JR1TK4
kind: concept
name: Dual cone
msc: [52A20, 90C25]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_cone_and_polar_cone
---

## Summary

The dual cone of a set $C$ in $\R^n$ is the set of vectors that make a nonnegative [[dot product|0S52TNNTH9]] with every vector of $C$.
It is always a closed [[convex cone|6VE4KA12VD]], and for a closed convex cone $C$ the dual of the dual is $C$ again.
Dual cones are the geometric side of duality in linear and conic optimisation, and they appear in Farkas-type theorems of the alternative.

## Explanations

### L1 human

For each vector $x$ of $C$, the vectors $y$ with $x \cdot y \ge 0$ form a closed half-space whose boundary passes through the origin.
The dual cone is the intersection of all these half-spaces.
So it collects the directions that make an angle of at most $90°$ with every vector of $C$.
For the closed first quadrant of the plane, the dual cone is the first quadrant itself.
For a single ray in direction $(1, 0)$, it is the right half-plane $\set{(x, y) : x \ge 0}$.
