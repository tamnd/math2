---
tag: 6R3FTQGV2V
kind: concept
name: Biochemical systems theory
msc: [92C42, 92C45, 34C60]
sources:
  - url: https://en.wikipedia.org/wiki/Biochemical_systems_theory
same_as:
  wikidata: Q4914715
  wikipedia: Biochemical systems theory
---

## Summary

Biochemical systems theory is a framework for modelling biochemical networks in which every rate is a product of power functions of the concentrations.
It was developed by Michael Savageau from the late 1960s on.
The power-law form comes from a first-order Taylor expansion in logarithmic coordinates, and the exponents are kinetic orders.
Its main model classes, generalized mass action systems and S-systems, have steady states that can be computed by linear algebra on logarithms.

## Explanations

### L1 human

Real rate laws can be complicated, but on a log–log plot they often look nearly straight over the range that matters.
A straight line on a log–log plot is a power law, such as rate $= 2\, X^{0.5} Y^{-1}$.
Biochemical systems theory writes every rate in this form, with exponents that say how sensitive the rate is to each substance.
This makes large networks easy to write down, simulate and compare, and its steady states come from solving linear equations in the logarithms.
