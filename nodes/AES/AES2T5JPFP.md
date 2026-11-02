---
tag: AES2T5JPFP
kind: concept
name: Tempered distribution
msc: [46F05, 46F10, 35D30]
sources:
  - url: https://en.wikipedia.org/wiki/Distribution_(mathematical_analysis)
---

## Summary

A tempered distribution on $\R^n$ is a continuous linear functional on the [[Schwartz space|CG9JEATW3Q]] of smooth, rapidly decreasing functions.
Tempered distributions include all $L^p$ functions, all polynomials, finite measures and the Dirac delta.
They form the natural domain of the [[Fourier transform|DPVM34ADZV]], which maps the space of tempered distributions onto itself.
For this reason they are the standard setting for linear partial differential equations with constant coefficients and for function spaces defined by Fourier analysis.

## Explanations

### L1 human

A tempered distribution is a "generalized function" that is known only through its averages against very nice test functions.
The test functions are smooth and decay faster than any power of $\abs{x}$, so the generalized function may grow, but at most like a polynomial.
A function $f$ of polynomial growth gives the tempered distribution $\varphi \mapsto \int f \varphi \, dx$.
The Dirac delta, $\varphi \mapsto \varphi(0)$, is a tempered distribution that is not a function at all.
The function $e^x$ on $\R$ grows too fast, and it is not a tempered distribution.
