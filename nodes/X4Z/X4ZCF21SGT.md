---
tag: X4ZCF21SGT
kind: definition
name: Geodetic datum
msc: [86A30]
defines: N8HZ9D1CF0
uses: [R9XX7TNJCH, 6QBV95NG6E]
sources:
  - url: https://en.wikipedia.org/wiki/Geodetic_datum
---

## Definition

A *geodetic datum* consists of the following data:

1. a [[reference ellipsoid|R9XX7TNJCH]], given by its semi-major axis $a$ and flattening $f$;
2. a Cartesian frame fixed to the Earth: an origin, an axis direction for $z$, and a direction for $x$ in the plane $z = 0$;
3. the convention that the ellipsoid is centred at the origin with its axis along $z$.

The direction of $x$ fixes the prime meridian $\lambda = 0$.
Given a datum, each point of space receives [[geodetic coordinates|6QBV95NG6E]] $(\varphi, \lambda, h)$ with respect to the placed ellipsoid.

## Remarks

Example: WGS 84 uses the ellipsoid with $a = 6378137$ m and $1/f = 298.257223563$, an origin at the Earth's centre of mass, and the $z$-axis along the conventional mean rotation axis.
Non-example: the ellipsoid GRS 80 alone is not a datum, since it says nothing about where the ellipsoid is placed relative to the Earth (clause 2 fails).
A datum whose origin is the centre of mass is called geocentric.
In practice a datum is realised by the coordinates of a network of physical markers or stations.
