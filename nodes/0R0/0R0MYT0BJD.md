---
tag: 0R0MYT0BJD
kind: statement
role: corollary
name: Continuity of the sum of a uniformly convergent series of functions
msc: [40A30, 26A15]
uses: [0MRE6XRE5V, 0X9XT05JVC, 0NX5NWAFC9]
sources:
  - url: https://en.wikipedia.org/wiki/Weierstrass_M-test
    locator: Statement
---

## Statement

Let $S \subseteq \mathbb{R}$, and let $f_n \colon S \to \mathbb{R}$ be continuous for each $n \ge 0$.
If the [[series|0MRE6XRE5V]] $\sum_{n=0}^{\infty} f_n$ converges uniformly on $S$, then its sum is continuous on $S$.

## Remarks

The partial sums are continuous, and they converge uniformly. Apply the [[uniform limit theorem|0X9XT05JVC]].
Uniform convergence often comes from the [[M-test|0NX5NWAFC9]]. Mathlib states the result in this form as `continuous_tsum`.
For example, $\sum_{n=1}^{\infty} \frac{\cos(n x)}{n^2}$ is continuous on $\mathbb{R}$.

## Explanations

### L1 human

Adding infinitely many continuous functions gives a continuous function, if the sum converges uniformly.
