---
tag: ERZZHWZW3E
kind: definition
name: Equatorial coordinate system
msc: [85A04]
defines: QBEJJPMWV1
uses: [YT0G7RE2GM, W7GD4WR497]
sources:
  - url: https://en.wikipedia.org/wiki/Equatorial_coordinate_system
---

## Definition

The *equatorial coordinate system* is the [[celestial coordinate system|YT0G7RE2GM]] on the geocentric [[celestial sphere|W7GD4WR497]] with these data:

1. the fundamental plane is the plane of the Earth's equator, and its great circle is the celestial equator;
2. the pole is the north celestial pole, the direction of the Earth's rotation axis towards the north;
3. the primary direction is the March equinox, the point where the Sun crosses the celestial equator from south to north.

The latitude is the declination $\delta \in [-90^\circ, 90^\circ]$.
The longitude, measured eastward, is the right ascension $\alpha$, usually given in hours from $0^{\mathrm h}$ to $24^{\mathrm h}$, with $1^{\mathrm h} = 15^\circ$.

## Remarks

The unit vector of the direction $(\alpha, \delta)$ is $(\cos\delta\cos\alpha, \cos\delta\sin\alpha, \sin\delta)$.
Example: the north celestial pole has $\delta = +90^\circ$, and the March equinox has $\alpha = 0^{\mathrm h}$, $\delta = 0^\circ$.
The angular distance $\theta$ between $(\alpha_1, \delta_1)$ and $(\alpha_2, \delta_2)$ satisfies $\cos\theta = \sin\delta_1\sin\delta_2 + \cos\delta_1\cos\delta_2\cos(\alpha_1 - \alpha_2)$.
Non-example: a frame that turns with the Earth, with longitude counted from the meridian of Greenwich, is not the equatorial system.
In that frame the longitude of a star grows by $360^\circ$ each sidereal day.
The equator and equinox move slowly by precession and nutation, so equatorial coordinates refer to an epoch such as J2000.0.
