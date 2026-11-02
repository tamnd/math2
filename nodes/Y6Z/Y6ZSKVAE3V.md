---
tag: Y6ZSKVAE3V
kind: concept
name: Injectivity radius
msc: [53C22, 53C20]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_Riemannian_and_metric_geometry
---

## Summary

Let $p$ be a point of a [[Riemannian manifold|7CBT4SM83Y]].
Its injectivity radius at $p$ is the largest $r$ such that the [[exponential map|Y7Z0AGY1A7]] at $p$ is a diffeomorphism on the $r$-ball in $T_pM$.
Within this radius, [[normal coordinates|RRHKMGNKG9]] at $p$ exist and each point is joined to $p$ by a unique shortest geodesic.
The injectivity radius of the whole manifold is the infimum over all points.
Lower bounds for it are a key ingredient in compactness and finiteness theorems.

## Explanations

### L1 human

From a point $p$, send out geodesics in all directions at the same speed.
For a while they spread out without meeting, and every nearby point is reached in exactly one way.
The injectivity radius is how far one can go before this breaks down.
On the unit sphere all geodesics from the north pole meet again at the south pole, at distance $\pi$, so the injectivity radius is $\pi$.
On a thin cylinder of circumference $c$, geodesics going around in opposite directions meet after distance $c/2$, so the injectivity radius is $c/2$.
