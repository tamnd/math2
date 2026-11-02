---
tag: 7HYF6YG0RS
kind: concept
name: Numerical integration
msc: [65D30, 65D32, 41A55]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_integration
same_as:
  wikidata: Q753445
  wikipedia: Numerical integration
---

## Summary

Numerical integration is the computation of approximate values of [[definite integrals|04TMP0XGMJ]] from finitely many values of the integrand.
It is needed when an antiderivative has no closed form or when the integrand is only known at sample points.
It is also needed for integrals over domains of many dimensions.
The main tools are [[quadrature rules|ADSVMCY77A]], weighted sums of function values, together with error estimates based on the smoothness of the integrand.

## Explanations

### L1 human

The integral of a function is the area under its graph, but often there is no formula for it.
Numerical integration estimates that area by measuring the height of the graph at some points and adding up suitable weighted heights.
The simplest example cuts the interval into strips and replaces each strip by a trapezoid.
For $\int_0^1 e^{-x^2}\, dx$, which has no elementary antiderivative, such methods give $0.7468\ldots$ to any accuracy one wants.
