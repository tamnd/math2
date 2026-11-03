---
tag: TBWVJXMM45
kind: concept
name: Wiener index
msc: [05C09, 05C92, 05C12]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener_index
same_as:
  wikidata: Q909065
  wikipedia: Wiener index
---

## Summary

The Wiener index of a connected graph is the sum of the [[distances|0QV9VNNB4Z]] between all unordered pairs of vertices.
Harry Wiener introduced it in 1947 to predict boiling points of alkanes from their carbon skeletons.
It is the oldest topological index of [[chemical graph theory|AE724Y8CQX]].
In graph theory it is studied as a measure of how compact a graph is.

## Explanations

### L1 human

Pick two atoms of a molecule and count the bonds on the shortest route between them.
Do this for every pair and add up the counts: the total is the Wiener index.
A long, thin molecule has a large index, and a compact, branched one has a smaller index.
For the four-carbon skeletons, the path has index $10$ and the star with three leaves has index $9$.
Branched alkanes tend to boil at lower temperatures, and the index captures part of this trend.
