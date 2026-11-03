---
tag: M6G5M21WJX
kind: definition
name: Ray parameter
msc: [86A15, 74J05]
defines: JAFNCJNF6E
uses: [AZFGJKMKTP]
sources:
  - url: https://en.wikipedia.org/wiki/Seismic_wave
---

## Definition

Let $x(s)$ be a [[seismic ray|AZFGJKMKTP]] in an isotropic medium with wave speed $v$.

1. Let $v = v(z)$ depend only on the depth $z$, and let $i$ be the angle between the ray and the vertical at depth $z$.
The *ray parameter* of the ray is $p = \sin i / v(z)$.
2. Let $v = v(r)$ depend only on the distance $r$ from the centre of a sphere.
Let $i$ be the angle between the ray and the radial direction at radius $r$.
The ray parameter is $p = r \sin i / v(r)$.

In both cases $p$ does not depend on the point of the ray chosen.
In case 1 it has units of time per length, and in case 2 units of time per radian.

## Remarks

Equivalently, $p$ is the horizontal component of the slowness vector $\nabla T$, where $T$ is the travel time; in case 2, $p$ is the component along the great circle times $r$.
If $T(X)$ is the travel time from a surface source to a surface receiver at distance $X$, then $dT/dX = p$ for the ray that arrives at $X$.
Example: in a half-space with $v(z) = v_0 + g z$, $g > 0$, a ray leaving the surface at angle $i_0$ has $p = \sin i_0 / v_0$.
It turns where $\sin i = 1$, that is at the depth $z$ with $v(z) = 1/p$, so $z = (1/p - v_0)/g$.
Non-example: if $v$ also depends on the horizontal position, $\sin i / v$ changes along a ray, so case 1 does not define a single number for the ray.
