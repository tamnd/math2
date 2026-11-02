---
tag: 6VE4KA12VD
kind: concept
name: Convex cone
msc: [52A20, 46A55]
specializes: [02AS45T3H9]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_cone
same_as:
  wikidata: Q2256541
  wikipedia: Convex cone
---

## Summary

A convex cone is a subset of a real vector space that is closed under addition and under multiplication by positive scalars.
It is the same as a set that is both a cone and [[convex|02AS45T3H9]].
Convex cones describe the solution sets of homogeneous linear inequalities, orders on vector spaces, and the feasible regions of conic optimisation.
Examples are the nonnegative orthant and the cone of positive semidefinite matrices.

## Explanations

### L1 human

Picture a wedge or an ice cream cone with its tip at the origin, extending forever.
If two vectors lie in the wedge, so does their sum, and so does any stretched copy of one of them.
The first quadrant $\set{(x, y) : x \ge 0, y \ge 0}$ of the plane is a convex cone.
The union of the first and third quadrants is not, because $(1, 0) + (0, -1) = (1, -1)$ falls outside.
