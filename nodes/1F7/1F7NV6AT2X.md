---
tag: 1F7NV6AT2X
kind: definition
name: hp-FEM
msc: [65N30, 65N50]
defines: ZYZM357DQV
uses: [98GZ9DVHTA, Y5B0PEBKE8, M4CEZ5K9HP]
sources:
  - url: https://en.wikipedia.org/wiki/Hp-FEM
---

## Definition

Let $\Omega \subset \R^d$ be a bounded polygonal domain, and let $V$ be a [[Sobolev space|M4CEZ5K9HP]] on $\Omega$ such as $H^1_0(\Omega)$.
An *hp finite element space* is given by two data:

1. a mesh $\mathcal{T}$ of $\Omega$ into elements $K$;
2. a degree vector $p = (p_K)_{K \in \mathcal{T}}$ of positive integers.

The space $V_{\mathcal{T}, p}$ is the set of $v \in V$ whose restriction to each $K$ is a polynomial of degree at most $p_K$.
The *hp-FEM* is the [[Galerkin method|Y5B0PEBKE8]] on a sequence of such spaces.
In this sequence, both the mesh and the degree vector may change from one step to the next.

## Remarks

The $h$-version is the case of constant $p$ and finer meshes, and the $p$-version is the case of a fixed mesh and growing degrees.
Both are special cases of the [[finite element method|98GZ9DVHTA]] in this setting.

Example: on $\Omega = (0, 1)$ with a solution behaving like $x^\lambda$ near $0$, with $0 < \lambda < 1$, take a geometric mesh with nodes $0, \sigma^{n-1}, \ldots, \sigma, 1$ for some $0 < \sigma < 1$.
Take degrees that grow linearly away from $0$.
For such geometric meshes, the energy error decays exponentially in a root of the number of unknowns $N$.
In two dimensions the rate is $\exp(-b N^{1/3})$ for piecewise analytic data on polygons.

Non-example: let $V = H^1_0(\Omega)$ and take all functions that are polynomials of degree at most $p_K$ on each $K$, with no continuity across elements.
A function with a jump across an interior face is not in $H^1(\Omega)$, so this set fails the condition $v \in V$.
Such spaces are used by hp discontinuous Galerkin methods instead.
