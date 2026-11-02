---
tag: 9ZBWK5WSC7
kind: definition
name: Euler equations
msc: [35Q31, 76B03]
defines: RW0JK9VDZE
uses: [GC5BDZ6QBC, 0299VCW1TH, 0ABK9V9Y64, 0MWV6ZTK6S]
sources:
  - url: https://en.wikipedia.org/wiki/Euler_equations_(fluid_dynamics)
---

## Definition

Let $\Omega \subseteq \R^3$ be an open set and let $T > 0$.
The *incompressible Euler equations* are the system
$$\partial_t u + (u \cdot \nabla) u = - \nabla p, \qquad \nabla \cdot u = 0,$$
for an unknown [[vector field|0299VCW1TH]] $u \colon \Omega \times (0, T) \to \R^3$, the velocity, and an unknown function $p \colon \Omega \times (0, T) \to \R$, the pressure.
Here $\nabla p$ is the [[gradient|0ABK9V9Y64]] of $p$ in $x$, $\nabla \cdot u$ is the [[divergence|0MWV6ZTK6S]] of $u$, and $(u \cdot \nabla) u$ has components $\sum_{j=1}^3 u_j \partial_j u_i$.
The density is normalised to $1$.
On a bounded domain one adds the boundary condition $u \cdot n = 0$, where $n$ is the outer unit normal.

## Remarks

Example: on $\Omega = \R^3$, the rigid rotation $u = (-y, x, 0)$ with pressure $p = (x^2 + y^2)/2$ is a solution.
Indeed $\nabla \cdot u = 0$, $(u \cdot \nabla) u = (-x, -y, 0)$ and $-\nabla p = (-x, -y, 0)$.

Non-example: $u = (x, 0, 0)$ is not a solution for any pressure, because $\nabla \cdot u = 1 \ne 0$.

The *compressible Euler equations* have the density $\rho$ and the pressure as further unknowns:
$$\partial_t \rho + \nabla \cdot (\rho u) = 0, \qquad \partial_t (\rho u) + \nabla \cdot (\rho u \otimes u) + \nabla p = 0,$$
together with an energy equation or an equation of state that relates $p$ to $\rho$.
They form a system of hyperbolic conservation laws, whose solutions can develop shock waves.
