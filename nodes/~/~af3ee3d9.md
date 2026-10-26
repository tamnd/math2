---
tag: ~af3ee3d9
kind: definition
name: Refinement of a partition
msc: [26A42]
defines: ~acbdba39
uses: [~de6fd15c]
sources:
  - url: https://en.wikipedia.org/wiki/Partition_of_an_interval
    locator: Refinement of a partition
---

## Definition

Let $P$ and $Q$ be [[partitions|~de6fd15c]] of $[a, b]$.
The partition $Q$ is a refinement of $P$ if each point of $P$ is also a point of $Q$.

## Remarks

Any two partitions $P$ and $Q$ have a common refinement, made of the points of both.
Refining a partition lowers the upper [[Darboux sum|~fb054658]] and raises the lower Darboux sum, or leaves them unchanged.

## Explanations

### L1 human

A refinement cuts the interval at more points.
Each old subinterval is cut into one or more new subintervals.
