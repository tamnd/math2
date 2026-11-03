---
tag: BZJMY230YG
kind: concept
name: Bühlmann model
msc: [91G05, 62P05]
specializes: [KWYCW4P8RH]
sources:
  - url: https://en.wikipedia.org/wiki/Bühlmann_model
same_as:
  wikidata: Q5005264
  wikipedia: Bühlmann model
---

## Summary

The Bühlmann model is the basic model of greatest accuracy [[credibility theory|KWYCW4P8RH]].
Each risk has an unknown parameter drawn from a common distribution, and given the parameter its yearly claims are independent and identically distributed.
The best linear predictor of the risk's mean claim is then a credibility premium with factor $Z = n/(n + k)$.
Here $k$ is the expected process variance divided by the variance of the hypothetical means.

## Explanations

### L1 human

Think of a portfolio of drivers, each with a hidden level of riskiness.
Two sources of variation matter: how much one driver's claims vary from year to year, and how much the drivers differ from each other.
If drivers differ a lot, the own record of a driver is very informative, and $Z$ is close to $1$.
If drivers are all alike, the collective mean is a better guide, and $Z$ is close to $0$.
For example, with $k = 4$, a driver with $n = 4$ years of data gets $Z = 4/8 = 1/2$.
