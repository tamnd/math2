---
tag: 7QPQ1AHD5H
kind: definition
name: Gravitational radiation reaction
msc: ["83C35", "83C10", "83C25"]
defines: EB51RMJ5Z0
uses: [7HC8RM1EH9, F541Z4R4ZX, SJ0A4TZTFR]
sources:
  - url: https://en.wikipedia.org/wiki/Gravitational_wave
---

## Definition

Consider a slowly moving, weakly self-gravitating source of mass density $\rho(t, x)$ and reduced quadrupole moment $Q_{ij}(t)$, as in the [[quadrupole formula|F541Z4R4ZX]].
Consider the [[post-Newtonian expansion|7HC8RM1EH9]] of the equations of motion of the source.
The *gravitational radiation reaction* is the leading part of the force that is odd under time reversal.
It appears at order $(v/c)^5$ relative to the Newtonian force.
In Burke–Thorne gauge it is given by the potential
$$\Phi_{RR}(t, x) = \frac{G}{5c^5} \frac{d^5 Q_{ij}}{dt^5}(t)\, x_i x_j,$$
with summation over $i, j \in \set{1, 2, 3}$, which adds the force density $-\rho \nabla \Phi_{RR}$ to the Newtonian equations.

## Remarks

The work done by this force on the source is $-\int \rho\, v \cdot \nabla\Phi_{RR}\, d^3x = -\frac{G}{5c^5} Q^{(5)}_{ij} \dot Q_{ij}$, using the continuity equation.
After integration by parts in time and averaging over several periods it equals $-\frac{G}{5c^5}\langle \dddot Q_{ij} \dddot Q_{ij} \rangle$.
This is minus the power carried by the [[gravitational waves|SJ0A4TZTFR]], so the energy balance holds.

Example: for two point masses $m_1, m_2$ on a circular orbit of separation $a$, energy balance with $E = -G m_1 m_2/(2a)$ gives
$$\frac{da}{dt} = -\frac{64}{5} \frac{G^3 m_1 m_2 (m_1 + m_2)}{c^5 a^3}.$$
So $a^4$ decreases linearly in time and the bodies collide after a finite time.

Non-example: the first post-Newtonian corrections to the force, at order $(v/c)^2$, are even under time reversal.
They are conservative, cause effects such as perihelion precession, and are not part of radiation reaction.
