---
tag: PX31ZNYS3Z
kind: concept
name: Matroid
msc: [05B35]
sources:
  - url: https://en.wikipedia.org/wiki/Matroid
same_as:
  wikidata: Q898572
  wikipedia: Matroid
---

## Summary

A matroid is a finite set together with a notion of independence for its subsets that behaves like [[linear independence|0CRMGPAH83]] of vectors.
Matroids abstract both linear independence in vector spaces and acyclic sets of edges ([[forests|0GGXWDNKBR]]) in graphs.
They have many equivalent descriptions, by independent sets, [[bases|QTSQR7130G]], [[rank functions|SYRCTH853H]], circuits or closure, and every matroid has a [[dual|6QF83CFK2G]].
Matroids explain why the greedy algorithm works and carry invariants such as the [[Tutte polynomial|C81RAXD6DV]].

## Explanations

### L1 human

Take some vectors, and call a set of them independent if none is a combination of the others.
Or take the edges of a graph, and call a set of edges independent if it contains no cycle.
In both cases, small independent sets can always be enlarged using elements of bigger ones.
A matroid keeps only this rule and forgets where the elements came from.
