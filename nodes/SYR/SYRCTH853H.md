---
tag: SYRCTH853H
kind: concept
name: Matroid rank
msc: [05B35]
sources:
  - url: https://en.wikipedia.org/wiki/Matroid_rank
same_as:
  wikidata: Q3851976
  wikipedia: Matroid rank
---

## Summary

The rank function of a [[matroid|PX31ZNYS3Z]] assigns to each subset of the ground set the size of its largest independent subsets.
The rank of the matroid is the rank of the whole ground set, the common size of its [[bases|QTSQR7130G]].
Rank generalizes the [[rank of a matrix|0ZC9YTXZRY]] and the size of a spanning forest of a graph, and its properties, notably submodularity, characterize matroids.

## Explanations

### L1 human

Given some of the elements of a matroid, ask how many of them you can keep while staying independent.
That number is their rank.
For a set of vectors it is the dimension of the space they span.
For a set of edges of a graph, keep all the vertices but only these edges.
The rank is the number of vertices minus the number of connected pieces.
In a triangle, the three edges together have rank $3 - 1 = 2$.
