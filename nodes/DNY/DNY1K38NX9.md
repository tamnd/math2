---
tag: DNY1K38NX9
kind: definition
name: Etendue
msc: [78A05]
defines: M8FEBN0QSE
uses: [9VGK0SP6EQ, T56WHM058J]
sources:
  - url: https://en.wikipedia.org/wiki/Etendue
---

## Definition

Let a beam of light cross a surface $S$ in a medium of [[refractive index|9VGK0SP6EQ]] $n$.
At each point of $S$, let the beam fill a set of directions, measured by the solid angle $\Omega$.
Let $\theta$ be the angle between a direction and the normal to $S$.
The *etendue* of the beam through $S$ is
$$G = n^2 \int_S \int \cos\theta \, d\Omega \, dA,$$
where the inner integral runs over the directions of the beam at each point.

## Remarks

In the coordinates of [[Hamiltonian optics|T56WHM058J]], with $S$ a plane $z = \text{const}$, one has $n^2 \cos\theta \, d\Omega \, dA = dx \, dy \, dp \, dq$.
So $G$ is the phase-space volume of the beam, and it is conserved by Liouville's theorem for Hamiltonian flows.

Example: a flat source of area $A$ in air that emits into a cone of half-angle $\alpha$ about its normal.
Check: $\int \cos\theta \, d\Omega = \int_0^{2\pi} \int_0^\alpha \cos\theta \sin\theta \, d\theta \, d\phi = \pi \sin^2 \alpha$, so $G = \pi A \sin^2\alpha$.

Non-example: the product of the area and the solid angle, $A \cdot 2\pi(1 - \cos\alpha)$, is not the etendue.
It lacks the factor $\cos\theta$ and the factor $n^2$, and it is not conserved by refraction.
