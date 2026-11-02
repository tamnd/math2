---
tag: VQ2BTYFST4
kind: concept
name: Geometric integrator
msc: [37M15, 65P10, 65L06]
sources:
  - url: https://en.wikipedia.org/wiki/Geometric_integrator
same_as:
  wikidata: Q5535490
  wikipedia: Geometric integrator
---

## Summary

A geometric integrator is a numerical method for differential equations that keeps exactly a geometric property of the exact [[flow|06738GGWWK]].
Examples of such properties are symplecticity, a conserved quantity, volume, time-reversibility, and staying on a manifold.
General-purpose methods only approximate such properties, and the small violations add up over long times.
Keeping the structure exactly gives much better qualitative behaviour in long simulations, for example in celestial mechanics and molecular dynamics.
[[Symplectic integrators|B4C25SXFRE]] are the best known class.

## Explanations

### L1 human

The exact motion of a frictionless pendulum keeps its energy, and its phase-space picture has a precise geometric structure.
A typical numerical method makes tiny errors in this structure at each step, and after many steps the computed pendulum may spiral outwards or inwards.
A geometric integrator is designed so that the structure is kept exactly, step by step.
Its trajectories may still be slightly off, but they look like trajectories of a nearby system of the same kind.
For example, the symplectic Euler method on the harmonic oscillator maps each step by a matrix of determinant $1$, so areas in the phase plane are kept.
The explicit Euler method inflates them by the factor $1 + h^2$ at every step.
