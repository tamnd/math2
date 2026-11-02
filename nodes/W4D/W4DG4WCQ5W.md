---
tag: W4DG4WCQ5W
kind: concept
name: Cellular homology
msc: [55N10, 55U15]
sources:
  - url: https://en.wikipedia.org/wiki/Cellular_homology
same_as:
  wikidata: Q3139849
  wikipedia: Cellular homology
---

## Summary

Cellular homology is a homology theory for [[CW complexes|5W95QFHXPR]] whose chain groups are free abelian groups on the cells.
Its boundary maps are built from the degrees of the attaching maps of the cells.
It agrees with [[singular homology|M0Q5CFJ7ZH]], so it is often the fastest way to compute the singular homology of a space with a cell structure.

## Explanations

### L1 human

A CW complex is built by gluing points, then intervals, then discs, and so on.
Cellular homology counts these building blocks in each dimension and records how the boundary of each cell wraps around the cells one dimension lower.
The sphere $S^2$ can be built from one point and one disc whose whole boundary is collapsed to the point.
There is one cell in dimension $0$, one in dimension $2$, and no boundary map can be nonzero.
So the homology is $\Z$ in dimensions $0$ and $2$ and zero elsewhere.
