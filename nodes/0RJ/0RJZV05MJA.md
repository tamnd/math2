---
tag: 0RJZV05MJA
kind: definition
name: Polar coordinates
msc: [51N20]
defines: 0BSW4T7THS
uses: [0XPR1E85W0, 0Z1Y7JHGBR]
sources:
  - url: https://en.wikipedia.org/wiki/Polar_coordinate_system
    locator: Converting between polar and Cartesian coordinates
  - url: https://en.wikipedia.org/wiki/Polar_coordinate_system
    locator: Uniqueness of polar coordinates
---

## Definition

The polar coordinate map is $P \colon [0, \infty) \times \mathbb{R} \to \mathbb{R}^2$, $P(r, \theta) = (r \cos \theta, r \sin \theta)$.
A pair $(r, \theta)$ with $P(r, \theta) = (x, y)$ is a pair of polar coordinates of the point $(x, y)$. Here $r = \sqrt{x^2 + y^2}$ is the radial coordinate and $\theta$ is the angular coordinate.

## Remarks

Each point other than the origin has exactly one pair of polar coordinates with $r > 0$ and $\theta \in [0, 2\pi)$. The origin has $r = 0$ and any $\theta$.
For $x > 0$, $\theta = \arctan(y / x)$ is one valid angle. In general one uses the two-argument function $\operatorname{atan2}(y, x)$, with values in $(-\pi, \pi]$.
The restriction of $P$ to $(0, \infty) \times (0, 2\pi)$ is a $C^\infty$ [[diffeomorphism|0Z1Y7JHGBR]] onto the plane without the half-line $\{(x, 0) : x \ge 0\}$. Its Jacobian determinant is $r$.
The circle of radius $a$ about the origin is $r = a$, and the ray at angle $\alpha$ is $\theta = \alpha$.

## Explanations

### L1 human

Instead of moving $x$ units right and $y$ units up, you turn by the angle $\theta$ and then walk the distance $r$.
Both descriptions name the same point.
