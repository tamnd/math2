---
tag: SZ1R8N1NR7
kind: concept
name: Manifold with corners
msc: [58A05, 57R99]
sources:
  - url: https://en.wikipedia.org/wiki/Manifold
---

## Summary

A smooth manifold with corners is a space modelled near each point on an open subset of the closed orthant $[0, \infty)^n$.
Its changes of chart are smooth.
It allows boundary points where several boundary faces meet at an angle, like the vertices of a square or a cube.
Products of manifolds with boundary are manifolds with corners.
This is one reason the notion is needed, for example in cobordism theory and in Stokes' theorem on cubes.

## Explanations

### L1 human

A closed square has an edge, like a closed disk, but its edge has four sharp corners.
As a topological space the square is just a disk, so the corners only matter when one wants to do calculus.
A manifold with corners keeps track of them: near a corner it looks like the corner of the quarter-plane $\set{x \ge 0, y \ge 0}$.
The solid cube is a $3$-dimensional example, with faces, edges and vertices as boundary strata.
