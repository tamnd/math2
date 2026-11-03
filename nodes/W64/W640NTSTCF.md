---
tag: W640NTSTCF
kind: statement
role: fact
name: Tidal locking
msc: [70F15, 85A04]
uses: [48JY6FBEHB, BXFSBB8Q46, 7147M98XNR, 9636MFFSGC]
about: [48JY6FBEHB]
sources:
  - url: https://en.wikipedia.org/wiki/Tidal_locking
same_as:
  wikidata: Q109144
  wikipedia: Tidal locking
---

## Statement

Let a deformable body (the satellite) of mass $m$ and radius $R$ move around a body of mass $M_p$.
Its orbit is a circular [[Kepler orbit|BXFSBB8Q46]] of radius $a$ with mean motion $n$.
The satellite spins with angular velocity $\omega$ about an axis perpendicular to the orbital plane.
Assume that the [[tidal force|48JY6FBEHB]] of $M_p$ raises a bulge on the satellite.
Assume that friction inside the satellite delays the bulge, with a finite tidal quality factor $Q$.
Then the tidal [[torque|9636MFFSGC]] on the bulge changes $\omega$ towards $n$.
The spin ends in the stable state $\omega = n$, called synchronous rotation or tidal locking.
In this state the satellite always shows the same face to $M_p$.
For an initial spin $\omega_0 \gg n$, the time needed is of order
$$t_{\text{lock}} \approx \frac{\omega_0 \, a^6 \, I \, Q}{3 \, G \, M_p^2 \, k_2 \, R^5}.$$
Here $I$ is the moment of inertia of the satellite, $k_2$ is its tidal Love number and $G$ is the gravitational constant.

## Remarks

Idea: the tidal bulge is dragged ahead of (or behind) the line joining the centres by the rotation and lags because of friction.
The pull of $M_p$ on the misaligned bulge gives a torque that slows (or speeds up) the spin, and the change in spin [[angular momentum|7147M98XNR]] is transferred to the orbit.
When $\omega = n$ the bulge stays aligned with $M_p$, the torque vanishes and nothing more is dissipated.
The steep factor $a^6$ explains why close satellites lock quickly while distant ones do not.

Example: the Moon rotates once per orbit, about every $27.3$ days, so the far side cannot be seen from Earth.
Pluto and Charon are locked to each other.

The circular orbit is needed.
On an eccentric orbit the averaged tidal torque vanishes at a spin rate faster than $n$.
A permanent asymmetry of the body can then capture it in a spin–orbit resonance.
Mercury, with eccentricity about $0.21$, is captured in a $3{:}2$ spin–orbit resonance, rotating three times in two orbits, instead of synchronous rotation.

## Explanations

### L1 human

Tidal locking is why we always see the same side of the Moon.
Earth's gravity stretches the Moon slightly, and internal friction turns this stretch into a brake on its spin.
Over a long time the Moon's day became exactly as long as its month, and then the brake stops acting.

### L2 human

The locking time depends on the distance as $a^6$.
So it is much less than the age of the Solar System for close moons, and much more for distant planets.
Planets in the habitable zone of small red dwarf stars are close to their star and are expected to be locked, with a permanent day side and night side.
The same tidal torque acting on the primary slows the Earth's rotation and pushes the Moon outward, by conservation of the total angular momentum.
