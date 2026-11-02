---
tag: VNWH2KADN7
kind: concept
name: Function approximation
msc: [41A65, 41A30]
sources:
  - url: https://en.wikipedia.org/wiki/Function_approximation
same_as:
  wikidata: Q3445816
  wikipedia: Function approximation
---

## Summary

Function approximation is the task of choosing, from a fixed class of simple functions, one that is close to a given target function.
Closeness is measured by a [[norm|0V2WP9B1MF]], for instance the largest pointwise difference or a mean square difference.
The task appears in numerical analysis, in signal processing and in machine learning, where the target is often known only through samples.

## Explanations

### L1 human

Imagine a complicated curve that you want to replace by something easy to store and evaluate.
You choose a family of easy curves, such as polynomials of degree $2$, and pick one whose graph stays near the target.
For instance, on $[0, 1]$ the polynomial $1 + x + x^2/2$ stays within $0.22$ of $e^x$.
How good such a replacement can be depends on the family you allow and on how you measure the gap.
