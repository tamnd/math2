---
tag: BP8S3Z5TW9
kind: definition
name: Convergence in measure
msc: [28A20]
defines: G5WT6QN8WR
uses: [P15VQS5DJ9, YYNCJSR0PJ]
sources:
  - url: https://en.wikipedia.org/wiki/Convergence_in_measure
---

## Definition

Let $(X, \Sigma, \mu)$ be a [[measure space|P15VQS5DJ9]], and let $f_1, f_2, \ldots$ and $f$ be [[measurable functions|YYNCJSR0PJ]] from $X$ to $\R$.
The sequence $(f_n)$ *converges in measure* to $f$ if for every $\varepsilon > 0$
$$\lim_{n \to \infty} \mu\big(\set{x \in X : \abs{f_n(x) - f(x)} \ge \varepsilon}\big) = 0.$$

## Remarks

Example: on $[0, 1]$ with Lebesgue measure, write $n = 2^k + j$ with $0 \le j < 2^k$ and let $f_n = \mathbf{1}_{[j 2^{-k}, (j+1) 2^{-k}]}$.
For $0 < \varepsilon \le 1$, the set where $\abs{f_n} \ge \varepsilon$ has measure $2^{-k}$, which tends to $0$, so $f_n \to 0$ in measure.
But each $x \in [0, 1]$ has $f_n(x) = 1$ for infinitely many $n$, so $f_n(x)$ converges for no $x$.
Non-example: on $\R$ with Lebesgue measure, $f_n = \mathbf{1}_{[n, n+1]}$ tends to $0$ at every point, but the set where $\abs{f_n} \ge 1/2$ has measure $1$ for all $n$.
A local variant asks the limit to be $0$ only for the restriction to each set of finite measure.
Convergence in $L^p$ for some $1 \le p < \infty$ implies convergence in measure, by Chebyshev's inequality.
