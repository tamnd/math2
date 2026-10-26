---
tag: 0NX5NWAFC9
kind: statement
role: theorem
name: Weierstrass M-test
msc: [40A30]
uses: [0MRE6XRE5V, 04Z5G0THN6, 01XAY17QA3]
sources:
  - url: https://en.wikipedia.org/wiki/Weierstrass_M-test
    locator: Statement
same_as:
  wikidata: Q1072412
  wikipedia: Weierstrass M-test
---

## Statement

Let $S$ be a set and let $f_n \colon S \to \mathbb{R}$ for $n \ge 0$.
Assume that there are real numbers $M_n \ge 0$ with $|f_n(x)| \le M_n$ for all $n$ and all $x \in S$, and $\sum_{n=0}^{\infty} M_n < \infty$.
Then the [[series of functions|0MRE6XRE5V]] $\sum_{n=0}^{\infty} f_n$ converges absolutely and uniformly on $S$.

## Remarks

Absolute convergence at each $x$ follows from the [[comparison test|04Z5G0THN6]]. For $m < n$, $|s_n(x) - s_m(x)| \le \sum_{k=m+1}^{n} M_k$. So the partial sums are [[uniformly Cauchy|01XAY17QA3]].
For example, $\sum \frac{\sin(n x)}{n^2}$ converges uniformly on $\mathbb{R}$, with $M_n = 1/n^2$.
Mathlib states it as `tendstoUniformlyOn_tsum`.

## Explanations

### L1 human

If each function is bounded by a number, and these numbers have a finite sum, then the series of functions converges uniformly.
The bounds do not depend on $x$, so the convergence is the same everywhere.
