---
tag: ZZWHGGFB4P
kind: concept
name: Obstruction theory
msc: [55S35, 55S36, 55S40]
sources:
  - url: https://en.wikipedia.org/wiki/Obstruction_theory
same_as:
  wikidata: Q1017338
  wikipedia: Obstruction theory
---

## Summary

Obstruction theory studies when a map defined on part of a [[CW complex|5W95QFHXPR]] extends to the whole complex, or when a fibration has a section.
It works by extending one skeleton at a time.
At each step the problem of going one cell dimension higher is measured by a cohomology class, the obstruction.
The method turns geometric extension problems into computations in [[singular cohomology|6N7BC70CX0]] with coefficients in [[homotopy groups|P976WYEFMB]].
Characteristic classes such as the Euler class and the Stiefel–Whitney classes arise as obstructions of this kind.

## Explanations

### L1 human

To extend a map over a CW complex, one builds it cell by cell, in order of dimension.
A map on the boundary sphere of a new cell extends over the cell exactly when it is null-homotopic.
Recording, for each cell, the homotopy class of the map on its boundary gives a cochain, the obstruction cocycle.
If its cohomology class vanishes, one can change the map on lower cells so that every cell of the next dimension can be filled.
For example, the identity of $S^n$ does not extend over the disc $D^{n+1}$, and the obstruction is the generator of $H^{n+1}(D^{n+1}, S^n; \Z) \cong \Z$.
