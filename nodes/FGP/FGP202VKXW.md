---
tag: FGP202VKXW
kind: definition
name: Holomorphic vector bundle
msc: [32L05, 32L10]
defines: TKA958Z4KZ
uses: [JSGWAN2RJV, P4DZM975BV, 3MQTWKBBBT]
sources:
  - url: https://en.wikipedia.org/wiki/Holomorphic_vector_bundle
---

## Definition

Let $X$ be a [[complex manifold|JSGWAN2RJV]] and let $r \ge 0$ be an integer.
A *holomorphic vector bundle* of rank $r$ over $X$ is a complex manifold $E$ with a [[holomorphic map|3MQTWKBBBT]] $\pi \colon E \to X$ such that:

1. Each fibre $E_x = \pi^{-1}(x)$ has the structure of a complex vector space of dimension $r$.
2. Each point of $X$ has an open neighbourhood $U$ and a biholomorphic map $\varphi \colon \pi^{-1}(U) \to U \times \C^r$ with $\mathrm{pr}_1 \circ \varphi = \pi$.
3. For each $x \in U$, the restriction $\varphi \colon E_x \to \set{x} \times \C^r$ is $\C$-linear.

## Remarks

Given two such trivializations $\varphi_i$ over $U_i$ and $\varphi_j$ over $U_j$, one has $\varphi_i \circ \varphi_j^{-1}(x, v) = (x, g_{ij}(x) v)$ with $g_{ij} \colon U_i \cap U_j \to GL_r(\C)$ holomorphic.
Conversely, holomorphic maps $g_{ij}$ with $g_{ij} g_{jk} = g_{ik}$ on triple overlaps glue the products $U_i \times \C^r$ to a holomorphic vector bundle.
A holomorphic vector bundle is in particular a smooth complex [[vector bundle|P4DZM975BV]].

Example: the holomorphic tangent bundle $T X$ of a complex manifold of dimension $n$ has rank $n$.
A holomorphic chart $z = (z_1, \dots, z_n)$ trivializes it by the frame $\partial/\partial z_1, \dots, \partial/\partial z_n$.
The transition functions are the complex Jacobian matrices of the coordinate changes, which are holomorphic.

Non-example: cover the Riemann sphere by $U_0 = \C$ and $U_1 = \mathbb{P}^1 \setminus \set{0}$, and glue $U_0 \times \C$ and $U_1 \times \C$ over $\C^*$ with $g_{01}(z) = \bar z$.
This gives a smooth complex line bundle, but $g_{01}$ is not holomorphic.
So the trivializations of this atlas are not biholomorphic for any complex structure on the glued space, and clause 2 fails for them.

The sheaf of holomorphic sections of $E$ is a locally free sheaf of $\mathcal{O}_X$-modules of rank $r$, and every such sheaf arises in this way.
