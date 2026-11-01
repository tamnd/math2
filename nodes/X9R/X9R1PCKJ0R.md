---
tag: X9R1PCKJ0R
kind: concept
name: Sub-Gaussian distribution
msc: ["60E15", "60E05"]
specializes: [0DVDCMA2DK]
sources:
  - url: https://en.wikipedia.org/wiki/Sub-Gaussian_distribution
same_as:
  wikidata: Q25303973
  wikipedia: Sub-Gaussian distribution
---

## Summary

A real random variable is sub-Gaussian when its tails decay at least as fast as those of a [[normal distribution|05AQE0QR0D]], that is, like $e^{-c t^2}$.
Normal variables and bounded variables are sub-Gaussian.
Sums of independent sub-Gaussian variables are again sub-Gaussian, with explicit constants, and this gives concentration bounds of [[Hoeffding|0WPDNXGSSN]] type.
The notion is central in high-dimensional probability, random matrix theory and statistical learning.

## Explanations

### L1 human

A sub-Gaussian variable is one that is very unlikely to be far from $0$: the chance of exceeding $t$ drops like $e^{-c t^2}$, as for a bell curve.
A fair $\pm 1$ coin is sub-Gaussian, since it never exceeds $1$ at all.
An [[exponential|0E99F51GVB]] variable is not, since $P(X > t) = e^{-t}$ decays only like $e^{-t}$.
The average of many independent sub-Gaussian variables is sharply concentrated around its mean.
