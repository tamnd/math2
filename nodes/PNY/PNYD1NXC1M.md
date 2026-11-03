---
tag: PNYD1NXC1M
kind: concept
name: Dyson series
msc: [81Q15, 81Q05]
sources:
  - url: https://en.wikipedia.org/wiki/Dyson_series
same_as:
  wikidata: Q3957888
  wikipedia: Dyson series
---

## Summary

The Dyson series expresses the time evolution operator of a quantum system with a time-dependent Hamiltonian as a sum of iterated integrals of the perturbation.
It is the formal solution of the Schrödinger equation in the [[interaction picture|3R1P5CQ1Y7]], often written as a time-ordered exponential.
Truncating it gives time-dependent perturbation theory, and in quantum field theory its terms are drawn as Feynman diagrams.
For bounded perturbations it converges, by the same estimate as [[Picard iteration|0RJ5NHWYTP]].

## Explanations

### L1 human

When a system is pushed by a force that changes in time, there is usually no closed formula for its evolution.
The Dyson series builds the answer step by step: no push, then one push at some moment, then two pushes at two moments, and so on.
Each extra push adds one more integral over time and one more factor of the small perturbation.
If the perturbation does not depend on time, the series is just the power series of the exponential.
