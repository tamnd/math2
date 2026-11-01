---
tag: HS65DW0HXH
kind: concept
name: Bump function
msc: ["26E10", 46F05]
specializes: [0V33BNKZ9S]
sources:
  - url: https://en.wikipedia.org/wiki/Bump_function
same_as:
  wikidata: Q1143737
  wikipedia: Bump function
---

## Summary

A bump function is a [[smooth function|0V33BNKZ9S]] that vanishes outside a bounded region.
Such functions exist because some smooth functions are not analytic.
They are used to cut off, localize and glue functions.
Examples are smooth partitions of unity, mollification, and test functions in the theory of distributions.

## Explanations

### L1 human

Picture a smooth hill that rises from flat ground and returns to flat ground, with no corners anywhere.
Outside the hill, the function is exactly zero.
A polynomial cannot do this: a polynomial that is zero on an interval is zero everywhere.
The standard formula is $e^{-1/(1 - x^2)}$ for $\abs{x} < 1$ and $0$ elsewhere.
