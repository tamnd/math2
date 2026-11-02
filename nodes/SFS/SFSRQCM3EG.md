---
tag: SFSRQCM3EG
kind: concept
name: Energy of a measure
msc: [31B15, 31A15]
sources:
  - url: https://en.wikipedia.org/wiki/Capacity_of_a_set
---

## Summary

The energy of a positive measure is the double integral of a potential-theoretic kernel against the measure in both variables.
Typical kernels are $\abs{x - y}^{2-n}$ in $\R^n$ for $n \ge 3$ and $\log(1/\abs{x - y})$ in the plane.
Physically it is the electrostatic energy of the charge distribution described by the measure.
Minimising the energy over probability measures on a compact set defines its [[capacity|4YZVFGJVSZ]] and its equilibrium measure.
Sets that carry no nonzero measure of finite energy are the negligible sets of potential theory.

## Explanations

### L1 human

Spread a unit of electric charge over a body.
Every pair of tiny bits of charge repels with an energy that grows as they get closer, and the energy of the measure adds up all these pair energies.
A point charge has infinite energy, because the charge sits on top of itself.
Charge spread evenly over the unit sphere in space has energy $1$ for the kernel $1/\abs{x - y}$.
