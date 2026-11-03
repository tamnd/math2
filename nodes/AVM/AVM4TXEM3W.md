---
tag: AVM4TXEM3W
kind: concept
name: Gompertz–Makeham law of mortality
msc: [91G05, 91D20, 62P05]
sources:
  - url: https://en.wikipedia.org/wiki/Gompertz–Makeham_law_of_mortality
same_as:
  wikidata: Q2734378
  wikipedia: Gompertz–Makeham law of mortality
---

## Summary

The Gompertz–Makeham law of mortality models the death rate of adults as the sum of an exponentially growing part and a constant part.
The exponential part describes ageing, and the constant part describes deaths that do not depend on age, such as accidents.
It fits human mortality well over a wide range of adult ages and is a standard parametric model for a [[hazard function|Y959NKQ3XW]] in actuarial work.

## Explanations

### L1 human

The risk of dying in the next year grows with age, and for adults it grows roughly geometrically.
In the pure Gompertz model it doubles over a fixed span of years, which for humans is often quoted as about eight years.
Makeham added a constant background risk on top.
So the death rate at age $x$ looks like $\lambda + \alpha e^{\beta x}$: flat near $\lambda$ for the young, then rising steeply for the old.
