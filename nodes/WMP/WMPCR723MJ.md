---
tag: WMPCR723MJ
kind: concept
name: Weak and strong extremum
msc: [49K05, 49K99]
sources:
  - url: https://en.wikipedia.org/wiki/Calculus_of_variations
---

## Summary

In the calculus of variations a local minimum depends on what "nearby" means for functions.
A strong local minimum beats every admissible function whose values are close.
A weak local minimum only beats those whose values and slopes are both close.
Every strong local extremum is a weak one, but not conversely.
The [[Euler–Lagrange equation|PS0VV149ET]] and the [[Legendre condition|4HZX2EN319]] are necessary for weak extrema, while the [[Weierstrass excess function|R8TWRPSPNV]] gives a further necessary condition for strong ones.

## Explanations

### L1 human

Two curves can be close in height but very different in slope, like a straight line and a fine zigzag near it.
A weak minimum only has to win against curves that are close in height and in slope.
A strong minimum must also win against wiggly curves that stay close only in height.
Take the functional $\int_0^1 y'(x)^3 \, dx$ with ends $y(0) = 0$ and $y(1) = 1$.
The line $y = x$ wins against all gentle perturbations.
But a curve that drops steeply for a very short time and then climbs gives a much lower value.
