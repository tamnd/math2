---
tag: FBJ4JCP5SR
kind: definition
name: Godunov's scheme
msc: [65M08, 35L65, 65M06]
defines: 43HZJ7DRT0
uses: [8RA7AMWSAF, GJWKX22VVE, XN081NCPF5]
sources:
  - url: https://en.wikipedia.org/wiki/Godunov%27s_scheme
---

## Definition

Let $u_t + F(u)_x = 0$ be a [[hyperbolic system of conservation laws|XN081NCPF5]] with $F \colon \R^m \to \R^m$ smooth.
Fix $\Delta x, \Delta t > 0$, put $\lambda = \Delta t / \Delta x$, and let the cells be $C_j = (x_{j-1/2}, x_{j+1/2})$ with $x_{j+1/2} = (j + \tfrac12) \Delta x$.
Let $\Lambda$ bound the absolute values of the eigenvalues of $DF$ on the relevant states, and assume $\Lambda \lambda \le 1/2$.
Given cell values $u_j^n$, *Godunov's scheme* computes $u_j^{n+1}$ as follows.

1. Let $\tilde u$ be the function equal to $u_j^n$ on $C_j$ for each $j$.
2. Let $v$ be the entropy solution on $t_n \le t \le t_{n+1}$ with $v(\cdot, t_n) = \tilde u$, made of the solutions of the [[Riemann problems|GJWKX22VVE]] at the points $x_{j+1/2}$.
3. Set $u_j^{n+1} = \frac{1}{\Delta x} \int_{C_j} v(x, t_{n+1})\, dx$.

## Remarks

Let $u^*(u_l, u_r)$ be the value at $x/t = 0$ of the Riemann solution with states $u_l, u_r$.
Integrating the equation over $C_j \times (t_n, t_{n+1})$ gives the conservation form
$$u_j^{n+1} = u_j^n - \lambda \left( F(u^*(u_j^n, u_{j+1}^n)) - F(u^*(u_{j-1}^n, u_j^n)) \right).$$
In this form the scheme only needs $\Lambda \lambda \le 1$.
For a scalar law the numerical flux is $\min_{u_l \le w \le u_r} F(w)$ if $u_l \le u_r$, and $\max_{u_r \le w \le u_l} F(w)$ if $u_l > u_r$.

Example: for $u_t + a u_x = 0$ with $a > 0$, the Riemann solution at $x/t = 0$ is $u_l$.
So the flux at $x_{j+1/2}$ is $a u_j^n$, and the scheme is the upwind scheme $u_j^{n+1} = u_j^n - a \lambda (u_j^n - u_{j-1}^n)$.

Non-example: the downwind scheme $u_j^{n+1} = u_j^n - a\lambda(u_{j+1}^n - u_j^n)$ uses the flux $a u_{j+1}^n$ instead.
This is not the Riemann solution value, and the scheme is unstable for every $\lambda > 0$ when $a > 0$.

## Explanations

### L1 human

The scheme thinks of the solution as constant in each cell.
It moves the solution forward exactly for one short step, then takes averages again.
Only the jumps at the cell boundaries matter, and each of them is a Riemann problem.
