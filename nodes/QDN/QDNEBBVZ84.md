---
tag: QDNEBBVZ84
kind: concept
name: Voronoi diagram
msc: [52C99, 68U05]
sources:
  - url: https://en.wikipedia.org/wiki/Voronoi_diagram
same_as:
  wikidata: Q757267
  wikipedia: Voronoi diagram
---

## Summary

The Voronoi diagram of a finite set of points, the sites, divides space into cells, one for each site.
The cell of a site consists of the points that are at least as close to it as to any other site.
Voronoi diagrams are a basic structure of computational geometry, with uses in nearest-neighbour search, mesh generation and the geometry of numbers.

## Explanations

### L1 human

Imagine a few post offices in a town, and assign every house to its nearest post office.
The regions that you get are the cells of the Voronoi diagram.
For two sites the dividing line is the perpendicular bisector of the segment between them.
For more sites each cell is a convex polygon, possibly unbounded, bounded by pieces of such bisectors.
