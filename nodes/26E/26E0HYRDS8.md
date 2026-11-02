---
tag: 26E0HYRDS8
kind: concept
name: Dickey–Fuller test
msc: [62M07, 62M10, 91B84]
specializes: [087P03NEND]
sources:
  - url: https://en.wikipedia.org/wiki/Dickey%E2%80%93Fuller_test
same_as:
  wikidata: Q1209988
  wikipedia: Dickey–Fuller test
---

## Summary

The Dickey–Fuller test is a [[statistical test|087P03NEND]] for an autoregressive time series.
Its null hypothesis is a unit root, which means random-walk behaviour, and its alternative is stationarity.
Its test statistic is an ordinary $t$-ratio.
Under the null hypothesis this ratio does not follow a Student or normal distribution, so special critical values are needed.
David Dickey and Wayne Fuller introduced it in 1979, and its augmented version is a standard first step in the analysis of economic time series.

## Explanations

### L1 human

Some series, like a stock price, wander without any pull back to a fixed level: a shock today moves them for good.
Other series fluctuate around a level and forget shocks over time.
The Dickey–Fuller test asks which kind a series is, by regressing each change on the previous level.
If high levels tend to be followed by falls, strongly enough by the test's standard, the series is pulled back and the random-walk hypothesis is rejected.
