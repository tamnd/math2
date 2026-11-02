---
tag: Q6KKBP3RRP
kind: concept
name: Polygon triangulation
msc: [68U05, 52C45]
sources:
  - url: https://en.wikipedia.org/wiki/Polygon_triangulation
same_as:
  wikidata: Q3045660
  wikipedia: Polygon triangulation
---

## Summary

A polygon triangulation cuts a simple polygon into triangles by drawing diagonals between its vertices.
Every simple polygon with $n$ vertices has one, and each triangulation has exactly $n - 2$ triangles and $n - 3$ diagonals.
Triangulations reduce questions about a complicated polygon to questions about triangles.
They are a basic tool of [[computational geometry|KAT7K2NE9Z]], used for area computation, guarding problems such as the [[art gallery theorem|G4WSPQJ6W1]], and graphics.

## Explanations

### L1 human

Take a polygon drawn on paper whose sides do not cross.
Draw straight cuts from corner to corner, staying inside the polygon, until no more cuts fit without crossing.
The polygon is then split into triangles whose corners are corners of the polygon.
For a convex hexagon, the three cuts from one corner to the three non-adjacent corners give $4$ triangles.
It is a planar cousin of the [[triangulation|YH170WBQ6M]] of a space in topology.
