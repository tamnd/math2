---
tag: 4Z73AFN7WT
kind: concept
name: Monotone likelihood ratio
msc: [62F03]
sources:
  - url: https://en.wikipedia.org/wiki/Monotone_likelihood_ratio
same_as:
  wikidata: Q6902029
  wikipedia: Monotone likelihood ratio
---

## Summary

Consider a family of densities indexed by a real parameter.
It has a monotone likelihood ratio in a statistic $T$ when larger parameters make larger values of $T$ relatively more likely.
The ratio of the densities at two parameter values is then a nondecreasing function of $T$.
This property makes one-sided testing simple: tests that reject for large $T$ are optimal.
One-parameter exponential families with an increasing natural parameter have this property.

## Explanations

### L1 human

Think of $T$ as a signal that points towards larger parameter values.
In a family with a monotone likelihood ratio, the larger $T$ is, the more the data favour a larger parameter over a smaller one, for every pair of parameters.
For coin tosses with head probability $p$, the number of heads $T$ is such a signal.
Seeing more heads always favours a larger $p$ over a smaller one.
