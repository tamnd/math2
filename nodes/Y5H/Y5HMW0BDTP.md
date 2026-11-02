---
tag: Y5HMW0BDTP
kind: concept
name: Score test
msc: [62F03, 62F05]
specializes: [087P03NEND]
sources:
  - url: https://en.wikipedia.org/wiki/Score_test
same_as:
  wikidata: Q4456449
  wikipedia: Score test
---

## Summary

The score test is a [[hypothesis test|087P03NEND]] that uses the slope of the log-likelihood at the null value of the parameter.
If the null hypothesis is true, the [[score|CP97GRVTQ0]] there should be close to zero, measured against the [[Fisher information|G1Z3WSTE8Q]].
It needs only the fit under the null hypothesis, and it is also called Rao's score test or the Lagrange multiplier test.

## Explanations

### L1 human

At the true parameter, the log-likelihood is flat on average: it has no tendency to go up or down.
The score test checks whether the log-likelihood is steep at the value claimed by the null hypothesis.
A steep slope means that moving away from that value would raise the likelihood of the data by a large amount.
For a coin with $60$ heads in $100$ tosses and $H_0 \colon p = 0.5$, the score statistic is $(60 - 50)^2/25 = 4$, which is beyond the $95\%$ chi-squared quantile $3.84$.
