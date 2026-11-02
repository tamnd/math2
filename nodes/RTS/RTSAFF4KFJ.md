---
tag: RTSAFF4KFJ
kind: concept
name: Mesh generation
msc: [65N50, 65M50, 65D18]
sources:
  - url: https://en.wikipedia.org/wiki/Mesh_generation
same_as:
  wikidata: Q4418033
  wikipedia: Mesh generation
---

## Summary

Mesh generation is the construction of a mesh: a subdivision of a geometric domain into many small simple cells.
Typical cells are triangles, tetrahedra, quadrilaterals or hexahedra.
Meshes are the discrete setting of the [[finite element method|98GZ9DVHTA]], the [[finite volume method|HGKN8E09RS]] and many other numerical methods for partial differential equations.
The quality of a mesh, the size and shape of its cells, controls both the accuracy and the cost of the computation.
Standard tools include [[Delaunay triangulations|259Y10BYJC]], advancing front methods, and [[adaptive mesh refinement|X001F42KH8]].

## Explanations

### L1 human

To compute heat flow in an engine part, a computer cannot handle the solid shape directly.
It first cuts the shape into many small pieces, like a mosaic of tiny triangles or bricks, and computes a simple approximation on each piece.
Making these pieces is mesh generation.
A square, for example, can be cut along a diagonal into two triangles.
Each triangle can be cut again into four smaller ones by joining the midpoints of its sides.
Good meshes use small pieces where the solution changes fast and avoid very thin, flat pieces.
