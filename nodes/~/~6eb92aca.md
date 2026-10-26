---
tag: ~6eb92aca
kind: statement
role: theorem
name: Cauchy product of absolutely convergent series
msc: [40A05]
uses: [~db2ea8fc, ~2aabc312]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_product
    locator: Convergence and Mertens' theorem
---

## Statement

Let $\sum a_n$ and $\sum b_n$ be real series that [[converge absolutely|~2aabc312]], with sums $A$ and $B$.
Then their [[Cauchy product|~db2ea8fc]] $\sum c_n$ converges absolutely, and its sum is $A B$.

## Remarks

The double series $\sum_{i,j} a_i b_j$ converges absolutely, so its terms can be grouped in any order. The Cauchy product groups them by $i + j$.
[[Mertens' theorem|~92c835ee]] needs absolute convergence of only one of the two series, but then gives only convergence.
Mathlib states it for complete normed rings, as `tsum_mul_tsum_eq_tsum_sum_range_of_summable_norm`.

## Explanations

### L1 human

When both series converge absolutely, we may multiply them term by term as with finite sums.
The order in which we add the products does not change the result.
