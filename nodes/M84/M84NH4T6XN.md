---
tag: M84NH4T6XN
kind: concept
name: Embedded submanifold with boundary
msc: [57R40, 58A05]
uses: [7DS6B2BFK8, VKFW27WXEZ, 6P9PXQDSEN, 0JGB7A6GTS]
sources:
  - url: https://github.com/jirilebl/scv/blob/78d7d41554695c389552c301398803d4633b9208/scv.tex#L18087
    locator: scv.tex:18087
---

## Summary

Let $\mathbb{H}^k = \{x \in \mathbb{R}^k : x_k \geq 0\}$ be the closed half-space. Give a subset $M \subset \mathbb{R}^n$ the subspace topology. Then $M$ is an embedded submanifold with boundary of dimension $k$ if every point $p \in M$ has a chart of the following kind.

There is an open neighborhood $W$ of $p$ in $\mathbb{R}^n$, a point $q \in \mathbb{H}^k$ and a neighborhood $U$ of $q$ in $\mathbb{H}^k$. There is also a smooth injective map $\varphi \colon U \to M$ with these properties:

- $\varphi(q) = p$.
- $\varphi$ is open onto $M$: the image of each open subset of $U$ is relatively open in $M$.
- The [[differential|6P9PXQDSEN]] of $\varphi$ has [[rank|0JGB7A6GTS]] $k$ at every point of $U$.
- $\varphi(U) = M \cap W$.

Such a map $\varphi$ is a local parametrization. A point $p = \varphi(q)$ with $q_k = 0$ is a boundary point. The set of boundary points is written $\partial M$. When $\partial M$ is empty, $M$ is called an embedded submanifold. This is the version of a [[submanifold|VKFW27WXEZ]] with boundary inside $\mathbb{R}^n$, in the spirit of a [[manifold with boundary|7DS6B2BFK8]].
