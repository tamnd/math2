---
tag: MT5JZ63RD4
kind: concept
name: Mittag-Leffler summation
msc: ["40G10", "33E12"]
specializes: [8X25Q4XYMN]
sources:
  - url: https://en.wikipedia.org/wiki/Mittag-Leffler_summation
same_as:
  wikidata: Q6883441
  wikipedia: Mittag-Leffler summation
---

## Summary

Mittag-Leffler summation is a [[summability method|8X25Q4XYMN]] that divides the $k$-th term of a series by $\Gamma(1 + \alpha k)$ and lets $\alpha$ decrease to $0$.
Here $\Gamma$ is the [[gamma function|0H5SYBSED9]].
For $\alpha = 1$ the divided series is an exponential series, and the method is related to [[Borel summation|8DJPSYSHGJ]].
Applied to the Taylor series of an analytic function, it sums the series in the [[Mittag-Leffler star|C21ECQ1H84]] of the function.

## Explanations

### L1 human

Dividing the $k$-th term by $\Gamma(1 + \alpha k)$ shrinks the late terms strongly, since the gamma function grows like a factorial.
So the divided series converges for many divergent series.
As $\alpha$ goes to $0$, $\Gamma(1 + \alpha k)$ tends to $\Gamma(1) = 1$ for each $k$, and the division disappears.
The Mittag-Leffler sum is the limit of the divided sums.
