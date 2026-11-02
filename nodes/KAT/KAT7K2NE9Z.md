---
tag: KAT7K2NE9Z
kind: concept
name: Computational geometry
msc: [68U05, 52B55]
sources:
  - url: https://en.wikipedia.org/wiki/Computational_geometry
same_as:
  wikidata: Q874709
  wikipedia: Computational geometry
---

## Summary

Computational geometry is the study of algorithms and data structures for geometric objects such as points, segments, polygons and polyhedra.
Typical problems are computing a [[convex hull|0FQSDC2EQ2]], a [[polygon triangulation|Q6KKBP3RRP]], a [[Voronoi diagram|QDNEBBVZ84]] or a [[Delaunay triangulation|259Y10BYJC]], and finding intersections among many segments.
Its results are measured by running time and memory in terms of the input size, and it relies on combinatorial bounds from [[discrete geometry|Q0RW86P85F]].
Applications include computer graphics, geographic information systems, robotics and computer-aided design.

## Explanations

### L1 human

Computational geometry asks how a computer can answer geometric questions quickly.
Given a million points on a map, which is the nearest post office to each house, and which points form the outer boundary of the set?
A naive method may compare every pair of points, which takes about $n^2$ steps for $n$ points.
Clever methods often need only about $n \log n$ steps, which is a huge saving for large $n$.
