---
tag: X1GZ9WKQEW
kind: definition
name: Wolff potential
msc: [31C45, 31B15]
defines: EBD8TWFNS0
uses: [HZNEQQBCW4, 1V2N8MFSHC]
sources:
  - url: https://en.wikipedia.org/wiki/P-Laplacian
---

## Definition

Let $n \ge 1$, let $1 < p < \infty$ and let $0 < \alpha < n/p$.
Let $\mu$ be a positive [[Radon measure|HZNEQQBCW4]] on $\R^n$, and let $B(x, t)$ be the open ball of center $x$ and radius $t$.
The *Wolff potential* of $\mu$ is the function $W^{\mu}_{\alpha, p} \colon \R^n \to [0, \infty]$ given by
$$W^{\mu}_{\alpha, p}(x) = \int_0^\infty \left( \frac{\mu\big(B(x, t)\big)}{t^{\,n - \alpha p}} \right)^{1/(p - 1)} \frac{dt}{t}.$$
For $R > 0$, the *truncated Wolff potential* $W^{\mu}_{\alpha, p}(x, R)$ is the same integral over $0 < t < R$.

## Remarks

Example: let $\mu = \delta_0$ be the unit point mass at $0$.
For $x \ne 0$, $\mu(B(x, t)) = 0$ when $t \le \abs{x}$ and $= 1$ when $t > \abs{x}$, so
$$W^{\delta_0}_{\alpha, p}(x) = \int_{\abs{x}}^\infty t^{-\frac{n - \alpha p}{p - 1} - 1} \, dt = \frac{p - 1}{n - \alpha p}\, \abs{x}^{-\frac{n - \alpha p}{p - 1}},$$
while $W^{\delta_0}_{\alpha, p}(0) = \infty$.
For $p = 2$, exchanging the order of integration gives $W^{\mu}_{\alpha, 2}(x) = \frac{1}{n - 2\alpha} \int \abs{x - y}^{2\alpha - n} \, d\mu(y)$, a multiple of the [[Riesz potential|1V2N8MFSHC]] of order $2\alpha$ of $\mu$.
The condition $\alpha < n/p$ is needed: if $\alpha p \ge n$ and $\mu \ne 0$, then $\mu(B(x, t))$ is bounded below for large $t$, the integrand does not decay fast enough, and $W^{\mu}_{\alpha, p} = \infty$ everywhere.
The truncated potential has no such problem and is used for local estimates.
The case $\alpha = 1$ is the one tied to the $p$-Laplace equation.
