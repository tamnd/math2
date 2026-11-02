---
tag: NBK6G2VB7A
kind: concept
name: Sign test
msc: [62G10]
specializes: [087P03NEND]
sources:
  - url: https://en.wikipedia.org/wiki/Sign_test
same_as:
  wikidata: Q2301904
  wikipedia: Sign test
---

## Summary

The sign test is a [[hypothesis test|087P03NEND]] about the [[median|07Y2E7P9NP]] of a distribution, or about the median difference within matched pairs.
It uses only whether each observation lies above or below the hypothesised median.
So under the null hypothesis the count of observations above has a [[binomial distribution|0WCWA1KT3M]] with success probability $1/2$.
It needs almost no assumptions on the shape of the distribution, which makes it one of the simplest tests of [[nonparametric statistics|VFAJ1EG3X5]].

## Explanations

### L1 human

Suppose a claim says that half of all values lie above $10$.
Look at a sample and count how many values are above $10$.
If the claim is true, each value is above $10$ with chance one half, like a fair coin toss.
Ten values out of ten above $10$ would be like ten heads in a row, which has chance $1/1024$, so the claim looks doubtful.
