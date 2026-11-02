---
tag: SXR93CAP1R
kind: concept
name: Sequential probability ratio test
msc: [62L10, 62F03]
specializes: [087P03NEND]
sources:
  - url: https://en.wikipedia.org/wiki/Sequential_probability_ratio_test
same_as:
  wikidata: Q2271882
  wikipedia: Sequential probability ratio test
---

## Summary

The sequential probability ratio test, or SPRT, is a sequential test of a simple null hypothesis against a simple alternative.
After each observation it updates the likelihood ratio of the data and stops as soon as this ratio leaves a fixed interval.
Abraham Wald introduced it, and it is the basic procedure of [[sequential analysis|9CWYNB9003]].
Among all tests with the same error probabilities, it needs the smallest expected number of observations under both hypotheses.

## Explanations

### L1 human

Two explanations of the data compete, and each new observation makes one of them a little more plausible than the other.
The test keeps a running score, the ratio of how likely the data are under the two explanations.
It stops and picks the alternative when the score climbs above an upper bar, and picks the null hypothesis when it falls below a lower bar.
For example, to test whether a coin shows heads with probability $1/2$ or $2/3$, each head multiplies the score by $4/3$ and each tail by $2/3$.
