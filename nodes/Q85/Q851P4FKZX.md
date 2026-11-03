---
tag: Q851P4FKZX
kind: definition
name: Ecliptic coordinate system
msc: [85A04]
defines: 3ND041H1AA
uses: [YT0G7RE2GM, W7GD4WR497]
sources:
  - url: https://en.wikipedia.org/wiki/Ecliptic_coordinate_system
---

## Definition

The *ecliptic coordinate system* is the [[celestial coordinate system|YT0G7RE2GM]] on the [[celestial sphere|W7GD4WR497]] with these data:

1. the fundamental plane is the plane of the Earth's orbit around the Sun, and its great circle is the ecliptic;
2. the pole is the north ecliptic pole, on the same side of the plane as the north celestial pole;
3. the primary direction is the March equinox.

The latitude is the ecliptic latitude $\beta \in [-90^\circ, 90^\circ]$ and the longitude, measured eastward, is the ecliptic longitude $\lambda \in [0^\circ, 360^\circ)$.

## Remarks

The ecliptic is tilted against the celestial equator by the obliquity $\varepsilon \approx 23.44^\circ$.
Both systems share the primary direction, so they differ by a rotation by $\varepsilon$ about it.
In terms of [[equatorial coordinates|QBEJJPMWV1]] $(\alpha, \delta)$:
$$\sin\beta = \sin\delta\cos\varepsilon - \cos\delta\sin\varepsilon\sin\alpha,$$
$$\cos\beta\cos\lambda = \cos\delta\cos\alpha, \qquad \cos\beta\sin\lambda = \sin\delta\sin\varepsilon + \cos\delta\cos\varepsilon\sin\alpha.$$
Example: the north celestial pole, $\delta = 90^\circ$, gets $\sin\beta = \cos\varepsilon$, so $\beta = 90^\circ - \varepsilon$.
Non-example: the system with the plane of the Milky Way as fundamental plane is the galactic system, not the ecliptic one.
Heliocentric and geocentric ecliptic coordinates use the same angles with different centres.
