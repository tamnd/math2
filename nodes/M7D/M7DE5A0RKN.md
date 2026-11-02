---
tag: M7DE5A0RKN
kind: definition
name: Analytic index
msc: [58J20, 47A53]
defines: 44GBFZ16SG
uses: [P4DZM975BV, MT9P2X85V8, 8HWGKWD6ZM, 2V9Q4KHY1T]
sources:
  - url: https://en.wikipedia.org/wiki/Atiyah–Singer_index_theorem
---

## Definition

Let $M$ be a closed smooth manifold and let $E$, $F$ be smooth complex [[vector bundles|P4DZM975BV]] over $M$.
Let $P \colon C^\infty(M; E) \to C^\infty(M; F)$ be an [[elliptic differential operator|MT9P2X85V8]].
Then $\ker P$ and $\operatorname{coker} P = C^\infty(M; F) / P(C^\infty(M; E))$ are finite-dimensional.
The *analytic index* of $P$ is the integer
$$\operatorname{ind} P = \dim \ker P - \dim \operatorname{coker} P.$$

## Remarks

If $E$ and $F$ carry Hermitian metrics and $M$ carries a smooth positive density, then $\operatorname{coker} P$ is isomorphic to $\ker P^*$, where $P^*$ is the formal adjoint, so $\operatorname{ind} P = \dim \ker P - \dim \ker P^*$.
Let $m$ be the order of $P$ and let $H^s$ denote Sobolev spaces.
For every real $s$, the extension $P \colon H^{s}(M; E) \to H^{s - m}(M; F)$ is a [[Fredholm operator|8HWGKWD6ZM]].
Its [[Fredholm index|2V9Q4KHY1T]] equals $\operatorname{ind} P$.
The index depends only on the homotopy class of the principal symbol of $P$ through elliptic symbols.

Example: on $S^1 = \R / 2\pi\Z$, let $P = d/d\theta$ on complex functions.
The kernel is the constant functions, of dimension $1$.
The image is the functions with $\int_0^{2\pi} f \, d\theta = 0$, so the cokernel has dimension $1$, and $\operatorname{ind} P = 0$.

Non-example: the zero operator $C^\infty(S^1) \to C^\infty(S^1)$, viewed as an operator of order $1$, is not elliptic, since its principal symbol vanishes.
Its kernel and cokernel are infinite-dimensional, so it has no analytic index.
