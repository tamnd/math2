---
tag: VED29VB4ZS
kind: definition
name: Tollmien–Schlichting wave
msc: ["76E05", 76D10, 76F06]
defines: TQE8EN865Z
uses: [G0ADVS0K99, YCFPD0GE5G, VJ752BFSQF, JH9EJ0HA0R]
sources:
  - url: https://en.wikipedia.org/wiki/Tollmien–Schlichting_wave
---

## Definition

Consider a parallel or nearly parallel shear flow $U(y)$ of a viscous incompressible fluid along a wall $y = 0$, at [[Reynolds number|JH9EJ0HA0R]] $\mathrm{Re}$.
Examples are channel flows and [[boundary layers|YCFPD0GE5G]].
Assume that the profile $U$ has no inflection point inside the flow.
A *Tollmien–Schlichting wave* is a two-dimensional disturbance with stream function $\varphi(y) e^{i \alpha (x - c t)}$ of the following kind.
The pair $(\varphi, c)$ is the eigenmode of the [[Orr–Sommerfeld equation|G0ADVS0K99]] that becomes unstable, $\operatorname{Im} c > 0$, as $\mathrm{Re}$ passes its critical value.

## Remarks

Such a profile is stable in inviscid theory by Rayleigh's inflection point criterion, so the instability of the Tollmien–Schlichting mode is a viscous effect.
The critical layer is where $U(y)$ equals the real part of $c$.
Viscosity near the wall and near the critical layer shifts the phase of the Reynolds stress, so that the wave extracts energy from the mean shear.
The waves are slow, with phase speed a fraction of the free-stream speed, and long compared with the boundary layer thickness.

Example: for the [[Blasius boundary layer|VJ752BFSQF]] on a flat plate, the parallel-flow approximation gives a critical Reynolds number of about $520$ based on the displacement thickness.
For plane Poiseuille flow the critical mode, at $\mathrm{Re} \approx 5772$, is also a Tollmien–Schlichting wave.
Non-example: the growing waves of a free mixing layer $U(y) = \tanh y$ are not Tollmien–Schlichting waves.
That profile has an inflection point, and its instability persists in inviscid theory as a Kelvin–Helmholtz type instability.
