---
tag: XC2YPC2BSW
kind: concept
name: Local martingale
msc: [60G44, 60G48]
specializes: [0QH5ENKZM1]
sources:
  - url: https://en.wikipedia.org/wiki/Local_martingale
same_as:
  wikidata: Q1868500
  wikipedia: Local martingale
---

## Summary

A local martingale is a process that becomes a [[martingale|0D0GBNDKDH]] when it is stopped at suitable stopping times that increase to infinity.
Every martingale is a local martingale, but not conversely.
Stochastic integrals with respect to Brownian motion are local martingales, which is why the notion is central in [[Itô calculus|JA95NH206E]].

## Explanations

### L1 human

A local martingale is a fair game as long as you stop it before it runs out of control.
You choose a sequence of stopping rules, such as "stop when the size reaches $n$", and each stopped game is fair.
The full game may still fail to be fair, because rare huge swings can push the expected value away from its start.
For example, a Brownian motion started at $0$ is a martingale and hence a local martingale.
