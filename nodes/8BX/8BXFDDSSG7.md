---
tag: 8BXFDDSSG7
kind: concept
name: Kantorovich polynomials
msc: [41A36, 41A10, 41A35]
sources:
  - url: https://en.wikipedia.org/wiki/Bernstein_polynomial
---

## Summary

Kantorovich polynomials are a variant of [[Bernstein polynomials|0JT92VK307]] that use averages of $f$ over small intervals instead of point values.
Because they only need integrals, they are defined for every integrable function on $[0, 1]$.
They converge to $f$ in the $L^p$ norm for $1 \le p < \infty$.
This makes sense for elements of $L^p$, where point values are not defined.

## Explanations

### L1 human

A Bernstein polynomial looks at $f$ only at the points $k/n$.
If $f$ is only known up to its values on sets of measure zero, those point values mean nothing.
The Kantorovich polynomial replaces the value at a point by the average of $f$ over a small interval around it.
For the constant $1$, every average is $1$, and the Kantorovich polynomial is again $1$.
