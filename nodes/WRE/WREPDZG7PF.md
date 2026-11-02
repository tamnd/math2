---
tag: WREPDZG7PF
kind: concept
name: Abstract polytope
msc: [52B15, 51M20, 06A07]
specializes: [1C7TKGTB2F]
sources:
  - url: https://en.wikipedia.org/wiki/Abstract_polytope
same_as:
  wikidata: Q4669958
  wikipedia: Abstract polytope
---

## Summary

An abstract polytope is a partially ordered set that behaves like the set of faces of a polytope ordered by inclusion.
It keeps only the incidence pattern of vertices, edges and higher faces and forgets all geometry.
The axioms ask for a grading by dimension, a connectedness condition, and the diamond condition.
The diamond condition says that between two faces whose dimensions differ by two there are exactly two faces.
Abstract polytopes include the face lattices of convex polytopes, but also tilings and objects such as the hemicube that no convex polytope realises.

## Explanations

### L1 human

Write down the vertices, edges and faces of a shape, and record only which ones touch which.
This list of incidences, ordered by "is part of", is the skeleton that an abstract polytope keeps.
In a polygon, each vertex is on exactly two edges, and each edge has exactly two vertices; the diamond rule generalises this to all dimensions.
Shapes like the hemicube, made by gluing opposite faces of a cube together, fit the rules even though they cannot be built as convex solids.
