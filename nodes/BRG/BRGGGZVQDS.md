---
tag: BRGGGZVQDS
kind: concept
name: Breakdown point
msc: [62F35, 62G35]
sources:
  - url: https://en.wikipedia.org/wiki/Robust_statistics
    locator: Breakdown point
---

## Summary

The breakdown point of an estimator is the smallest fraction of the data that can ruin the estimate.
Ruin means that replacing this fraction by arbitrary values can carry the estimate arbitrarily far.
It measures the global robustness of an estimator against gross outliers.
The sample mean has breakdown point $1/n$, which tends to $0$.
The median has breakdown point close to $1/2$, the largest possible value for equivariant estimators of location.

## Explanations

### L1 human

Ask how many data points an adversary must corrupt to push your estimate as far away as they like.
For the average, one corrupted point is enough: making it huge makes the average huge.
For the median, the adversary needs to corrupt about half of the points.
The breakdown point is this number of points divided by the sample size.
