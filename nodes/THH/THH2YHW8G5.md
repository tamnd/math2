---
tag: THH2YHW8G5
kind: concept
name: Hartogs domain
msc: [32Q02, 32D05]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudoconvexity
---

## Summary

A Hartogs domain is a domain in $\C^n$ that is unchanged when the last coordinate is rotated about the origin.
Such domains are described by the radii of their circles in the last variable over each point of the remaining variables.
They are the standard testing ground for extension phenomena and for convexity notions in several complex variables.
Every [[Reinhardt domain|WA0SE56FVH]] is a Hartogs domain.

## Explanations

### L1 human

Fix the first $n - 1$ coordinates and look at the slice of the domain in the last coordinate.
For a Hartogs domain every such slice is a union of circles centred at $0$, so it is a disc, an annulus, or a union of such rings.
A typical example in $\C^2$ is $\set{(z, w) : \abs{z} < 1, \ \abs{w} < e^{-\varphi(z)}}$ for a continuous function $\varphi$ on the unit disc.
Its slices are discs whose radius $e^{-\varphi(z)}$ varies with $z$.
Such a domain is pseudoconvex exactly when $\varphi$ is [[subharmonic|Z1MHMGFNFW]], which makes these domains very convenient for building examples.
