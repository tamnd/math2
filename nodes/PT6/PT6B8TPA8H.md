---
tag: PT6B8TPA8H
kind: definition
name: Fractional Brownian motion
msc: [60G22, 60G18, 60G15]
defines: VC6R7XSKRQ
uses: [22WEM6RTW0, 0KBFAWYRTE, 552AWX3QXN]
sources:
  - url: https://en.wikipedia.org/wiki/Fractional_Brownian_motion
---

## Definition

Let $H \in (0, 1)$.
A *fractional Brownian motion* with Hurst index $H$ is a real stochastic process $(B^H_t)_{t \ge 0}$ such that:

1. $(B^H_t)$ is a [[Gaussian process|22WEM6RTW0]] with $E[B^H_t] = 0$ for all $t \ge 0$.
2. Its [[covariance|0KBFAWYRTE]] is
$$E[B^H_s B^H_t] = \tfrac{1}{2}\bigl(s^{2H} + t^{2H} - \abs{t - s}^{2H}\bigr) \quad \text{for all } s, t \ge 0.$$
3. Almost surely, the path $t \mapsto B^H_t$ is continuous.

## Remarks

For $H = 1/2$ the covariance is $\frac{1}{2}(s + t - \abs{t - s}) = \min(s, t)$, so $B^{1/2}$ is a [[Wiener process|552AWX3QXN]].
Clause 2 gives $B^H_0 = 0$ and $E[(B^H_t - B^H_s)^2] = \abs{t - s}^{2H}$, so the increments are stationary and the process is [[self-similar|KS3KDRRJ58]] with index $H$.
The value $H = 1$ is excluded: the formula then gives covariance $st$, realised by the degenerate process $t \xi$ with $\xi$ standard normal, which has no randomness in its shape.
Disjoint increments are positively correlated for $H > 1/2$ and negatively correlated for $H < 1/2$.
Almost every path is Hölder continuous of every order less than $H$, and for $H \ne 1/2$ the process is not a [[semimartingale|MZNFPJJMY9]].
