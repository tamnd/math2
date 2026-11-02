---
tag: ZP55RF3A0C
kind: concept
name: Uniform algebra
msc: [46J10, 46J05]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_algebra
same_as:
  wikidata: Q7885096
  wikipedia: Uniform algebra
---

## Summary

A uniform algebra is a closed subalgebra of the continuous complex functions on a compact Hausdorff space that contains the constants and separates points.
It is a commutative Banach algebra with the sup norm.
The main examples come from complex analysis, such as the disc algebra of functions holomorphic inside the disc and continuous up to the boundary.
The [[Stone–Weierstrass theorem|1P8D3MK79H]] says the only uniform algebra on $X$ closed under complex conjugation is $C(X)$ itself.
So the theory of uniform algebras studies the closed subalgebras that are not closed under conjugation.

## Explanations

### L1 human

Start with all continuous functions on a compact space, measured by their largest absolute value.
A uniform algebra is a smaller family that is still closed under sums, products and uniform limits, contains the constants, and can tell any two points apart.
The polynomials in $z$ on the closed unit disc, together with all their uniform limits, form such a family.
It is smaller than all continuous functions: $\overline{z}$ is not a uniform limit of polynomials in $z$.
