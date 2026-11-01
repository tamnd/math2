---
tag: V8GZ0W1ZZ5
kind: concept
name: Simplicial complex
msc: ["05E45", 55U10]
sources:
  - url: https://en.wikipedia.org/wiki/Abstract_simplicial_complex
same_as:
  wikidata: Q4669959
  wikipedia: Abstract simplicial complex
---

## Summary

An abstract simplicial complex is a family of finite sets closed under taking subsets.
Each set of size $k + 1$ stands for a $k$-dimensional simplex: a point, a segment, a triangle, a tetrahedron, and so on.
Simplicial complexes describe spaces by finite combinatorial data, and they link combinatorics with topology and commutative algebra through [[f-vectors and h-vectors|DCK64GFPD7]], homology and Stanley–Reisner rings.

## Explanations

### L1 human

Build a shape by gluing points, segments, triangles and their higher analogues along common faces.
Record each piece by its set of corner labels.
If a triangle $\set{1, 2, 3}$ is in the list, then its edges $\set{1, 2}$, $\set{1, 3}$, $\set{2, 3}$ and its corners must be in the list too.
The list of the three corners and the three edges of a triangle, without the triangle itself, describes a loop: the boundary of the triangle.
