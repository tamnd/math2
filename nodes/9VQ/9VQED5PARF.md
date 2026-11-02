---
tag: 9VQED5PARF
kind: definition
name: Symmetric space
msc: [53C35]
defines: PAA93R4WYD
uses: [7CBT4SM83Y, R9YWQS15AA, 6P9PXQDSEN]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_space
---

## Definition

Let $(M, g)$ be a connected [[Riemannian manifold|7CBT4SM83Y]].
The manifold $M$ is a *(Riemannian globally) symmetric space* if each point $p \in M$ has an [[isometry|R9YWQS15AA]] $s_p \colon M \to M$ with two properties.
The map $s_p$ satisfies $s_p(p) = p$, and its [[differential|6P9PXQDSEN]] $(ds_p)_p \colon T_p M \to T_p M$ equals $-\id$.
The map $s_p$ is the *geodesic symmetry* at $p$.

## Remarks

Example: the unit sphere $S^n \subset \R^{n+1}$ with the induced metric.
For $p \in S^n$ put $s_p(x) = 2 \ip{x}{p} p - x$.
It is the restriction of a linear orthogonal map, so it is an isometry of $S^n$; it fixes $p$; and on $T_p S^n = p^\perp$ it acts as $v \mapsto -v$.

Non-example: a closed surface of genus $2$ with a metric of constant curvature $-1$.
Its isometry group is finite, so it does not act transitively on the surface.
A symmetric space is homogeneous, since $s_q$, for $q$ the midpoint of a shortest geodesic from $p$ to $p'$, swaps $p$ and $p'$; so the surface is not symmetric.
It is *locally* symmetric: its curvature tensor is parallel.

A symmetric space is complete, and $s_p$ is unique: it maps $\exp_p(v)$ to $\exp_p(-v)$.
Let $G$ be the identity component of the isometry group and $K$ the stabilizer of a point; then $M = G/K$.
Conjugation by $s_p$ gives an involution $\sigma$ of $G$, and its fixed point group satisfies $(G^\sigma)_0 \subseteq K \subseteq G^\sigma$.
