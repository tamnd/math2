---
tag: 0TJ8QBJX5K
kind: statement
role: theorem
name: Term-by-term differentiation
msc: [40A30, 26A24]
uses: [0CS42KEM5C, 0MRE6XRE5V]
sources:
  - url: https://en.wikipedia.org/wiki/Function_series
    locator: Convergence
---

## Statement

Let $a < b$, and let $f_n \colon [a, b] \to \mathbb{R}$ be differentiable for each $n \ge 0$.
Assume that $\sum_{n} f_n(x_0)$ converges for some $x_0 \in [a, b]$, and that $\sum_{n} f_n'$ converges uniformly on $[a, b]$.
Then $\sum_{n} f_n$ converges uniformly on $[a, b]$, its sum is differentiable, and
$$\Big( \sum_{n=0}^{\infty} f_n \Big)' = \sum_{n=0}^{\infty} f_n'.$$

## Remarks

Apply [[the theorem on sequences|0CS42KEM5C]] to the partial sums.
The derivative series often converges uniformly by the M-test. Mathlib states that form as `hasDerivAt_tsum`.
Power series satisfy the hypotheses on each closed interval inside the interval of convergence.

## Explanations

### L1 human

We may differentiate a series term by term, if the series of derivatives converges uniformly.
Then the derivative of the sum is the sum of the derivatives.
