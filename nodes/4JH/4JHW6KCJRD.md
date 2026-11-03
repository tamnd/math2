---
tag: 4JHW6KCJRD
kind: definition
name: Congruence of geodesics
msc: ["53C50", "83C10"]
defines: CWHM6AV4G3
uses: [BY4QYYS788, NSYMQMHPDN, 5FZDQQHQKM, RNRTS8WWNM, G49G4R1K04, TWXJH5ZEHA]
sources:
  - url: https://en.wikipedia.org/wiki/Congruence_(general_relativity)
---

## Definition

Let $(M, g)$ be a [[Lorentzian manifold|BY4QYYS788]] of dimension $4$ with Levi-Civita [[covariant derivative|5FZDQQHQKM]] $\nabla$, and let $U \subseteq M$ be open.
A *congruence* on $U$ is the family of integral curves of a smooth nowhere-vanishing vector field on $U$.
Through each point of $U$ passes exactly one curve of the family.
A *congruence of timelike geodesics* on $U$ is the family of integral curves of a smooth vector field $u$ on $U$ such that

1. $g(u, u) = -1$, so the curves are timelike and parametrized by proper time;
2. $\nabla_u u = 0$, so each curve is a [[geodesic|NSYMQMHPDN]].

## Remarks

For such a congruence set $B_{ab} = \nabla_b u_a$ and $h_{ab} = g_{ab} + u_a u_b$, the metric on vectors orthogonal to $u$.
Then $B_{ab} u^a = B_{ab} u^b = 0$, and $B_{ab}$ splits into the *expansion* $\theta = \nabla_a u^a$, the *shear* $\sigma_{ab} = B_{(ab)} - \frac13 \theta h_{ab}$ and the *rotation* $\omega_{ab} = B_{[ab]}$, with $B_{ab} = \frac13 \theta h_{ab} + \sigma_{ab} + \omega_{ab}$.
The rotation vanishes exactly when $u$ is orthogonal to a family of hypersurfaces.
Congruences of null geodesics are defined in the same way with $g(u, u) = 0$, using a two-dimensional transverse space.

Example: in [[Minkowski space|G49G4R1K04]], inside the future light cone of the origin, let $\tau = \sqrt{-x_\mu x^\mu}$ and $u^\mu = x^\mu / \tau$.
The curves are straight lines through the origin, so they are geodesics, and $g(u, u) = x_\mu x^\mu / \tau^2 = -1$.
Here $\theta = \partial_\mu u^\mu = 4/\tau + x^\mu x_\mu / \tau^3 = 3/\tau$, so this congruence of [[free-fall world lines|RNRTS8WWNM]] expands.

Non-example: the world lines of uniformly accelerated observers in [[Rindler coordinates|TWXJH5ZEHA]] form a congruence of timelike curves with $g(u, u) = -1$.
But $\nabla_u u \ne 0$, so clause 2 fails and it is not a congruence of geodesics.
