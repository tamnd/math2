---
tag: QED889GZDE
kind: concept
name: Horvitz–Thompson estimator
msc: [62D05]
specializes: [0SSS6ERQ0S]
sources:
  - url: https://en.wikipedia.org/wiki/Horvitz–Thompson_estimator
same_as:
  wikidata: Q17027597
  wikipedia: Horvitz–Thompson estimator
---

## Summary

The Horvitz–Thompson estimator estimates the total of a finite population from a random sample in which units may have unequal chances of selection.
Each sampled value is divided by its inclusion probability, the probability that its unit enters the sample.
It is unbiased for every sampling design in which every unit has a positive inclusion probability.
It is the basic estimator of survey sampling and the model for inverse probability weighting.

## Explanations

### L1 human

A unit that had a small chance of being sampled stands for many units like it that were missed.
So its value is weighted up by the inverse of its chance of selection.
For example, if a farm had a chance of $1/10$ of being sampled and it grows $50$ tonnes of wheat, it contributes $500$ tonnes to the estimated total.
Adding these weighted values over the sample gives an estimate of the whole population total that is right on average.
