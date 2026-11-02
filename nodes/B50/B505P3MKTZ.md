---
tag: B505P3MKTZ
kind: concept
name: Lindelöf summation
msc: ["40G10"]
specializes: [8X25Q4XYMN]
sources:
  - url: https://en.wikipedia.org/wiki/Divergent_series
---

## Summary

Lindelöf summation is a [[summability method|8X25Q4XYMN]] that damps the $n$-th term of a series by the factor $n^{-hn}$ and lets $h$ decrease to $0$.
The damping factors decay faster than any geometric sequence, so the damped series converges for many divergent series.
The method is regular: it gives the usual sum to every convergent series.
Applied to the Taylor series of an analytic function, it sums the series in the whole [[Mittag-Leffler star|C21ECQ1H84]] of the function.

## Explanations

### L1 human

Multiply the $n$-th term of a series by $n^{-hn}$ for a small positive number $h$.
For large $n$ this factor is tiny, so even a series with fast-growing terms can converge after damping.
As $h$ shrinks to $0$, every factor tends to $1$ and the damping disappears.
If the damped sums approach a limit, that limit is the Lindelöf sum.
