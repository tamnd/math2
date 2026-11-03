---
tag: R9QXJKR32A
kind: statement
role: lemma
name: Lightest edge leaving a component of a spanning forest extends to a minimum spanning tree
msc: [05C05, 05C85]
uses: [09JP6G9FTA, 01VVP10MWJ, 0FQ5B8S1ZC, 0Z367CGNRM]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_graphalgorithms_min-wt-span.ptx#L75
    locator: source/s_graphalgorithms_min-wt-span.ptx:75
---

## Statement

Let $G$ be a finite connected [[graph|0JD5C82QMB]] with real edge weights.
Let $F$ be a spanning [[forest|09JP6G9FTA]] of $G$, and let $C$ be a [[connected component|01VVP10MWJ]] of $F$.
Suppose that $e = xy$ has the least weight among all edges of $G$ with exactly one endpoint in $C$.

Then, among the [[spanning trees|0FQ5B8S1ZC]] of $G$ that contain $F$, some tree of least weight contains $e$.

## Remarks

This is the key step behind greedy methods for a [[minimum spanning tree|0Z367CGNRM]], such as Prim's algorithm and Kruskal's algorithm.
The usual proof takes a lightest spanning tree containing $F$ that misses $e$, adds $e$, and removes another edge of the new cycle that leaves $C$.
