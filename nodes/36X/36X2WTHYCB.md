---
tag: 36X2WTHYCB
kind: concept
name: Dimension of an algebraic variety
msc: [14A10, 13C15]
sources:
  - url: https://en.wikipedia.org/wiki/Dimension_of_an_algebraic_variety
same_as:
  wikidata: Q5277261
  wikipedia: Dimension of an algebraic variety
---

## Summary

The dimension of an algebraic variety is the length of the longest chain of nested irreducible closed subsets in it.
For an affine variety it equals the Krull dimension of the coordinate ring.
For any variety it equals the transcendence degree of the function field over the base field.
These different descriptions agree, which makes dimension one of the most robust invariants in algebraic geometry: points have dimension $0$, curves $1$, surfaces $2$.

## Explanations

### L1 human

Inside a surface, a chain of ever smaller irreducible pieces can go surface, then a curve on it, then a point on that curve.
That chain has two steps, and the surface has dimension $2$.
Another way to see it is to count how many coordinates can be chosen freely.
On the sphere $x^2 + y^2 + z^2 = 1$ over $\C$, two coordinates are free, and then the third has at most two possible values.
So the sphere is a surface, of dimension $2$.
