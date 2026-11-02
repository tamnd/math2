---
tag: V2AA2D23JC
kind: definition
name: Banach–Lie group
msc: ["22E65", 58B25]
defines: MC5CGVRFJM
uses: [VB95VVVDM8, G5S1M9, 0BDTTM24DP]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_group
---

## Definition

A *Banach–Lie group* is a [[group|G5S1M9]] $G$ with the structure of a smooth [[Banach manifold|VB95VVVDM8]] such that:

1. The multiplication $G \times G \to G$, $(g, h) \mapsto g h$, is smooth.
2. The inversion $G \to G$, $g \mapsto g^{-1}$, is smooth.

## Remarks

Example: let $E$ be a real [[Banach space|0BDTTM24DP]] and $\mathcal{L}(E)$ the Banach space of bounded linear operators with the operator norm.
The group $GL(E)$ of invertible operators is an open subset of $\mathcal{L}(E)$, so it is a Banach manifold with one chart.
Multiplication is the restriction of a continuous bilinear map, hence smooth, and inversion is smooth because near $A$ it is given by the convergent series $(A - X)^{-1} = \sum_{k \ge 0} (A^{-1} X)^k A^{-1}$.

Non-example: on $\R$ with its standard smooth structure, define $x * y = (x^{1/3} + y^{1/3})^3$.
This is a group, isomorphic to $(\R, +)$ through $x \mapsto x^{1/3}$, but the partial derivative of $x * y$ in $x$ at the point $(0, 1)$ does not exist, so clause 1 fails.

The tangent space at the identity carries a Lie bracket and is a Banach–Lie algebra.
Every finite-dimensional Lie group is a Banach–Lie group.
