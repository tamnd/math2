---
tag: ~2c6dfc1d
kind: statement
role: theorem
name: Harmonic series diverges
msc: [40A05]
uses: [~69b94ce4, ~b32d2eb9, ~1eb3c5e8]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_series_(mathematics)
    locator: Comparison test
---

## Statement

The partial sums $H_N = \sum_{n=1}^{N} \frac{1}{n}$ of the [[harmonic series|~69b94ce4]] tend to $+\infty$ as $N \to \infty$.
In particular, the harmonic series is a divergent series.

## Remarks

The classical proof groups the terms in blocks from $2^{k-1} + 1$ to $2^k$. Each block has $2^{k-1}$ terms, each at least $1/2^k$, so each block sums to at least $1/2$. Thus $H_{2^k} \ge 1 + k/2$.
A second proof uses the [[integral test|~2af9eb66]]: $H_N \ge \int_1^{N+1} dx/x = \ln(N + 1)$.
Mathlib states it as the limit of $\sum_{n < N} 1/(n+1)$, in `Real.tendsto_sum_range_one_div_nat_succ_atTop`.

## History

Nicole Oresme proved the divergence in the 14th century, with the grouping argument. Pietro Mengoli and Jacob Bernoulli gave other proofs in the 17th century.

## Explanations

### L1 human

Group the terms: $1/3 + 1/4 \ge 1/2$, then $1/5 + \cdots + 1/8 \ge 1/2$, then $1/9 + \cdots + 1/16 \ge 1/2$, and so on.
There are infinitely many such groups, so the sum exceeds each bound.
