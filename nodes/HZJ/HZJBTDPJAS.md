---
tag: HZJBTDPJAS
kind: definition
name: Escape velocity
msc: [70F05, 70M20]
defines: DJGG5SN382
uses: [29WRN5J730, C9YCMAPKMT, DF7DKHTQ7A, AV2WRWW1TN]
sources:
  - url: https://en.wikipedia.org/wiki/Escape_velocity
---

## Definition

Let a body of mass $M > 0$ be spherically symmetric, fixed, and the only source of force, and let $G > 0$ be the gravitational constant.
A test particle moves outside it by [[Newton's law of gravitation|29WRN5J730]].
Consider a particle at distance $r$ from the centre, moving in a direction that does not lead into the body.
The *escape velocity* at distance $r$ is the least speed $v_e$ such that every such particle with speed $v \ge v_e$ escapes.
Here escaping means that the distance to the centre tends to $\infty$.
It equals
$$v_e = \sqrt{\frac{2 G M}{r}}.$$

## Remarks

The value follows from [[conservation of energy|AV2WRWW1TN]]: the particle escapes exactly when its [[kinetic energy|C9YCMAPKMT]] plus its [[potential energy|DF7DKHTQ7A]] is at least $0$, that is $\frac{1}{2} m v^2 - G M m / r \ge 0$.
The value does not depend on the mass $m$ of the particle or on the direction of launch.

Example: for the Earth, $G M \approx 3.986 \times 10^{14}\ \mathrm{m^3/s^2}$ and $r \approx 6.371 \times 10^6$ m, so $v_e \approx 11.2$ km/s.

Non-example: the speed $\sqrt{G M / r}$ of a circular orbit of radius $r$ is smaller than $v_e$ by the factor $\sqrt{2}$, so the energy is negative and the particle stays bound.

One often writes $\mu = G M$, so that $v_e = \sqrt{2 \mu / r}$.
