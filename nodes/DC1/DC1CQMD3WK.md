---
tag: DC1CQMD3WK
kind: concept
name: Graph of groups
msc: ["20E08", "20E06"]
sources:
  - url: https://en.wikipedia.org/wiki/Graph_of_groups
same_as:
  wikidata: Q3115551
  wikipedia: Graph of groups
---

## Summary

A graph of groups is a connected graph with a group attached to each vertex and each edge.
Each edge group comes with injective homomorphisms into the groups of the end vertices of the edge.
Its fundamental group glues the vertex groups along the edge groups.
It is the central object of [[Bass–Serre theory|6M731X66RD]]: groups acting on trees are exactly fundamental groups of graphs of groups.
The simplest cases give the amalgamated free product and the [[HNN extension|YEYERRY37K]].

## Explanations

### L1 human

Think of each vertex group as a building block, and each edge as an instruction to glue two blocks along a common piece, the edge group.
With two vertices and one edge one gets an amalgam $A *_C B$: two groups glued along a shared subgroup.
With one vertex and a loop one glues a group to itself, which gives an HNN extension.
If all the groups are trivial, the fundamental group is just the fundamental group of the graph, a free group.
