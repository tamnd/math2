---
tag: 5HDG31YEPW
kind: definition
name: Riemannian manifold
msc: [53C20, 53B20]
defines: 7CBT4SM83Y
uses: [F45VQ47GPV, Q61VFHCH2J]
sources:
  - url: https://en.wikipedia.org/wiki/Riemannian_manifold
---

## Definition

A *Riemannian manifold* is a pair $(M, g)$ where $M$ is a [[smooth manifold|F45VQ47GPV]] and $g$ is a [[Riemannian metric|Q61VFHCH2J]] on $M$.
An isometry between Riemannian manifolds $(M, g)$ and $(N, h)$ is a diffeomorphism $\varphi : M \to N$ with $\varphi^* h = g$.

## Remarks

Example: the unit sphere $S^n \subset \R^{n+1}$ with $g_p(u, v) = u \cdot v$ for $u, v \in T_pS^n \subset \R^{n+1}$ is a Riemannian manifold.
Indeed $g_p$ is the restriction of the dot product, so it is symmetric and positive definite, and it depends smoothly on $p$.
More generally, every immersed submanifold of $\R^N$ is a Riemannian manifold with the induced metric, and by the Nash embedding theorem every Riemannian manifold arises this way.
Non-example: $\R^2$ with $g = dx^2 - dy^2$ is not a Riemannian manifold, because $g(\partial_y, \partial_y) = -1 < 0$; it is a pseudo-Riemannian manifold.
A connected Riemannian manifold is a metric space, with distance the infimum of the lengths of piecewise smooth curves joining two points, and this metric induces the manifold topology.
