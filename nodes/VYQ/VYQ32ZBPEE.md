---
tag: VYQ32ZBPEE
kind: concept
name: Graph minor
msc: [05C83]
sources:
  - url: https://en.wikipedia.org/wiki/Graph_minor
same_as:
  wikidata: Q905837
  wikipedia: Graph minor
---

## Summary

A graph $H$ is a minor of a graph $G$ if $H$ can be obtained from $G$ by deleting vertices, deleting edges and contracting edges.
The minor relation is a partial order on finite graphs up to isomorphism.
Many natural classes, such as planar graphs and forests, are closed under taking minors.
[[Wagner's theorem|1B2ZJPVV03]] describes planar graphs by two forbidden minors, and the [[Robertson–Seymour theorem|WP3GDNWJJW]] shows that every minor-closed class has a finite list of forbidden minors.

## Explanations

### L1 human

Take a graph and allow three moves: erase a vertex, erase an edge, or shrink an edge so that its two ends merge into one vertex.
Any graph you can reach this way is a minor of the original.
For example, shrinking the five spokes of the Petersen graph turns it into the complete graph $K_5$.
Minors capture the idea of one graph being hidden inside another in a coarse, flexible way.
