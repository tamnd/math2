---
tag: ZCJX7THBNJ
kind: concept
name: Minimum-variance unbiased estimator
msc: [62F10]
specializes: [0SSS6ERQ0S]
sources:
  - url: https://en.wikipedia.org/wiki/Minimum-variance_unbiased_estimator
same_as:
  wikidata: Q3755281
  wikipedia: Minimum-variance unbiased estimator
---

## Summary

A minimum-variance unbiased estimator is an unbiased estimator with the smallest variance among all unbiased estimators.
It must be smallest at every value of the parameter.
It is also called a uniformly minimum-variance unbiased estimator (UMVUE).
It need not exist, but when it does it is unique with probability one.
The Rao–Blackwell and Lehmann–Scheffé theorems construct it from a complete sufficient statistic.

## Explanations

### L1 human

Among all rules that are right on average, pick the one that scatters least around the truth, whatever the truth is.
That rule is the minimum-variance unbiased estimator.
For coin flips, the proportion of heads is such a rule for the probability of heads.
The requirement "whatever the truth is" is strong: a rule that is best for one value of the parameter but worse for another does not qualify.
