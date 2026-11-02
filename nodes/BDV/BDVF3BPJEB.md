---
tag: BDVF3BPJEB
kind: concept
name: Energy drift
msc: [65P10, 65L20]
sources:
  - url: https://en.wikipedia.org/wiki/Energy_drift
same_as:
  wikidata: Q5377040
  wikipedia: Energy drift
---

## Summary

Energy drift is the gradual, systematic change of the total energy of a [[Hamiltonian system|0EDKGA2FAK]] in a numerical simulation.
The exact solution keeps the energy constant.
It comes from the accumulation of the small errors of the integrator over many steps.
Its size and growth are a basic test of the quality of a long simulation, for example in molecular dynamics.
Its absence is one of the main benefits of [[symplectic integrators|B4C25SXFRE]].

## Explanations

### L1 human

A frictionless pendulum keeps its energy forever.
A computer simulation of it makes a small error at each step, and with many methods these errors push the energy steadily up or down.
After a long run, the simulated pendulum swings much higher or lower than it should: this is energy drift.
With the explicit Euler method on the oscillator $q' = p$, $p' = -q$, the energy is multiplied by $1 + h^2$ at every step, so it grows without bound.
Good methods for long runs let the energy wobble a little around its true value, without a trend.
