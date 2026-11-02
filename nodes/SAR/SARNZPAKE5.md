---
tag: SARNZPAKE5
kind: definition
name: Kolmogorov–Smirnov test
msc: [62G10, 62G30]
defines: YZYHWC6C5F
uses: [A05WR6TEK5, 087P03NEND, 0MXMS3AE13, 0AJN7WHBJZ]
sources:
  - url: https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test
---

## Definition

Let $X_1, \dots, X_n$ be [[i.i.d.|0AJN7WHBJZ]] real random variables with [[cumulative distribution function|0MXMS3AE13]] $F$, and let $F_n$ be their [[empirical distribution function|A05WR6TEK5]].
Let $F_0$ be a fixed continuous cumulative distribution function.
The *one-sample Kolmogorov–Smirnov statistic* is
$$D_n = \sup_{x \in \R} \abs{F_n(x) - F_0(x)}.$$
The *Kolmogorov–Smirnov test* of the null hypothesis $H_0 \colon F = F_0$ at level $\alpha$ rejects $H_0$ when $D_n > c_{n, \alpha}$, where $c_{n, \alpha}$ is chosen so that $P(D_n > c_{n, \alpha}) \le \alpha$ under $H_0$.

Let two independent i.i.d. samples of sizes $n$ and $m$ have empirical distribution functions $F_n$ and $G_m$.
The *two-sample statistic* is $D_{n,m} = \sup_{x} \abs{F_n(x) - G_m(x)}$.
It tests whether the two samples have the same continuous distribution.

## Remarks

Under $H_0$ the law of $D_n$ is the same for every continuous $F_0$, because $F_0(X_i)$ is uniform on $[0, 1]$.
As $n \to \infty$, $\sqrt{n} D_n$ converges in distribution to the Kolmogorov distribution, the law of $\sup_{0 \le t \le 1} \abs{B(t)}$ for a [[Brownian bridge|3MCVMBAGD1]] $B$:
$$\lim_{n \to \infty} P(\sqrt{n} D_n \le t) = 1 - 2 \sum_{k=1}^{\infty} (-1)^{k-1} e^{-2k^2 t^2}, \qquad t > 0.$$
For ordered data $x_{(1)} \le \dots \le x_{(n)}$ the supremum is a finite maximum: $D_n = \max_{i} \max\big(i/n - F_0(x_{(i)}), \, F_0(x_{(i)}) - (i - 1)/n\big)$.

Example: $n = 1$, $X_1 = 0.3$ and $F_0(x) = x$ on $[0, 1]$.
Then $F_1$ jumps from $0$ to $1$ at $0.3$, and $D_1 = \max(0.3, 1 - 0.3) = 0.7$.

Non-example: testing normality with the mean and variance estimated from the same data is not this test.
Then $F_0$ is not fixed in advance, and the null law of $D_n$ changes; the corrected procedure is the Lilliefors test.
