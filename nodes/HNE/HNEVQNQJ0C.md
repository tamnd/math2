---
tag: HNEVQNQJ0C
kind: definition
name: Geodetic coordinates
msc: [86A30]
defines: 6QBV95NG6E
uses: [R9XX7TNJCH, 0RWKYX8339, 01QFQAQ2PA]
sources:
  - url: https://en.wikipedia.org/wiki/Geodetic_coordinates
---

## Definition

Let $\mathcal{E}$ be a [[reference ellipsoid|R9XX7TNJCH]] with semi-axes $a \ge b > 0$ and squared eccentricity $e^2 = 1 - b^2/a^2$.
Place it at the origin of a [[Cartesian coordinate system|0RWKYX8339]], with its axis along the $z$-axis.
For a geodetic latitude $\varphi \in [-\pi/2, \pi/2]$, set
$$N(\varphi) = \frac{a}{\sqrt{1 - e^2 \sin^2 \varphi}}.$$
The point with *geodetic coordinates* $(\varphi, \lambda, h)$, where $\lambda$ is the longitude and $h \in \R$ the ellipsoidal height, is
$$X = (N + h) \cos\varphi \cos\lambda, \quad Y = (N + h) \cos\varphi \sin\lambda, \quad Z = \big((1 - e^2) N + h\big) \sin\varphi,$$
with $N = N(\varphi)$.
Geometrically, $h$ is the signed distance from the point to $\mathcal{E}$ along the normal to $\mathcal{E}$.
The latitude $\varphi$ is the angle between this normal and the equatorial plane.

## Remarks

Example: on the equator, $\varphi = 0$ gives $N = a$, so $(0, 0, h)$ is the point $(a + h, 0, 0)$, at height $h$ above the ellipsoid.
Non-example: the geocentric latitude, the angle between the equatorial plane and the line from the origin, is not the geodetic latitude when $e > 0$ and $0 < \abs{\varphi} < \pi/2$.
When $e = 0$ the formulas reduce to [[spherical coordinates|01QFQAQ2PA]] with radius $a + h$ and latitude $\varphi$.
The number $N(\varphi)$ is the prime vertical radius of curvature.
