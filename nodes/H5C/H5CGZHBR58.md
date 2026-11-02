---
tag: H5CGZHBR58
kind: concept
name: Weighted least squares
msc: [62J05]
specializes: [P142WXJCF3]
sources:
  - url: https://en.wikipedia.org/wiki/Weighted_least_squares
same_as:
  wikidata: Q20025290
  wikipedia: Weighted least squares
---

## Summary

Weighted least squares fits a regression model by minimising a sum of squared residuals in which each observation has its own positive weight.
It is the case of [[generalized least squares|P142WXJCF3]] in which the errors are uncorrelated but [[heteroscedastic|D8VX6XQ3TT]].
With weights inversely proportional to the error variances, it gives the best linear unbiased estimator.
It is also the inner step of iteratively reweighted least squares, used to fit [[generalized linear models|K6C48KMRKC]] and robust regressions.

## Explanations

### L1 human

Some data points are more precise than others.
Weighted least squares lets the precise points pull harder on the fitted line.
Each squared residual is multiplied by a weight, and a point with weight $2$ counts as much as two copies of the same point.
For a model that is just a constant, weighted least squares gives the weighted average $\sum_i w_i y_i / \sum_i w_i$.
