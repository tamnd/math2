---
tag: 6DK7EQT95Y
kind: definition
name: Poynting vector
msc: [78A25, 78A40]
defines: P3PK0Q02CZ
uses: [YZ7Q9DP8RT, XRED3C547P, A2WZA4QA3V, 0N5N15HWZ7]
sources:
  - url: https://en.wikipedia.org/wiki/Poynting_vector
---

## Definition

Let $E$ be the [[electric field|YZ7Q9DP8RT]] and $H = B / \mu_0 - M$ the magnetizing field, where $B$ is the [[magnetic field|XRED3C547P]], $M$ the [[magnetization|A2WZA4QA3V]] and $\mu_0 > 0$ the vacuum permeability.
The *Poynting vector* is
$$S = E \times H,$$
where $\times$ is the [[cross product|0N5N15HWZ7]].
In vacuum $M = 0$ and $S = \frac{1}{\mu_0} E \times B$.
It is measured in watts per square metre.

## Remarks

Example: the plane wave $E = (0, E_0 \cos(kx - \omega t), 0)$, $B = (0, 0, \frac{E_0}{c} \cos(kx - \omega t))$ in vacuum, with $\omega = ck$, has
$$S = \frac{E_0^2}{\mu_0 c} \cos^2(kx - \omega t) \, (1, 0, 0),$$
since $(0, 1, 0) \times (0, 0, 1) = (1, 0, 0)$.
It points in the direction of propagation, and its time average is $E_0^2 / (2 \mu_0 c)$.

Non-example: the vector $E \times B$ without the factor $1/\mu_0$ is not the Poynting vector.
It has the wrong units, and its divergence does not match the rate of change of the field energy.

Only the divergence of $S$ and its flux through closed surfaces have a direct physical meaning, through Poynting's theorem.
Adding the curl of any vector field to $S$ does not change these, so the local energy flux is not determined by the energy balance alone.
For instance, a static charge next to a static magnet has $S \neq 0$ but $\nabla \cdot S = 0$, and no energy is transported in a measurable way.
