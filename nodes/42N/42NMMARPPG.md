---
tag: 42NMMARPPG
kind: definition
name: Classical electromagnetism
msc: [78A25, 35Q61]
defines: A34AF4ZVKM
uses: [9BWWD4QK8Y, S3RZRCH0T5, YZ7Q9DP8RT, XRED3C547P, 6XPSV47R56, 0299VCW1TH]
sources:
  - url: https://en.wikipedia.org/wiki/Classical_electromagnetism
---

## Definition

*Classical electromagnetism* is the physical theory with the following content.

1. The state of the field at time $t$ is a pair of [[vector fields|0299VCW1TH]] on $\R^3$: the [[electric field|YZ7Q9DP8RT]] $E$ and the [[magnetic field|XRED3C547P]] $B$.
2. The sources are a charge density $\rho$ and a current density $J$ on $\R^3 \times \R$, made of [[electric charges|6XPSV47R56]] and their motion.
3. The fields obey [[Maxwell's equations|9BWWD4QK8Y]] with these sources.
4. A point charge $q$ at position $x(t)$ with velocity $v = \dot x$ feels the [[Lorentz force|S3RZRCH0T5]] $F = q \big(E(x, t) + v \times B(x, t)\big)$.
   It moves by the relativistic law $\frac{d}{dt} \big( m \gamma v \big) = F$.
   Here $m$ is its rest mass, $\gamma = (1 - \abs{v}^2 / c^2)^{-1/2}$ and $c$ is the speed of light.

## Remarks

In matter the equations are often written with the fields $D$ and $H$ and with constitutive relations that describe the medium.

Example: a charge $q$ at rest at the origin, with no other sources, gives $\rho = q \delta_0$, $J = 0$, the Coulomb field $E(x) = q x / (4 \pi \varepsilon_0 \abs{x}^3)$ and $B = 0$.
This pair solves Maxwell's equations in the sense of distributions.

Non-example: Newtonian gravity is not part of the theory; it has no field like $B$ and no finite speed of propagation.

The coupled system of fields and point charges has a known difficulty.
The field of a point charge is infinite at the charge, so the force of a charge on itself is not defined without further assumptions.
