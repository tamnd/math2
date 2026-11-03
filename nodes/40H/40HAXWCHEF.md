---
tag: 40HAXWCHEF
kind: definition
name: Goldreich–Julian density
msc: [85A30, 78A25, 82D10]
defines: KT4BCA2EYV
uses: [9BWWD4QK8Y]
sources:
  - url: https://en.wikipedia.org/wiki/Pulsar
---

## Definition

Let a star rotate with constant angular velocity vector $\Omega$ about an axis through the origin.
Let $B(r)$ be a static magnetic field in the region around it, and let $\varepsilon_0$ be the vacuum permittivity.
The *Goldreich–Julian density* at a point $r$ is the charge density
$$\rho_{GJ}(r) = -2 \varepsilon_0 \, \Omega \cdot B(r).$$
Its number density is $n_{GJ} = \abs{\rho_{GJ}}/e$, where $e$ is the elementary charge.

## Remarks

Assume that the magnetospheric plasma is a perfect conductor that corotates with the star, with velocity $u = \Omega \times r$, so that $E + u \times B = 0$.
By [[Maxwell's equations|9BWWD4QK8Y]], $\rho = \varepsilon_0 \nabla \cdot E$, and
$$\nabla \cdot (u \times B) = B \cdot (\nabla \times u) - u \cdot (\nabla \times B) = 2 \Omega \cdot B - u \cdot (\nabla \times B).$$
If the currents are negligible, $\nabla \times B = 0$, and so $\rho = -\varepsilon_0 \nabla \cdot (u \times B) = -2 \varepsilon_0 \Omega \cdot B$.
This is valid well inside the light cylinder, where $\abs{\Omega \times r} \ll c$; a fuller relativistic treatment divides by $1 - \abs{\Omega \times r}^2/c^2$.
In Gaussian units the density is $-\Omega \cdot B / (2\pi c)$.

Example: for an aligned dipole, with $\Omega$ along the magnetic axis, $\rho_{GJ}$ has one sign near the poles and the opposite sign near the equator.
It vanishes on the cones where $\Omega \cdot B = 0$, which for a dipole are at $\cos^2\theta = 1/3$ from the axis.

Non-example: a non-rotating magnetized star, with $\Omega = 0$, has $\rho_{GJ} = 0$; no space charge is needed, since the plasma at rest feels no motional electric field.
