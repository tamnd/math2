---
tag: 22K8CSQTYM
kind: concept
name: Complete measure
msc: [28A12]
specializes: [PR11BZQQPG]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_measure
same_as:
  wikidata: Q527101
  wikipedia: Complete measure
---

## Summary

A measure is complete if every subset of a set of measure zero is measurable.
Then such subsets automatically have measure zero.
Lebesgue measure on the Lebesgue measurable sets is complete, while its restriction to the Borel sets is not.

## Explanations

### L1 human

If a set has size zero, then any part of it should also have size zero.
A complete measure makes sure that every such part is allowed to be measured at all.
Without completeness, a subset of a negligible set could be left out of the σ-algebra, which is awkward when one works with properties that hold almost everywhere.
Every measure can be completed by adding these subsets.
