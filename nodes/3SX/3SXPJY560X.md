---
tag: 3SXPJY560X
kind: concept
name: Stoer–Wagner algorithm
sources:
  - wikipedia: en:48751362@r1283990532
    locator: Stoer–Wagner algorithm
    note: adopted
    mention: wikipedia://en/48751362
    sections: [Summary]
same_as:
  wikidata: Q23808439
  wikipedia: Stoer–Wagner algorithm
inventory: [9DB3ZM1TC1]
---

## Summary

In graph theory, the **Stoer–Wagner algorithm** is a recursive algorithm to solve the minimum cut problem in undirected weighted graphs with non-negative weights. It was proposed by Mechthild Stoer and Frank Wagner in 1995. The essential idea of this algorithm is to shrink the graph by merging the most intensive vertices, until the graph only contains two combined vertex sets. At each phase, the algorithm finds the minimum $s$-$t$ cut for two vertices $s$ and $t$ chosen at its will. Then the algorithm shrinks the edge between $s$ and $t$ to search for non $s$-$t$ cuts. The minimum cut found in all phases will be the minimum weighted cut of the graph.
