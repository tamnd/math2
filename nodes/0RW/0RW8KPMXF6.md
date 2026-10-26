---
tag: 0RW8KPMXF6
kind: definition
name: Spherical coordinates
msc: [51N20]
defines: 01QFQAQ2PA
uses: [0XPR1E85W0, 0RJZV05MJA]
sources:
  - url: https://en.wikipedia.org/wiki/Spherical_coordinate_system
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Spherical_coordinate_system
    locator: Cartesian coordinates
---

## Definition

The spherical coordinate map is $S \colon [0, \infty) \times [0, \pi] \times \mathbb{R} \to \mathbb{R}^3$,
$$S(\rho, \varphi, \theta) = (\rho \sin \varphi \cos \theta, \ \rho \sin \varphi \sin \theta, \ \rho \cos \varphi).$$
A triple $(\rho, \varphi, \theta)$ with $S(\rho, \varphi, \theta) = (x, y, z)$ is a triple of spherical coordinates of $(x, y, z)$.
Here $\rho = \sqrt{x^2 + y^2 + z^2}$ is the distance to the origin, $\varphi$ is the polar angle from the positive $z$-axis, and $\theta$ is the azimuth.

## Remarks

The pair $(\rho \sin \varphi, \theta)$ is a pair of [[polar coordinates|0RJZV05MJA]] of $(x, y)$, and $\cos \varphi = z / \rho$ for $\rho > 0$.
The coordinates are unique for points off the $z$-axis if $\rho > 0$, $0 < \varphi < \pi$ and $\theta \in [0, 2\pi)$.
The sphere of radius $a$ is $\rho = a$, and $\varphi = \pi / 4$ is a cone around the positive $z$-axis.
This is a common convention in mathematics. Physics texts often write $(r, \theta, \varphi)$, with $\theta$ the polar angle and $\varphi$ the azimuth.

## Explanations

### L1 human

To locate a point in space, give its distance from the origin, how far it tilts away from the north pole, and its longitude.
This is like latitude and longitude on the Earth, with the polar angle measured from the north pole.
