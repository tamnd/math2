---
tag: Y6ZG7PRXW3
kind: statement
role: corollary
name: Convolution of central binomial coefficients
msc: [05A10, 05A15]
uses: [0JPH2Y4DFV, 0GBZM0MT0F]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_genfunction_binom-app.ptx#L73
    locator: source/s_genfunction_binom-app.ptx:73
---

## Statement

Let $n \ge 0$ be an integer.
Multiply the [[central binomial coefficient|0JPH2Y4DFV]] $\binom{2k}{k}$ by $\binom{2n-2k}{n-k}$, and add these products over $k = 0, 1, \dots, n$.
The total is $4^n$:
$$\sum_{k=0}^{n} \binom{2k}{k}\binom{2n-2k}{n-k} = 2^{2n}.$$

## Remarks

For $n = 2$: $1\cdot 6 + 2\cdot 2 + 6 \cdot 1 = 16 = 4^2$.
The sum is the coefficient of $x^n$ in the square of the series $\sum_{m} \binom{2m}{m} x^m$. That series is $(1-4x)^{-1/2}$, so its square is $(1-4x)^{-1} = \sum_n 4^n x^n$.
