---
tag: RADE160VJN
kind: concept
name: Minimal sufficient statistic
msc: [62B05]
specializes: [WP4TGXJQJG]
sources:
  - url: https://en.wikipedia.org/wiki/Sufficient_statistic
    locator: Minimal sufficiency
---

## Summary

A minimal sufficient statistic is a [[sufficient statistic|WP4TGXJQJG]] that reduces the data as much as possible without losing information about the parameter.
It is a function of every other sufficient statistic.
In regular models it exists and can be found from ratios of likelihoods.

## Explanations

### L1 human

The whole data set is always sufficient, but it is not a summary at all.
A minimal sufficient statistic is the most compressed summary that still keeps everything relevant about the parameter.
For coin tosses it is the number of heads; for normal data with unknown mean and variance it is the pair (sample mean, sample variance).
Any further compression would lose information.
