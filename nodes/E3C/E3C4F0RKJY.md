---
tag: E3C4F0RKJY
kind: concept
name: L-estimator
msc: [62G05, 62G30, 62G35]
specializes: [0SSS6ERQ0S]
sources:
  - url: https://en.wikipedia.org/wiki/L-estimator
same_as:
  wikidata: Q6456129
  wikipedia: L-estimator
---

## Summary

An L-estimator is an [[estimator|0SSS6ERQ0S]] that is a linear combination of the [[order statistics|58NHGZDSRE]] of the sample.
The sample median, the trimmed means, the midrange and the interquartile range are all L-estimators.
Small or zero weights on the extreme order statistics give estimators that resist outliers.
This makes L-estimators a basic family of [[robust statistics|J7410PG2DR]].

## Explanations

### L1 human

Sort the data from smallest to largest.
An L-estimator multiplies each sorted value by a fixed weight and adds the results.
The mean gives every value the same weight, while the median puts all the weight on the middle value.
A trimmed mean drops a few values at each end and averages the rest, so a single wild value cannot pull it far.
