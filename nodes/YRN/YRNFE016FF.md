---
tag: YRNFE016FF
kind: concept
name: Adapted process
msc: [60G05, 60G07]
specializes: [0QH5ENKZM1]
sources:
  - url: https://en.wikipedia.org/wiki/Adapted_process
same_as:
  wikidata: Q4680695
  wikipedia: Adapted process
---

## Summary

A [[stochastic process|0QH5ENKZM1]] is adapted to a [[filtration|HNK1Y62G7V]] when its value at each time is determined by the information available at that time.
Adapted processes cannot see the future.
Adaptedness is part of the definition of a [[martingale|0D0GBNDKDH]] and of the stochastic integral, where the integrand must not anticipate the noise.

## Explanations

### L1 human

Think of a gambler who chooses each bet using only the results seen so far.
The gambler's fortune over time is an adapted process: at every moment it depends only on the past and present.
A strategy that peeks at the next coin toss is not adapted.
Every process is adapted to its own history, called its natural filtration.
