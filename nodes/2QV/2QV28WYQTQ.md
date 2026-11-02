---
tag: 2QV28WYQTQ
kind: concept
name: Least squares approximation
msc: [41A10, 65D10, 41A50]
specializes: [7N4988HN3P]
sources:
  - url: https://en.wikipedia.org/wiki/Least-squares_function_approximation
same_as:
  wikidata: Q6510405
  wikipedia: Least-squares function approximation
---

## Summary

Least squares approximation replaces a function by the element of a given finite-dimensional family that is closest in a mean square sense.
It is the [[best approximation|7N4988HN3P]] in an [[inner product space|0QVNCJXRY3]], so it is the [[orthogonal projection|0B8KZRT28M]] onto the family.
Unlike the uniform best approximation, it is found by solving a linear system, and an orthogonal basis makes it explicit.
It is the function version of the [[least squares|0BYTQ4X1HC]] method for linear systems.

## Explanations

### L1 human

Measure the error of an approximation by squaring the gap at each point and adding up, or integrating.
The least squares approximation is the choice with the smallest total squared error.
Large gaps count a lot, but a single bad point does not decide everything, as it does for the largest-error measure.
For example, the best constant approximation of $x^2$ on $[-1, 1]$ in this sense is its mean value $1/3$.
