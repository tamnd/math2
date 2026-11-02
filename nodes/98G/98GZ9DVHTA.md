---
tag: 98GZ9DVHTA
kind: concept
name: Finite element method
msc: [65N30, 65M60]
specializes: [Y5B0PEBKE8]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_element_method
same_as:
  wikidata: Q220184
  wikipedia: Finite element method
---

## Summary

The finite element method is a way to compute approximate solutions of boundary value problems for [[partial differential equations|GC5BDZ6QBC]].
It writes the problem in [[weak form|SJZX81A783]] and splits the domain into small pieces such as triangles.
Then it looks for the best approximation among functions that are polynomials on each piece.
It is a [[Galerkin method|Y5B0PEBKE8]] whose basis functions are supported on a few pieces, so it leads to a large sparse linear system.
It handles complicated geometries well and is the standard tool of engineering simulation in structural mechanics, heat flow and electromagnetism.

## Explanations

### L1 human

Cover the region with a mesh of small triangles.
On each triangle, approximate the unknown function by a flat (linear) piece, and glue the pieces so that the result is continuous.
Each such function is fixed by its values at the corners of the triangles, so the problem becomes finding finitely many numbers.
The equation is not imposed point by point, but in an averaged sense against every function of the same kind.
For the equation $-u'' = f$ on an interval with "hat" functions on a uniform grid, this gives the tridiagonal system with rows $(-1, 2, -1)/h$.
