---
tag: 0GXKM1R7E4
kind: concept
name: Telescoping series
msc: [40A05]
uses: [0JH4MN4K1C, 0NB643K60Q]
sources:
  - url: https://en.wikipedia.org/wiki/Telescoping_series
    locator: Definition
same_as:
  wikidata: Q2164293
  wikipedia: Telescoping series
---

## Summary

A telescoping series is a series whose terms have the form $a_n = b_n - b_{n+1}$ for a sequence $(b_n)$. Its partial sums collapse: $\sum_{n=0}^{N} (b_n - b_{n+1}) = b_0 - b_{N+1}$. Thus the series converges if and only if $(b_n)$ converges, and then its sum is $b_0 - \lim b_n$.

## Remarks

For example, $\frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}$, so $\sum_{n=1}^{\infty} \frac{1}{n(n+1)} = 1$.
The finite form $\sum_{k=0}^{n-1} (f(k+1) - f(k)) = f(n) - f(0)$ is a discrete analogue of the [[fundamental theorem of calculus|0NHGY0N0JB]]. Mathlib states it as `Finset.sum_range_sub`.

## Explanations

### L1 human

In a telescoping sum, each term cancels part of the next term, like the segments of a telescope that slide into each other.
Only the first piece and the last piece survive.
