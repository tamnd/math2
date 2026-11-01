---
tag: X6KCW4X5JA
kind: concept
name: Rough path
msc: [60L20]
sources:
  - url: https://en.wikipedia.org/wiki/Rough_path
same_as:
  wikidata: Q7370888
  wikipedia: Rough path
---

## Summary

A rough path is a path together with extra data that play the role of its iterated integrals.
For paths with [[Hölder regularity|012PBA0FMD]] of exponent at most $1/2$, such as Brownian paths, these iterated integrals are not determined by the path itself.
Once they are given, differential equations driven by the path can be solved path by path, and the solution depends continuously on the rough path.
Rough path theory, introduced by Terry Lyons, thus separates the probabilistic and the analytic parts of stochastic calculus.

## Explanations

### L1 human

To solve an equation driven by a very irregular signal, it is not enough to know the signal; one also needs its "areas", the integrals of the signal against itself.
For a smooth signal these areas can be computed, but for a Brownian path different natural choices give different answers.
The Itô and the Stratonovich integrals are two such choices.
A rough path fixes the choice once and for all, and then the equation has a unique, stable solution.
