---
tag: G9WB27VWP7
kind: concept
name: Coordinate ring
msc: [14A10, 14A05]
sources:
  - url: https://en.wikipedia.org/wiki/Affine_variety
---

## Summary

The coordinate ring of an algebraic set $X \subseteq k^n$ is the ring of polynomial functions on $X$.
It is the quotient of the polynomial ring by the ideal of $X$.
It carries the geometry of $X$: points, closed subsets and morphisms of affine varieties are read off from it.
Also $X$ is irreducible exactly when this ring is an integral domain.

## Explanations

### L1 human

On a set of points cut out by equations, two polynomials give the same function when their difference vanishes there.
The coordinate ring is the ring of these functions.
On the circle $x^2 + y^2 = 1$, the polynomials $x^2$ and $1 - y^2$ give the same function, so they are equal in the coordinate ring.
On the $x$-axis, every polynomial in $x$ and $y$ agrees with a polynomial in $x$ alone, so the coordinate ring is just $k[x]$.
