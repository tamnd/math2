---
tag: 2GFFGE6WK1
kind: definition
name: Mean curvature flow
msc: ["53E10", 35K55]
defines: 2YYV01C7QQ
uses: [PA78NFEPCF, 0WQJJCCTC8, F45VQ47GPV]
sources:
  - url: https://en.wikipedia.org/wiki/Mean_curvature_flow
---

## Definition

Let $M$ be a smooth $n$-dimensional [[manifold|F45VQ47GPV]] and let $T > 0$.
A *mean curvature flow* is a smooth map $F \colon M \times [0, T) \to \R^{n+1}$ such that:

1. for each $t \in [0, T)$, the map $F_t = F(\cdot, t)$ is an immersion of $M$ as a hypersurface;
2. $\partial_t F(p, t) = \vec{H}(p, t)$ for all $p \in M$ and $t \in [0, T)$.

Here $\vec{H}(p, t) = -H \nu$ is the mean curvature vector of $F_t$ at $p$.
The vector $\nu$ is a unit [[normal vector|0WQJJCCTC8]], and $H$ is the [[mean curvature|PA78NFEPCF]], the sum of the principal curvatures with respect to $\nu$.

## Remarks

Example: let $F(p, t) = R(t)\, p$ for $p$ in the unit sphere $S^n \subset \R^{n+1}$, with $R(t) = \sqrt{R_0^2 - 2nt}$.
The sphere of radius $R$ has mean curvature vector of length $n/R$ pointing to the centre, so the flow condition is $R'(t) = -n/R(t)$.
This holds since $\frac{d}{dt} R^2 = -2n$, and the flow exists until $T = R_0^2/(2n)$.
Non-example: $R(t) = R_0 + t$ moves the sphere outward, against the mean curvature vector, so it fails clause 2.
A plane or any minimal hypersurface, with $\vec H = 0$, is a stationary flow.
Sign conventions for $H$ and $\nu$ vary, but $\vec H$ always points toward the centre of a round sphere.
