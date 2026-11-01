---
tag: 4WCYBSH1P6
kind: concept
name: Matroid minor
msc: [05B35]
sources:
  - url: https://en.wikipedia.org/wiki/Matroid_minor
same_as:
  wikidata: Q17086290
  wikipedia: Matroid minor
---

## Summary

A minor of a [[matroid|PX31ZNYS3Z]] is a matroid obtained from it by deleting some elements and contracting others.
Deletion and contraction generalize the deletion and contraction of edges of a graph, and they are exchanged by [[matroid duality|6QF83CFK2G]].
Many classes of matroids are closed under minors and are characterized by a list of excluded minors.
This parallels the role of [[graph minors|VYQ32ZBPEE]] for classes of graphs.

## Explanations

### L1 human

Deleting an element just throws it away together with every independent set that uses it.
Contracting an element that is not a loop means treating it as already chosen: a set counts as independent when it stays independent after adding that element.
For a graph, deletion removes an edge and contraction shrinks an edge to a point.
A minor is anything you can reach by doing these two operations several times.
