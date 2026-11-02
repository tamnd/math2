---
tag: CRFQEGJDA9
kind: concept
name: Fuzzy measure
msc: ["28E10"]
sources:
  - url: https://en.wikipedia.org/wiki/Fuzzy_measure_theory
---

## Summary

A fuzzy measure, also called a capacity or a monotone measure, is a set function that vanishes on the empty set and is monotone.
It drops the additivity of a [[measure|PR11BZQQPG]] and keeps only the rule that bigger sets get bigger values.
Fuzzy measures model the worth of coalitions in cooperative games and the importance of groups of criteria in decision making.
One integrates against them with the [[Choquet integral|36TXCRZ6GC]] or the Sugeno integral.

## Explanations

### L1 human

Suppose several criteria judge a product, and a group of criteria gets a weight.
Two criteria that measure almost the same thing should not count twice, so the weight of the pair may be less than the sum of the two weights.
Two criteria that support each other may get more than the sum.
A fuzzy measure allows both effects and asks only that adding a criterion never lowers the weight.
