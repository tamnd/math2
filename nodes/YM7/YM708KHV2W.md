---
tag: YM708KHV2W
kind: concept
name: Ordinary least squares
msc: [62J05]
specializes: [0BYTQ4X1HC]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinary_least_squares
same_as:
  wikidata: Q2912993
  wikipedia: Ordinary least squares
---

## Summary

Ordinary least squares estimates the coefficients of a [[linear regression|41FVC4P5JB]] by minimising the sum of squared residuals.
The estimate has the closed form $\hat\beta = (X^T X)^{-1} X^T y$ when the design matrix has full column rank.
Geometrically, the fitted values are the [[orthogonal projection|0B8KZRT28M]] of the data onto the column space of the design matrix.
By the [[Gauss–Markov theorem|N3YMNMWANM]], it is the best linear unbiased estimator under the classical assumptions.

## Explanations

### L1 human

Draw a line through a cloud of points.
For each point, measure the vertical gap between the point and the line, and square it.
Ordinary least squares picks the line that makes the sum of these squared gaps as small as possible.
For the points $(0, 0)$, $(1, 1)$ and $(2, 3)$, the best line is $y = -1/6 + 3x/2$.
