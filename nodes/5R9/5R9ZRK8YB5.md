---
tag: 5R9ZRK8YB5
kind: definition
name: MacCormack method
msc: [65M06, 35L65]
defines: PGXZJ2YWVJ
uses: [8RA7AMWSAF, X7HYEBA5SA, YHZ9BCNDRZ]
sources:
  - url: https://en.wikipedia.org/wiki/MacCormack_method
---

## Definition

Let $f \colon \R^m \to \R^m$ be smooth, and consider the [[conservation law|8RA7AMWSAF]] $u_t + f(u)_x = 0$.
Fix $\Delta x > 0$ and $\Delta t > 0$, put $\lambda = \Delta t / \Delta x$, and let $u_j^n$ approximate $u(j \Delta x, n \Delta t)$.
The *MacCormack method* computes $u^{n+1}$ from $u^n$ in two steps.

1. Predictor, with a forward difference: $u_j^{*} = u_j^n - \lambda \left( f(u_{j+1}^n) - f(u_j^n) \right)$.
2. Corrector, with a backward difference: $u_j^{n+1} = \frac12 \left( u_j^n + u_j^{*} \right) - \frac{\lambda}{2} \left( f(u_j^{*}) - f(u_{j-1}^{*}) \right)$.

## Remarks

Example: for $f(u) = a u$ and $\nu = a \lambda$, the predictor gives $u_j^* - u_{j-1}^* = (u_j^n - u_{j-1}^n) - \nu (u_{j+1}^n - 2u_j^n + u_{j-1}^n)$.
Putting this into the corrector gives
$$u_j^{n+1} = u_j^n - \frac{\nu}{2} (u_{j+1}^n - u_{j-1}^n) + \frac{\nu^2}{2} (u_{j+1}^n - 2u_j^n + u_{j-1}^n),$$
which is the [[Lax–Wendroff method|YHZ9BCNDRZ]]; so the method is second-order accurate and stable for $\abs{\nu} \le 1$ in this case.
Non-example: using a forward difference in the corrector as well gives, for $f(u) = a u$, the scheme $u_j^{n+1} = u_j^n - \nu (u_{j+1}^n - u_j^n) + \frac{\nu^2}{2}(u_{j+2}^n - 2u_{j+1}^n + u_j^n)$, whose Taylor expansion leaves the error term $-\frac{a \Delta x}{2} u_{xx}$, so it is only first order.
The order of the one-sided differences may be reversed (backward in the predictor, forward in the corrector); alternating the two orders from step to step is common.

## Explanations

### L1 human

Predict with differences pointing forward, correct with differences pointing back, and average.
For linear problems this is exactly the Lax–Wendroff scheme.
