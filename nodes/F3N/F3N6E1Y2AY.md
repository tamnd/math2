---
tag: F3N6E1Y2AY
kind: concept
name: Stable distribution
msc: ["60E07", 60G52]
specializes: [BX3V3NYM1Y]
sources:
  - url: https://en.wikipedia.org/wiki/Stable_distribution
same_as:
  wikidata: Q1934245
  wikipedia: Stable distribution
---

## Summary

A stable distribution is a law on $\R$ whose type is preserved under independent sums.
A sum of independent copies has the same law up to a change of scale and location.
Each stable law has an index $\alpha \in (0, 2]$; the [[normal distribution|05AQE0QR0D]] is the case $\alpha = 2$ and the [[Cauchy distribution|0GPG24Q3GR]] is a case with $\alpha = 1$.
Stable laws are exactly the possible nondegenerate limits of suitably normalised sums of i.i.d. random variables, which extends the [[central limit theorem|0EPZC4Z1FC]] to variables of infinite variance.
Every stable law is [[infinitely divisible|BX3V3NYM1Y]].

## Explanations

### L1 human

Add two independent normal variables and you get a normal variable again, only wider; stable laws are the laws with this property.
For an index $\alpha < 2$ the tails are heavy: the chance that $\abs{X}$ exceeds $x$ falls like $x^{-\alpha}$, and the variance is infinite.
For example, the average of $n$ independent standard Cauchy variables is again standard Cauchy, so averaging does not reduce the spread at all.
Stable laws appear as limits whenever many independent heavy-tailed effects add up.
