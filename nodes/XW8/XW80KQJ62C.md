---
tag: XW80KQJ62C
kind: definition
name: Conformal geometry
msc: [53C18, 51B10]
defines: GTVQFG2SH9
uses: [F45VQ47GPV, Q61VFHCH2J, 0KZZ70ZHXP, 0YYT36R4YD]
sources:
  - url: https://en.wikipedia.org/wiki/Conformal_geometry
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]] of dimension $n \ge 2$.
Two [[Riemannian metrics|Q61VFHCH2J]] $g$ and $g'$ on $M$ are *conformally equivalent* when $g' = e^{2f} g$ for some smooth function $f \colon M \to \R$.
A *conformal structure* on $M$ is an equivalence class $[g]$ for this relation, and $(M, [g])$ is a *conformal manifold*.
A [[diffeomorphism|0KZZ70ZHXP]] $\varphi \colon (M, [g]) \to (N, [h])$ is *conformal* when $\varphi^* h \in [g]$.
*Conformal geometry* is the study of the properties of conformal manifolds that are invariant under conformal diffeomorphisms.

## Remarks

The angle between two tangent vectors at a point is the same for all metrics in $[g]$, so angles are defined in a conformal manifold, while lengths are not.
Accordingly, conformal diffeomorphisms are exactly the diffeomorphisms that are [[conformal maps|0YYT36R4YD]], that is, that preserve angles.
Example: stereographic projection from the north pole identifies $S^n$ minus a point with $\R^n$, and the round metric becomes $\dfrac{4}{(1 + \abs{x}^2)^2} \abs{dx}^2$.
This is $e^{2f}$ times the flat metric with $f(x) = \ln 2 - \ln(1 + \abs{x}^2)$, so the round sphere minus a point is conformally equivalent to Euclidean space.
Non-example: the map $(x, y) \mapsto (2x, y)$ of $\R^2$ pulls back $dx^2 + dy^2$ to $4\, dx^2 + dy^2$, which is not a multiple of $dx^2 + dy^2$; it does not preserve the angle between the vectors $(1, 1)$ and $(1, -1)$.
On an oriented surface, a conformal structure is the same thing as a structure of Riemann surface.
