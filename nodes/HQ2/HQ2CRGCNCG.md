---
tag: HQ2CRGCNCG
kind: concept
name: Numerical relativity
msc: ["83-08", "83C05", "65M06"]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_relativity
same_as:
  wikidata: Q10359034
  wikipedia: Numerical relativity
---

## Summary

Numerical relativity is the branch of general relativity that computes approximate solutions of the [[Einstein field equations|3MCZ97SW6V]] by numerical methods.
Most work follows the [[initial value formulation|SB7BVCZJ3F]].
One solves the constraint equations for initial data, evolves them with a hyperbolic formulation, and extracts physical quantities such as gravitational waves.
In 2005 the first complete simulations of the inspiral and merger of two black holes were achieved.
They were done by Pretorius and by two groups using moving punctures.
The waveforms computed in this way are used to detect and interpret signals in gravitational wave observatories.

## Explanations

### L1 human

Einstein's equations can be solved exactly only in very symmetric situations, such as a single black hole at rest.
For two black holes that orbit each other and merge, one must let a computer solve the equations step by step.
Space is replaced by a grid of points, and the geometry at each point is updated in small time steps.
The result is a prediction of the gravitational waves emitted, which detectors on Earth compare with their data.
