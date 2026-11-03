---
tag: KWYCW4P8RH
kind: concept
name: Credibility theory
msc: [91G05, 62P05]
sources:
  - url: https://en.wikipedia.org/wiki/Credibility_theory
same_as:
  wikidata: Q3526803
  wikipedia: Credibility theory
---

## Summary

Credibility theory is the part of actuarial mathematics that sets an insurance premium for one risk.
It mixes the claims record of that risk with the experience of a larger collective.
The premium has the form $Z \bar{X} + (1 - Z) \mu$.
Here $\bar{X}$ is the mean of the risk's own claims, $\mu$ is the collective mean and $Z \in [0, 1]$ is the credibility factor.
The theory explains how to choose $Z$, either from fluctuation limits or as the best linear estimate in mean square, as in the [[Bühlmann model|BZJMY230YG]].

## Explanations

### L1 human

An insurer has a long record for all drivers and a short record for one driver.
The short record alone is too noisy, and the long record ignores what is special about this driver.
Credibility theory takes a weighted average of the two.
For example, if the collective mean claim is $500$, the driver's own mean is $800$ and $Z = 0.25$, the premium is $0.25 \cdot 800 + 0.75 \cdot 500 = 575$.
The more data the driver has, the larger $Z$ becomes.
