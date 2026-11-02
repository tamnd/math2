---
tag: 2Z7NASDQB6
kind: statement
role: theorem
name: von Neumann stability analysis
msc: [65M12, 65M06]
uses: [X7HYEBA5SA, RXFJ47VYGX, D5M7TRD3MY, MTCRZC5QKT, FQVVNYV6N8]
about: [X7HYEBA5SA]
sources:
  - url: https://en.wikipedia.org/wiki/Von_Neumann_stability_analysis
---

## Statement

Let $\Delta x > 0$ and $\Delta t > 0$.
Consider a linear two-level [[finite difference|X7HYEBA5SA]] scheme on the grid $\Delta x \Z$:
$$\sum_{k=-K}^{K} b_k\, u_{j+k}^{n+1} = \sum_{k=-K}^{K} c_k\, u_{j+k}^n, \qquad j \in \Z,\ n \ge 0.$$
The unknown is scalar, and the complex coefficients $b_k$, $c_k$ do not depend on $j$ or $n$.
Assume that $\beta(\xi) = \sum_k b_k e^{i k \xi}$ has no zero for $\xi \in [-\pi, \pi]$.
The amplification factor of the scheme is
$$g(\xi) = \frac{\sum_k c_k e^{i k \xi}}{\sum_k b_k e^{i k \xi}}, \qquad \xi \in [-\pi, \pi].$$
The coefficients may depend on $\Delta t$ and $\Delta x$ through a relation $\Delta t = \Lambda(\Delta x)$ fixed in advance.
Use the norm $\norm{u}^2 = \Delta x \sum_j \abs{u_j}^2$.
The scheme is called stable if for each $T > 0$ there is $C_T$ with $\norm{u^n} \le C_T \norm{u^0}$ whenever $n \Delta t \le T$.
The scheme is stable if and only if there are constants $K_0$ and $\tau > 0$ such that
$$\abs{g(\xi)} \le 1 + K_0 \Delta t \qquad \text{for all } \xi \in [-\pi, \pi] \text{ and all } 0 < \Delta t \le \tau.$$
If $g$ does not depend on $\Delta t$, the condition is $\abs{g(\xi)} \le 1$ for all $\xi$.

## Remarks

The proof uses the [[discrete-time Fourier transform|RXFJ47VYGX]] $\hat u(\xi) = \Delta x \sum_j u_j e^{-i j \xi}$, which turns the scheme into $\hat u^{n+1}(\xi) = g(\xi)\, \hat u^n(\xi)$, so $\hat u^n = g^n \hat u^0$.
By Parseval's identity, $\norm{u^n}$ equals the $L^2$ norm of $g^n \hat u^0$ up to a constant factor, so stability is equivalent to a bound on $\sup_\xi \abs{g(\xi)}^n$ for $n \Delta t \le T$.
This bound holds exactly when $\abs{g} \le 1 + K_0 \Delta t$, because $(1 + K_0 \Delta t)^n \le e^{K_0 T}$.
Example: the [[upwind scheme|MTCRZC5QKT]] $u_j^{n+1} = u_j^n - \nu (u_j^n - u_{j-1}^n)$ for $u_t + a u_x = 0$, with $\nu = a \Delta t / \Delta x$, has $\abs{g(\xi)}^2 = 1 - 2 \nu (1 - \nu)(1 - \cos \xi)$; this is at most $1$ for all $\xi$ exactly when $0 \le \nu \le 1$, which is the [[Courant–Friedrichs–Lewy condition|FQVVNYV6N8]] for this scheme.
For systems of equations, the analogous condition on the spectral radius of the amplification matrix is necessary but not sufficient in general.
For variable coefficients or boundaries, the analysis is only a heuristic test.

## Explanations

### L1 human

Errors in a computed solution can be written as a sum of waves of different frequencies.
For a linear scheme with constant coefficients, each wave is multiplied by a fixed factor at every time step.
If some factor has size larger than one, that wave grows exponentially and ruins the computation; if all factors have size at most one, nothing blows up.
Von Neumann analysis computes these factors and checks this condition.

### L2 human

The analysis is the practical tool to test a new difference scheme: substitute $u_j^n = g^n e^{i j \xi}$ and solve for $g$.
Combined with consistency, stability gives convergence by the [[Lax equivalence theorem|D5M7TRD3MY]].
The term $K_0 \Delta t$ allows schemes for equations with lower-order terms, such as $u_t = u_{xx} + u$, whose exact solutions also grow.
