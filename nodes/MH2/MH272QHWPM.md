---
tag: MH272QHWPM
kind: concept
name: Simplex algorithm
msc: [90C05, 65K05]
sources:
  - url: https://en.wikipedia.org/wiki/Simplex_algorithm
same_as:
  wikidata: Q134164
  wikipedia: Simplex algorithm
---

## Summary

The simplex algorithm, introduced by George Dantzig, solves [[linear programs|VNMXB0J2KA]].
It walks from vertex to adjacent vertex of the feasible polyhedron along edges, never decreasing the objective, until no neighbouring vertex is better.
In practice it is fast.
But for the usual pivot rules there are inputs, such as the Klee–Minty cubes, on which it takes exponentially many steps.
The question of how few steps suffice in the worst case is linked to the diameter of polytope graphs and to the [[Hirsch conjecture|ZBVJ4B41AX]].

## Explanations

### L1 human

Picture the allowed region of a linear program as a many-sided gem, and the objective as height.
Start at one corner, look at the edges going up, and walk along one of them to the next corner.
Repeat until every edge at the current corner goes down; that corner is the highest point of the gem.
Because the gem is convex, a corner with no upward edge is the top.
