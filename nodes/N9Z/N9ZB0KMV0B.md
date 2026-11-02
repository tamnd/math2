---
tag: N9ZB0KMV0B
kind: concept
name: Anderson–Darling test
msc: [62G10, 62G30]
specializes: [087P03NEND]
sources:
  - url: https://en.wikipedia.org/wiki/Anderson%E2%80%93Darling_test
same_as:
  wikidata: Q491401
  wikipedia: Anderson–Darling test
---

## Summary

The Anderson–Darling test is a goodness-of-fit [[hypothesis test|087P03NEND]] for whether a sample comes from a given distribution.
Its statistic is an integrated squared difference between the [[empirical distribution function|A05WR6TEK5]] and the hypothesised distribution function, weighted so that the tails count more.
It is a weighted form of the [[Cramér–von Mises criterion|G14XJXPKFS]], and it is often more sensitive than the [[Kolmogorov–Smirnov test|YZYHWC6C5F]] to departures in the tails.

## Explanations

### L1 human

Near the far ends of a distribution the staircase of the data and the expected curve are both close to $0$ or to $1$.
So a gap there looks small, even if it means that the data have too many or too few extreme values.
The Anderson–Darling test divides each squared gap by $F_0(1 - F_0)$, which is small in the tails, so that tail gaps count fully.
This makes it good at detecting heavy or light tails.
