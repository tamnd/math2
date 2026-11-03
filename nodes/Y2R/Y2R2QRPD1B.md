---
tag: Y2R2QRPD1B
kind: problem
name: Circular restricted three-body problem
msc: [70F07, 70F15, 37N05]
uses: [JE1Z920QKT, CSVPJAA75E, HNXK6CJ5B2, 0EDKGA2FAK, 0262JP0NV9, DBKXCGDKTD]
about: [JE1Z920QKT]
sources:
  - url: https://en.wikipedia.org/wiki/Three-body_problem
    locator: Restricted three-body problem
history:
  posed_by: "Leonhard Euler"
  first_stated: "1767"
  notes: "Euler studied the restricted problem; Jacobi found its conserved quantity in 1836."
---

## Problem

Let $\mu \in (0, \frac{1}{2}]$.
Two bodies, the primaries, have masses $1 - \mu$ and $\mu$.
They move on circles around their common centre of mass, at distance $1$ from each other and with angular velocity $1$.
This is a circular solution of the [[two-body problem|CSVPJAA75E]], in units where the gravitational constant times the total mass is $1$.
A third body of negligible mass moves in their gravitational field and does not affect them.
Use the [[rotating frame|HNXK6CJ5B2]] in which the primaries stay at $(-\mu, 0, 0)$ and $(1 - \mu, 0, 0)$.
In this frame the position $(x, y, z)$ of the third body satisfies
$$x'' - 2 y' = \frac{\partial \Omega}{\partial x}, \qquad y'' + 2 x' = \frac{\partial \Omega}{\partial y}, \qquad z'' = \frac{\partial \Omega}{\partial z},$$
where
$$\Omega(x, y, z) = \frac{x^2 + y^2}{2} + \frac{1 - \mu}{r_1} + \frac{\mu}{r_2},$$
and $r_1 = \sqrt{(x + \mu)^2 + y^2 + z^2}$ and $r_2 = \sqrt{(x - 1 + \mu)^2 + y^2 + z^2}$ are the distances to the primaries.
Given the initial position and velocity of the third body, describe its motion for all time.

## Remarks

The problem is a limit case of the [[three-body problem|JE1Z920QKT]] in which one mass tends to $0$.
It is a [[Hamiltonian system|0EDKGA2FAK]] with three degrees of freedom, or two in the planar case $z = 0$.
Its Hamiltonian does not depend on time, because the frame rotates with the primaries.
The quantity $2 \Omega - (x'^2 + y'^2 + z'^2)$ is a [[first integral|0262JP0NV9]], the Jacobi integral.
Check: multiplying the three equations by $x', y', z'$ and adding gives $\frac{1}{2} \frac{d}{dt}(x'^2 + y'^2 + z'^2) = \frac{d}{dt} \Omega$, since the Coriolis terms cancel.
Poincaré showed that the problem has no further analytic first integral, and its motion is in general [[chaotic|DBKXCGDKTD]].
There are five equilibrium points in the rotating frame, the Lagrange points.
The model describes, to a first approximation, a spacecraft in the Earth–Moon system or an asteroid moving under the Sun and Jupiter.

## Explanations

### L1 human

Two heavy bodies, such as the Sun and Jupiter, go around each other on circles.
A tiny third body, such as an asteroid, moves under their pull without disturbing them.
The question is how the tiny body moves.
Even this simplified problem has no general formula for its solution, and its orbits can be chaotic.
