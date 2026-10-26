---
tag: 0MRE6XRE5V
kind: definition
name: Series of functions
msc: [40A30]
defines: 0Y3KSN2E9X
uses: [0JH4MN4K1C, 056FSKG32J, 08FPABDQ4C]
sources:
  - url: https://en.wikipedia.org/wiki/Function_series
    locator: Convergence
---

## Definition

Let $S$ be a set and let $f_n \colon S \to \mathbb{R}$ for $n \ge 0$.
The series of functions $\sum_{n=0}^{\infty} f_n$ is the sequence of partial sums $s_N = \sum_{n=0}^{N} f_n$.
The series converges pointwise, or uniformly, on $S$ if the sequence $(s_N)$ converges [[pointwise|056FSKG32J]], or [[uniformly|08FPABDQ4C]], on $S$.
The limit is the sum $\sum_{n=0}^{\infty} f_n(x)$.

## Remarks

Power series and Fourier series are series of functions.
The [[Weierstrass M-test|0NX5NWAFC9]] is the main tool to prove uniform convergence.
By the [[uniform limit theorem|0X9XT05JVC]], a uniformly convergent series of continuous functions has a continuous sum.

## Explanations

### L1 human

A series of functions adds infinitely many functions, point by point.
At each $x$ it is an ordinary series of numbers.
