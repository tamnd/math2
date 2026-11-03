---
tag: V6M7XMFER7
kind: definition
name: Horizontal coordinate system
msc: [85A04]
defines: DMAYYCRMJD
uses: [YT0G7RE2GM, W7GD4WR497]
sources:
  - url: https://en.wikipedia.org/wiki/Horizontal_coordinate_system
---

## Definition

Fix an observer on the Earth at geographic latitude $\varphi$.
The *horizontal coordinate system* is the [[celestial coordinate system|YT0G7RE2GM]] on the observer's [[celestial sphere|W7GD4WR497]] with these data:

1. the fundamental plane is the local horizontal plane, and its great circle is the horizon;
2. the pole is the zenith, the direction opposite to local gravity;
3. the primary direction is the north point of the horizon.

The latitude is the altitude $a \in [-90^\circ, 90^\circ]$.
The longitude is the azimuth $A \in [0^\circ, 360^\circ)$, measured from north through east.

## Remarks

With azimuth from north through east, the frame (north, east, zenith) is left-handed, unlike the equatorial frame.
Some older texts measure azimuth from the south instead.
The zenith distance is $z = 90^\circ - a$.
For a star of declination $\delta$ and hour angle $H$, the altitude satisfies
$$\sin a = \sin\varphi\sin\delta + \cos\varphi\cos\delta\cos H.$$
Example: at the North Pole, $\varphi = 90^\circ$, this gives $a = \delta$, so each star circles at constant altitude.
Non-example: the equatorial coordinates of a star are not horizontal coordinates.
They do not depend on the observer, while the altitude of a star changes during the night.
