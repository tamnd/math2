---
tag: M6J7J3H7FN
kind: definition
name: Incompressible flow
msc: [76D05, 76B99, 76A02]
defines: 2JZ0C15A9C
uses: [F2JRWJNYN4, CJW50K5HZB, 0MWV6ZTK6S, FD4NR553YR]
sources:
  - url: https://en.wikipedia.org/wiki/Incompressible_flow
---

## Definition

Let a [[fluid flow|F2JRWJNYN4]] on an open set $\Omega \subseteq \R^3$ and an open interval $I$ have density $\rho > 0$ and velocity $\mathbf{u}$.
Assume both are continuously differentiable and satisfy the [[continuity equation|FD4NR553YR]].
The flow is *incompressible* if the [[material derivative|CJW50K5HZB]] of the density vanishes:
$$\frac{D\rho}{Dt} = \frac{\partial \rho}{\partial t} + \mathbf{u} \cdot \nabla \rho = 0 \quad \text{on } \Omega \times I.$$

## Remarks

Since the continuity equation reads $D\rho/Dt + \rho \, \nabla \cdot \mathbf{u} = 0$ and $\rho > 0$, the flow is incompressible if and only if the [[divergence|0MWV6ZTK6S]] of the velocity is zero, $\nabla \cdot \mathbf{u} = 0$.
Equivalently, the flow map preserves the volume of every region of fluid.
Example: the plane flow $\mathbf{u} = (x, -y)$ with constant density is incompressible; check: $\partial_x x + \partial_y (-y) = 1 - 1 = 0$.
Non-example: the flow $\mathbf{u} = (x, y)$ has divergence $2$, so it is not incompressible; the fluid spreads out and its density must fall.
Incompressible does not mean constant density: a stratified ocean with density varying in depth can still flow incompressibly.
