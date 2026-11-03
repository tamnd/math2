---
tag: JHYVWKAW94
kind: definition
name: Tidal acceleration
msc: [70F15, 86A04, 85A04]
defines: QE7VTGRZ05
uses: [48JY6FBEHB, 7147M98XNR, GCX7TC88B2, 9636MFFSGC]
sources:
  - url: https://en.wikipedia.org/wiki/Tidal_acceleration
---

## Definition

Let a satellite of mass $m$ move on a circular orbit of radius $a$ and angular velocity $n$ about a primary of mass $M$.
Let the primary spin with angular velocity $\Omega$ about the normal of the orbital plane, in the same sense as the orbit.
Let $C$ be its moment of inertia about that axis.
The [[tidal force|48JY6FBEHB]] of the satellite raises a bulge on the primary.
Dissipation in the primary makes the bulge lag in time behind the tidal forcing.
*Tidal acceleration* is the resulting secular evolution when $\Omega > n$:

1. The bulge leads the satellite and exerts on it a [[torque|9636MFFSGC]] along its orbital motion.
2. The orbital angular momentum $\mu \sqrt{G (M + m) a}$, with $\mu = Mm/(M + m)$ and $G$ the gravitational constant, increases, so $a$ increases and $n$ decreases.
3. The spin angular momentum $C \Omega$ decreases by the same amount, so $\Omega$ decreases.

## Remarks

The total [[angular momentum|7147M98XNR]] $C\Omega + \mu\sqrt{G(M + m)a}$ is conserved, as [[conservation of angular momentum|GCX7TC88B2]] requires for an isolated pair of bodies, while mechanical energy is dissipated as heat.
Example: for the Earth and the Moon, $\Omega$ is one turn per day and $n$ one turn per month, so $\Omega > n$.
Hence the Moon recedes, by about $3.8$ cm per year, and the tidal part of the lengthening of the day is about $2.3$ ms per century.
Non-example: Phobos orbits Mars faster than Mars spins, so $\Omega < n$ and clause 1 fails.
The bulge then trails the satellite, the torque reverses, and Phobos spirals inward; this is called tidal deceleration.
The evolution stops when $\Omega = n$, a state of synchronous rotation of the primary.
