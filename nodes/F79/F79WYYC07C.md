---
tag: F79WYYC07C
kind: concept
name: Hausdorff distance
msc: ["54E35", 52A20, 54B20]
sources:
  - url: https://en.wikipedia.org/wiki/Hausdorff_distance
same_as:
  wikidata: Q1501997
  wikipedia: Hausdorff distance
---

## Summary

The Hausdorff distance measures how far two subsets of a [[metric space|0VKD1TP7F3]] are from each other.
It is the smallest $\varepsilon$ such that each set lies in the $\varepsilon$-neighbourhood of the other.
On the nonempty compact subsets of a metric space it is a metric.
With it, the compact convex sets of $\R^n$ form the basic space of convex geometry.

## Explanations

### L1 human

Two shapes are close in the Hausdorff distance if every point of each shape is near some point of the other shape.
Picture thickening one shape by a margin $\varepsilon$ until it swallows the other, and doing the same the other way round.
The smallest margin that works both ways is the Hausdorff distance.
For the intervals $[0, 1]$ and $[0, 2]$ on the line, the distance is $1$: the point $2$ is at distance $1$ from $[0,1]$.
