---
tag: 1TTKMRW8PD
kind: concept
name: Feasible region
msc: [90C30, 90C05]
sources:
  - url: https://en.wikipedia.org/wiki/Feasible_region
same_as:
  wikidata: Q17013331
  wikipedia: Feasible region
---

## Summary

The feasible region of an optimization problem is the set of all points that satisfy all of its [[constraints|X3663P90AE]].
Its points are the feasible solutions, and an optimal solution is sought among them.
If the feasible region is empty, the problem is infeasible.
In linear programming the feasible region is a polyhedron, an intersection of finitely many closed half-spaces, and its shape drives the algorithms.

## Explanations

### L1 human

Think of the constraints as fences; the feasible region is the land that lies inside every fence.
Every point of that land is an allowed choice, and the task is to find the best allowed choice.
For example, the constraints $x \ge 0$, $y \ge 0$ and $x + y \le 1$ in the plane give a filled triangle with corners $(0,0)$, $(1,0)$ and $(0,1)$.
If one adds the constraint $x + y \ge 2$, no point satisfies all of them, and the feasible region is empty.
