---
tag: WW4ZVV9ZW8
kind: definition
name: Reynolds equation
msc: [76D08]
defines: K2W9427PJ2
uses: [90FD7XNX72, GC5BDZ6QBC, DF0M8YNQ3D]
sources:
  - url: https://en.wikipedia.org/wiki/Reynolds_equation
---

## Definition

Let a fluid of dynamic viscosity $\mu > 0$ fill a thin gap $0 < z < h(x, y, t)$, under the assumptions of [[lubrication theory|90FD7XNX72]].
The lower surface $z = 0$ slides with constant velocity $(U, 0, 0)$ in its own plane, and the upper surface has no tangential velocity and moves only vertically.
The *Reynolds equation* is the equation
$$\partial_x \Big( h^3 \, \partial_x p \Big) + \partial_y \Big( h^3 \, \partial_y p \Big) = 6 \mu U \, \partial_x h + 12 \mu \, \partial_t h$$
for the pressure $p(x, y, t)$ in the film.

## Remarks

Derivation: by the lubrication equations and the [[no-slip condition|DF0M8YNQ3D]], $u = \frac{1}{2 \mu} \partial_x p \, (z^2 - z h) + U (1 - z / h)$ and $v = \frac{1}{2 \mu} \partial_y p \, (z^2 - z h)$.
The fluxes across the gap are $q_x = -\frac{h^3}{12 \mu} \partial_x p + \frac{U h}{2}$ and $q_y = -\frac{h^3}{12 \mu} \partial_y p$.
Conservation of mass across the gap gives $\partial_t h + \partial_x q_x + \partial_y q_y = 0$, which is the equation.

Example: a slider bearing with $h(x) = h_1 + (h_0 - h_1) x / L$ on $0 < x < L$, with $h_0 > h_1$, steady and uniform in $y$, gives $\frac{d}{dx}\big( h^3 p' \big) = 6 \mu U h'$.
With $p = 0$ at both ends, the solution is positive inside when $U > 0$, so the film carries a load.

Non-example: if $h$ is constant in space and time, the right side vanishes and the equation becomes $\Delta p = 0$.
With $p = 0$ at the edges of the film, the only solution is $p = 0$, so a parallel film carries no load; a converging gap is needed.

When $h$ is constant the equation is a Laplace equation for $p$, which is the case of [[Hele-Shaw flow|CM1R6CSHAA]].
For a compressible lubricant the density enters in the form $\nabla \cdot (\rho h^3 \nabla p) = 6 \mu U \partial_x (\rho h) + 12 \mu \partial_t (\rho h)$.
