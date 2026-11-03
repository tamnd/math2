---
tag: 56QFEBPYGZ
kind: definition
name: Relativistic angular momentum
msc: [83A05, 70H40]
defines: FRDTZ2NT72
uses: [G49G4R1K04, S8RKKKMSTG, 67N6B8MJ3X, 7147M98XNR]
sources:
  - url: https://en.wikipedia.org/wiki/Relativistic_angular_momentum
---

## Definition

Let $(\R^4, \eta)$ be [[Minkowski space|G49G4R1K04]] with inertial coordinates $x = (x^0, x^1, x^2, x^3) = (ct, \vec x)$, where $c$ is the speed of light.
Let a particle be at the event $x$ with [[four-momentum|67N6B8MJ3X]] $p = (E/c, \vec p)$.
The *relativistic angular momentum* of the particle about the origin is the antisymmetric tensor with components
$$M^{\mu\nu} = x^\mu p^\nu - x^\nu p^\mu, \qquad \mu, \nu \in \set{0, 1, 2, 3}.$$
For a system of particles, the total angular momentum is the sum of these tensors, all taken at the same time $t$.

## Remarks

The space components $M^{ij}$ with $i, j \in \set{1, 2, 3}$ are the components of the classical [[angular momentum|7147M98XNR]] $\vec L = \vec x \times \vec p$; for example $M^{12} = x^1 p^2 - x^2 p^1 = L_3$.
The mixed components are $M^{0i} = c t \, p^i - x^i E/c$.
For a free particle, $x(\tau) = x(0) + \tau p/m$, and the term $\tau p/m$ drops out of $x^\mu p^\nu - x^\nu p^\mu$, so $M$ is constant along the motion.
Example: a particle with $\vec p = (p, 0, 0)$ moving on the line $y = b$, $z = 0$ has $L_3 = M^{12} = x^1 p^2 - x^2 p^1 = -bp$ at every time.
Non-example: the vector $\vec x \times \vec p$ alone is not a four-dimensional tensor; under a boost it mixes with the components $M^{0i}$.
Under a translation of the origin by $a$, $M^{\mu\nu}$ changes to $M^{\mu\nu} - (a^\mu p^\nu - a^\nu p^\mu)$.
