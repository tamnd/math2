---
tag: 8VDNRZG3R1
kind: concept
name: Efficiency of an estimator
msc: [62F10, 62F12]
sources:
  - url: https://en.wikipedia.org/wiki/Efficiency_(statistics)
same_as:
  wikidata: Q2265984
  wikipedia: Efficiency (statistics)
---

## Summary

The efficiency of an unbiased estimator measures how close its variance comes to the smallest possible variance, the Cramér–Rao lower bound.
An estimator whose variance attains the bound is called efficient.
The relative efficiency of two estimators is the ratio of their variances.
It tells how many more observations the worse estimator needs to match the better one.
Asymptotic versions compare the variances of the limit distributions as the sample size grows.

## Explanations

### L1 human

Two estimators can both be right on average, but one may scatter less around the truth.
The one with smaller scatter uses the information in the data better; it is more efficient.
For normal data, the sample mean and the sample median both estimate the centre, but the median has about $1/0.64 \approx 1.57$ times the variance of the mean in large samples.
So the median needs about $57\%$ more data to be as precise as the mean.
