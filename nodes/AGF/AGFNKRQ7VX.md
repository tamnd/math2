---
tag: AGFNKRQ7VX
kind: definition
name: Duality of electric and magnetic fields
msc: [78A25, 35Q61]
defines: MTMHQQ47N3
uses: [9BWWD4QK8Y, YZ7Q9DP8RT, XRED3C547P, QQ7HF9X1GQ, P3PK0Q02CZ]
sources:
  - url: https://en.wikipedia.org/wiki/Duality_(electricity_and_magnetism)
---

## Definition

Let $c > 0$ be the speed of light, and let $E, B \colon \R^3 \times \R \to \R^3$ be an [[electric field|YZ7Q9DP8RT]] and a [[magnetic field|XRED3C547P]].
For $\theta \in \R$, the *duality rotation* by the angle $\theta$ maps $(E, B)$ to $(E', B')$ with
$$E' = E \cos\theta + c B \sin\theta, \qquad c B' = -E \sin\theta + c B \cos\theta.$$
The *duality transformation* is the case $\theta = \pi/2$, namely $E' = cB$ and $B' = -E / c$.
*Electromagnetic duality* is the fact that duality rotations map solutions of the source-free [[Maxwell's equations|9BWWD4QK8Y]] to solutions.

## Remarks

Check for $\theta = \pi/2$: if $\nabla \times E = -\partial_t B$ and $\nabla \times B = \frac{1}{c^2} \partial_t E$, then $\nabla \times E' = c \nabla \times B = \frac{1}{c} \partial_t E = -\partial_t B'$ and $\nabla \times B' = -\frac{1}{c} \nabla \times E = \frac{1}{c} \partial_t B = \frac{1}{c^2} \partial_t E'$; the divergences stay $0$.
The energy density $\frac{\varepsilon_0}{2} (\abs{E}^2 + c^2 \abs{B}^2)$ and the [[Poynting vector|P3PK0Q02CZ]] $E \times B / \mu_0$ are invariant under every duality rotation.

Example: the plane wave $E = (0, E_0 \cos(kx - \omega t), 0)$, $B = (0, 0, \frac{E_0}{c} \cos(kx - \omega t))$ with $\omega = ck$ is mapped to $E' = (0, 0, E_0 \cos(kx - \omega t))$, $B' = (0, -\frac{E_0}{c} \cos(kx - \omega t), 0)$, the same wave with the polarization turned by a right angle.

Non-example: with sources the map fails.
For the field $E$ of a point charge at rest and $B = 0$, the image $B' = -E/c$ has nonzero divergence at the charge, which violates Gauss's law for magnetism.
The symmetry is restored if one allows [[magnetic monopoles|QQ7HF9X1GQ]] and rotates the pair of electric and magnetic charge densities in the same way.

## Explanations

### L1 human

The duality rotation mixes the electric field with the magnetic field, scaled by $c$ so that both have the same units.
In empty space it sends solutions of Maxwell's equations to solutions.
It is a hidden symmetry of light that does not show up in the forces between ordinary charges.
