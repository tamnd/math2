---
tag: HD74ZBGCJ2
kind: definition
name: Energy method
msc: [35L05, 35B45, 35A02]
defines: G8J0YQRPA3
uses: [5EHD2XBQDG, W09B9NZ9B5, 0E0B6RA8K0]
sources:
  - url: https://en.wikipedia.org/wiki/Well-posed_problem
---

## Definition

Let $u$ be a solution of an evolution equation on $\Omega \times [0, T]$, with $\Omega \subseteq \R^n$ open.
The *energy method* is the following kind of argument.

1. Choose an energy $E(t) \ge 0$, an integral over $\Omega$ of a nonnegative quadratic expression in $u(\cdot, t)$ and its derivatives.
2. Differentiate $E$ in $t$, use the equation, and integrate by parts with the boundary conditions. The aim is a bound $E'(t) \le C E(t) + F(t)$ with a constant $C \ge 0$ and a known function $F \ge 0$.
3. Conclude by Grönwall's inequality that $E(t) \le e^{Ct}\big(E(0) + \int_0^t F(s)\, ds\big)$ for $0 \le t \le T$.

Apply the argument to the difference of two solutions of a linear problem, with $F = 0$.
It gives uniqueness and continuous dependence on the data, as required for a [[well-posed problem|W09B9NZ9B5]].

## Remarks

Example: let $\Omega$ be bounded with smooth boundary and let $u \in C^2(\overline{\Omega} \times [0, T])$ solve the [[wave equation|5EHD2XBQDG]] $u_{tt} = \Delta u$ with $u = 0$ on $\partial\Omega$.
Take $E(t) = \frac{1}{2}\int_\Omega \big(u_t^2 + \abs{\nabla u}^2\big)\, dx$, where $\Delta$ is the [[Laplacian|0E0B6RA8K0]].
Then $E'(t) = \int_\Omega (u_t u_{tt} + \nabla u \cdot \nabla u_t)\, dx = \int_\Omega u_t (u_{tt} - \Delta u)\, dx = 0$, since the boundary term contains $u_t = 0$ on $\partial\Omega$.
So $E$ is constant, and two solutions with the same data and boundary values coincide.
For the heat equation $u_t = \Delta u$ with $u = 0$ on $\partial\Omega$, the energy $E(t) = \frac{1}{2}\int_\Omega u^2\, dx$ satisfies $E'(t) = -\int_\Omega \abs{\nabla u}^2\, dx \le 0$.
Non-example: for the backward heat equation $u_t = -\Delta u$ the same computation gives $E'(t) = \int_\Omega \abs{\nabla u}^2\, dx$, which is not bounded by $C E(t)$, so step 2 fails; indeed that problem is ill-posed.
