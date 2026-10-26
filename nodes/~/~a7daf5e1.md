---
tag: ~a7daf5e1
kind: definition
name: Series of functions
msc: [40A30]
defines: ~2b9db30d
uses: [~6612f89e, ~e1684463, ~dcbabb8f]
sources:
  - url: https://en.wikipedia.org/wiki/Function_series
    locator: Convergence
---

## Definition

Let $S$ be a set and let $f_n \colon S \to \mathbb{R}$ for $n \ge 0$.
The series of functions $\sum_{n=0}^{\infty} f_n$ is the sequence of partial sums $s_N = \sum_{n=0}^{N} f_n$.
The series converges pointwise, or uniformly, on $S$ if the sequence $(s_N)$ converges [[pointwise|~e1684463]], or [[uniformly|~dcbabb8f]], on $S$.
The limit is the sum $\sum_{n=0}^{\infty} f_n(x)$.

## Remarks

Power series and Fourier series are series of functions.
The [[Weierstrass M-test|~2034293f]] is the main tool to prove uniform convergence.
By the [[uniform limit theorem|~e994aadc]], a uniformly convergent series of continuous functions has a continuous sum.

## Explanations

### L1 human

A series of functions adds infinitely many functions, point by point.
At each $x$ it is an ordinary series of numbers.
