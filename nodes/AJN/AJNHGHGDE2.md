---
tag: AJNHGHGDE2
kind: definition
name: Planetary migration
msc: [85A04, 70F15]
defines: YMDCDFBTQ1
uses: [BXFSBB8Q46, 7147M98XNR, 9636MFFSGC, 6ADKW56QGV, 3K553QG5BZ]
sources:
  - url: https://en.wikipedia.org/wiki/Planetary_migration
---

## Definition

Let a planet of mass $m$ orbit a star of mass $M_\star \gg m$ on a nearly circular [[Kepler orbit|BXFSBB8Q46]] of semi-major axis $a(t)$.
The planet moves inside a gas disk or a population of small bodies.
Its orbital [[angular momentum|7147M98XNR]] is $L = m \sqrt{G M_\star a}$, where $G$ is the gravitational constant.
*Planetary migration* is a systematic drift of $a(t)$ over many orbits.
It is caused by a net [[torque|9636MFFSGC]] $\Gamma$ of the surrounding matter on the planet.
Since $dL/dt = \Gamma$, the drift rate is
$$\frac{da}{dt} = \frac{2 a \, \Gamma}{L}.$$

## Remarks

Common types are distinguished by the mechanism.

1. Type I: a low-mass planet in a gas [[disk|6ADKW56QGV]] feels the torques of the spiral waves it launches at Lindblad resonances, and the corotation torque.
   Its migration rate is proportional to the planet mass.
2. Type II: a giant planet opens a gap in the disk and then drifts with the viscous evolution of the disk.
3. Planetesimal-driven migration: the planet scatters many small bodies and recoils.

Example: if the net torque is $\Gamma = -\varepsilon L/\tau$ for constants $\varepsilon > 0$ and $\tau > 0$, then $da/dt = -2\varepsilon a/\tau$, so $a(t) = a(0) e^{-2\varepsilon t/\tau}$ and the planet drifts inward.

Non-example: a planet whose semi-major axis only oscillates under the periodic pull of a neighbour, with no net change over many orbits, does not migrate.

Two migrating planets whose period ratio approaches a ratio of small integers can be captured into an [[orbital resonance|3K553QG5BZ]].
