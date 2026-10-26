---
tag: 0SKVEMXJWF
kind: statement
role: theorem
name: Stability of linear systems via eigenvalues
msc: [34D20, 34A30]
uses: [0VJF99CZ0Z, 0YC8JT513J, 092S6VBECQ, 05Y1JAM3Y5]
sources:
  - url: https://en.wikipedia.org/wiki/Stability_theory
    locator: Linear autonomous systems
  - url: https://en.wikipedia.org/wiki/Lyapunov_stability
    locator: Stability for linear state space models
---

## Statement

Let $A$ be a real $n \times n$ matrix and consider the [[linear system with constant coefficients|0VJF99CZ0Z]] $x' = A x$ on $\mathbb{R}^n$, with the equilibrium point $0$.
(1) The point $0$ is [[asymptotically stable|05Y1JAM3Y5]] if and only if each eigenvalue $\lambda$ of $A$ has $\operatorname{Re} \lambda < 0$.
(2) If some eigenvalue $\lambda$ of $A$ has $\operatorname{Re} \lambda > 0$, then $0$ is unstable.
(3) The point $0$ is [[Lyapunov stable|092S6VBECQ]] if and only if two conditions hold. Each eigenvalue has $\operatorname{Re} \lambda \le 0$. Each eigenvalue with $\operatorname{Re} \lambda = 0$ has equal algebraic and geometric multiplicities.

## Remarks

The proof uses the [[matrix exponential|0YC8JT513J]]. The entries of $e^{tA}$ are sums of terms $t^k e^{\lambda t}$. Here $\lambda$ is an eigenvalue and $k$ is less than the size of its largest Jordan block.
In case (1), there are constants $C, \alpha > 0$ with $\|e^{tA}\| \le C e^{-\alpha t}$ for $t \ge 0$. So the origin is globally and exponentially stable.
For $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, both eigenvalues are $0$ but the solution $(t, 1)$ is unbounded. So $0$ is unstable, in accordance with (3).
The Routh–Hurwitz criterion tests the condition of (1) from the coefficients of the characteristic polynomial, without computing the roots.

## Explanations

### L1 human

For a linear system, the eigenvalues decide everything.
Eigenvalues with negative real part give decaying solutions, and an eigenvalue with positive real part gives a growing solution.
