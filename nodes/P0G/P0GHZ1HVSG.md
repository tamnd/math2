---
tag: P0GHZ1HVSG
kind: concept
name: Computational electromagnetics
msc: [35Q61, 65Z05, 78A25]
sources:
  - url: https://en.wikipedia.org/wiki/Computational_electromagnetics
same_as:
  wikidata: Q5157313
  wikipedia: Computational electromagnetics
---

## Summary

Computational electromagnetics is the field of numerical methods that compute solutions of [[Maxwell's equations|9BWWD4QK8Y]] for given sources, materials and geometries.
Exact solutions exist only for simple shapes, so antennas, circuits, optical devices and radar targets are studied with these methods.
One main family solves differential equations on a volume grid, as the [[finite-difference time-domain method|57XRW2119C]] and the [[finite element method|98GZ9DVHTA]] do.
The other solves integral equations on surfaces, as the [[method of moments|YXKZYG618P]] does.
Fast solvers such as the [[fast multipole method|4TA4GXQP6Q]] and absorbing boundaries such as the [[perfectly matched layer|GFKAG6BAXX]] make large problems tractable.

## Explanations

### L1 human

Maxwell's equations describe all of classical electricity, magnetism and light, but they can be solved by hand only in very simple cases.
Computational electromagnetics replaces the continuous fields by finitely many numbers, for example the field values on a grid.
The equations then become a large system that a computer can solve.
For example, an engineer can simulate how a phone antenna radiates before building it.
