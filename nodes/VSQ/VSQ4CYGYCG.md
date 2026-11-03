---
tag: VSQ4CYGYCG
kind: definition
name: Hodograph transformation
msc: [76N15, 76H05, 35M10]
defines: 9AR4ZZRRAM
uses: [RW0JK9VDZE, 470A1RJWBP, SN4J6KP03C, HKPHRSN3ER]
sources:
  - url: https://en.wikipedia.org/wiki/Hodograph
---

## Definition

Consider a steady planar irrotational isentropic flow of a gas in an open set $\Omega \subseteq \R^2$.
Its velocity $(u, v)$ is a $C^1$ function of $(x, y) \in \Omega$, and its [[speed of sound|SN4J6KP03C]] $c$ is a function of $u^2 + v^2$ by Bernoulli's law.
The equations of motion are
$$(c^2 - u^2) u_x - uv (u_y + v_x) + (c^2 - v^2) v_y = 0, \qquad u_y - v_x = 0.$$
Assume that the Jacobian $J = u_x v_y - u_y v_x$ does not vanish in $\Omega$ and that the map $(x, y) \mapsto (u, v)$ is injective on $\Omega$.
The *hodograph transformation* takes $x$ and $y$ as unknown functions of $(u, v)$ on the image of this map, the hodograph plane.

## Remarks

The inverse function theorem gives $u_x = J y_v$, $u_y = -J x_v$, $v_x = -J y_u$ and $v_y = J x_u$.
Substituting and dividing by $J$, the equations become
$$(c^2 - u^2)\, y_v + uv\, (x_v + y_u) + (c^2 - v^2)\, x_u = 0, \qquad x_v = y_u.$$
These are linear in $(x, y)$, since $c$ depends only on $(u, v)$.
With the [[velocity potential|470A1RJWBP]] $\varphi$, the [[Legendre transformation|HKPHRSN3ER]] $\Phi = xu + yv - \varphi$ satisfies $x = \Phi_u$ and $y = \Phi_v$, and the first equation becomes the linear equation $(c^2 - v^2)\Phi_{uu} + 2uv\, \Phi_{uv} + (c^2 - u^2) \Phi_{vv} = 0$.
In polar coordinates of the hodograph plane this is [[Chaplygin's equation|GC17HMC8FN]].

Example: in the incompressible limit $c \to \infty$ the equations become $x_u + y_v = 0$ and $x_v = y_u$, so $x - iy$ is a holomorphic function of $u + iv$ wherever it is defined.

Non-example: a uniform flow, or a simple wave such as the [[Prandtl–Meyer expansion fan|D9J383MG41]], has $J = 0$ everywhere.
Such flows have no hodograph image of positive area and are not obtained by the transformation.
