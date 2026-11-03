---
tag: YXKZYG618P
kind: concept
name: Method of moments in electromagnetics
msc: [78M05, 65R20]
sources:
  - url: https://en.wikipedia.org/wiki/Method_of_moments_(electromagnetics)
same_as:
  wikidata: Q1943821
  wikipedia: Method of moments (electromagnetics)
---

## Summary

The method of moments solves the [[integral equations|R3SG1SN7JQ]] of electromagnetics, such as the [[electric field integral equation|CPF9Q1GR10]], by turning them into a matrix equation.
The unknown current on the surface of a scatterer or antenna is expanded in basis functions, and the equation is tested against weighting functions.
When the weighting functions are the basis functions themselves, it is the [[Galerkin method|Y5B0PEBKE8]].
It is the standard method for antennas and radar scattering, and it is the electromagnetic form of the [[boundary element method|4KPQ61JGD5]].
It is not the method of moments of statistics.

## Explanations

### L1 human

The field scattered by a metal object is produced by currents that flow on its surface.
The method guesses this current as a sum of simple pieces, for example small patches, each with an unknown strength.
Asking the equation to hold "on average" over each patch gives as many equations as unknowns.
Solving this linear system gives the current, and from it the radiated field.
