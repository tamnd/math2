---
tag: QRAPTPVH8C
kind: concept
name: Uniformly most powerful test
msc: [62F03]
sources:
  - url: https://en.wikipedia.org/wiki/Uniformly_most_powerful_test
same_as:
  wikidata: Q7885148
  wikipedia: Uniformly most powerful test
---

## Summary

A uniformly most powerful test of level $\alpha$ is a [[hypothesis test|087P03NEND]] of level $\alpha$ with the largest possible [[power|4RJSN0QARD]].
Its power beats that of every other test of level $\alpha$, at every parameter value of the alternative.
For simple hypotheses the [[Neyman–Pearson lemma|0EE19CFEEF]] gives such a test.
For one-sided hypotheses in families with a [[monotone likelihood ratio|4Z73AFN7WT]], the [[Karlin–Rubin theorem|RCASN31FFS]] gives one.
For many other problems no such test exists.

## Explanations

### L1 human

Among all tests with the same false-alarm rate, one would like the test that best detects every possible alternative at once.
Such a test is called uniformly most powerful.
For a normal mean with known variance, the test that rejects when the sample mean is large is uniformly most powerful against all larger means.
Against "the mean is different", no single test is best everywhere: a test tuned for larger means loses against smaller means.
