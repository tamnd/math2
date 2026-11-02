---
tag: QDCD33CS21
kind: concept
name: Topological index
msc: [58J20, 19K56]
sources:
  - url: https://en.wikipedia.org/wiki/Atiyah–Singer_index_theorem
---

## Summary

The topological index of an elliptic operator on a closed manifold is an integer built only from topological data.
These data are the K-theory class of the principal symbol and the characteristic classes of the manifold.
Atiyah and Singer defined it by pushing the symbol class forward along an embedding of the manifold into a Euclidean space.
Their index theorem states that it equals the [[analytic index|44GBFZ16SG]].
In cohomology it is an integral of the Chern character of the symbol times the [[Todd class|2YDB5089FR]].

## Explanations

### L1 human

The analytic index is computed by solving equations, which is hard.
The topological index is computed from the symbol alone, the top-order part of the operator, read as a family of matrices over the cotangent bundle.
A small change of the operator does not change the topology of its symbol, so the topological index cannot jump.
For the operator $d + d^*$ from even to odd forms, the topological index is the Euler characteristic of the manifold.
