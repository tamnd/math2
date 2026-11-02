---
tag: ZGD3TQX0K6
kind: example
name: Flexible polyhedron
msc: [52C25, 52B10, 51M20]
illustrates: [V5YS9BZX0N, CJ7KCDDF31]
sources:
  - url: https://en.wikipedia.org/wiki/Flexible_polyhedron
same_as:
  wikidata: Q3889052
  wikipedia: Flexible polyhedron
---

## Example

A *flexible polyhedron* is a closed polyhedral surface in $\R^3$ that admits a continuous non-rigid motion in which every face stays congruent to itself.
Its edges act as hinges, and the shape changes while each face moves rigidly.
In the language of [[rigidity of frameworks|V5YS9BZX0N]], its framework of vertices and edges, with the faces triangulated, is flexible.

Bricard found flexible octahedra in 1897.
Their surfaces pass through themselves, so they are not boundaries of solids.
Connelly constructed in 1977 the first flexible polyhedron without self-intersections.
A simpler example is Steffen's polyhedron, with $9$ vertices, $21$ edges and $14$ triangular faces.
It satisfies Euler's formula $9 - 21 + 14 = 2$.

These examples are not convex, as they must be.
[[Cauchy's rigidity theorem|CJ7KCDDF31]] shows that no convex polyhedron is flexible.

## Explanations

### L1 human

Imagine a closed surface made of rigid triangles joined by hinges along their edges.
For a convex shape such as a cube cut into triangles, nothing can move.
Some cleverly built nonconvex shapes do wobble: they bend at the hinges while every triangle stays the same.
Such a shape is a flexible polyhedron.
