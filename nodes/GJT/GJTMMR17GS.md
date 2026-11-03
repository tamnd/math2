---
tag: GJTMMR17GS
kind: definition
name: Arnold's geometric formulation of the Euler equations
msc: [37K65, 58D05, 35Q31]
defines: 8F1W980F5G
uses: [RW0JK9VDZE, 7JBRGCVJRB, Q61VFHCH2J, NSYMQMHPDN, 0KZZ70ZHXP]
sources:
  - url: https://en.wikipedia.org/wiki/Euler_equations_(fluid_dynamics)
---

## Definition

Let $M$ be a compact oriented Riemannian manifold, possibly with boundary, with volume form $\mu$.
Let $G = \mathrm{SDiff}(M)$ be the group, under composition, of [[diffeomorphisms|0KZZ70ZHXP]] $g \colon M \to M$ that preserve $\mu$.
Its tangent space at the identity is the space of vector fields $v$ on $M$ with $\operatorname{div} v = 0$ and $v$ tangent to $\partial M$.
For $g \in G$ and tangent vectors $X \circ g$, $Y \circ g$ at $g$, put
$$\langle X \circ g, Y \circ g \rangle_g = \int_M \langle X, Y \rangle \, \mu.$$
This is a right-invariant (weak) [[Riemannian metric|Q61VFHCH2J]] on $G$, the kinetic energy metric.
*Arnold's geometric formulation* of the incompressible [[Euler equations|RW0JK9VDZE]] describes ideal fluid motion as the [[geodesic|NSYMQMHPDN]] flow of this metric.
Precisely, a path $g(t)$ in $G$ is a geodesic if and only if its Eulerian velocity $u(t) = \dot g(t) \circ g(t)^{-1}$ satisfies the system below.
$$\partial_t u + \nabla_u u = -\nabla p, \qquad \operatorname{div} u = 0, \qquad u \text{ tangent to } \partial M.$$
Here $p$ is some function on $M$, and $\nabla_u u$ is the covariant derivative of $u$ along itself.

## Remarks

Here $g(t)$ maps the initial position of each fluid particle to its position at time $t$.
In Arnold's 1966 paper the correspondence is formal, since $G$ is not a Lie group in the finite-dimensional sense.
Ebin and Marsden made it rigorous in 1970 on groups of Sobolev class diffeomorphisms.

Example: for $M$ the circle $\R / \Z$ with the standard metric, $\operatorname{div} v = v'$, so the only divergence-free fields are constants and $G$ is the group of rotations.
The geodesics are the uniform rotations $g(t)(x) = x + c t$, whose Eulerian velocity is the constant $c$, and constant $u$ with constant $p$ solves the Euler equations on the circle.

Non-example: the path of rotations $g(t)(x) = x + t^2$ in the same group is not a geodesic.
Its Eulerian velocity $u = 2t$ has $\partial_t u = 2$, while $-\nabla p = -p'$ has mean zero on the circle, so it cannot equal $2$.

The same scheme with other groups and metrics gives other equations.
The rotation group $SO(3)$ gives the Euler equations of a rigid body.
The circle diffeomorphism group with the $L^2$ metric gives $\partial_t u + 3 u \, \partial_x u = 0$, a rescaled inviscid Burgers equation (see [[diffeomorphism group|WTCNKST134]]).
