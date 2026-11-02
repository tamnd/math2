---
tag: P142WXJCF3
kind: concept
name: Generalized least squares
msc: [62J05]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_least_squares
same_as:
  wikidata: Q2246261
  wikipedia: Generalized least squares
---

## Summary

Generalized least squares estimates the coefficients of a linear model whose errors have a known covariance structure that is not a multiple of the identity.
It minimises a squared distance weighted by the inverse of the error covariance matrix.
Under the analogue of the [[Gauss–Markov theorem|N3YMNMWANM]], due to Aitken, it is the best linear unbiased estimator in that setting.
[[Weighted least squares|H5CGZHBR58]] is the special case of uncorrelated errors with unequal variances.

## Explanations

### L1 human

[[Ordinary least squares|YM708KHV2W]] treats all observations as equally reliable and unrelated.
When some observations are noisier, or when errors are correlated, as in data over time, that is wasteful.
Generalized least squares first changes coordinates so that the errors become uncorrelated with equal variances, and then applies ordinary least squares.
For example, if each observation is the mean of a different number of measurements, the means of many measurements get more weight.
