---
tag: 1WWZ4ZQQ1V
kind: definition
name: Reference ellipsoid
msc: [86A30]
defines: R9XX7TNJCH
uses: [NE1PZM0HBN, 0VKCCEXBJ1]
sources:
  - url: https://en.wikipedia.org/wiki/Earth_ellipsoid
---

## Definition

Let $a$ and $b$ be real numbers with $a \ge b > 0$.
The *ellipsoid of revolution* with semi-axes $a$ and $b$ is the surface
$$\frac{x^2 + y^2}{a^2} + \frac{z^2}{b^2} = 1$$
in $\R^3$.
It is obtained by rotating an [[ellipse|0VKCCEXBJ1]] with semi-axes $a$ and $b$ about its minor axis.
A *reference ellipsoid* is such a surface, with chosen values of $a$ and of the [[flattening|NE1PZM0HBN]] $f = (a - b)/a$, used as a model of the Earth.
The $z$-axis models the rotation axis, and the plane $z = 0$ models the equatorial plane.

## Remarks

Example: GRS 80 has $a = 6378137$ m and $1/f = 298.257222101$, so $b \approx 6356752.314$ m; here $a > b$, as required.
Non-example: the ellipsoid $x^2/a^2 + y^2/a^2 + z^2/b^2 = 1$ with $b > a$ is prolate, elongated along the axis, and does not model the Earth.
The equatorial radius $a$ is called the semi-major axis and the polar radius $b$ the semi-minor axis.
Two further constants, the mass parameter $GM$ and the angular velocity $\omega$, turn it into a level ellipsoid used for normal gravity.
