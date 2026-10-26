---
tag: 0YBY3VYX0K
kind: statement
role: theorem
name: Term-by-term integration
msc: [40A30, 26A42]
uses: [0BWGW68B66, 0MRE6XRE5V]
sources:
  - url: https://en.wikipedia.org/wiki/Function_series
    locator: Convergence
---

## Statement

Let $a < b$, and let $f_n \colon [a, b] \to \mathbb{R}$ be Riemann integrable for each $n \ge 0$.
If $\sum_{n} f_n$ converges uniformly on $[a, b]$, then its sum is Riemann integrable, and
$$\int_a^b \sum_{n=0}^{\infty} f_n(x) \, dx = \sum_{n=0}^{\infty} \int_a^b f_n(x) \, dx.$$

## Remarks

Apply [[the theorem on sequences|0BWGW68B66]] to the partial sums.
For example, integrating $\frac{1}{1 + t} = \sum (-t)^n$ term by term over $[0, x]$, with $|x| < 1$, gives the Mercator series for $\ln(1 + x)$.
Mathlib states a version with summable sup norms as `intervalIntegral.tsum_intervalIntegral_eq_of_summable_norm`.

## Explanations

### L1 human

We may integrate a uniformly convergent series term by term.
The integral of the sum is the sum of the integrals.
