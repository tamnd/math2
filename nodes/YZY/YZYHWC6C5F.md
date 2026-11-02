---
tag: YZYHWC6C5F
kind: concept
name: Kolmogorov–Smirnov test
msc: [62G10, 62G30]
specializes: [087P03NEND]
sources:
  - url: https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test
same_as:
  wikidata: Q575766
  wikipedia: Kolmogorov–Smirnov test
---

## Summary

The Kolmogorov–Smirnov test is a [[hypothesis test|087P03NEND]] of whether a sample comes from a given continuous distribution.
A two-sample version tests whether two samples come from the same distribution.
Its statistic is the largest vertical distance between an [[empirical distribution function|A05WR6TEK5]] and the hypothesised [[cumulative distribution function|0H8H7ZTHW2]], or between two empirical distribution functions.
Under the null hypothesis its law does not depend on the continuous distribution being tested, so one table of critical values serves all cases.
It is one of the basic tests of [[nonparametric statistics|VFAJ1EG3X5]].

## Explanations

### L1 human

Draw the staircase made by the data: it rises by $1/n$ at each data point.
Draw on the same picture the smooth curve of the distribution that you expect.
The test looks for the place where the staircase and the curve are farthest apart.
If that gap is too large for the sample size, the data probably do not come from the expected distribution.
For example, one observation $0.3$ tested against the uniform law on $[0, 1]$ gives a largest gap of $0.7$, at $0.3$ itself.
