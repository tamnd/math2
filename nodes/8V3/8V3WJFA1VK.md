---
tag: 8V3WJFA1VK
kind: definition
name: Jacobi integral
msc: [70F07, 70H33, 70F15]
defines: KBR6WZQN6F
uses: [Y2R2QRPD1B, 0262JP0NV9, HNXK6CJ5B2]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobi_integral
---

## Definition

Let $\mu \in (0, \frac{1}{2}]$ and consider the [[circular restricted three-body problem|Y2R2QRPD1B]] in its normalised [[rotating frame|HNXK6CJ5B2]], with primaries of masses $1 - \mu$ and $\mu$ at $(-\mu, 0, 0)$ and $(1 - \mu, 0, 0)$.
Let $r_1$ and $r_2$ be the distances from the point $(x, y, z)$ to the two primaries, and let
$$\Omega(x, y, z) = \frac{x^2 + y^2}{2} + \frac{1 - \mu}{r_1} + \frac{\mu}{r_2}.$$
The *Jacobi integral* is the function of position and velocity
$$C = 2 \, \Omega(x, y, z) - \left( x'^2 + y'^2 + z'^2 \right).$$
Its value along a motion is the *Jacobi constant* of that motion.

## Remarks

$C$ is a [[first integral|0262JP0NV9]]: the equations of motion are $x'' - 2 y' = \Omega_x$, $y'' + 2 x' = \Omega_y$, $z'' = \Omega_z$, and multiplying them by $x'$, $y'$, $z'$ and adding gives $x' x'' + y' y'' + z' z'' = \frac{d}{dt} \Omega$, so $C' = 0$.
Example: a third body at rest at the triangular Lagrange point $\left( \frac{1}{2} - \mu, \frac{\sqrt{3}}{2}, 0 \right)$ has $r_1 = r_2 = 1$, and its Jacobi constant is $C = \frac{1}{4} - \mu + \mu^2 + \frac{3}{4} + 2 = 3 - \mu + \mu^2$.
The ordinary energy $\frac{1}{2}(x'^2 + y'^2 + z'^2) - \frac{1 - \mu}{r_1} - \frac{\mu}{r_2}$ in the rotating frame is not a first integral, because it omits the centrifugal term $\frac{x^2 + y^2}{2}$.

Since $x'^2 + y'^2 + z'^2 \ge 0$, a motion with Jacobi constant $C$ stays in the Hill region $\set{2 \Omega \ge C}$.
Its boundary $\set{2 \Omega = C}$ is the zero-velocity surface.
In units where the distance, the angular velocity and the gravitational parameters are not normalised, $C = n^2 (x^2 + y^2) + 2 \left( \frac{G m_1}{r_1} + \frac{G m_2}{r_2} \right) - (x'^2 + y'^2 + z'^2)$, where $n$ is the angular velocity of the primaries.

## Explanations

### L1 human

The Jacobi integral is the energy of the small body in the rotating frame, with a sign change and a factor two, including the potential of the centrifugal force.
It does not change as the body moves.
