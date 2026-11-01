---
tag: EE1QZRCFPJ
kind: concept
name: Stratonovich integral
msc: [60H05]
sources:
  - url: https://en.wikipedia.org/wiki/Stratonovich_integral
same_as:
  wikidata: Q7622233
  wikipedia: Stratonovich integral
---

## Summary

The Stratonovich integral $\int Y \circ dX$ is a stochastic integral.
It evaluates the integrand at the midpoint of each time step, not at the left end.
It differs from the [[Itô integral|JA95NH206E]] by half the [[quadratic covariation|X4DHMZD5JA]] of $Y$ and $X$.
With this integral the ordinary chain rule of calculus holds, which makes it natural in physics and in stochastic differential geometry.

## Explanations

### L1 human

To integrate against a Brownian path, one sums values of the integrand times small increments of the path.
The Itô integral takes the value at the start of each step, while the Stratonovich integral takes the average of the start and end values.
For smooth paths both choices give the same limit, but for Brownian paths they do not.
For example, $\int_0^t B_s \circ dB_s = \tfrac12 B_t^2$ when $B_0 = 0$, just as in ordinary calculus.
The Itô version instead gives $\tfrac12 (B_t^2 - t)$.
