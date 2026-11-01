---
tag: VC6R7XSKRQ
kind: concept
name: Fractional Brownian motion
msc: [60G22, 60G18, 60G15]
specializes: [22WEM6RTW0, RASDTDEKP7]
sources:
  - url: https://en.wikipedia.org/wiki/Fractional_Brownian_motion
same_as:
  wikidata: Q1143293
  wikipedia: Fractional Brownian motion
---

## Summary

Fractional Brownian motion is a continuous centred [[Gaussian process|22WEM6RTW0]] with stationary increments that is [[self-similar|RASDTDEKP7]] with a Hurst index $H \in (0, 1)$.
For $H = 1/2$ it is the [[Wiener process|22735FGJV6]].
For $H \ne 1/2$ its increments are correlated.
For $H > 1/2$ this gives long memory, which is used to model data in hydrology, finance and network traffic.

## Explanations

### L1 human

Ordinary Brownian motion forgets its past: each new step is independent of the earlier ones.
Fractional Brownian motion has a memory controlled by one number $H$ between $0$ and $1$.
For $H > 1/2$, a rise tends to be followed by a rise, so paths look smoother and trend more.
For $H < 1/2$, a rise tends to be followed by a fall, so paths look rougher and more jagged.
