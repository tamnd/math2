---
tag: GYNYT7KTC3
kind: statement
role: theorem
name: Broyden's method
msc: [65H10]
uses: [07EXVNF9VP, 047NDTEPCV, 0AW1E6YTJY, YWZQC5E54B, 0EB9N0S33C, JT8Q204E4R, 9ZC177PVPC]
about: [07EXVNF9VP]
sources:
  - url: https://en.wikipedia.org/wiki/Broyden%27s_method
same_as:
  wikidata: Q761993
  wikipedia: Broyden's method
---

## Statement

Let $U \subseteq \R^n$ be open and let $F \colon U \to \R^n$ be continuously differentiable, with [[Jacobian matrix|047NDTEPCV]] $J(x)$.
Let $x^* \in U$ satisfy $F(x^*) = 0$, let $J(x^*)$ be [[invertible|0EB9N0S33C]], and let $J$ be [[Lipschitz continuous|0AW1E6YTJY]] near $x^*$.
*Broyden's method* starts from $x_0 \in U$ and an invertible $n \times n$ matrix $B_0$, and for $k \ge 0$ sets
$$x_{k+1} = x_k - B_k^{-1} F(x_k), \qquad s_k = x_{k+1} - x_k, \qquad y_k = F(x_{k+1}) - F(x_k),$$
$$B_{k+1} = B_k + \frac{(y_k - B_k s_k) \, s_k^T}{s_k^T s_k}.$$
Then there are $\varepsilon > 0$ and $\delta > 0$ such that, if $\norm{x_0 - x^*} < \varepsilon$ and $\norm{B_0 - J(x^*)} < \delta$, the iterates are defined and $x_k \to x^*$ superlinearly:
$$\lim_{k \to \infty} \frac{\norm{x_{k+1} - x^*}}{\norm{x_k - x^*}} = 0,$$
whenever $x_k \ne x^*$ for all $k$.

## Remarks

The update makes $B_{k+1}$ satisfy the secant equation $B_{k+1} s_k = y_k$, the analogue of the [[secant method|9ZC177PVPC]] slope in several variables.
Among all matrices that satisfy it, $B_{k+1}$ is the closest to $B_k$ in the [[Frobenius norm|JT8Q204E4R]], and $B_{k+1} - B_k$ has rank at most $1$.
By the Sherman–Morrison formula, $B_{k+1}^{-1}$ is obtained from $B_k^{-1}$ in $O(n^2)$ operations, so no linear system has to be solved from scratch.
The proof first shows that the errors decrease linearly while $B_k$ stays close to $J(x^*)$, and then that $(B_k - J(x^*)) s_k / \norm{s_k} \to 0$, which is the Dennis–Moré condition for superlinear [[convergence|YWZQC5E54B]].
The matrices $B_k$ need not converge to $J(x^*)$.
For $n = 1$ the method is the secant method.

## Explanations

### L1 human

[[Newton's method|07EXVNF9VP]] for a system of equations needs the full matrix of derivatives at every step, which can be expensive.
Broyden's method guesses this matrix once and then corrects the guess cheaply after each step, using only the change in the function values.
It is slower than Newton's method near the solution, but each step is much cheaper.

### L2 human

Broyden's method is the first and simplest quasi-Newton method for nonlinear systems.
Its update is the model for the BFGS and DFP updates in optimization, which keep the matrix symmetric.
In practice $B_0$ is often a finite-difference Jacobian, and a line search or trust region makes the method converge from farther away.
