---
tag: Q2R5BHK82Z
kind: definition
name: Declination
msc: [85A04]
defines: 5HD86E1TEH
uses: [QBEJJPMWV1]
sources:
  - url: https://en.wikipedia.org/wiki/Declination
---

## Definition

Let $u$ be a direction on the celestial sphere.
The *declination* $\delta$ of $u$ is the angle between $u$ and the plane of the celestial equator.
It is taken positive when $u$ lies on the side of the north celestial pole and negative otherwise, so $\delta \in [-90^\circ, 90^\circ]$.
It is the latitude of $u$ in the [[equatorial coordinate system|QBEJJPMWV1]].

## Remarks

If $u$ is a unit vector and $p$ is the unit vector of the north celestial pole, then $\sin\delta = u \cdot p$.
Example: the north celestial pole has $\delta = 90^\circ$, and every point of the celestial equator has $\delta = 0^\circ$.
Non-example: the angle of a star above the horizon is its altitude, not its declination; the two agree for every star only for an observer at the North Pole.
For an observer at latitude $\varphi > 0$, a star never sets when $\delta > 90^\circ - \varphi$ and never rises when $\delta < \varphi - 90^\circ$, ignoring refraction.
The complement $90^\circ - \delta$ is the polar distance.
