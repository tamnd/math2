---
tag: DPW8KNHE6P
kind: concept
name: Wald test
msc: [62F03, 62F05]
specializes: [087P03NEND]
sources:
  - url: https://en.wikipedia.org/wiki/Wald_test
same_as:
  wikidata: Q748664
  wikipedia: Wald test
---

## Summary

The Wald test is a [[hypothesis test|087P03NEND]] that measures how far an unrestricted estimate of a parameter lies from its null value.
The distance is scaled by the estimated standard error, usually from the [[Fisher information|G1Z3WSTE8Q]] at the [[maximum likelihood estimate|0FREPFKNS7]].
It needs only the unrestricted fit, and it is the test behind the usual "estimate divided by standard error" output of regression software.

## Explanations

### L1 human

Estimate the parameter, then ask how many standard errors the estimate is from the value claimed by the null hypothesis.
If it is more than about two standard errors away, reject at level about $5\%$.
For a coin with $60$ heads in $100$ tosses, the estimate is $0.6$ with standard error $\sqrt{0.6 \cdot 0.4/100} \approx 0.049$.
So the estimate is about $2.04$ standard errors from $0.5$, and the Wald test rejects a fair coin at level $5\%$.
