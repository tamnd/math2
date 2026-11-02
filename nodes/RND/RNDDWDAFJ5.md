---
tag: RNDDWDAFJ5
kind: concept
name: Euler characteristic
msc: [55N10, 57N65]
sources:
  - url: https://en.wikipedia.org/wiki/Euler_characteristic
same_as:
  wikidata: Q852973
  wikipedia: Euler characteristic
---

## Summary

The Euler characteristic $\chi(X)$ of a space is the alternating sum $b_0 - b_1 + b_2 - \cdots$ of its [[Betti numbers|ST71ZV3FES]].
For a finite [[CW complex|5W95QFHXPR]] it equals the alternating count of cells, which recovers $V - E + F$ for polyhedra.
It is a homotopy invariant, and it is multiplicative for products and finite coverings.
It links topology with geometry through results such as the Gauss–Bonnet theorem.

## Explanations

### L1 human

Count the vertices, edges and faces of a convex polyhedron, and compute $V - E + F$.
The answer is always $2$, whatever the polyhedron, for example $8 - 12 + 6 = 2$ for a cube.
This number belongs to the sphere, not to the particular polyhedron.
For the surface of a doughnut the same count always gives $0$.
The Euler characteristic extends this count to any reasonable space, using homology in place of counting cells.
