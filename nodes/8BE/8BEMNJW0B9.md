---
tag: 8BEMNJW0B9
kind: concept
name: Wishart distribution
msc: [62H10, "60E05"]
specializes: [0DVDCMA2DK]
sources:
  - url: https://en.wikipedia.org/wiki/Wishart_distribution
same_as:
  wikidata: Q1930697
  wikipedia: Wishart distribution
---

## Summary

The Wishart distribution is a probability distribution on symmetric positive semidefinite matrices.
It is the distribution of the scatter matrix $\sum_i X_i X_i^T$ of independent centred multivariate normal vectors.
It is the matrix version of the chi-squared distribution, and it is the sampling distribution of the sample covariance matrix of normal data.
In Bayesian statistics it is the conjugate prior of the precision matrix of a multivariate normal distribution.

## Explanations

### L1 human

Draw $n$ random points in $p$-dimensional space from a normal distribution centred at the origin.
Add up the matrices $X_i X_i^T$; the result records how the cloud of points spreads in every direction.
This random matrix has the Wishart distribution.
In dimension $p = 1$ the matrix is the number $\sum_i X_i^2$, so the Wishart distribution is a scaled chi-squared distribution.
