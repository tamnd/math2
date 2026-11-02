---
tag: H1HWSWME6B
kind: statement
role: theorem
name: Liouville–Neumann series
msc: [45B05, 45L05]
uses: [8KJCN49V64, ZM5G144PZG, 9QNBFERMHD, 0NX5NWAFC9, 8QJ91709V2]
about: [8KJCN49V64, 9QNBFERMHD]
sources:
  - url: https://en.wikipedia.org/wiki/Liouville%E2%80%93Neumann_series
same_as:
  wikidata: Q4402528
  wikipedia: Liouville–Neumann series
---

## Statement

Let $a < b$, let $K \colon [a, b] \times [a, b] \to \C$ be a [[continuous kernel|ZM5G144PZG]] with $M = \max \abs{K}$, and let $K_n$ be its [[iterated kernels|9QNBFERMHD]].
Let $f \colon [a, b] \to \C$ be continuous and let $\lambda \in \C$ with $\abs{\lambda} M (b - a) < 1$.
Then the series
$$\varphi(x) = f(x) + \sum_{n=1}^{\infty} \lambda^n \int_a^b K_n(x, s) f(s) \, ds$$
converges absolutely and uniformly on $[a, b]$.
Its sum $\varphi$ is the unique continuous solution of the [[integral equation of the second kind|8KJCN49V64]]
$$\varphi(x) = f(x) + \lambda \int_a^b K(x, s) \varphi(s) \, ds, \quad x \in [a, b].$$

## Remarks

Proof idea: $\abs{K_n} \le M^n (b - a)^{n-1}$, so the $n$-th term is bounded by $\max \abs{f} \cdot (\abs{\lambda} M (b - a))^n$, and the [[Weierstrass M-test|0NX5NWAFC9]] gives uniform convergence.
Substituting the series into the equation and integrating term by term shows that $\varphi$ is a solution.
If $\psi$ is a second continuous solution, then $\max \abs{\varphi - \psi} \le \abs{\lambda} M (b - a) \max \abs{\varphi - \psi}$, so $\varphi = \psi$.
This is the [[Neumann series|8QJ91709V2]] $(I - \lambda K)^{-1} = \sum_{n \ge 0} \lambda^n K^n$ for the integral operator on continuous functions with the maximum norm.

Example: for $K = 1$ on $[0, 1]$ and $\abs{\lambda} < 1$, all $K_n = 1$, and the series gives $\varphi = f + \frac{\lambda}{1 - \lambda} \int_0^1 f$.
The condition on $\lambda$ cannot be dropped in general: for $\lambda = 1$ the equation $\varphi = f + \int_0^1 \varphi$ has no solution when $\int_0^1 f \ne 0$.
For Volterra kernels the bound improves to $\abs{K_n(x, s)} \le M^n (x - s)^{n-1} / (n-1)!$, and the series converges for every $\lambda$.

## Explanations

### L1 human

The equation says that the unknown is $f$ plus a small correction computed from the unknown itself.
Start from $f$, compute the correction, add it, and repeat.
When $\lambda$ is small, each round changes the answer less, and the rounds add up to the exact solution.

### L2 human

The partial sums of the series are the iterates $\varphi_0 = f$, $\varphi_{k} = f + \lambda K \varphi_{k-1}$ of the method of successive approximations.
Collecting the terms gives the resolvent kernel $R = \sum_{n \ge 1} \lambda^{n-1} K_n$ and the formula $\varphi = f + \lambda \int R f$.
The series in $\lambda$ converges for $\abs{\lambda}$ below the smallest absolute value of a characteristic value of $K$, and for all $\lambda$ if there is none.
Beyond that disc one needs Fredholm determinants or the theory of compact operators.
