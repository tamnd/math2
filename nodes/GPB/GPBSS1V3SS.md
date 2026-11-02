---
tag: GPBSS1V3SS
kind: concept
name: Shrinkage estimator
msc: [62J07, 62F10]
specializes: [0SSS6ERQ0S]
sources:
  - url: https://en.wikipedia.org/wiki/Shrinkage_(statistics)
---

## Summary

A shrinkage estimator is an estimator obtained by pulling a basic estimator toward a fixed target or a pooled value.
Shrinking adds some bias but can lower the variance by more, so the mean squared error goes down.
Examples are the [[James–Stein estimator|709T196XCT]], posterior means under normal priors, and penalized regression such as [[ridge regression|3KZW2930V2]].

## Explanations

### L1 human

Raw estimates computed from little data tend to be too extreme: some are too high and some too low just by chance.
A shrinkage estimator moves each raw estimate part of the way toward a sensible central value.
The less reliable the raw estimate, the more it is moved.
For example, a batting average from only ten games is better predicted by moving it toward the league average than by taking it at face value.
