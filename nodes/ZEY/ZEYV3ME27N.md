---
tag: ZEYV3ME27N
kind: definition
name: Cosmological principle
msc: ["83F05"]
defines: Q8MSCRDFAT
uses: [BY4QYYS788, 63ZKC7AFX2, 02HPP5VCZH]
sources:
  - url: https://en.wikipedia.org/wiki/Cosmological_principle
---

## Definition

Let $(M, g)$ be a [[spacetime|63ZKC7AFX2]], that is, a time-oriented four-dimensional [[Lorentzian manifold|BY4QYYS788]].
Let $u$ be a unit timelike vector field on $M$, the velocity of a family of observers.
Let $(\Sigma_t)_{t \in I}$ be a foliation of $M$ by spacelike hypersurfaces orthogonal to $u$.
The spacetime satisfies the *cosmological principle* with respect to $u$ and $(\Sigma_t)$ when it is spatially homogeneous and isotropic in the following sense.

1. Homogeneity: for each $t \in I$ and all points $p, q \in \Sigma_t$, there is an [[isometry|02HPP5VCZH]] of $(M, g)$ that maps $\Sigma_t$ onto itself and maps $p$ to $q$.
2. Isotropy: let $p \in M$, and let $v, w \in T_p M$ be unit vectors orthogonal to $u_p$.
   Then there is an isometry of $(M, g)$ that fixes $p$, maps $u$ to $u$, and has differential sending $v$ to $w$.

## Remarks

Minkowski space with $u = \partial_t$ and the slices $t = \text{const}$ satisfies both clauses: translations in space give homogeneity, and rotations about a point give isotropy.
The Schwarzschild spacetime fails homogeneity: the curvature invariant $R_{abcd}R^{abcd}$ depends on the radius, so no isometry maps a point near the centre to a point far away.
Isotropy about every point already implies homogeneity.
Under these two clauses each slice $\Sigma_t$, with its induced metric, has constant sectional curvature, and the metric takes the [[Friedmann–Lemaître–Robertson–Walker|ECJMS4VDTF]] form.
