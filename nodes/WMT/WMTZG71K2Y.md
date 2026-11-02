---
tag: WMTZG71K2Y
kind: concept
name: Richardson extrapolation
msc: [65B05, 40A25]
specializes: [B1S2XJPGYD]
sources:
  - url: https://en.wikipedia.org/wiki/Richardson_extrapolation
same_as:
  wikidata: Q1063089
  wikipedia: Richardson extrapolation
---

## Summary

Richardson extrapolation combines two approximations computed with step sizes $h$ and $h/t$ so that the leading term of their error cancels.
It applies whenever the error of a method has a known expansion in powers of the step size.
Repeated, it turns the trapezoidal rule into Romberg integration, and it is used throughout numerical differentiation, integration and the solution of differential equations.

## Explanations

### L1 human

Suppose a method has error roughly proportional to $h^2$, where $h$ is a step size.
Halving $h$ divides the error by about $4$.
Knowing this, one can combine the two results so that the $h^2$ parts cancel exactly: $\frac{4 A(h/2) - A(h)}{3}$.
What remains is a much smaller error, of higher order in $h$.
