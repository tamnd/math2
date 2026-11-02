---
tag: FDFYCM3YYC
kind: concept
name: Kan complex
msc: [18N50, 55U10]
specializes: [WW81ARB8K9]
sources:
  - url: https://en.wikipedia.org/wiki/Kan_fibration
---

## Summary

A Kan complex is a [[simplicial set|WW81ARB8K9]] in which every horn can be filled to a full simplex.
Kan complexes behave like topological spaces.
Their simplicial homotopy groups are well defined and agree with those of their geometric realization.
The singular simplicial set of every space is a Kan complex.
Kan complexes are the fibrant objects of the Kan–Quillen model structure on simplicial sets.
They are a standard model of $\infty$-groupoids.

## Explanations

### L1 human

A simplicial set is built from points, edges, triangles and higher simplices glued along faces.
A horn is a simplex with one face and its interior removed, like two edges of a triangle that meet at a corner.
In a Kan complex every such horn is part of a full simplex, so two edges that meet can always be completed to a triangle.
This lets one compose and invert paths, as in a space.
The singular simplicial set of a space, whose $n$-simplices are all continuous maps from the standard $n$-simplex, is the basic example.
