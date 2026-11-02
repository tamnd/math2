---
tag: ZT9A6JK8QF
kind: concept
name: Projective space
msc: [14N05, 51N15]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_space
same_as:
  wikidata: Q877775
  wikipedia: Projective space
---

## Summary

The projective space $\mathbb{P}^n$ over a field $k$ is the set of lines through the origin in $k^{n+1}$.
A point is written in homogeneous coordinates $[x_0 : \dots : x_n]$, defined up to a common nonzero factor.
Projective space adds points at infinity to affine space.
Then, for example, any two distinct lines in the projective plane meet in exactly one point.
It is the ambient space of projective varieties, the compact objects of algebraic geometry.

## Explanations

### L1 human

Stand at the origin of $k^{n+1}$ and look out: each direction you can look in is one point of $\mathbb{P}^n$.
The points $(1, 2, 3)$ and $(2, 4, 6)$ lie on the same line through the origin, so they give the same point $[1 : 2 : 3]$ of the projective plane.
The points with $x_0 \ne 0$ can be scaled to $[1 : a_1 : \dots : a_n]$ and form a copy of $k^n$.
The remaining points, with $x_0 = 0$, are the points at infinity, where parallel lines of $k^n$ meet.
