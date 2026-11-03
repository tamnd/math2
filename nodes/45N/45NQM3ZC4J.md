---
tag: 45NQM3ZC4J
kind: definition
name: Gibbons–Hawking–York boundary term
msc: ["83C05", "49S05"]
defines: SAAB5S5A0D
uses: [GH6CXWFNDJ, JPE3A1SN7V, 9KHQR16P1B, PA78NFEPCF]
sources:
  - url: https://en.wikipedia.org/wiki/Gibbons%E2%80%93Hawking%E2%80%93York_boundary_term
---

## Definition

Let $(M, g)$ be an $n$-dimensional Lorentzian or Riemannian [[pseudo-Riemannian manifold|GH6CXWFNDJ]] with smooth boundary $\partial M$.
Assume that the induced metric $h$ on $\partial M$ is nondegenerate, so $\partial M$ is nowhere null.
Let $n^\mu$ be the outward unit normal to $\partial M$ and let $\varepsilon = g(n, n) \in \set{-1, +1}$.
Let $K = \nabla_\mu n^\mu$ be the trace of the extrinsic curvature ([[second fundamental form|9KHQR16P1B]]) of $\partial M$.
The *Gibbons–Hawking–York boundary term* is
$$S_{\mathrm{GHY}} = \frac{1}{8\pi G} \oint_{\partial M} \varepsilon K \sqrt{\abs{\det h}} \, d^{n-1}y,$$
where $G$ is the gravitational constant, units have $c = 1$, and $y$ are coordinates on $\partial M$.

## Remarks

The total action $S = \frac{1}{16\pi G}\int_M R \sqrt{\abs{\det g}}\, d^n x + S_{\mathrm{GHY}}$, with $R$ the scalar curvature, has a stationary point exactly at the solutions of the vacuum Einstein equations among metrics with $\delta g = 0$ on $\partial M$.
For the [[Einstein–Hilbert action|JPE3A1SN7V]] alone, the variation leaves a boundary integral with normal derivatives of $\delta g$, which do not vanish under this boundary condition.

Example: let $M$ be the closed ball of radius $r$ in Euclidean $\R^3$.
The outward normal is $n = x / \abs{x}$, so $\varepsilon = 1$ and $K = \nabla \cdot n = 2/r$ on the sphere $\abs{x} = r$.
The boundary has area $4\pi r^2$, so $S_{\mathrm{GHY}} = \frac{1}{8\pi G} \cdot \frac{2}{r} \cdot 4\pi r^2 = r/G$.

Non-example: a region of Minkowski space bounded by part of a light cone has a null boundary piece.
There $h$ is degenerate and the normal cannot be normalised, so the term above is not defined; null boundaries need a different boundary term.

Often $K$ is written as $K = h^{ab} K_{ab}$, the trace of the extrinsic curvature tensor $K_{ab}$; it is $n - 1$ times the [[mean curvature|PA78NFEPCF]] when the mean curvature is taken as an average.
Sign conventions for $K$ and $\varepsilon$ vary between authors.
