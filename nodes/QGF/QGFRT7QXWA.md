---
tag: QGFRT7QXWA
kind: definition
name: Linear algebraic group
msc: [20G15, 14L17]
defines: GA81VVQHEP
uses: [GH81SYAPPN, B3V3XJ2W8G, 0FCHE902D7]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_algebraic_group
---

## Definition

Let $k$ be a field.
A *linear algebraic group* over $k$ is an [[algebraic group|GH81SYAPPN]] $G$ over $k$ whose underlying scheme is [[affine|B3V3XJ2W8G]].

## Remarks

Every linear algebraic group over $k$ is isomorphic to a closed subgroup scheme of $\mathrm{GL}_n$ for some $n$.
So an equivalent definition is: a closed subgroup scheme of some [[general linear group|0FCHE902D7]] $\mathrm{GL}_n$.
In the classical language, with $k$ algebraically closed, it is a subgroup of $\mathrm{GL}_n(k)$ that is the zero set of a set of polynomials in the matrix entries.
Many authors also require $G$ to be smooth.

Example: $\mathrm{SL}_n = \operatorname{Spec} k[x_{ij}] / (\det - 1)$.
It is a closed subgroup of $\mathrm{GL}_n$, cut out by $\det = 1$, so it is affine.

Non-example: an elliptic curve $E$ over $k$ is an algebraic group, but it is projective of positive dimension and so not affine.
