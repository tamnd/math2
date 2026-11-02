---
tag: ZATS7NV9WD
kind: concept
name: Linear discriminant analysis
msc: [62H30]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_discriminant_analysis
same_as:
  wikidata: Q1228929
  wikipedia: Linear discriminant analysis
---

## Summary

Linear discriminant analysis assigns an observation to one of several classes with a rule whose decision boundaries are hyperplanes.
It is the optimal rule when each class has a [[multivariate normal distribution|0XN3K7RSZY]] and all classes share one [[covariance matrix|0V7G6WMFK0]].
In practice the means and the common covariance are estimated from labelled data.
It is closely tied to Fisher's linear discriminant, which also gives a dimension reduction.

## Explanations

### L1 human

Two kinds of flowers differ on average in petal length and width, but the measurements overlap.
Linear discriminant analysis draws a straight line through the plane of measurements and calls every flower on one side the first kind.
The line is placed using the class averages and the shared spread, measured by the [[Mahalanobis distance|P546TSFBK2]].
For one measurement with class means $-1$ and $1$, equal variances and equal sizes, the rule simply looks at the sign of the measurement.
