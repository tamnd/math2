---
tag: ST71ZV3FES
kind: concept
name: Betti number
msc: [55N10]
sources:
  - url: https://en.wikipedia.org/wiki/Betti_number
same_as:
  wikidata: Q429593
  wikipedia: Betti number
---

## Summary

The $k$-th Betti number $b_k(X)$ of a topological space $X$ is the rank of its $k$-th integral [[singular homology|M0Q5CFJ7ZH]] group.
Informally, $b_0$ counts the path components, $b_1$ counts independent loops that do not bound, and $b_2$ counts enclosed cavities.
Betti numbers are homotopy invariants, and their alternating sum is the [[Euler characteristic|RNDDWDAFJ5]].

## Explanations

### L1 human

Betti numbers count holes of each dimension.
A circle has one piece and one loop around a hole, so $b_0 = 1$ and $b_1 = 1$.
The surface of a doughnut has one piece, two independent loops (around the tube and around the central hole) and one enclosed cavity, so its Betti numbers are $1, 2, 1$.
A solid ball has $b_0 = 1$ and no holes at all, so its other Betti numbers are zero.
