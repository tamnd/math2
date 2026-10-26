---
tag: ~da3e8f8b
kind: definition
name: Cycle
msc: [05C38]
defines: ~a80a0b8c
uses: [~afb368b0]
sources:
  - url: https://en.wikipedia.org/wiki/Cycle_(graph_theory)
    locator: Circuit and cycle
---

## Definition

Let $G$ be a [[graph|~3f82cef4]].
A cycle in $G$ is a [[circuit|~afb368b0]] $(w_0, w_1, \dots, w_k)$ whose vertices $w_1, \dots, w_k$ are pairwise distinct.

## Remarks

The only repeated vertex is $w_0 = w_k$. In a simple graph, each cycle has length $k \ge 3$.
The vertices and edges of a cycle of length $k$ form a subgraph isomorphic to the [[cycle graph|~19143ce5]] $C_k$.
A graph with no cycle is [[acyclic|~d867bc00]].

## Explanations

### L1 human

A cycle is a round trip that visits each of its vertices once and comes back to the start.
A triangle is the shortest possible cycle in a simple graph.
