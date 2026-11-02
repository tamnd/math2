---
tag: 1A83RGDDNE
kind: concept
name: Convex join
msc: [52A05]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_hull
---

## Summary

The convex join of two sets is the union of all [[line segments|VQ4Q2V45RP]] that start in the first set and end in the second.
When both sets are [[convex|02AS45T3H9]] and nonempty, the convex join is the [[convex hull|0FQSDC2EQ2]] of their union.
So it gives a concrete way to build the hull of two convex pieces from segments alone.

## Explanations

### L1 human

Take two shapes and join every point of the first to every point of the second by a straight segment.
The region covered by all these segments is the convex join.
For a point $p$ and a disc, the join is a cone shape: the disc together with all segments from $p$ to it.
For the two points $(0, 0)$ and $(1, 0)$ of the plane, the join is just the segment between them.
