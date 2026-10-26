---
tag: 07CT9RDY7Q
kind: definition
name: Cycle
msc: [05C38]
defines: 0Z05VCBQ7Y
uses: [0PD57PSHNR]
sources:
  - url: https://en.wikipedia.org/wiki/Cycle_(graph_theory)
    locator: Circuit and cycle
---

## Definition

Let $G$ be a [[graph|0JD5C82QMB]].
A cycle in $G$ is a [[circuit|0PD57PSHNR]] $(w_0, w_1, \dots, w_k)$ whose vertices $w_1, \dots, w_k$ are pairwise distinct.

## Remarks

The only repeated vertex is $w_0 = w_k$. In a simple graph, each cycle has length $k \ge 3$.
The vertices and edges of a cycle of length $k$ form a subgraph isomorphic to the [[cycle graph|0QQ0F12962]] $C_k$.
A graph with no cycle is [[acyclic|0XNN9Z8E5A]].

## Explanations

### L1 human

A cycle is a round trip that visits each of its vertices once and comes back to the start.
A triangle is the shortest possible cycle in a simple graph.
