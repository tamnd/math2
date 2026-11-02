---
tag: ZR1DPX6VAN
kind: definition
name: Total variation diminishing scheme
msc: [65M08, 65M12, 35L65]
defines: NX8RE9B72A
uses: [8QA5DEWNYD, 8RA7AMWSAF, MTCRZC5QKT, YHZ9BCNDRZ]
sources:
  - url: https://en.wikipedia.org/wiki/Total_variation_diminishing
---

## Definition

Consider a scalar [[conservation law|8RA7AMWSAF]] $u_t + f(u)_x = 0$ in one space dimension, and a numerical scheme that maps a grid function $u^n = (u_j^n)_{j \in \Z}$ to $u^{n+1} = (u_j^{n+1})_{j \in \Z}$.
The discrete [[total variation|8QA5DEWNYD]] of a grid function $v$ is
$$TV(v) = \sum_{j \in \Z} \abs{v_{j+1} - v_j}.$$
The scheme is *total variation diminishing* (TVD) if $TV(u^{n+1}) \le TV(u^n)$ for every grid function $u^n$ with $TV(u^n) < \infty$.

## Remarks

Example: for $u_t + a u_x = 0$ with $a > 0$, the [[upwind scheme|MTCRZC5QKT]] with $0 \le \nu \le 1$ gives $u_{j+1}^{n+1} - u_j^{n+1} = (1 - \nu)(u_{j+1}^n - u_j^n) + \nu (u_j^n - u_{j-1}^n)$.
By the triangle inequality and a shift of the index, $TV(u^{n+1}) \le (1 - \nu) TV(u^n) + \nu\, TV(u^n) = TV(u^n)$.
Non-example: the [[Lax–Wendroff method|YHZ9BCNDRZ]] with $\nu = 1/2$, applied to the step $u_j^n = 1$ for $j \le 0$ and $u_j^n = 0$ for $j \ge 1$, gives $u_0^{n+1} = 1.125$, $u_1^{n+1} = 0.375$ and $u_j^{n+1} = u_j^n$ for the other $j$.
So $TV(u^{n+1}) = 0.125 + 0.75 + 0.375 = 1.25 > 1 = TV(u^n)$.
Harten's criterion: a scheme that can be written as $u_j^{n+1} = u_j^n + C_{j+1/2} (u_{j+1}^n - u_j^n) - D_{j-1/2} (u_j^n - u_{j-1}^n)$ with $C_{j+1/2} \ge 0$, $D_{j+1/2} \ge 0$ and $C_{j+1/2} + D_{j+1/2} \le 1$ for all $j$ is TVD.
Every monotone conservative scheme is TVD, and every TVD scheme is monotonicity preserving.

## Explanations

### L1 human

A scheme is TVD when the total amount of up-and-down in the solution can only shrink.
This forbids new wiggles near jumps.
