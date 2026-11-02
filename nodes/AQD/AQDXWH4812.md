---
tag: AQDXWH4812
kind: concept
name: Positive linear operator
msc: [47B65, 41A36, 46A40]
sources:
  - url: https://en.wikipedia.org/wiki/Positive_linear_operator
same_as:
  wikidata: Q96399850
  wikipedia: Positive linear operator
---

## Summary

A positive linear operator is a [[linear map|0NRYHJPQG2]] between ordered vector spaces that sends nonnegative elements to nonnegative elements.
On spaces of functions, it maps nonnegative functions to nonnegative functions.
Bernstein polynomials, convolution with nonnegative kernels and integration are all positive linear operators.
Their positivity gives strong convergence tests, such as Korovkin's theorem.

## Explanations

### L1 human

A positive operator never turns something nonnegative into something negative.
Averaging is the typical example: an average of nonnegative numbers is nonnegative.
So any operator that replaces $f(x)$ by a weighted average of values of $f$, with nonnegative weights, is positive.
Differentiation is not positive: $1 - x$ is nonnegative on $[0, 1]$, but its derivative is $-1$.
