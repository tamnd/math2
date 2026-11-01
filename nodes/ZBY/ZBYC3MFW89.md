---
tag: ZBYC3MFW89
kind: definition
name: Quadratic variation
msc: [60G44, 60H05]
defines: X4DHMZD5JA
uses: [0QH5ENKZM1, 0QA1HBD9Z4]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_variation
---

## Definition

Let $(X_t)_{t \ge 0}$ be a real [[stochastic process|0QH5ENKZM1]].
For a partition $\pi = \{0 = t_0 < t_1 < \dots < t_m = t\}$ of $[0, t]$, let $\norm{\pi} = \max_k (t_k - t_{k-1})$ be its mesh.
The process $X$ has *quadratic variation* $([X]_t)_{t \ge 0}$ if for every $t \ge 0$
$$[X]_t = \lim_{\norm{\pi} \to 0} \sum_{k=1}^{m} \bigl(X_{t_k} - X_{t_{k-1}}\bigr)^2,$$
where the limit is taken in [[probability|0QA1HBD9Z4]] over partitions $\pi$ of $[0, t]$.

## Remarks

A Wiener process $W$ has $[W]_t = t$.
Check: the sum $Q_\pi$ has mean $\sum_k (t_k - t_{k-1}) = t$ and variance $2 \sum_k (t_k - t_{k-1})^2 \le 2t \norm{\pi}$, so $Q_\pi \to t$ in $L^2$ and hence in probability.
A continuously differentiable function $f$ has $[f]_t = 0$, because $\sum_k (f(t_k) - f(t_{k-1}))^2 \le \max\abs{f'}^2 \, t \norm{\pi}$.
For [[fractional Brownian motion|VC6R7XSKRQ]] with Hurst index $H < 1/2$, the sums over uniform partitions tend to infinity, so the limit does not exist.
Every [[semimartingale|MZNFPJJMY9]] has a quadratic variation, given by $[X]_t = X_t^2 - X_0^2 - 2 \int_0^t X_{s-} \, dX_s$.
For a continuous [[local martingale|ZWJ9G89W3T]] $M$, $[M]$ is the unique continuous non-decreasing adapted process with $[M]_0 = 0$ such that $M^2 - [M]$ is a local martingale.
