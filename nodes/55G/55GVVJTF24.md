---
tag: 55GVVJTF24
kind: concept
name: Numerical diffusion
msc: [65M06, 65M15]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_diffusion
same_as:
  wikidata: Q7069655
  wikipedia: Numerical diffusion
---

## Summary

Numerical diffusion is the smearing of a computed solution caused by the discretisation itself.
It acts like an extra diffusion term that the original equation does not have.
It is most visible in advection problems: a sharp front that should move without change of shape spreads out more and more.
It is measured by the coefficient of the second-derivative term in the modified equation of the scheme.
It is typical of first-order schemes such as the [[upwind scheme|MTCRZC5QKT]].
Some numerical diffusion is often needed for stability, but too much of it destroys the resolution of fine features.

## Explanations

### L1 human

Imagine a square pulse of dye carried by a steady current.
The exact pulse keeps its shape, but a simple computer simulation shows its edges blurring, as if the dye were also spreading by diffusion.
This blur is not physics; it is an error of the method, and it behaves like a diffusion whose strength shrinks with the grid size.
For the upwind scheme, the extra diffusion coefficient is $\frac{a \Delta x}{2}(1 - \nu)$, where $a$ is the speed and $\nu = a \Delta t / \Delta x$.
