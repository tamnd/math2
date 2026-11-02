---
tag: 5WYZPX1ZVW
kind: statement
role: theorem
name: Bilinear series of a symmetric kernel
msc: [45C05, 47B10]
uses: [WWMWX7AD4V, 2ZB3NFZ94T, 4NSACSWRJZ, DC7HMHVREP, A1G25R99PY, 047RFCNVSK, 0S9GGTR0EX]
about: [2ZB3NFZ94T]
sources:
  - url: https://en.wikipedia.org/wiki/Mercer%27s_theorem
---

## Statement

Let $a < b$ and let $K \in L^2([a, b] \times [a, b])$ be a [[square-integrable kernel|WWMWX7AD4V]] that is [[Hermitian|2ZB3NFZ94T]]: $K(y, x) = \overline{K(x, y)}$ for almost all $x, y$.
Let $(\varphi_n)_{n \in N}$ be an orthonormal family of [[eigenfunctions|4NSACSWRJZ]] of the integral operator $T_K$, with nonzero eigenvalues $\mu_n$.
Assume that, for each nonzero eigenvalue, the $\varphi_n$ with that eigenvalue form a basis of its eigenspace.
Let $\lambda_n = 1/\mu_n$ be the corresponding [[characteristic values|DC7HMHVREP]].
Then
$$K(x, y) = \sum_{n \in N} \mu_n \, \varphi_n(x) \overline{\varphi_n(y)} = \sum_{n \in N} \frac{\varphi_n(x) \overline{\varphi_n(y)}}{\lambda_n},$$
where the series converges in $L^2([a, b] \times [a, b])$, and
$$\sum_{n \in N} \mu_n^2 = \int_a^b \int_a^b \abs{K(x, y)}^2 \, dx \, dy.$$

## Remarks

The functions $\varphi_n(x) \overline{\varphi_m(y)}$ form an orthonormal family in $L^2([a, b]^2)$.
The coefficient of $K$ on $\varphi_n(x) \overline{\varphi_m(y)}$ is $\int \int K(x, y) \varphi_m(y) \overline{\varphi_n(x)} \, dy \, dx = \mu_m \ip{\varphi_m}{\varphi_n}$, which is $\mu_n$ if $m = n$ and $0$ otherwise.
So the series is the orthogonal projection of $K$ onto the span of this family.
The difference between $K$ and the series is a kernel with operator $T_K - \sum_n \mu_n \ip{\cdot}{\varphi_n} \varphi_n$.
This operator is $0$ by the [[spectral theorem for compact self-adjoint operators|A1G25R99PY]], so the difference is $0$ almost everywhere.
The identity for $\sum \mu_n^2$ is then [[Parseval's identity|047RFCNVSK]].

Example: for $K(x, y) = \min(x, y)$ on $[0, 1]$,
$$\min(x, y) = \sum_{n \ge 1} \frac{2 \sin\left((n - \tfrac12)\pi x\right) \sin\left((n - \tfrac12)\pi y\right)}{(n - \tfrac12)^2 \pi^2},$$
and the identity gives $\sum_{n \ge 1} \frac{1}{(n - \frac12)^4 \pi^4} = \int_0^1 \int_0^1 \min(x, y)^2 = \frac{1}{6}$.

In general the convergence is only in $L^2$.
Under the extra hypotheses of [[Mercer's theorem|PKGADWXPYH]], continuity and positivity of the kernel, the series converges absolutely and uniformly.

## Explanations

### L1 human

A symmetric kernel can be rebuilt from its eigenfunctions and eigenvalues.
Each eigenfunction contributes one simple product term, weighted by its eigenvalue.
This is the integral form of writing a symmetric matrix as a sum of rank-one pieces along its eigenvectors.

### L2 human

The bilinear series diagonalizes the kernel itself, not only the operator.
It gives the estimate $\sum \mu_n^2 < \infty$, so the characteristic values grow fast enough that $\sum 1/\lambda_n^2$ converges.
For positive continuous kernels it is upgraded to uniform convergence by Mercer's theorem, which also gives the trace formula $\sum \mu_n = \int K(x, x) \, dx$.
