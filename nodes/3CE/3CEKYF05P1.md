---
tag: 3CEKYF05P1
kind: definition
name: Deformation of complex structure
msc: [32G05, 14D15]
defines: VKQSM3BCE4
uses: [JSGWAN2RJV, 3MQTWKBBBT, 15XEBGNGHC, FX92PP3HZR]
sources:
  - url: https://en.wikipedia.org/wiki/Kodaira%E2%80%93Spencer_map
---

## Definition

Let $X$ be a compact [[complex manifold|JSGWAN2RJV]].
A *complex analytic family* of compact complex manifolds is a [[holomorphic map|3MQTWKBBBT]] $\varpi \colon \mathcal{X} \to B$ between connected complex manifolds such that:

1. $\varpi$ is [[proper|15XEBGNGHC]];
2. $\varpi$ is a submersion: its differential is surjective at every point of $\mathcal{X}$.

Then each fibre $X_t = \varpi^{-1}(t)$ is a compact complex manifold.
A *deformation* of $X$ is such a family together with a point $0 \in B$ and a [[biholomorphism|FX92PP3HZR]] $X \to X_0$.

## Remarks

Two deformations of $X$ over the same pointed base are isomorphic if there is a biholomorphism of the total spaces over $B$ compatible with the identifications of $X_0$ with $X$.
By Ehresmann's theorem, conditions 1 and 2 imply that $\varpi$ is a smooth fiber bundle, so all fibres are diffeomorphic to $X$.
The fibres need not be biholomorphic to each other.

Example: let $\mathbb{H}$ be the upper half-plane and let $\Z^2$ act on $\C \times \mathbb{H}$ by $(m, n) \cdot (z, \tau) = (z + m + n\tau, \tau)$.
The quotient $\mathcal{X}$ is a complex manifold, and the projection $\mathcal{X} \to \mathbb{H}$ is a proper submersion with fibre $\C / (\Z + \tau\Z)$ over $\tau$.
So it is a deformation of the elliptic curve $\C/(\Z + i\Z)$ over $(\mathbb{H}, i)$.

Non-example: remove one point from the total space $\mathcal{X}$ of the previous family.
The restricted projection is still a holomorphic submersion, but it is not proper, since one fibre is now a punctured torus, which is not compact.
