---
tag: MPB3QF09E5
kind: statement
role: theorem
name: Picard's criterion for first-kind equations
msc: [45Q05, 47A52, 45B05]
uses: [HM2HHE3J51, M2NEP1K5AE, QSJKPKPM7H, 6HSJBJ8TTQ]
about: [QSJKPKPM7H]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_value_decomposition
---

## Statement

Let $X$ and $Y$ be [[Hilbert spaces|HM2HHE3J51]] and let $K \colon X \to Y$ be a [[compact linear operator|M2NEP1K5AE]] with [[adjoint|6HSJBJ8TTQ]] $K^*$.
Let $(\sigma_n, v_n, u_n)_{n \in N}$ be a singular system of $K$, with $N$ finite or $N = \set{1, 2, \dots}$.
This means that the $\sigma_n > 0$ are the nonzero [[singular values|QSJKPKPM7H]] of $K$, and $K v_n = \sigma_n u_n$ and $K^* u_n = \sigma_n v_n$.
It also means that $(v_n)$ is an orthonormal basis of $\ker(K)^\perp$ and $(u_n)$ is an orthonormal basis of the closure of $K(X)$.
Let $y \in Y$.
Then the equation $K x = y$ has a solution $x \in X$ if and only if

1. $y \in \ker(K^*)^\perp$, and
2. $\displaystyle \sum_{n \in N} \frac{\abs{\ip{y}{u_n}}^2}{\sigma_n^2} < \infty$.

In this case $x^\dagger = \sum_{n \in N} \sigma_n^{-1} \ip{y}{u_n} v_n$ is a solution, and it is the unique solution of smallest norm.

## Remarks

Proof idea: if $K x = y$, then $y \perp \ker(K^*)$ and $\ip{y}{u_n} = \ip{x}{K^* u_n} = \sigma_n \ip{x}{v_n}$, so the sum in clause 2 equals $\sum_n \abs{\ip{x}{v_n}}^2 \le \norm{x}^2$ by Bessel's inequality.
Conversely, clause 2 makes the series for $x^\dagger$ converge.
Then $K x^\dagger = \sum_n \ip{y}{u_n} u_n$ is the orthogonal projection of $y$ onto the closure of $K(X)$, which is $\ker(K^*)^\perp$.
Clause 1 makes it equal to $y$.
The solution $x^\dagger$ lies in $\ker(K)^\perp$, so it has the smallest norm among all solutions.

Example: the Volterra operator $(V x)(t) = \int_0^t x(s) \, ds$ on $L^2(0, 1)$ is injective with dense range.
Its singular system is $\sigma_n = \frac{2}{(2n - 1)\pi}$, $v_n(s) = \sqrt{2} \cos\big((n - \tfrac{1}{2}) \pi s\big)$ and $u_n(t) = \sqrt{2} \sin\big((n - \tfrac{1}{2}) \pi t\big)$.
So $V x = y$ is solvable if and only if $\sum_n (2n - 1)^2 \abs{\ip{y}{u_n}}^2 < \infty$, a condition on the decay of the coefficients of $y$ that expresses the differentiability of $y$.

## Explanations

### L1 human

A compact operator shrinks the component of $x$ along the $n$-th singular direction by the factor $\sigma_n$, and these factors tend to zero.
To undo it one must divide the components of the data by $\sigma_n$.
Picard's criterion says that the equation can be solved exactly when the result of these divisions still has finite energy.
Data whose components do not decay fast enough, for example noisy data, are not in the range.

### L2 human

The criterion is the infinite-dimensional form of solving a linear system by the singular value decomposition, see [[singular value decomposition|000NPTMX6J]].
It shows the [[ill-posedness of first-kind equations|KHXYWTNN2R]] in a quantitative way: an error of size $\delta$ in the coefficient $\ip{y}{u_n}$ becomes an error $\delta / \sigma_n$ in the solution.
The faster the singular values decay, the smoother the data must be, and the more ill posed the problem.
Regularization methods such as truncated singular value expansion and Tikhonov regularization replace the factors $1/\sigma_n$ by bounded filter factors.
The map $y \mapsto x^\dagger$ is the [[Moore–Penrose inverse|0YY8VX28JR]] of $K$ on its natural domain.
