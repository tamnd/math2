---
tag: MZ6XDATQKR
kind: statement
role: theorem
name: Chevalley's structure theorem
msc: [14L10, 14K05, 20G15]
uses: [GH81SYAPPN, GA81VVQHEP, R7W03TXRS9, 0CB0DX5BVV, 0KYX2N69J0]
about: [GH81SYAPPN]
sources:
  - url: https://en.wikipedia.org/wiki/Chevalley%27s_structure_theorem
same_as:
  wikidata: Q5094298
  wikipedia: Chevalley's structure theorem
---

## Statement

Let $k$ be a perfect field.
Let $G$ be a smooth connected [[algebraic group|GH81SYAPPN]] over $k$.
Then there is a unique smooth connected [[normal subgroup|0CB0DX5BVV]] $H$ of $G$ such that:

1. $H$ is a [[linear algebraic group|GA81VVQHEP]];
2. the [[quotient|0KYX2N69J0]] $G / H$ is an [[abelian variety|R7W03TXRS9]].

## Remarks

Uniqueness is the easy part.
If $H$ and $H'$ both satisfy the conclusion, the image of $H$ in $G / H'$ is a connected linear algebraic group and also a closed subvariety of an abelian variety.
So it is both affine and complete, hence a point, and $H \subseteq H'$.
By symmetry $H = H'$.
Existence is the deep part of the theorem.

Example: let $E$ be an elliptic curve over $k$ and $G = E \times \mathbb{G}_m$.
Then $H = \set{0} \times \mathbb{G}_m$ is linear, and $G / H \cong E$ is an abelian variety.

Over imperfect fields the statement can fail, so the hypothesis that $k$ is perfect cannot simply be dropped.

## Explanations

### L1 human

Every connected algebraic group is assembled from two kinds of groups that are opposite in nature.
One kind is a group of matrices, which is affine.
The other kind is an abelian variety, which is complete.
The theorem says the matrix part sits inside as a normal subgroup, with an abelian variety as quotient.

### L2 human

The theorem reduces many questions about algebraic groups to the two separate theories of linear algebraic groups and abelian varieties.
For example, a connected algebraic group that is affine has trivial abelian quotient, and one that is complete has trivial linear part.
A standard family of examples are the generalized Jacobians of singular curves.
Such a group is an extension of the Jacobian of the normalized curve by a linear group.
