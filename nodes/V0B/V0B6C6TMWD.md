---
tag: V0B6C6TMWD
kind: concept
name: Triangulation of a point set
msc: [52C99, 68U05, 52B70]
sources:
  - url: https://en.wikipedia.org/wiki/Point-set_triangulation
same_as:
  wikidata: Q17078161
  wikipedia: Point-set triangulation
---

## Summary

A triangulation of a finite set of points in the plane divides the [[convex hull|0FQSDC2EQ2]] of the set into triangles.
The corners of the triangles are exactly the given points.
The triangles meet edge to edge, without overlaps.
Triangulations are used to build meshes, to interpolate data and to study the combinatorics of point sets.

## Explanations

### L1 human

Scatter some nails on a board and stretch a rubber band around all of them; the band shows the convex hull.
Now draw straight segments between nails, without crossings, until no more segment can be added.
The region inside the band is then cut into triangles, and this is a triangulation.
Four points at the corners of a square have two triangulations, one for each diagonal.
