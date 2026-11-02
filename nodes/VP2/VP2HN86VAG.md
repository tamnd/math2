---
tag: VP2HN86VAG
kind: concept
name: Heat equation
msc: [35K05]
specializes: [1CCTH8X2FT]
sources:
  - url: https://en.wikipedia.org/wiki/Heat_equation
same_as:
  wikidata: Q6510488
  wikipedia: Heat equation
---

## Summary

The heat equation $\partial_t u = \Delta u$ describes how temperature, or the concentration of a diffusing substance, evolves in time.
Here $\Delta$ is the [[Laplacian|0E0B6RA8K0]] in the space variables.
It is the model [[parabolic partial differential equation|1CCTH8X2FT]].
Its solutions become smooth at once, spread information at infinite speed, and decay toward equilibrium.
It is linked to probability through the [[Wiener process|22735FGJV6]], and to geometry through the spectrum of the Laplacian.

## Explanations

### L1 human

Heat flows from warm places to cold places, at a rate that depends on how uneven the temperature is.
The Laplacian measures how much the temperature at a point differs from the average around it.
The heat equation says that a point warms up when it is colder than its surroundings and cools down when it is warmer.
On a rod, $u(x, t) = e^{-t} \sin x$ is a solution: a sine-shaped temperature profile that keeps its shape and fades away.
