---
tag: 0KDADE9RQ8
kind: definition
name: Vertex cover
msc: [05C70, 05C69]
defines: 0AHKWBQSWV
sources:
  - url: https://en.wikipedia.org/wiki/Vertex_cover
    locator: Definition
inventory: [J9T2YR1VBK]
---

## Definition

Let $G$ be a [[graph|0JD5C82QMB]].
A vertex cover of $G$ is a set $S$ of vertices of $G$ that contains at least one end of each edge.

## Remarks

A set $S$ is a vertex cover if and only if its complement is an [[independent set|0KZJ82WEPP]].
For the [[complete bipartite graph|0V0GC7BQAN]] $K_{m,n}$, the least size of a vertex cover is $\min\{m, n\}$.
Each vertex of a cover meets at most one edge of a [[matching|0Z87BHAFTB]]. Thus every vertex cover has at least as many vertices as any matching has edges.

## Explanations

### L1 human

A vertex cover is a set of vertices that touches every edge.
Think of guards at crossings: each street must have a guard at one of its two ends.
