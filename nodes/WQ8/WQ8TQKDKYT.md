---
tag: WQ8TQKDKYT
kind: concept
name: Jackknife
msc: [62G09, 62F40]
sources:
  - url: https://en.wikipedia.org/wiki/Jackknife_resampling
same_as:
  wikidata: Q847158
  wikipedia: Jackknife resampling
---

## Summary

The jackknife is a resampling method that recomputes a [[statistic|0Q5CG2NEQ8]] on each of the $n$ samples obtained by leaving out one observation.
From these leave-one-out values it estimates the [[bias|0BWGTN92FG]] and the variance of the statistic and gives a bias-corrected estimate.
Quenouille introduced it for bias reduction, and Tukey proposed its use for variance estimation.
It works well for smooth statistics, and it is a forerunner of the [[bootstrap|40ATJEVR32]].

## Explanations

### L1 human

Take your sample, remove the first observation, and compute your estimate again.
Put it back, remove the second one instead, and repeat until each observation has been left out once.
If these $n$ estimates move a lot, your estimate is sensitive to individual data points and thus uncertain.
Their systematic shift from the full-sample estimate also tells you roughly how biased the estimate is.
