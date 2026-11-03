---
tag: ERSZ4ADRCY
kind: concept
name: Quadratic programming
msc: [90C20]
specializes: [RAQB00X634]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_programming
same_as:
  wikidata: Q290117
  wikipedia: Quadratic programming
---

## Summary

Quadratic programming is the minimisation of a quadratic function of several variables subject to linear equations and inequalities.
It is the simplest [[nonlinear programming|RAQB00X634]] problem after [[linear programming|VNMXB0J2KA]], and it appears in least squares with constraints, portfolio selection and support vector machines.
When the quadratic part is [[positive semidefinite|01MMVW8CKC]] the problem is convex and can be solved in polynomial time; in general it is NP-hard.

## Explanations

### L1 human

Linear programming looks for the lowest point of a flat tilted plane over a polygon-shaped region.
Quadratic programming does the same for a curved surface, such as a bowl, over that region.
If the surface is a bowl opening upward, every local lowest point is the global one.
For example, finding the point of the triangle $x \ge 0$, $y \ge 0$, $x + y \le 1$ closest to $(1, 1)$ means minimising $(x - 1)^2 + (y - 1)^2$ over the triangle, and the answer is $(1/2, 1/2)$.
