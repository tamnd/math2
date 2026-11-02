---
tag: 4RJSN0QARD
kind: concept
name: Power of a test
msc: [62F03]
sources:
  - url: https://en.wikipedia.org/wiki/Power_(statistics)
same_as:
  wikidata: Q1199823
  wikipedia: Power (statistics)
---

## Summary

The power of a [[hypothesis test|087P03NEND]] at a parameter value is the probability that the test rejects the null hypothesis.
Here the data are assumed to come from that parameter value.
Under the alternative it equals one minus the probability of a [[type II error|03N8C8ZR4B]].
Power is the main criterion to compare tests of the same level, and it guides the choice of a sample size.

## Explanations

### L1 human

Power measures how good a test is at detecting an effect that is really there.
A test with power $0.8$ finds a true effect of the given size in $80\%$ of repeated experiments.
For a sensible test, such as a one-sided z-test, the power grows with the sample size and with the size of the effect.
For example, a test for a biased coin with $10$ tosses rarely detects a probability of heads of $0.55$, while $10000$ tosses detect it almost always.
