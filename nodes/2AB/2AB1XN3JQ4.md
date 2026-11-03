---
tag: 2AB1XN3JQ4
kind: definition
name: Geoid
msc: [86A30, 86A20]
defines: 999BYZY0ZG
uses: [5Y2BWNY6MF, 0B2RZ0778N, R9XX7TNJCH]
sources:
  - url: https://en.wikipedia.org/wiki/Geoid
---

## Definition

Let $W$ be the [[geopotential|5Y2BWNY6MF]] of the Earth.
The *geoid* is the [[level set|0B2RZ0778N]]
$$\set{\mathbf{x} \in \R^3 : W(\mathbf{x}) = W_0},$$
where the constant $W_0$ is chosen so that this surface best fits mean sea level.
The fit is in the least squares sense.
The *geoid undulation* $N$ at a point of a [[reference ellipsoid|R9XX7TNJCH]] is the height of the geoid above the ellipsoid, measured along the ellipsoid normal.

## Remarks

Example: for a non-rotating Earth with spherically symmetric density, $W = GM/r$ outside the Earth, so every level set there is a sphere $r = GM/W_0$; the geoid would be a sphere.
Non-example: the instantaneous sea surface is not the geoid, since tides, winds and currents move it away from a level surface by up to a few metres.
The geoid is everywhere perpendicular to the gravity vector $\nabla W$.
The orthometric height $H$ of a point, its height above the geoid, satisfies $h \approx H + N$, where $h$ is the ellipsoidal height.
On the Earth, $N$ ranges roughly between $-106$ m and $+85$ m.
