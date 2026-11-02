---
tag: J8ZRM7KFJH
kind: definition
name: Lax–Wendroff method
msc: [65M06, 35L65]
defines: YHZ9BCNDRZ
uses: [PVD7VZJZ9B, X7HYEBA5SA, 8RA7AMWSAF, VY3J2NKGKW]
sources:
  - url: https://en.wikipedia.org/wiki/Lax%E2%80%93Wendroff_method
---

## Definition

Fix $\Delta x > 0$ and $\Delta t > 0$, put $\lambda = \Delta t / \Delta x$, and let $u_j^n$ approximate $u(j \Delta x, n \Delta t)$.

1. For the [[transport equation|PVD7VZJZ9B]] $u_t + a u_x = 0$ with $a \in \R$ and $\nu = a \lambda$, the *Lax–Wendroff method* is the explicit [[finite difference|X7HYEBA5SA]] scheme
$$u_j^{n+1} = u_j^n - \frac{\nu}{2} \left( u_{j+1}^n - u_{j-1}^n \right) + \frac{\nu^2}{2} \left( u_{j+1}^n - 2 u_j^n + u_{j-1}^n \right).$$
2. For a [[conservation law|8RA7AMWSAF]] $u_t + f(u)_x = 0$ with a smooth flux $f$, its two-step (Richtmyer) form is
$$u_{j+1/2}^{n+1/2} = \frac{u_j^n + u_{j+1}^n}{2} - \frac{\lambda}{2} \left( f(u_{j+1}^n) - f(u_j^n) \right), \qquad u_j^{n+1} = u_j^n - \lambda \left( f(u_{j+1/2}^{n+1/2}) - f(u_{j-1/2}^{n+1/2}) \right).$$

## Remarks

For $f(u) = a u$, the two-step form reduces to the scheme of clause 1.
The first step is a [[Lax–Friedrichs|VY3J2NKGKW]] step over half a time step on the staggered grid.
Example: for clause 1, the Fourier mode $e^{i j \xi}$ is multiplied by $g = 1 - i \nu \sin \xi - \nu^2 (1 - \cos \xi)$, and a short computation gives $\abs{g}^2 = 1 - 4 \nu^2 (1 - \nu^2) \sin^4 (\xi / 2)$.
So $\abs{g} \le 1$ for all $\xi$ exactly when $\abs{\nu} \le 1$, and the scheme is stable under this condition.
Taylor expansion shows that the local truncation error is $O(\Delta x^3)$ for fixed $\nu$, so the method is second-order accurate.
Non-example: dropping the last term gives the forward-time centred-space scheme, which is only first order in time and has $\abs{g}^2 = 1 + \nu^2 \sin^2 \xi > 1$ for $\sin \xi \ne 0$, so it is unstable.

## Explanations

### L1 human

The scheme is the second-order Taylor step in time, with the time derivatives traded for space derivatives through the equation.
The last term adds just enough smoothing to make the centred scheme stable.
