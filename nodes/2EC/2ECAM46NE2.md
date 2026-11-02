---
tag: 2ECAM46NE2
kind: concept
name: Permutation test
msc: [62G10, 62G09]
specializes: [087P03NEND]
sources:
  - url: https://en.wikipedia.org/wiki/Permutation_test
same_as:
  wikidata: Q108839445
  wikipedia: Permutation test
---

## Summary

A permutation test is a [[hypothesis test|087P03NEND]] that gets its null distribution by rearranging the data.
It recomputes the test statistic on all rearrangements that the null hypothesis allows.
In the two-sample case the null hypothesis says that the group labels do not matter, so every reassignment of the labels is equally likely.
The [[p-value|0GGKJGZF6D]] is the share of rearrangements whose statistic is at least as extreme as the observed one.
Under the null hypothesis the chance of a false rejection is at most the chosen level, with no assumption on the shape of the distribution.

## Explanations

### L1 human

Suppose a new method scores higher than an old one in a small trial.
If the method makes no difference, the labels "new" and "old" are arbitrary, and any other split of the same scores was just as likely.
So list all ways to split the scores into two groups of the same sizes, and compute the difference of means for each.
If the real difference is among the largest few percent of these, chance alone is a poor explanation.
