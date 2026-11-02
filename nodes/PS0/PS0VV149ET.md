---
tag: PS0VV149ET
kind: concept
name: Euler–Lagrange equation
msc: [49K10, 35A15, 49K05]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%E2%80%93Lagrange_equation
same_as:
  wikidata: Q875744
  wikipedia: Euler–Lagrange equation
---

## Summary

The Euler–Lagrange equation of an integral functional $\int L(x, u, \nabla u) \, dx$ is the differential equation satisfied by its smooth critical points, in particular by its smooth minimisers.
It is the analogue, for functionals, of the condition that the derivative vanishes at a minimum.
Many equations of physics and geometry arise this way.
Examples are Laplace's equation from the Dirichlet energy, the minimal surface equation from area, and Newton's equations from the action.
It is the basic necessary condition of the [[calculus of variations|PQ25NHV0KS]].

## Explanations

### L1 human

If a function makes an energy as small as possible, then small changes of the function cannot lower the energy, to first order.
Writing out this condition and integrating by parts gives a differential equation, the Euler–Lagrange equation.
For the length $\int \sqrt{1 + y'^2} \, dx$ of a graph, the equation says $y'' = 0$, so shortest graphs are straight lines.
For the energy $\int \frac{1}{2} \abs{\nabla u}^2 \, dx$, the equation is Laplace's equation $\Delta u = 0$.
