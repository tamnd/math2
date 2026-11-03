---
tag: WDJNQVGTX0
kind: object
name: Lagrange points
msc: [70F07, 70K42, 70F15]
instance_of: [0N8NGKDZDZ]
uses: [Y2R2QRPD1B, 0N8NGKDZDZ, 0F2SYCKDT2, HNXK6CJ5B2]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange_point
same_as:
  wikidata: Q190463
  wikipedia: Lagrange point
---

## Description

Consider the [[circular restricted three-body problem|Y2R2QRPD1B]] with mass parameter $\mu \in (0, \frac{1}{2}]$.
Use the [[rotating frame|HNXK6CJ5B2]] where the primaries of masses $1 - \mu$ and $\mu$ stay at $(-\mu, 0, 0)$ and $(1 - \mu, 0, 0)$.
The *Lagrange points* are the five [[equilibrium points|0N8NGKDZDZ]] of the third body in this frame, that is, the critical points of
$$\Omega(x, y, z) = \frac{x^2 + y^2}{2} + \frac{1 - \mu}{r_1} + \frac{\mu}{r_2}.$$
At such a point the third body stays at rest relative to the two primaries.

1. $L_1$, $L_2$ and $L_3$ lie on the $x$-axis: $L_1$ between the primaries, $L_2$ beyond the smaller primary, and $L_3$ beyond the larger one.
2. $L_4$ and $L_5$ are the points $\left( \frac{1}{2} - \mu, \pm \frac{\sqrt{3}}{2}, 0 \right)$, which form an equilateral triangle with the two primaries.

Check for $L_4$: there $r_1 = r_2 = 1$, and $\partial_x \Omega = x - (1 - \mu) \frac{x + \mu}{r_1^3} - \mu \frac{x - 1 + \mu}{r_2^3} = 0$, because $(1 - \mu)(x + \mu) + \mu (x - 1 + \mu) = x$.
Similarly $\partial_y \Omega = y \left( 1 - \frac{1 - \mu}{r_1^3} - \frac{\mu}{r_2^3} \right) = 0$, and $\partial_z \Omega = 0$ since $z = 0$.

## Remarks

The collinear points $L_1$, $L_2$, $L_3$ are unstable for every $\mu$.
The triangular points $L_4$ and $L_5$ are linearly stable exactly when $27 \mu (1 - \mu) < 1$, that is, when $\mu < \frac{1}{2} \left( 1 - \sqrt{23/27} \right) \approx 0.0385$.
For the Sun and Jupiter, $\mu \approx 0.001$, and the Trojan asteroids cluster around the points $L_4$ and $L_5$ of this pair.
The collinear solutions of the full three-body problem were found by Euler, and the equilateral ones by Lagrange.

## Explanations

### L1 human

Around two bodies that circle each other, such as the Sun and the Earth, there are five places where a small object can stay still relative to both.
There the pulls of the two bodies and the effect of the rotation exactly balance.
Three of these points lie on the line through the two bodies, and two form equilateral triangles with them.
Space telescopes are often placed near the Sun–Earth point $L_2$, beyond the Earth.
