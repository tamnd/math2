---
tag: T6KRQAQQ15
kind: concept
name: Hodges–Lehmann estimator
msc: [62G05, 62G35]
specializes: [0SSS6ERQ0S]
sources:
  - url: https://en.wikipedia.org/wiki/Hodges%E2%80%93Lehmann_estimator
same_as:
  wikidata: Q15729148
  wikipedia: Hodges–Lehmann estimator
---

## Summary

The Hodges–Lehmann estimator estimates the centre of a symmetric distribution by the [[median|07Y2E7P9NP]] of all pairwise averages of the observations.
It is the estimator that corresponds to the [[Wilcoxon signed-rank test|38SETDT2HN]], and it inherits its good properties.
It resists outliers much better than the mean, and for normal data it is almost as precise, with asymptotic relative efficiency $3/\pi \approx 0.955$.
A two-sample version estimates a shift between two populations by the median of all pairwise differences.

## Explanations

### L1 human

Take every pair of data points, including each point paired with itself, and write down the midpoint of the pair.
The median of all these midpoints is the Hodges–Lehmann estimate.
For the data $1, 2, 9$ the midpoints are $1, 1.5, 2, 5, 5.5, 9$, and their median is $3.5$.
This lies between the median $2$, which ignores how far $9$ is, and the mean $4$, which is pulled by it.
