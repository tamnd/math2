---
tag: GTJ6KBD4PX
kind: definition
name: Zeta-regularized determinant
msc: [58J52, 11M41]
defines: YT3ZQ2F7FG
uses: [VJCJYXGTDY, MT9P2X85V8, 0NEGN5CRSC, T1039Q9FY0]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_determinant
---

## Definition

Let $M$ be a closed smooth manifold of dimension $n$ with a Hermitian vector bundle $E$.
Let $A$ be a formally [[self-adjoint|0NEGN5CRSC]] [[elliptic differential operator|MT9P2X85V8]] of order $m > 0$ on $E$, with nonnegative spectrum.
Let $0 < \mu_1 \le \mu_2 \le \cdots$ be its nonzero eigenvalues, counted with multiplicity.
Its spectral zeta function $\zeta_A(s) = \sum_{j \ge 1} \mu_j^{-s}$ converges for $\operatorname{Re} s > n/m$ and has a meromorphic continuation to $\C$ that is holomorphic at $s = 0$.
The *zeta-regularized determinant* of $A$ is
$$\det{}'_\zeta A = \exp\big( -\zeta_A'(0) \big).$$
If $\ker A = 0$ it is written $\det_\zeta A$.

## Remarks

It is the [[zeta-regularized product|VJCJYXGTDY]] of the nonzero eigenvalues.
For the Laplace–Beltrami operator, $\zeta_A$ is the [[Minakshisundaram–Pleijel zeta function|T1039Q9FY0]].
If $A$ were a positive definite matrix, $-\zeta_A'(0) = \sum_j \log \mu_j$ and the definition would give the usual determinant.
The regularized determinant is not multiplicative in general: $\det_\zeta(AB)$ may differ from $\det_\zeta A \det_\zeta B$ by a multiplicative anomaly.

Example: on $S^1 = \R / 2\pi\Z$ let $A = -d^2/d\theta^2$.
The nonzero eigenvalues are $k^2$ with multiplicity $2$, so $\zeta_A(s) = 2\zeta(2s)$ and $\zeta_A'(0) = 4\zeta'(0) = -2 \log(2\pi)$, using $\zeta'(0) = -\tfrac12 \log(2\pi)$.
Hence $\det{}'_\zeta A = 4\pi^2$.

Non-example: the operator $-d^2/d\theta^2 - c$ with $0 < c < 1$ on $S^1$ has the negative eigenvalue $-c$.
It does not fit the definition, since $\mu^{-s}$ for $\mu < 0$ needs a choice of branch of the logarithm.
