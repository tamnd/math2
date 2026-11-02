---
tag: KFCXGKK288
kind: concept
name: Gale diagram
msc: [52B35, 52B11]
sources:
  - url: https://en.wikipedia.org/wiki/Gale_diagram
same_as:
  wikidata: Q99675552
  wikipedia: Gale diagram
---

## Summary

The Gale diagram, or Gale transform, turns $n$ points spanning $\R^d$ into $n$ vectors in $\R^{n-d-1}$.
The new vectors encode the affine dependences of the old points.
The faces of the [[convex hull|0FQSDC2EQ2]] of the points can be read off from them.
Suppose a [[convex polytope|300K6CB1KH]] has only a few more vertices than its dimension.
Then its Gale diagram lives in a very low dimension and can be drawn.
This makes Gale diagrams a main tool for classifying such polytopes and for building polytopes with unexpected properties.

## Explanations

### L1 human

A polytope in high dimension with few corners is hard to picture directly.
The Gale diagram trades the dimension of the space for the number of extra corners.
For example, a $d$-dimensional polytope with $d + 3$ corners becomes a set of vectors in the plane.
Questions about faces of the polytope then become questions about which vectors surround the origin.
