---
tag: N1NA5MEFWX
kind: definition
name: Empirical distribution function
msc: [62G30]
defines: A05WR6TEK5
uses: [0AJN7WHBJZ, 0MXMS3AE13, 036756NFD6]
sources:
  - url: https://en.wikipedia.org/wiki/Empirical_distribution_function
    locator: Definition
---

## Definition

Let $X_1, \dots, X_n$ be real random variables, typically [[i.i.d.|0AJN7WHBJZ]] with [[cumulative distribution function|0MXMS3AE13]] $F$.
The *empirical distribution function* of the sample is the random function $\hat{F}_n \colon \R \to [0, 1]$ given by
$$\hat{F}_n(t) = \frac{1}{n} \sum_{i=1}^{n} \mathbf{1}\set{X_i \le t},$$
where $\mathbf{1}\set{X_i \le t}$ is $1$ if $X_i \le t$ and $0$ otherwise.

## Remarks

For each $\omega$, $\hat{F}_n$ is the distribution function of the empirical measure $\frac{1}{n}\sum_{i} \delta_{X_i(\omega)}$, so it is non-decreasing, right-continuous, and has limits $0$ and $1$ at $-\infty$ and $+\infty$.
Example: for the data $1, 2, 2, 5$, one has $\hat{F}_4(2) = 3/4$, because three of the four values are at most $2$.
Non-example: the function $t \mapsto \frac{1}{n}\#\set{i : X_i < t}$ uses strict inequality; it is left-continuous and is not a distribution function in the usual convention.
For fixed $t$ and an i.i.d. sample, $n \hat{F}_n(t)$ has the binomial distribution with parameters $n$ and $F(t)$.
So $\hat{F}_n(t)$ is an unbiased estimator of $F(t)$ with variance $F(t)(1 - F(t))/n$.
