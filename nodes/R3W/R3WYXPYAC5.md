---
tag: R3WYXPYAC5
kind: definition
name: Numerical relativity
msc: ["83-08", "83C05", "65M06"]
defines: HQ2CRGCNCG
uses: [7C2WP33E10, SB7BVCZJ3F, CFAFAPV7HB, P458KSQTWV, PPB51F8QVK, X7HYEBA5SA]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_relativity
---

## Definition

*Numerical relativity* is the computation of approximate solutions of the [[Einstein field equations|7C2WP33E10]], usually together with equations for matter, by discretisation.
In its standard form, a computation has three parts.

1. Initial data: one solves numerically the constraint equations of the [[initial value formulation|SB7BVCZJ3F]] on a spatial slice.
2. Evolution: one writes the remaining equations as a hyperbolic system, chooses gauge conditions for lapse and shift, and integrates in time.
3. Extraction: one computes physical quantities from the solution, such as gravitational waveforms, horizons, masses and momenta.

## Remarks

Common evolution systems are the [[BSSN formalism|P458KSQTWV]] and the generalised harmonic formulation, which builds on the [[harmonic coordinate condition|PPB51F8QVK]].
The [[ADM formalism|CFAFAPV7HB]] gives the 3+1 split used in both, but its own evolution equations are only weakly hyperbolic and not stable in practice.
Spatial derivatives are approximated by [[finite difference methods|X7HYEBA5SA]] or by spectral methods, often with adaptive mesh refinement.
Example: a simulation of two equal-mass black holes, from orbit to merger and ringdown, is a computation in this sense.
Non-example: the post-Newtonian expansion of the same system is an analytic approximation in powers of $v/c$, not a discretisation of the field equations.
Black hole interiors contain singularities, which codes avoid by excision or by puncture methods.

## Explanations

### L1 human

Numerical relativity solves Einstein's equations on a computer when no formula for the solution is known.
