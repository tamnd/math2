---
tag: G87YVCE8Z5
kind: definition
name: FTCS scheme
msc: [65M06, "80M20", 35K05]
defines: H28GYT3HHA
uses: [1QCG88BQC2, VNB1BFDEYK, 2Z7NASDQB6, 3KM7HQWKXP]
sources:
  - url: https://en.wikipedia.org/wiki/FTCS_scheme
---

## Definition

Let $\alpha > 0$ and consider the [[heat equation|VNB1BFDEYK]] $u_t = \alpha u_{xx}$ in one space dimension.
Let $\Delta x > 0$ and $\Delta t > 0$, and let $u_j^n$ denote the approximation of $u(j \Delta x, n \Delta t)$ for integers $j$ and $n \ge 0$.
Put $r = \alpha \Delta t / \Delta x^2$.
The *FTCS scheme* is the explicit [[finite difference scheme|1QCG88BQC2]]
$$u_j^{n+1} = u_j^n + r \left( u_{j+1}^n - 2 u_j^n + u_{j-1}^n \right).$$
It comes from replacing $u_t$ by the forward difference $(u_j^{n+1} - u_j^n)/\Delta t$ and $u_{xx}$ by the centred difference $(u_{j+1}^n - 2u_j^n + u_{j-1}^n)/\Delta x^2$.

## Remarks

Its local [[truncation error|3KM7HQWKXP]] is $O(\Delta t + \Delta x^2)$ for smooth solutions.
[[Von Neumann analysis|2Z7NASDQB6]] gives the amplification factor $g(\xi) = 1 - 4 r \sin^2(\xi/2)$, so the scheme is stable if and only if $r \le 1/2$.
For $r \le 1/2$ the new value $u_j^{n+1} = (1 - 2r) u_j^n + r u_{j+1}^n + r u_{j-1}^n$ is a convex combination of old values, which gives a discrete maximum principle.
Example: with $r = 1/2$ the scheme reads $u_j^{n+1} = (u_{j+1}^n + u_{j-1}^n)/2$.
Starting from $u^0_0 = 1$ and $u^0_j = 0$ for $j \ne 0$, one step gives $u^1_{\pm 1} = 1/2$ and all other values $0$; the total heat $\sum_j u_j^n$ stays $1$.
Non-example: the Crank–Nicolson scheme also uses centred differences in space, but it evaluates them at the new time level as well.
So it is implicit and is not the FTCS scheme.
The same forward-time, centred-space construction applied to the advection equation $u_t + a u_x = 0$ with $a \ne 0$ is unstable for every ratio $\Delta t / \Delta x$.
