---
tag: E7A5DHFT01
kind: concept
name: Zariski tangent space
msc: [14A10, 14B05]
sources:
  - url: https://en.wikipedia.org/wiki/Zariski_tangent_space
same_as:
  wikidata: Q2031596
  wikipedia: Zariski tangent space
---

## Summary

The Zariski tangent space of a variety at a point is the linear space of directions in which the defining equations vanish to first order.
For a variety in $k^n$ it is the kernel of the Jacobian matrix of the defining polynomials at the point.
Intrinsically it is the dual of $\mathfrak m / \mathfrak m^2$, where $\mathfrak m$ is the maximal ideal of the point.
Its dimension is at least the dimension of the variety, with equality exactly at the nonsingular points.

## Explanations

### L1 human

Near a point, replace each defining equation by its best linear approximation, its differential at the point.
The common solutions of these linear equations form the tangent space.
For the circle $x^2 + y^2 = 1$ at $(1, 0)$, the differential is $2x \, dx + 2y \, dy = 2 \, dx$, so the tangent space is the vertical line $dx = 0$.
For the cusp $y^2 = x^3$ at the origin, all the differentials vanish, so the tangent space is the whole plane, larger than the curve's dimension $1$.
