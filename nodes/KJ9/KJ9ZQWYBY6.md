---
tag: KJ9ZQWYBY6
kind: concept
name: Observed information
msc: [62F10, 62B10]
sources:
  - url: https://en.wikipedia.org/wiki/Observed_information
same_as:
  wikidata: Q7075478
  wikipedia: Observed information
---

## Summary

The observed information is minus the second derivative of the log-likelihood of the data actually observed.
It is usually evaluated at the [[maximum likelihood estimate|0FREPFKNS7]].
It is a data-based counterpart of the [[Fisher information|G1Z3WSTE8Q]], whose expected value it equals under regularity conditions.
It gives standard errors for maximum likelihood estimates.

## Explanations

### L1 human

Draw the log-likelihood as a curve with a peak at the best estimate.
The observed information is the curvature at that peak.
A sharp peak means the data strongly favour a narrow range of values, so the estimate is precise.
For example, with Poisson counts of total $t$ in $n$ observations, the observed information at the estimate $t/n$ is $n^2/t$.
