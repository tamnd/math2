---
tag: MVGBS3J1P7
kind: concept
name: Krull dimension
msc: ["13C15"]
sources:
  - url: https://en.wikipedia.org/wiki/Krull_dimension
same_as:
  wikidata: Q1225713
  wikipedia: Krull dimension
---

## Summary

The Krull dimension of a commutative ring is the largest length of a strictly increasing chain of [[prime ideals|00MHHZ9SNE]].
It is the algebraic notion of dimension: the coordinate ring of an affine variety has Krull dimension equal to the dimension of the variety.
Fields have dimension $0$, and principal ideal domains that are not fields, such as $\Z$, have dimension $1$.
The polynomial ring in $n$ variables over a field has dimension $n$.

## Explanations

### L1 human

Points, curves and surfaces have dimensions $0$, $1$ and $2$.
In algebra, a point corresponds to a maximal ideal, and a bigger irreducible object corresponds to a smaller prime ideal.
The Krull dimension counts the longest staircase of prime ideals, each strictly inside the next.
In $k[x, y]$ the staircase $(0) \subset (x) \subset (x, y)$ goes from the whole plane, to a line, to a point, and has $2$ steps.
