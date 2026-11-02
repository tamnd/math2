---
tag: WT0HACKQV7
kind: concept
name: Euler transform
msc: [40A25, 65B10, 40G05]
specializes: [B1S2XJPGYD]
sources:
  - url: https://en.wikipedia.org/wiki/Binomial_transform
    locator: Euler transform
---

## Summary

The Euler transform rewrites an [[alternating series|0QED0GPYKY]] $\sum (-1)^n a_n$ as a new series built from the iterated differences of the $a_n$, with weights $2^{-n-1}$.
When the $a_n$ vary smoothly, the new series converges much faster, often geometrically.
It is a classical tool of [[series acceleration|B1S2XJPGYD]], and the same formula gives the [[Euler summation|81Q4ERP594]] method for some divergent series.

## Explanations

### L1 human

The terms of an alternating series cancel each other in pairs.
The Euler transform groups this cancellation in a systematic way using differences of consecutive terms.
For the [[alternating harmonic series|0JQ5Y3WWVE]] $1 - \frac12 + \frac13 - \cdots = \ln 2$, the transformed series is $\sum_{n \ge 1} \frac{1}{n 2^n}$.
Its terms shrink by about half each time, so a few terms already give several correct digits.
