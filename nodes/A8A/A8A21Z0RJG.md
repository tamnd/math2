---
tag: A8A21Z0RJG
kind: definition
name: Mittag-Leffler summation
msc: ["40G10", "33E12"]
defines: MT5JZ63RD4
uses: [8X25Q4XYMN, 0JH4MN4K1C, 0V3FZMVB4K, 0909PWZR62]
sources:
  - url: https://en.wikipedia.org/wiki/Mittag-Leffler_summation
---

## Definition

Let $\sum_{k \ge 0} a_k$ be a [[series|0JH4MN4K1C]] of complex numbers, and let $\Gamma$ be the [[gamma function|0V3FZMVB4K]].
For $\alpha > 0$ put
$$M(\alpha) = \sum_{k \ge 0} \frac{a_k}{\Gamma(1 + \alpha k)}$$
whenever this series converges.
The series $\sum a_k$ is *Mittag-Leffler summable* to $s$ if $M(\alpha)$ is defined for all small $\alpha > 0$ and the [[one-sided limit|0909PWZR62]] $\lim_{\alpha \to 0^+} M(\alpha)$ equals $s$.

## Remarks

For $a_k = z^k$ one gets $M(\alpha) = \sum_{k \ge 0} \frac{z^k}{\Gamma(1 + \alpha k)}$, the Mittag-Leffler function $E_\alpha(z)$.

Example: let $\sum a_k$ converge absolutely to $s$.
Since $\Gamma(x) \ge \frac12$ for all $x \ge 1$, one has $\abs{a_k / \Gamma(1 + \alpha k)} \le 2 \abs{a_k}$ for all $\alpha$ and $k$.
Each term tends to $a_k$ as $\alpha \to 0^+$, so by dominated convergence for series $M(\alpha) \to s$.

Non-example: for $1 + 1 + 1 + \cdots$, the terms $1/\Gamma(1 + \alpha k)$ are positive and tend to $1$ for each $k$.
So for each $N$, $M(\alpha) \ge \sum_{k=0}^{N} \frac{1}{\Gamma(1 + \alpha k)} \to N + 1$ as $\alpha \to 0^+$, and $M(\alpha)$ has no finite limit.
