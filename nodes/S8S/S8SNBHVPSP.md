---
tag: S8SNBHVPSP
kind: concept
name: Persistent homology
msc: [55N31, 62R40]
sources:
  - url: https://en.wikipedia.org/wiki/Persistent_homology
same_as:
  wikidata: Q17099562
  wikipedia: Persistent homology
---

## Summary

Persistent homology studies how the homology of a growing family of spaces changes, and records when each homology class is born and when it dies.
The input is a filtration of a space, often built from a finite point cloud at increasing scales.
The output is a barcode or persistence diagram, a multiset of intervals that summarises the shape of the data across all scales at once.
It is the central tool of topological data analysis.

## Explanations

### L1 human

Start with a finite cloud of points in the plane, and draw a disc of radius $r$ around each point.
As $r$ grows, discs merge, loops appear, and later loops fill in.
Persistent homology records for each component and each loop the radius at which it appears and the radius at which it disappears.
Features that last for a long range of radii are taken as real shape; short-lived ones are taken as noise.
For points spread evenly on a circle, one loop is born early and survives for a long time, which reveals the circle.
