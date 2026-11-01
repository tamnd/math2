---
tag: QHNWVSC6AQ
kind: concept
name: Beta function
msc: [33B15]
sources:
  - url: https://en.wikipedia.org/wiki/Beta_function
same_as:
  wikidata: Q468881
  wikipedia: Beta function
---

## Summary

The beta function $B(x, y)$ is the integral $\int_0^1 t^{x-1}(1 - t)^{y-1}\, dt$ for positive $x$ and $y$.
It is expressed through the [[gamma function|0V3FZMVB4K]] by $B(x, y) = \Gamma(x)\Gamma(y)/\Gamma(x + y)$.
It turns many integrals over intervals and over angles into products of gamma values.
It also gives the normalising constants of the beta distributions in probability.
At positive integers it is the reciprocal of a multiple of a binomial coefficient.

## Explanations

### L1 human

The beta function measures the area under the curve $t^{x-1}(1-t)^{y-1}$ between $0$ and $1$.
Large $x$ pushes the mass of this curve toward $t = 1$, and large $y$ pushes it toward $t = 0$.
For $x = y = 1$ the curve is the constant $1$ and the area is $1$.
For $x = 2$, $y = 1$ the curve is $t$ and the area is $\frac12$.
