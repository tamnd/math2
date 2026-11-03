---
tag: 2SF9VNPQQX
kind: definition
name: Oseen equations
msc: [76D07, 35Q35]
defines: 5632SYFZNF
uses: [18KXZHVF4M, 13CB7V2YM4, 0299VCW1TH]
sources:
  - url: https://en.wikipedia.org/wiki/Oseen_equations
---

## Definition

Let $\Omega \subseteq \R^3$ be an open set, let $\nu > 0$ be the kinematic viscosity, and let $U \in \R^3$ be a constant vector, the velocity of the free stream.
Let $f \colon \Omega \to \R^3$ be a given force.
A [[vector field|0299VCW1TH]] $u \colon \Omega \to \R^3$ and a function $p \colon \Omega \to \R$ satisfy the steady *Oseen equations* if
$$(U \cdot \nabla) u = \nu \Delta u - \nabla p + f, \qquad \nabla \cdot u = 0 \quad \text{in } \Omega.$$
Here the density is normalised to $1$.
In the application, the full velocity is $U + u$, and $u$ is the disturbance caused by a body.
It satisfies $u = -U$ on the body and $u \to 0$ at infinity.

## Remarks

Example: in the channel $-1 < y < 1$, with $U = (1, 0, 0)$ and $f = 0$, the field $u = (1 - y^2, 0, 0)$ with $p = -2 \nu x$ is a solution.
Indeed $(U \cdot \nabla) u = \partial_x u = 0$, $\nu \Delta u = (-2\nu, 0, 0) = \nabla p$, and $\nabla \cdot u = 0$.

Non-example: $u = (x, 0, 0)$ fails the second equation for every $p$, since $\nabla \cdot u = 1$.

The equations come from the [[Navier–Stokes equations|18KXZHVF4M]] by writing the velocity as $U + u$ and dropping the term $(u \cdot \nabla) u$, quadratic in the disturbance.
With $U = 0$ they reduce to the [[Stokes equations|13CB7V2YM4]].
The time-dependent version adds $\partial_t u$ on the left.
The operator is not symmetric: the term $(U \cdot \nabla) u$ makes the fundamental solution decay faster upstream than downstream, which models a wake.
