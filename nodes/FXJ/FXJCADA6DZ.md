---
tag: FXJCADA6DZ
kind: definition
name: Velocity potential
msc: [76B99, 76A02]
defines: 470A1RJWBP
uses: [0ABK9V9Y64, 0PKG97PX9Y, B3SXT9TWFA, 0QW64ARSHB, 2JZ0C15A9C, S8RG6N1PRT]
sources:
  - url: https://en.wikipedia.org/wiki/Velocity_potential
---

## Definition

Let $\Omega \subseteq \R^n$ be open, with $n = 2$ or $n = 3$, and let $\mathbf{u} \colon \Omega \to \R^n$ be a continuous velocity field.
A *velocity potential* for $\mathbf{u}$ is a continuously differentiable function $\phi \colon \Omega \to \R$ such that
$$\mathbf{u} = \nabla \phi \quad \text{on } \Omega.$$
If the flow depends on time, the equation holds at each fixed time.

## Remarks

A field with a velocity potential is a [[conservative vector field|0PKG97PX9Y]].
If $\mathbf{u}$ is continuously differentiable and has a potential, then its [[vorticity|B3SXT9TWFA]] $\nabla \times \mathbf{u}$ is zero.
Conversely, on a [[simply connected domain|0QW64ARSHB]] every continuously differentiable irrotational field has a potential, unique up to an additive constant.
If moreover the flow is [[incompressible|2JZ0C15A9C]], then $\Delta \phi = \nabla \cdot \mathbf{u} = 0$, so $\phi$ solves [[Laplace's equation|S8RG6N1PRT]].
Example: $\phi = (x^2 - y^2)/2$ is a potential for $\mathbf{u} = (x, -y)$; check: $\phi_x = x$ and $\phi_y = -y$.
Non-example: the rigid rotation $\mathbf{u} = (-y, x)$ has vorticity $2 \ne 0$, so it has no potential.
The point vortex $\mathbf{u} = (-y, x)/(x^2 + y^2)$ is irrotational on $\R^2 \setminus \set{0}$ but has no single-valued potential there, since its circulation around the origin is $2\pi$; the domain is not simply connected.
