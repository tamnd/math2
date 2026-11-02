---
tag: 99RQHAGNW1
kind: definition
name: Isometry of Riemannian manifolds
msc: [53C20, 53B20]
defines: R9YWQS15AA
uses: [7CBT4SM83Y, 0KZZ70ZHXP, 6P9PXQDSEN]
sources:
  - url: https://en.wikipedia.org/wiki/Isometry
---

## Definition

Let $(M, g)$ and $(N, h)$ be [[Riemannian manifolds|7CBT4SM83Y]].
Let $\varphi \colon M \to N$ be a [[diffeomorphism|0KZZ70ZHXP]], and let $d\varphi_p$ be its [[differential|6P9PXQDSEN]] at $p \in M$.
The map $\varphi$ is an *isometry* from $(M, g)$ to $(N, h)$ if, for all $p \in M$ and all $v, w \in T_pM$,
$$h_{\varphi(p)}\bigl(d\varphi_p(v), d\varphi_p(w)\bigr) = g_p(v, w).$$
Equivalently, $\varphi^* h = g$.

## Remarks

Example: let $A \in O(n + 1)$ be an orthogonal matrix.
The map $x \mapsto Ax$ restricts to a diffeomorphism of the unit sphere $S^n$ with differential $v \mapsto Av$.
Since $\ip{Av}{Aw} = \ip{v}{w}$, it is an isometry of the round sphere.

Non-example: the map $x \mapsto 2x$ of $\R^n$ is a diffeomorphism, but $\ip{2v}{2w} = 4 \ip{v}{w}$, so it does not preserve the metric.

Let $M$ and $N$ have the same dimension.
A smooth map $\varphi$ with $\varphi^* h = g$, not required to be a diffeomorphism, is a local isometry.
The covering map $\R \to S^1$, $t \mapsto (\cos t, \sin t)$, is an example.
An isometry preserves the [[Riemannian distance|B4QR306D8G]]; conversely, by the [[Myers–Steenrod theorem|Z3VRMW8ETQ]], a distance-preserving bijection between connected Riemannian manifolds is an isometry in this sense.
