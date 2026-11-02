---
tag: 52GCNZ1MZ8
kind: definition
name: Hermitian symmetric space
msc: [32M15, 53C35]
defines: NT4797Z9H8
uses: [PAA93R4WYD, CK1DCPC3D3, 9SYWRGVTRS, R9YWQS15AA]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_symmetric_space
---

## Definition

Let $(M, g)$ be a connected [[Hermitian manifold|CK1DCPC3D3]].
So $M$ is a complex manifold with integrable [[almost complex structure|9SYWRGVTRS]] $J$.
The Riemannian metric $g$ satisfies $g(JX, JY) = g(X, Y)$ for all tangent vectors $X, Y$.
The manifold $M$ is a *Hermitian symmetric space* if each point $p \in M$ has an [[isometry|R9YWQS15AA]] $s_p \colon M \to M$ with three properties.

1. $s_p$ is holomorphic.
2. $s_p \circ s_p = \id$.
3. $p$ is an isolated fixed point of $s_p$.

## Remarks

Conditions 2 and 3 force $(ds_p)_p = -\id$, so $(M, g)$ is a Riemannian [[symmetric space|PAA93R4WYD]] and $s_p$ is its geodesic symmetry.
The metric $g$ is then Kähler.

Example: the unit disc $D = \set{z \in \C : \abs{z} < 1}$ with the metric $\frac{4\,\abs{dz}^2}{(1 - \abs{z}^2)^2}$.
At $0$ take $s_0(z) = -z$: it is holomorphic, an isometry, an involution, and $0$ is its only fixed point.
The holomorphic isometries $z \mapsto e^{i t} \frac{z - a}{1 - \bar a z}$ act transitively, and conjugating $s_0$ by them gives $s_p$ at every point $p$.

Non-example: the round sphere $S^4$ is a Riemannian symmetric space, but it has no almost complex structure at all, so it is not a Hermitian symmetric space.

Each simply connected Hermitian symmetric space is a product of a flat part $\C^k$ and irreducible ones of compact type, such as $\C P^n$, and of noncompact type, such as $D$.
