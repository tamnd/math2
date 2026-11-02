---
tag: PAX9SHDHDW
kind: concept
name: Minkowski functional
msc: [46A03, 52A07]
sources:
  - url: https://en.wikipedia.org/wiki/Minkowski_functional
same_as:
  wikidata: Q649472
  wikipedia: Minkowski functional
---

## Summary

The Minkowski functional, or gauge, of an [[absorbing set|NM1BCK3ZX9]] $K$ in a vector space is a function on the space.
Its value at $x$ is the smallest factor by which $K$ must be scaled to contain $x$.
For convex sets it is sublinear, and for convex [[balanced|2TDSHJJYS4]] sets it is a [[seminorm|FP5GVCN8GV]].
It is the bridge between convex neighbourhoods of $0$ and seminorms, and so it is the main tool for describing [[locally convex spaces|B6GY2KJMWW]] by seminorms.

## Explanations

### L1 human

Take a convex shape around the origin, for example a disc or a square.
To measure a point $x$, blow up or shrink the shape until its boundary just reaches $x$; the scaling factor is the gauge of $x$.
If the shape is the unit disc, the gauge is the ordinary length.
If the shape is the square $[-1, 1]^2$, the gauge of $(x, y)$ is $\max(\abs{x}, \abs{y})$.
So every symmetric convex shape gives its own way of measuring size.
