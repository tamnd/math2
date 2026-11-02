---
tag: PKGADWXPYH
kind: statement
role: theorem
name: Mercer's theorem
msc: [45C05, 47B10, "46E22"]
uses: [ZM5G144PZG, ADTYF8FG6C, 4NSACSWRJZ, 0XRRYF1HPE, 08VZ57PT26, A1G25R99PY]
about: [ADTYF8FG6C]
sources:
  - url: https://en.wikipedia.org/wiki/Mercer%27s_theorem
same_as:
  wikidata: Q1716166
  wikipedia: Mercer's theorem
---

## Statement

Let $a < b$ and let $K \colon [a, b] \times [a, b] \to \R$ be a [[continuous kernel|ZM5G144PZG]] that is [[symmetric|ADTYF8FG6C]], $K(x, y) = K(y, x)$, and positive semidefinite: for every $m \ge 1$, all $x_1, \dots, x_m \in [a, b]$ and all $c_1, \dots, c_m \in \R$,
$$\sum_{i=1}^{m} \sum_{j=1}^{m} c_i c_j K(x_i, x_j) \ge 0.$$
Let $T_K$ be the integral operator $(T_K \varphi)(x) = \int_a^b K(x, y) \varphi(y) \, dy$ on $L^2[a, b]$.
Then there are an orthonormal family $(e_n)_{n \in N}$ in $L^2[a, b]$, finite or countable, of continuous [[eigenfunctions|4NSACSWRJZ]] of $T_K$, and eigenvalues $\mu_n > 0$, such that:

1. the $\mu_n$ are all the nonzero eigenvalues of $T_K$, each repeated as often as the dimension of its eigenspace;
2. for all $x, y \in [a, b]$,
$$K(x, y) = \sum_{n \in N} \mu_n \, e_n(x) \, e_n(y),$$
where the series converges absolutely and [[uniformly|08VZ57PT26]] on $[a, b] \times [a, b]$;
3. $\sum_{n \in N} \mu_n = \int_a^b K(x, x) \, dx$.

## Remarks

Positivity of the kernel gives $\ip{T_K \varphi}{\varphi} \ge 0$ for all $\varphi$, so all eigenvalues are nonnegative.
Positivity of the remainder kernel $K(x, y) - \sum_{n \le m} \mu_n e_n(x) e_n(y)$ gives $\sum_{n \le m} \mu_n e_n(x)^2 \le K(x, x)$ for every $m$.
So the diagonal series converges pointwise, and one shows its sum is $K(x, x)$, a continuous function.
[[Dini's theorem|0XRRYF1HPE]] then makes the convergence on the diagonal uniform, and the Cauchy–Schwarz inequality transfers this to the whole square.
Part 3 is part 2 on the diagonal, integrated.

Example: $K(x, y) = \min(x, y)$ on $[0, 1]$ is the covariance of Brownian motion, hence positive semidefinite.
Its expansion is $\min(x, y) = \sum_{n \ge 1} \frac{2 \sin\left((n - \tfrac12)\pi x\right) \sin\left((n - \tfrac12)\pi y\right)}{(n - \tfrac12)^2 \pi^2}$, uniformly on the square.
On the diagonal, part 3 gives $\sum_{n \ge 1} \frac{1}{(n - \frac12)^2 \pi^2} = \int_0^1 x \, dx = \frac12$.

Without positivity, the conclusions can fail: for a general continuous symmetric kernel the expansion is only guaranteed in $L^2$, and $\sum \abs{\mu_n}$ may diverge.

## Explanations

### L1 human

A positive kernel is the infinite analogue of a positive semidefinite symmetric matrix.
Such a matrix is a sum of rank-one pieces built from its eigenvectors, with nonnegative weights.
Mercer's theorem says the same for continuous positive kernels, and the sum converges as well as one could hope, uniformly at every pair of points.

### L2 human

The theorem upgrades the [[spectral theorem for compact self-adjoint operators|A1G25R99PY]], which gives only $L^2$ convergence, to uniform convergence of the kernel itself.
It is the basis of the Karhunen–Loève expansion of a stochastic process with continuous covariance.
In machine learning it explains why a positive kernel is an inner product of feature vectors $(\sqrt{\mu_n} e_n(x))_n$, which leads to reproducing kernel Hilbert spaces.
