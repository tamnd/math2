---
tag: CKF9KDXBP7
kind: concept
name: Mann–Whitney U test
msc: [62G10]
specializes: [087P03NEND]
sources:
  - url: https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U_test
same_as:
  wikidata: Q1424533
  wikipedia: Mann–Whitney U test
---

## Summary

The Mann–Whitney U test, also called the Wilcoxon rank-sum test, is a [[hypothesis test|087P03NEND]] that compares two independent samples.
Its statistic counts the pairs, one value from each sample, in which the first value is larger.
Under the null hypothesis that both samples come from the same continuous distribution, the law of this count does not depend on that distribution.
It is the rank-based counterpart of the two-sample $t$-test, and it does not need normality.

## Explanations

### L1 human

Put the two samples together and ask, for every pair made of one value from each sample, which is larger.
If the two samples come from the same population, the first sample should win about half of these duels.
If it wins nearly all of them, its values tend to be larger.
For example, with samples $(3, 5)$ and $(1, 4)$, the first sample wins $3$ of the $4$ duels.
