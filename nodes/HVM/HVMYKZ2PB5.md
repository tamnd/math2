---
tag: HVMYKZ2PB5
kind: definition
name: Algebraic group
msc: [14L10, 14L15, 20G15]
defines: GH81SYAPPN
uses: [TJ04VQP4NB, AHTE5DVX61]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_group
---

## Definition

Let $k$ be a field.
An *algebraic group* over $k$ is a [[group scheme|TJ04VQP4NB]] $G$ over $k$ whose underlying scheme is [[of finite type|AHTE5DVX61]] over $k$.
So $G$ comes with morphisms $m \colon G \times_k G \to G$, $i \colon G \to G$ and $e \colon \operatorname{Spec} k \to G$.
They satisfy associativity, the unit law and the inverse law as identities of morphisms.

## Remarks

Many authors also require $G$ to be smooth, or to be a variety; such groups are called group varieties.
Over a field of characteristic $0$, every algebraic group is smooth.

Example: the general linear group $\mathrm{GL}_n = \operatorname{Spec} k[x_{ij}, 1/\det]$, with matrix multiplication and the inverse matrix.
The entries of a product and of an inverse are polynomials in the $x_{ij}$ and $1/\det$, so these are morphisms, and the group axioms hold.

Non-example: the constant group scheme $\Z_k = \coprod_{n \in \Z} \operatorname{Spec} k$ is a group scheme over $k$.
It has infinitely many connected components, so it is not of finite type over $k$.

The group of points $G(k)$ is an abstract group, and $T \mapsto G(T)$ is a functor from $k$-schemes to groups.
