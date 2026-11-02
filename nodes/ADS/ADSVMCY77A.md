---
tag: ADSVMCY77A
kind: concept
name: Quadrature rule
msc: [65D32, 41A55]
sources:
  - url: https://en.wikipedia.org/wiki/Quadrature_(mathematics)
---

## Summary

A quadrature rule approximates a [[definite integral|04TMP0XGMJ]] $\int_a^b f$ by a weighted sum $\sum_i w_i f(x_i)$ of values of $f$ at fixed nodes.
It is the basic object of [[numerical integration|7HYF6YG0RS]] in one dimension.
Rules are compared by the polynomials they integrate exactly and by their error for smooth functions.
Newton–Cotes rules use equally spaced nodes, and Gaussian rules use optimally placed nodes.

## Explanations

### L1 human

To estimate an area under a curve, one can measure the curve's height at a few chosen spots and combine the heights with fixed multipliers.
The spots are the nodes, the multipliers are the weights, and the recipe is the quadrature rule.
The same recipe is then used for every function.
For example, the midpoint rule measures the height once, at the centre, and multiplies it by the length of the interval.
