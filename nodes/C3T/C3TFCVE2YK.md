---
tag: C3TFCVE2YK
kind: concept
name: Infinitesimal stability
msc: [58K25, 57R45]
sources:
  - url: https://en.wikipedia.org/wiki/Singularity_theory
---

## Summary

A smooth map is infinitesimally stable if every infinitesimal deformation of it can be undone.
The undoing uses infinitesimal changes of coordinates in the source and in the target.
It is the linearised form of [[stability|1991WETZF9]]: an equation for vector fields replaces a condition on diffeomorphisms.
Mather's theorem says that for proper maps the two notions agree.
This turns stability into a problem of linear algebra over rings of smooth functions.

## Explanations

### L1 human

Push a smooth map a tiny bit in some direction at each point; that push is a vector field along the map.
The map is infinitesimally stable if every such push can be produced in two steps.
One slides the points of the source along a vector field and the points of the target along another vector field.
A submersion, such as the projection of the plane onto a line, is infinitesimally stable, since any push can be produced by sliding the source alone.
A constant map from a circle to the line is not: sliding the target moves all points by the same amount, and sliding the source does nothing.
