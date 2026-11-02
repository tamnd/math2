---
tag: 1DBC9FYF7M
kind: concept
name: Martin kernel
msc: [31C35, 31B05]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson_boundary
---

## Summary

The Martin kernel of a domain is the [[Green's function|M36SD56MWQ]] normalised by its value at a fixed reference point: $M(x, y) = G(x, y) / G(x_0, y)$.
As the pole $y$ runs to the boundary, the functions $M(\cdot, y)$ accumulate at positive harmonic functions.
These limits are the points of the Martin boundary.
For a ball, the limits are the Poisson kernels, so the Martin kernel generalises the [[Poisson kernel|TCYSWCTYYM]] to arbitrary domains.

## Explanations

### L1 human

Put a unit charge at a point $y$ of a grounded domain and measure the potential at $x$.
Divide by the potential at a fixed point $x_0$, so that the value at $x_0$ is always $1$.
This ratio is the Martin kernel.
When $y$ approaches the boundary the potential itself tends to zero, but the ratio usually tends to a nonzero positive harmonic function.
For the unit ball these limits are the Poisson kernels, which describe how boundary values spread inside.
