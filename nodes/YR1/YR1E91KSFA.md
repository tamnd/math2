---
tag: YR1E91KSFA
kind: concept
name: Coherent risk measure
msc: [91G70, 91B05]
sources:
  - url: https://en.wikipedia.org/wiki/Coherent_risk_measure
same_as:
  wikidata: Q5141358
  wikipedia: Coherent risk measure
---

## Summary

A coherent risk measure assigns to each random loss a number, the capital needed to make the position acceptable.
It obeys four axioms: monotonicity, translation invariance, subadditivity and positive homogeneity.
The axioms were proposed by Artzner, Delbaen, Eber and Heath in 1999.
Subadditivity expresses that diversification does not increase risk.
[[Expected shortfall|KKVCHFGA14]] is coherent, while [[value at risk|C063APG9NT]] is not.

## Explanations

### L1 human

A risk measure turns an uncertain loss into one number of money, the amount of capital a regulator would ask you to hold.
Coherence asks for four common-sense rules.
A position that always loses more needs more capital.
Adding a sure loss of $m$ adds exactly $m$ to the capital.
Doubling a position doubles its capital.
Merging two portfolios never needs more capital than keeping them apart.
For example, the worst possible loss is a coherent risk measure, though a very cautious one.
