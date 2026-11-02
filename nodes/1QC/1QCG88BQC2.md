---
tag: 1QCG88BQC2
kind: definition
name: Finite difference method
msc: [65M06, 65N06]
defines: X7HYEBA5SA
uses: [GC5BDZ6QBC, 09EGC6F8PT]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_difference_method
---

## Definition

Let a [[partial differential equation|GC5BDZ6QBC]] $\mathcal{L} u = f$ be given on a domain $\Omega \subseteq \R^d$, possibly with time, together with boundary or initial conditions.
The *finite difference method* consists of:

1. A grid: finitely many points $x_j$ of $\overline{\Omega}$, usually $x_j = jh$ with mesh size $h > 0$, and time levels $t_n = nk$ with time step $k > 0$.
2. Difference quotients: each [[partial derivative|09EGC6F8PT]] in $\mathcal{L}$ is replaced by a linear combination of grid values, such as $(u_{j+1} - u_j)/h$ for $\partial_x u$ or $(u_{j+1} - 2u_j + u_{j-1})/h^2$ for $\partial_x^2 u$.
3. The discrete problem: the resulting algebraic equations and the discretized side conditions are solved for the grid values $u_j \approx u(x_j)$.

## Remarks

The local truncation error is the residual left when the exact solution is put into the scheme.
The scheme is consistent of order $p$ if this error is $O(h^p)$; for example, Taylor expansion gives $\frac{u(x+h) - 2u(x) + u(x-h)}{h^2} = u''(x) + \frac{h^2}{12} u^{(4)}(\xi)$ for some $\xi$ in $(x - h, x + h)$ when $u \in C^4$.
Example: for the heat equation $u_t = u_{xx}$, the explicit scheme is $u_j^{n+1} = u_j^n + r (u_{j+1}^n - 2u_j^n + u_{j-1}^n)$ with $r = k/h^2$.
It is consistent of order $1$ in $k$ and $2$ in $h$.
It is stable in the maximum norm when $r \le \tfrac12$, since then $u_j^{n+1}$ is a convex combination of $u_{j-1}^n, u_j^n, u_{j+1}^n$.
Non-example: the finite element method also yields algebraic equations on a mesh, but it does not satisfy clause 2.
It imposes the equation in weak form against basis functions instead of replacing derivatives by difference quotients.
