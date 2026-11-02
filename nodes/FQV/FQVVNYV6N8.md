---
tag: FQVVNYV6N8
kind: statement
role: theorem
name: Courant–Friedrichs–Lewy condition
msc: [65M12, 65M06, 35L03]
uses: [PVD7VZJZ9B, X7HYEBA5SA]
about: [X7HYEBA5SA]
sources:
  - url: https://en.wikipedia.org/wiki/Courant%E2%80%93Friedrichs%E2%80%93Lewy_condition
same_as:
  wikidata: Q1023483
  wikipedia: Courant–Friedrichs–Lewy condition
---

## Statement

Let $a \in \R$ and consider the [[transport equation|PVD7VZJZ9B]] $u_t + a u_x = 0$ with initial values $u(x, 0) = u_0(x)$.
Fix integers $p, q \ge 0$, real numbers $c_{-p}, \dots, c_q$ and a ratio $\lambda > 0$.
Consider the explicit [[finite difference scheme|X7HYEBA5SA]]
$$u_j^{n+1} = \sum_{k=-p}^{q} c_k\, u_{j+k}^n, \qquad u_j^0 = u_0(j \Delta x),$$
with time step $\Delta t = \lambda \Delta x$.
Suppose that for every smooth $u_0$ with compact support, $u_j^n \to u(x, t)$ whenever $\Delta x \to 0$, $j \Delta x \to x$ and $n \Delta t \to t$.
Then
$$-q \le a \lambda \le p.$$
In particular, for a three-point scheme ($p = q = 1$) convergence requires $\abs{a} \Delta t / \Delta x \le 1$.

## Remarks

Proof idea: $u_j^n$ depends only on the values $u_0(x_i)$ with $x_{j - pn} \le x_i \le x_{j + qn}$.
In the limit this is the interval $[x - p t/\lambda,\ x + q t/\lambda]$, the numerical domain of dependence of $(x, t)$.
The exact solution $u(x, t) = u_0(x - a t)$ depends only on the point $x - at$.
If $x - at$ lies outside the interval, change $u_0$ near $x - at$ only: the limit of the scheme stays the same, but $u(x, t)$ changes.

The condition is necessary but not sufficient.
The forward-time centred-space scheme has $p = q = 1$ and violates no CFL bound when $\abs{a}\lambda \le 1$, yet it diverges for every $\lambda > 0$.
The [[Lax–Friedrichs method|VY3J2NKGKW]] converges exactly when $\abs{a} \lambda \le 1$.
For $a \ge 0$, the upwind scheme $u_j^{n+1} = u_j^n - a\lambda(u_j^n - u_{j-1}^n)$ has $p = 1$ and $q = 0$, and it converges exactly when $a \lambda \le 1$.
For systems, the same argument gives $\Lambda \Delta t \le \Delta x$ for three-point schemes, where $\Lambda$ is the largest characteristic speed.

## Explanations

### L1 human

Information in a wave equation travels at a fixed speed.
An explicit scheme can only pass information one grid cell per time step.
If the time step is too large, the true information has moved further than the scheme can see, and the scheme cannot be right.
So the time step must be small compared with the space step divided by the wave speed.

### L2 human

The condition was found by Courant, Friedrichs and Lewy in 1928, in work on difference equations of mathematical physics.
In practice it sets the largest stable time step of explicit methods, such as $\Delta t \le \Delta x / \Lambda$.
Implicit schemes have a numerical domain of dependence equal to the whole grid, so the argument places no restriction on them.
Sufficient conditions come from stability analysis, and the [[Lax equivalence theorem|D5M7TRD3MY]] links stability with convergence for consistent linear schemes.
In the [[Glimm scheme|Y70AC2X30T]] and [[Godunov's scheme|43HZJ7DRT0]], a CFL bound also keeps neighbouring Riemann problems from interacting.
