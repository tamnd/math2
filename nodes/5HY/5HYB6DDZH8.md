---
tag: 5HYB6DDZH8
kind: concept
name: Weierstrass transform
msc: [44A15, 35K05]
specializes: [YCK709QB06]
sources:
  - url: https://en.wikipedia.org/wiki/Weierstrass_transform
same_as:
  wikidata: Q7979829
  wikipedia: Weierstrass transform
---

## Summary

The Weierstrass transform of a function $f$ on the real line is its average against a Gaussian weight of variance $2$ centred at each point.
It is the solution at time $t = 1$ of the [[heat equation|VP2HN86VAG]] $u_t = u_{xx}$ with initial value $f$.
It smooths every function it is applied to, and on the Fourier side it multiplies by a Gaussian.
Weierstrass used this smoothing in his proof of the approximation theorem that bears his name.

## Explanations

### L1 human

Imagine $f$ as a temperature profile along a long thin rod.
Let the heat flow for one unit of time: sharp peaks spread out and the profile becomes smooth.
The new profile is the Weierstrass transform of $f$.
Each new value is a weighted mean of old values, with the largest weights on nearby points.
For example, the transform of $x^2$ is $x^2 + 2$, because averaging adds the variance $2$ of the Gaussian weight.
