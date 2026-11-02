---
tag: YM1BNA80RC
kind: concept
name: Likelihood-ratio test
msc: [62F03, 62F05]
specializes: [087P03NEND]
sources:
  - url: https://en.wikipedia.org/wiki/Likelihood-ratio_test
same_as:
  wikidata: Q585740
  wikipedia: Likelihood-ratio test
---

## Summary

The likelihood-ratio test compares the best fit of a model under a null hypothesis with its best fit without that restriction.
It rejects the null hypothesis when the maximized [[likelihood|0VW9E4QXR6]] under the null is much smaller than the overall maximum.
It is the most widely used general method to build a [[hypothesis test|087P03NEND]], and [[Wilks' theorem|WQPB6GXD0M]] gives its approximate null law.

## Explanations

### L1 human

Fit the model twice: once with the constraint of the null hypothesis, and once freely.
The free fit is always at least as good, so the question is whether it is much better.
If the constrained fit explains the data far worse, the constraint is probably false.
For a coin with $60$ heads in $100$ tosses, the fair-coin likelihood is compared with the likelihood at $p = 0.6$, the best value.
