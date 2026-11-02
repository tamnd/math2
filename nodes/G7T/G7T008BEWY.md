---
tag: G7T008BEWY
kind: concept
name: Admissible function
msc: [49K05, 49J05]
sources:
  - url: https://en.wikipedia.org/wiki/Calculus_of_variations
---

## Summary

An admissible function of a variational problem is a function that is allowed to compete for the minimum.
It must lie in the domain of the functional and satisfy every constraint of the problem, such as boundary values or a fixed length.
The set of admissible functions fixes the problem as much as the functional does: a change of the class can change whether a minimiser exists.

## Explanations

### L1 human

Before looking for the best curve, one must say which curves are allowed.
In a problem with fixed ends, only smooth enough curves that start and end at the given points take part.
For example, with ends $y(0) = 0$ and $y(1) = 1$, the curves $y = x$ and $y = x^2$ are admissible, while $y = 2x$ is not, since it ends at height $2$.
