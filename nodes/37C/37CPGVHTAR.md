---
tag: 37CPGVHTAR
kind: definition
name: Abelian variety
msc: [14K05, 11G10]
defines: R7W03TXRS9
uses: [GH81SYAPPN, HV6YBS0YDH, 9537RKBZPP]
sources:
  - url: https://en.wikipedia.org/wiki/Abelian_variety
---

## Definition

Let $k$ be a field.
An *abelian variety* over $k$ is an [[algebraic group|GH81SYAPPN]] $A$ over $k$ such that:

1. $A$ is a geometrically integral [[variety|HV6YBS0YDH]] over $k$;
2. $A$ is complete, that is, the structure morphism $A \to \operatorname{Spec} k$ is [[proper|9537RKBZPP]].

Here the group structure is given by a multiplication morphism $m \colon A \times_k A \to A$, an inverse morphism $i \colon A \to A$ and a unit point $e \in A(k)$ that satisfy the group axioms.

## Remarks

Example: an elliptic curve $E$ over $k$, with its chord-and-tangent group law and the point at infinity as unit, is an abelian variety of dimension $1$.
It is a smooth projective curve, so it is geometrically integral and complete, and the group law is given by morphisms.

Non-example: the multiplicative group $\mathbb{G}_m = \operatorname{Spec} k[t, t^{-1}]$ is a geometrically integral algebraic group, but it is not complete.
It is an open subset of the projective line, and it is affine of positive dimension, so it is not proper over $k$.

The following three facts follow from the definition and are not part of it.
The group law of an abelian variety is commutative, so it is often written additively.
Every abelian variety is projective.
An abelian variety is smooth over $k$, since it is a geometrically reduced group variety.
