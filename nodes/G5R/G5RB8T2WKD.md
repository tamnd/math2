---
tag: G5RB8T2WKD
kind: definition
name: Upwind scheme
msc: [65M06, 65M08]
defines: MTCRZC5QKT
uses: [PVD7VZJZ9B, X7HYEBA5SA, FQVVNYV6N8]
sources:
  - url: https://en.wikipedia.org/wiki/Upwind_scheme
---

## Definition

Let $a \in \R$, and consider the [[transport equation|PVD7VZJZ9B]] $u_t + a u_x = 0$.
Fix $\Delta x > 0$ and $\Delta t > 0$, put $\nu = a \Delta t / \Delta x$, and let $u_j^n$ approximate $u(j \Delta x, n \Delta t)$.
The first-order *upwind scheme* is the explicit [[finite difference|X7HYEBA5SA]] scheme
$$u_j^{n+1} = \begin{cases} u_j^n - \nu \left( u_j^n - u_{j-1}^n \right) & \text{if } a \ge 0, \\ u_j^n - \nu \left( u_{j+1}^n - u_j^n \right) & \text{if } a < 0. \end{cases}$$
Equivalently, with $a^+ = \max(a, 0)$ and $a^- = \min(a, 0)$,
$$u_j^{n+1} = u_j^n - \frac{\Delta t}{\Delta x} \left( a^+ (u_j^n - u_{j-1}^n) + a^- (u_{j+1}^n - u_j^n) \right).$$

## Remarks

Example: let $a > 0$ and $0 \le \nu \le 1$.
Then $u_j^{n+1} = (1 - \nu) u_j^n + \nu u_{j-1}^n$ is a convex combination, so $\min_j u_j^n \le u_j^{n+1} \le \max_j u_j^n$, and the scheme is stable in the maximum norm.
The condition $\nu \le 1$ is the [[Courant–Friedrichs–Lewy condition|FQVVNYV6N8]]: the numerical domain of dependence must contain the characteristic through the point.
Non-example: for $a > 0$, the downwind scheme $u_j^{n+1} = u_j^n - \nu (u_{j+1}^n - u_j^n)$ uses the wrong side.
It multiplies the Fourier mode $e^{i j \xi}$ by $g = 1 + \nu - \nu e^{i\xi}$, with $\abs{g}^2 = 1 + 2\nu(1 + \nu)(1 - \cos \xi) > 1$ for $\xi \ne 0$, so it is unstable for every $\nu > 0$.
For a scalar conservation law $u_t + f(u)_x = 0$, upwinding takes the difference on the side given by the sign of the characteristic speed $f'(u)$.
The scheme is first-order accurate in $\Delta x$ for fixed $\nu$.

## Explanations

### L1 human

The difference is taken towards the side the wave comes from.
This simple rule is what makes the scheme stable.
