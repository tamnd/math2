---
tag: 0JDE56HWQ8
kind: definition
name: Path
msc: [05C38]
defines: 03NAMV1DHJ
uses: [0VJZM0F9YM]
sources:
  - url: https://en.wikipedia.org/wiki/Path_(graph_theory)
    locator: Walk, trail, and path
---

## Definition

Let $G$ be a [[graph|0JD5C82QMB]].
A path in $G$ is a [[walk|0VJZM0F9YM]] $(w_0, w_1, \dots, w_k)$ whose vertices $w_0, w_1, \dots, w_k$ are pairwise distinct.

## Remarks

A path uses each edge at most once, so every path is a [[trail|062MQGP8M5]].
A path of length $k$ has $k + 1$ vertices. Its vertices and edges form a subgraph isomorphic to the [[path graph|075WR6W3Y3]] $P_{k+1}$.
Each walk from $u$ to $v$ contains a path from $u$ to $v$. The node [[every walk contains a path|09VZBHB33V]] states this.

## Explanations

### L1 human

A path is a walk that never visits the same vertex twice.
On a map, it is a route that never passes through the same crossing again.
