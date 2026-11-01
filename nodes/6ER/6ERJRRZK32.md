---
tag: 6ERJRRZK32
kind: concept
name: Final topology
msc: [54A10, 54B15]
specializes: [0CQHFPGJ45]
sources:
  - url: https://en.wikipedia.org/wiki/Final_topology
same_as:
  wikidata: Q1416138
  wikipedia: Final topology
---

## Summary

Take a set and a family of maps from topological spaces into it.
The final topology on the set is the finest topology that makes all these maps continuous.
The [[quotient topology|0NQ1H2X495]] and the [[disjoint union topology|ZXJKSB30WF]] are both final topologies.
A map out of the set is continuous for it exactly when its composites with all the given maps are continuous.
The dual notion is the [[initial topology|1NWC3710WW]].

## Explanations

### L1 human

Suppose some spaces you understand map into a set.
You want as many open sets as possible while keeping every map continuous.
So you declare a set open exactly when each map pulls it back to an open set.
For example, the map from $[0, 1]$ onto a circle that glues $0$ to $1$ gives the circle its usual topology this way.
