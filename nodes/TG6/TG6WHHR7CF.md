---
tag: TG6WHHR7CF
kind: concept
name: Geometric realization
msc: [55U10, 18N50]
sources:
  - url: https://en.wikipedia.org/wiki/Simplicial_set
---

## Summary

The geometric realization $\abs{K}$ of a [[simplicial set|WW81ARB8K9]] $K$ is a topological space.
It has one topological $n$-simplex for each $n$-simplex of $K$, glued as the face and degeneracy maps prescribe.
It is a CW complex with one $n$-cell for each nondegenerate $n$-simplex.
Realization is left adjoint to the [[singular simplicial set|RWBMXQW6S5]] functor, and the two functors identify the homotopy theory of simplicial sets with that of spaces.

## Explanations

### L1 human

A simplicial set is a list of points, edges, triangles and higher simplices with instructions for how they meet.
The realization builds the actual shape: it takes a real triangle for each listed triangle, a real segment for each edge, and glues them together.
Degenerate simplices, which are collapsed copies of lower ones, are squashed and add nothing new.
For example, one vertex and one nondegenerate edge from that vertex to itself realize to a circle.
