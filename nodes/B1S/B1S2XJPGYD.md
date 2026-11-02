---
tag: B1S2XJPGYD
kind: concept
name: Series acceleration
msc: [65B10, 65B05, 40A25]
sources:
  - url: https://en.wikipedia.org/wiki/Series_acceleration
same_as:
  wikidata: Q1783478
  wikipedia: Series acceleration
---

## Summary

Series acceleration uses sequence transformations to speed up a slowly converging sequence, such as the [[partial sums|09RJ859N7A]] of a series.
The new sequence has the same limit but converges faster.
It matters in numerical work, where a series may need millions of terms for a few correct digits.
Classical methods are [[Aitken's delta-squared process|WF08BMN6Q6]], the [[Euler transform|WT0HACKQV7]], [[Richardson extrapolation|WMTZG71K2Y]], the [[Shanks transformation|C0TXDZZMH7]] and the [[Levin-type transformations|1P47PCRVTZ]].

## Explanations

### L1 human

A slowly converging series reaches its sum only after very many terms.
An acceleration method looks at the pattern of the first few partial sums and guesses where they are heading.
For the [[Leibniz series|037FD5NBRT]] $1 - \frac13 + \frac15 - \cdots = \frac{\pi}{4}$, the partial sums jump around $\frac{\pi}{4}$, and averaging neighbours already gives much better values.
No single method works for every sequence; each one is exact for some model of how the error behaves.
