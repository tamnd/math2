---
tag: ~2ade9cef
kind: statement
role: theorem
name: p-series test
msc: [40A05]
uses: [~b727755f, ~2c6dfc1d, ~7ee8b747]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_series_(mathematics)
    locator: Riemann zeta function
---

## Statement

Let $p$ be a real number.
The series $\sum_{n=1}^{\infty} \frac{1}{n^p}$ converges if and only if $p > 1$.

## Remarks

For $p = 1$ it is the [[harmonic series|~69b94ce4]], which diverges. For $p \le 0$ the terms do not tend to $0$.
One proof uses the [[Cauchy condensation test|~7ee8b747]]. The condensed series is $\sum 2^n \cdot 2^{-np} = \sum (2^{1-p})^n$, a geometric series with ratio $2^{1-p}$.
Another proof uses the [[integral test|~2af9eb66]] with $f(x) = x^{-p}$.
For $p > 1$ the sum is the value $\zeta(p)$ of the Riemann zeta function. For example, $\zeta(2) = \pi^2/6$, which is the [[Basel problem|~80048ce3]].

## Explanations

### L1 human

The terms $1/n^p$ shrink faster when $p$ is larger.
The value $p = 1$ is the border. Above it the sum is finite, and at it or below it the sum is infinite.
