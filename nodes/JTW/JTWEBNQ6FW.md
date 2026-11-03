---
tag: JTWEBNQ6FW
kind: definition
name: Celestial coordinate system
msc: [85A04]
defines: YT0G7RE2GM
uses: [W7GD4WR497, 01QFQAQ2PA]
sources:
  - url: https://en.wikipedia.org/wiki/Astronomical_coordinate_systems
---

## Definition

Let $S$ be the [[celestial sphere|W7GD4WR497]] of an observer.
A *celestial coordinate system* on $S$ is given by three data:

1. a fundamental plane through the centre of $S$, with a chosen pole $P$ on the normal line;
2. a primary direction $X$, a point of the great circle cut out by the fundamental plane;
3. a sense of rotation along that great circle, the sense of increasing longitude.

Take the orthonormal frame with $e_1$ pointing to $X$ and $e_3$ pointing to $P$.
The vector $e_2$ lies on the great circle, a quarter turn from $X$ in the chosen sense.
Each point $u \in S$ other than $\pm P$ is written uniquely as
$$u = (\cos b \cos l)\, e_1 + (\cos b \sin l)\, e_2 + (\sin b)\, e_3,$$
with latitude $b \in (-\pi/2, \pi/2)$ and longitude $l \in [0, 2\pi)$.
The poles $\pm P$ have latitude $\pm\pi/2$, and their longitude is undefined.

## Remarks

These are the [[spherical coordinates|01QFQAQ2PA]] of $u$, with latitude measured from the fundamental plane instead of from the pole.
Example: the equatorial system takes the celestial equator as fundamental plane and the March equinox as $X$; its coordinates are declination and right ascension.
Non-example: the pair of a star's altitude and right ascension is not a coordinate system in this sense.
The two angles refer to different fundamental planes, and they do not come from one frame.
Two celestial coordinate systems with frames of the same handedness differ by a rotation of the sphere.
So changing system means multiplying the unit vector by a rotation matrix.
