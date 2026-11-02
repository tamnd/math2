---
tag: 38SETDT2HN
kind: concept
name: Wilcoxon signed-rank test
msc: [62G10]
specializes: [087P03NEND]
sources:
  - url: https://en.wikipedia.org/wiki/Wilcoxon_signed-rank_test
same_as:
  wikidata: Q1751970
  wikipedia: Wilcoxon signed-rank test
---

## Summary

The Wilcoxon signed-rank test is a [[hypothesis test|087P03NEND]] for the centre of a symmetric distribution, most often applied to the differences within matched pairs.
It ranks the absolute values of the observations and adds the ranks of the positive ones.
Unlike the [[sign test|NBK6G2VB7A]], it uses how far each observation lies from the hypothesised centre.
So it is usually more powerful, but it assumes that the distribution is symmetric.
It is the rank-based counterpart of the one-sample $t$-test.

## Explanations

### L1 human

Suppose you measure each patient before and after a treatment and take the differences.
If the treatment does nothing, positive and negative differences of each size should be equally likely.
Sort the differences by size, ignoring the sign, and number them $1, 2, 3, \dots$ from smallest to largest.
Add up the numbers that belong to positive differences.
A total near the maximum means that the large differences are mostly positive, which is evidence of an effect.
