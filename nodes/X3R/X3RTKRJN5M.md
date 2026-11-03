---
tag: X3RTKRJN5M
kind: definition
name: Centrifugal force
msc: [70B05, 70A05]
defines: BSV03EAVYT
uses: [HNXK6CJ5B2, ZN2Z2HJY9Z, 2FTZ7D8Z0F, 0SEDGXG9S3]
sources:
  - url: https://en.wikipedia.org/wiki/Centrifugal_force
---

## Definition

Let a [[reference frame|HNXK6CJ5B2]] turn about a fixed origin with [[angular velocity|2FTZ7D8Z0F]] $\omega \in \R^3$ relative to an inertial frame.
Let a particle of mass $m > 0$ have position $r \in \R^3$ in the rotating frame, measured from the origin.
The *centrifugal force* on the particle is the [[fictitious force|ZN2Z2HJY9Z]]
$$F_{\mathrm{cf}} = -m\, \omega \times (\omega \times r),$$
where $\times$ is the [[cross product|0SEDGXG9S3]].

## Remarks

Write $r = r_\parallel + r_\perp$, with $r_\parallel$ parallel to $\omega$ and $r_\perp$ orthogonal to $\omega$.
The identity $a \times (b \times c) = b (a \cdot c) - c (a \cdot b)$ gives $F_{\mathrm{cf}} = m \abs{\omega}^2 r_\perp$.
So the force points straight away from the axis and has size $m \abs{\omega}^2 \abs{r_\perp}$.

Example: for $\omega = (0, 0, 2)$, $m = 1$ and $r = (3, 0, 5)$, one gets $\omega \times r = (0, 6, 0)$ and $\omega \times (0, 6, 0) = (-12, 0, 0)$, so $F_{\mathrm{cf}} = (12, 0, 0)$, which equals $m \abs{\omega}^2 r_\perp = 4 \cdot (3, 0, 0)$.

Non-example: a particle on the axis, such as $r = (0, 0, 5)$ above, feels no centrifugal force, since $r_\perp = 0$.
The force $-m\, \omega \times v$ that depends on the velocity $v$ is not the centrifugal force; up to the factor $2$ it is the Coriolis force.
