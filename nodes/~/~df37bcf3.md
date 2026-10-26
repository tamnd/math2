---
tag: ~df37bcf3
kind: definition
name: Cylindrical coordinates
msc: [51N20]
defines: ~6888d091
uses: [~4056ef33, ~a5928a9d]
sources:
  - url: https://en.wikipedia.org/wiki/Cylindrical_coordinate_system
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Cylindrical_coordinate_system
    locator: Line and volume elements
---

## Definition

The cylindrical coordinate map is $C \colon [0, \infty) \times \mathbb{R} \times \mathbb{R} \to \mathbb{R}^3$,
$$C(r, \theta, z) = (r \cos \theta, \ r \sin \theta, \ z).$$
A triple $(r, \theta, z)$ with $C(r, \theta, z) = (x, y, z)$ is a triple of cylindrical coordinates of $(x, y, z)$.
Here $r = \sqrt{x^2 + y^2}$ is the distance to the $z$-axis, $\theta$ is the azimuth, and $z$ is the height.

## Remarks

The pair $(r, \theta)$ is a pair of [[polar coordinates|~4056ef33]] of $(x, y)$. So, away from the $z$-axis, the coordinates are unique if $r > 0$ and $\theta \in [0, 2\pi)$.
The Jacobian determinant of $C$ is $r$, so the volume element is $dV = r \, dr \, d\theta \, dz$.
Example: the solid cylinder $x^2 + y^2 \le a^2$, $0 \le z \le h$ has volume $\int_0^h \int_0^{2\pi} \int_0^a r \, dr \, d\theta \, dz = \pi a^2 h$.
Some texts write $\rho$ or $s$ for $r$, and $\varphi$ for $\theta$.

## Explanations

### L1 human

Cylindrical coordinates are polar coordinates in the floor plan, together with the height.
Surfaces $r = $ constant are cylinders around the $z$-axis, which gives the coordinates their name.
