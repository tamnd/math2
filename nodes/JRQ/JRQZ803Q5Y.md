---
tag: JRQZ803Q5Y
kind: concept
name: Integral functional with a Lagrangian density
msc: [49J10, 49K10, 49K05]
specializes: [1EQM0DJ4NC]
sources:
  - url: https://en.wikipedia.org/wiki/Calculus_of_variations
---

## Summary

An integral functional assigns to a function $u$ the integral of an expression $L(x, u, \nabla u)$ built from the point, the value of $u$ and its derivatives.
The function $L$ is the Lagrangian density.
Most problems of the [[calculus of variations|PQ25NHV0KS]] concern such functionals, for example length, area, energy and action.
Their smooth critical points solve the [[Euler–Lagrange equation|PS0VV149ET]].

## Explanations

### L1 human

Many quantities are computed by adding up small local contributions.
The length of a graph adds up small pieces $\sqrt{1 + y'(x)^2} \, dx$, and an energy adds up local energy densities.
The rule that gives the local contribution from the position, the value and the slope is the Lagrangian density $L$.
For $L(x, z, p) = \sqrt{1 + p^2}$ on $[0, 1]$, the function $y(x) = x$ gets the value $\int_0^1 \sqrt{2} \, dx = \sqrt{2}$, the length of the diagonal of the unit square.
