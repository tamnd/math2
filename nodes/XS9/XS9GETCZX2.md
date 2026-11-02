---
tag: XS9GETCZX2
kind: concept
name: Hotelling's T-squared distribution
msc: [62H10, 62H15]
specializes: [0DVDCMA2DK]
sources:
  - url: https://en.wikipedia.org/wiki/Hotelling%27s_T-squared_distribution
same_as:
  wikidata: Q1393230
  wikipedia: Hotelling's T-squared distribution
---

## Summary

Hotelling's T-squared distribution is the multivariate analogue of the square of Student's $t$-distribution.
It is the distribution of a squared Mahalanobis-type length $m\, x^T M^{-1} x$ of a normal vector $x$, measured with an independent Wishart matrix $M$.
A rescaling of it is an F-distribution.
It is the null distribution of Hotelling's $T^2$ test for the mean vector of a multivariate normal sample.

## Explanations

### L1 human

To test whether the mean of one variable is zero, one divides the sample mean by its estimated standard error and gets a $t$ statistic.
With several variables at once, the variables have different scales and are correlated.
Hotelling's statistic measures the distance of the sample mean vector from the hypothesized mean in units given by the sample covariance matrix.
Its distribution, when the hypothesis holds, is Hotelling's T-squared distribution.
With a single variable it reduces to the square of the $t$ statistic.
