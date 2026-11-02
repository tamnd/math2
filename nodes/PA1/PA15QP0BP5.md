---
tag: PA15QP0BP5
kind: concept
name: S-finite measure
msc: [28A12]
specializes: [PR11BZQQPG]
sources:
  - url: https://en.wikipedia.org/wiki/S-finite_measure
same_as:
  wikidata: Q47008575
  wikipedia: S-finite measure
---

## Summary

An s-finite measure is a measure that is a countable sum of finite measures.
Every σ-finite measure is s-finite, but not conversely.
The class of s-finite measures is used in probability theory, for example for kernels and point processes.

## Explanations

### L1 human

An s-finite measure is built by stacking countably many finite measures on top of each other and adding them.
Each layer has finite total size, but the sum may be infinite everywhere it is not zero.
Infinitely many copies of length on the interval $[0, 1]$, added together, give a measure that is s-finite.
Every subset of $[0, 1]$ of positive length then has infinite size, and this measure is not σ-finite.
