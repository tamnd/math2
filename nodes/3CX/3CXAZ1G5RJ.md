---
tag: 3CXAZ1G5RJ
kind: statement
role: theorem
name: Hilbert–Schmidt expansion theorem
msc: [45C05, 47B07]
uses: [ZM5G144PZG, 2ZB3NFZ94T, 4NSACSWRJZ, A1G25R99PY, 0RBT5PB74K, 08VZ57PT26]
about: [4NSACSWRJZ, 2ZB3NFZ94T]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%E2%80%93Schmidt_theorem
---

## Statement

Let $a < b$ and let $K \colon [a, b] \times [a, b] \to \C$ be a [[continuous kernel|ZM5G144PZG]] that is [[Hermitian|2ZB3NFZ94T]]: $K(y, x) = \overline{K(x, y)}$ for all $x, y$.
Let $(\varphi_n)_{n \in N}$ be an orthonormal family of [[eigenfunctions|4NSACSWRJZ]] of $T_K \varphi = \int_a^b K(\cdot, y) \varphi(y) \, dy$, with real nonzero eigenvalues $\mu_n$.
Assume that, for each nonzero eigenvalue, the $\varphi_n$ with that eigenvalue form a basis of its eigenspace.
These eigenfunctions are continuous, since $\varphi_n = \mu_n^{-1} T_K \varphi_n$.
Let $h \in L^2[a, b]$ and $f = T_K h$, that is,
$$f(x) = \int_a^b K(x, y) \, h(y) \, dy.$$
Then for every $x \in [a, b]$,
$$f(x) = \sum_{n \in N} \ip{f}{\varphi_n} \varphi_n(x) = \sum_{n \in N} \mu_n \ip{h}{\varphi_n} \varphi_n(x),$$
where $\ip{u}{v} = \int_a^b u \overline{v}$, and the series converges absolutely and [[uniformly|08VZ57PT26]] on $[a, b]$.

## Remarks

For fixed $x$, the numbers $\mu_n \overline{\varphi_n(x)}$ are the Fourier coefficients of the function $y \mapsto \overline{K(x, y)}$, so [[Bessel's inequality|0RBT5PB74K]] gives $\sum_n \mu_n^2 \abs{\varphi_n(x)}^2 \le \int_a^b \abs{K(x, y)}^2 \, dy \le C$ for a constant $C$ independent of $x$.
The Cauchy–Schwarz inequality then bounds the tail $\sum_{n \ge m} \abs{\mu_n \ip{h}{\varphi_n} \varphi_n(x)}$ by $\sqrt{C} \left(\sum_{n \ge m} \abs{\ip{h}{\varphi_n}}^2\right)^{1/2}$, which tends to $0$ uniformly in $x$.
By the [[spectral theorem for compact self-adjoint operators|A1G25R99PY]], the series converges to $f$ in $L^2$; the uniform limit is continuous and so is $f$, hence they agree everywhere.

Example: for $K(x, y) = \min(x, y)$ on $[0, 1]$, the eigenfunctions are $\sqrt{2} \sin\left((n - \tfrac12) \pi x\right)$.
Every function $f = T_K h$ with $h \in L^2[0, 1]$ is continuous with $f(0) = 0$, and its expansion in these sines converges uniformly on $[0, 1]$.

The hypothesis $f = T_K h$ matters.
For a general function $f \in L^2[a, b]$, the eigenfunction series converges only in $L^2$.
Its sum is the orthogonal projection of $f$ onto the closed span of the $\varphi_n$, which may differ from $f$.

## Explanations

### L1 human

The eigenfunctions of a symmetric kernel are like the axes of an ellipse.
Any function produced by the integral operator can be written as a sum of these eigenfunctions.
The theorem says that this sum converges in the strongest usual sense, uniformly at every point.

### L2 human

This is the classical form of the [[spectral theorem for compact self-adjoint operators|A1G25R99PY]], adapted to continuous kernels.
It is used to solve the Fredholm equation of the second kind with a symmetric kernel: the solution of $\varphi - \lambda T_K \varphi = f$, for $\lambda$ not a characteristic value, is $\varphi = f + \lambda \sum_n \frac{\mu_n \ip{f}{\varphi_n}}{1 - \lambda \mu_n} \varphi_n$.
Through Green's functions it gives the uniform convergence of eigenfunction expansions for Sturm–Liouville problems.
