---
tag: WTXFYA093D
kind: concept
name: Estimating equations
msc: [62F10, 62F12]
sources:
  - url: https://en.wikipedia.org/wiki/Estimating_equations
same_as:
  wikidata: Q5401384
  wikipedia: Estimating equations
---

## Summary

The method of estimating equations defines an estimator as a solution of $\sum_i g(X_i, \theta) = 0$.
Here the function $g$ has mean zero at the true parameter.
The likelihood equations, the moment equations of the method of moments and the normal equations of least squares are all estimating equations.
The approach needs only a model for some moments, not a full probability model.
Its asymptotic theory is the same as that of M-estimators, with a sandwich formula for the variance.

## Explanations

### L1 human

Write down an equation that the true parameter satisfies on average, such as "the mean of $X - \theta$ is zero".
Replace the average over the population by the average over the sample and solve for $\theta$.
In the example this gives $\theta = \bar{X}$, the sample mean.
Because the sample average is close to the population average, the solution is close to the true parameter.
