---
tag: AQ4CNCXAJ0
kind: concept
name: Isogeometric analysis
msc: [65N30, 65D07, 74S22]
specializes: [Y5B0PEBKE8]
sources:
  - url: https://en.wikipedia.org/wiki/Isogeometric_analysis
same_as:
  wikidata: Q17082433
  wikipedia: Isogeometric analysis
---

## Summary

Isogeometric analysis is a [[Galerkin method|Y5B0PEBKE8]] built on spline functions, such as [[B-splines|62AFX32JGT]] and [[NURBS|Y8B2N9ERPE]].
The same functions describe the geometry and approximate the solution.
It was proposed by Thomas Hughes and coworkers to connect computer-aided design directly with simulation.
Geometries given by NURBS, such as circles and cylinders, are represented exactly, with no meshing error.
The basis functions can be smoother than standard finite elements, which helps for higher-order equations.
See the [[definition|VF17XWCK8Z]].

## Explanations

### L1 human

Engineers design shapes on computers with smooth spline curves and surfaces.
Classical finite element methods first replace the shape by a mesh of flat triangles or boxes, which loses the exact geometry.
Isogeometric analysis skips this step and computes directly with the spline functions of the design.
For example, a quarter of a circle is exactly a quadratic NURBS curve, so a ring-shaped part is described without error.
