---
tag: 8MTVCMAATD
kind: concept
name: F-test
msc: [62F03, 62J10]
specializes: [087P03NEND]
sources:
  - url: https://en.wikipedia.org/wiki/F-test
same_as:
  wikidata: Q1386253
  wikipedia: F-test
---

## Summary

An F-test is a [[hypothesis test|087P03NEND]] whose statistic has an [[F-distribution|PBT8VRJADK]] when the null hypothesis holds.
The statistic is a ratio of two independent variance estimates, each scaled by its degrees of freedom.
It compares group means in [[analysis of variance|M9AQ5HKGP4]] and nested [[linear regression|41FVC4P5JB]] models.
It also compares the variances of two normal samples.

## Explanations

### L1 human

An F-test asks whether one source of variation is large compared with another.
In a comparison of several groups, it compares the spread between the group means with the spread inside the groups.
If the group means differ only by chance, the ratio is near $1$.
A ratio much larger than $1$ suggests that the groups really differ.
