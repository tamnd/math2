---
tag: MM0YNN1MJA
kind: definition
name: Numerical diffusion
msc: [65M06, 65M15]
defines: 55GVVJTF24
uses: [PVD7VZJZ9B, X7HYEBA5SA, MTCRZC5QKT, VY3J2NKGKW, YHZ9BCNDRZ]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_diffusion
---

## Definition

Let $a \in \R$, and consider a consistent linear [[finite difference|X7HYEBA5SA]] scheme for the [[transport equation|PVD7VZJZ9B]] $u_t + a u_x = 0$, with mesh sizes $\Delta x$, $\Delta t$ and fixed ratio $\nu = a \Delta t / \Delta x$.
Its modified equation is the partial differential equation that the numerical solution satisfies to higher order in $\Delta x$.
It is found by Taylor expansion of the scheme, with time derivatives replaced by space derivatives.
Suppose the modified equation has the form
$$u_t + a u_x = D\, u_{xx} + \sum_{k \ge 3} c_k\, \partial_x^k u.$$
The coefficient $D$ is the *numerical diffusion* coefficient of the scheme.
The scheme is said to have numerical diffusion when $D > 0$.

## Remarks

Example: for the [[upwind scheme|MTCRZC5QKT]] $u_j^{n+1} = u_j^n - \nu (u_j^n - u_{j-1}^n)$ with $a > 0$, Taylor expansion gives $u_t + \frac{\Delta t}{2} u_{tt} + a u_x - \frac{a \Delta x}{2} u_{xx} = O(\Delta x^2)$.
Using $u_{tt} = a^2 u_{xx} + O(\Delta x)$ gives $D = \frac{a \Delta x}{2} (1 - \nu)$, which is positive for $0 < \nu < 1$.
For the [[Lax–Friedrichs method|VY3J2NKGKW]] the same computation gives $D = \frac{\Delta x^2}{2 \Delta t} (1 - \nu^2)$, which is larger than for upwind when $0 < \nu < 1$.
Non-example: for the [[Lax–Wendroff method|YHZ9BCNDRZ]] the coefficient of $u_{xx}$ is zero to this order, so $D = 0$.
Its leading error is a third-derivative term, which is dispersive (wiggles), not diffusive (smearing).
A negative $D$ means anti-diffusion, as for the downwind scheme $u_j^{n+1} = u_j^n - \nu (u_{j+1}^n - u_j^n)$ with $a > 0$, which is unstable.

## Explanations

### L1 human

Numerical diffusion is the hidden diffusion term that a scheme adds to the equation it solves.
Its coefficient is read off from the modified equation.
