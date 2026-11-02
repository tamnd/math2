---
tag: YCFPD0GE5G
kind: concept
name: Boundary layer
msc: ["34E15", 76D10]
sources:
  - url: https://en.wikipedia.org/wiki/Boundary_layer
---

## Summary

In a [[singular perturbation|G6J21TGRMM]] problem, a boundary layer is a thin region next to the boundary where the solution changes rapidly.
Outside the layer, the solution of the reduced problem is a good approximation; inside it, this approximation fails.
The layer thickness tends to $0$ with the small parameter.
The notion comes from fluid dynamics, where Prandtl introduced it for the thin layer of fluid near a wall in which viscosity matters.

## Explanations

### L1 human

Air flowing past a wing moves almost freely, except in a very thin sheet close to the surface where it is slowed down to rest.
That sheet is a boundary layer.
Take the equation $\varepsilon y'' + y' = 0$ with $y(0) = 0$ and $y(1) = 1$.
Its solution is close to $1$ on most of the interval, but it falls to $0$ in a region of width about $\varepsilon$ next to $x = 0$.
As $\varepsilon$ gets smaller, the layer gets thinner and steeper.
