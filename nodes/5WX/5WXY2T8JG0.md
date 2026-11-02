---
tag: 5WXY2T8JG0
kind: definition
name: Stokes flow
msc: [76D07, 35Q35]
defines: 13CB7V2YM4
uses: [18KXZHVF4M, 0299VCW1TH, 0ABK9V9Y64, 0MWV6ZTK6S, 0E0B6RA8K0]
sources:
  - url: https://en.wikipedia.org/wiki/Stokes_flow
---

## Definition

Let $\Omega \subseteq \R^3$ be an open set, let $\nu > 0$ be a constant, and let $f \colon \Omega \to \R^3$ be a given force.
Consider a [[vector field|0299VCW1TH]] $u \colon \Omega \to \R^3$, the velocity, and a function $p \colon \Omega \to \R$, the pressure.
The pair $(u, p)$ is a *Stokes flow* in $\Omega$ if it satisfies the *Stokes equations*
$$- \nu \Delta u + \nabla p = f, \qquad \nabla \cdot u = 0 \quad \text{in } \Omega.$$
Here $\Delta$ is the [[Laplacian|0E0B6RA8K0]] acting on each component, $\nabla p$ is the [[gradient|0ABK9V9Y64]] and $\nabla \cdot u$ is the [[divergence|0MWV6ZTK6S]].

## Remarks

Example: in the channel $\Omega = \set{(x, y, z) : -1 < y < 1}$ with $f = 0$, the Poiseuille flow $u = (1 - y^2, 0, 0)$ with $p = -2\nu x$ is a Stokes flow.
Indeed $\Delta u = (-2, 0, 0)$, so $-\nu \Delta u + \nabla p = (2\nu, 0, 0) + (-2\nu, 0, 0) = 0$, and $\nabla \cdot u = 0$.
It also vanishes on the walls $y = \pm 1$.

Non-example: the same $u$ with constant pressure is not a Stokes flow when $f = 0$, because then $-\nu \Delta u + \nabla p = (2\nu, 0, 0) \ne 0$.

The Stokes equations arise from the [[Navier–Stokes equations|18KXZHVF4M]] when the Reynolds number is small, so that the term $(u \cdot \nabla) u$ can be neglected, and the flow is steady.
The time-dependent version $\partial_t u - \nu \Delta u + \nabla p = f$ is also called the Stokes equations.
