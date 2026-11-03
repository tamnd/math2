---
tag: ENHQD5N9D8
kind: definition
name: Tisserand's parameter
msc: [70F07, 70F15]
defines: ASYXZZB77G
uses: [K6KNWEVRY4, Y2R2QRPD1B, KBR6WZQN6F]
sources:
  - url: https://en.wikipedia.org/wiki/Tisserand%27s_parameter
---

## Definition

Let a planet move on a circular orbit of radius $a_P > 0$ about the Sun.
Let a small body have osculating [[orbital elements|K6KNWEVRY4]] about the Sun with semi-major axis $a > 0$ and eccentricity $0 \le e < 1$.
Let $i$ be its inclination measured from the plane of the planet's orbit.
*Tisserand's parameter* of the small body relative to the planet is
$$T_P = \frac{a_P}{a} + 2 \cos i \sqrt{\frac{a}{a_P} (1 - e^2)}.$$

## Remarks

In the [[circular restricted three-body problem|Y2R2QRPD1B]] the [[Jacobi integral|KBR6WZQN6F]] is exactly conserved.
Write it in heliocentric elements and drop the terms of the order of the planet-to-Sun mass ratio.
It then says that $T_P$ is nearly constant, away from the immediate vicinity of the planet.

Example: the planet itself, with $a = a_P$, $e = 0$ and $i = 0$, has $T_P = 1 + 2 = 3$.
Bodies with $T_P$ close to $3$ have orbits similar to that of the planet and can meet it at low relative speed.

Non-example: the semi-major axis $a$ alone is not nearly conserved, since a close encounter with the planet can change it a lot while $T_P$ stays nearly fixed.

Relative to Jupiter, Jupiter-family comets typically have $2 < T_J < 3$.
