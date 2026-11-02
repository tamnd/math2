---
tag: FS9FRJ17D2
kind: concept
name: Homogeneous coordinates
msc: [51N15, 14N05]
sources:
  - url: https://en.wikipedia.org/wiki/Homogeneous_coordinates
same_as:
  wikidata: Q528525
  wikipedia: Homogeneous coordinates
---

## Summary

Homogeneous coordinates describe a point of the [[projective space|ZT9A6JK8QF]] $\mathbb{P}^n$ by $n + 1$ numbers, not all zero, taken up to a common nonzero factor.
They turn points at infinity into ordinary tuples, so that projective geometry can be done with linear algebra.
Projective transformations become matrices, and curves become zero sets of homogeneous polynomials.
They are standard in computer graphics, where translations and perspective become matrix products.

## Explanations

### L1 human

A point $(x, y)$ of the plane gets three coordinates $[x : y : 1]$, and any multiple such as $[2x : 2y : 2]$ names the same point.
To go back, divide by the last coordinate.
Triples with last coordinate $0$, such as $[1 : 1 : 0]$, cannot be divided back: they are the points at infinity, one for each direction of lines.
So the lines $y = x$ and $y = x + 1$, which are parallel, meet at $[1 : 1 : 0]$.
