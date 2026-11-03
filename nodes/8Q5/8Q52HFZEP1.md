---
tag: 8Q52HFZEP1
kind: concept
name: Cagniard–De Hoop method
msc: [74J05, 74H05, 35L05]
sources:
  - url: https://en.wikipedia.org/wiki/Cagniard–De_Hoop_method
same_as:
  wikidata: Q5017373
  wikipedia: Cagniard–De Hoop method
---

## Summary

The Cagniard–De Hoop method is a technique to find exact closed-form solutions of transient wave problems in media made of homogeneous layers or half-spaces.
It combines a [[Laplace transform|0V49JEZW06]] in time with a transform in the horizontal coordinates, and then deforms the integration contour in the complex plane.
On the deformed path the solution is visibly the Laplace transform of an explicit function of time, which can then be read off.
It is a standard tool of [[elastodynamics|T1PYEBKBAJ]] and of seismology, for example for pulses in an elastic half-space.

## Explanations

### L1 human

A sharp blow on the surface of the ground sends out several kinds of waves, which arrive at a listener at different times.
Usually one computes such waves with transforms and then has to invert the transforms, which is hard.
The trick of this method is to bend the path of integration so cleverly that the inverse transform can be read off without computing it.
The answer comes out as a formula in time, with each wave arrival showing up as the moment where a term switches on.
For the simplest case, a line source in a uniform plane medium, it gives the familiar wave that starts at time $r/c$ and then slowly fades.
