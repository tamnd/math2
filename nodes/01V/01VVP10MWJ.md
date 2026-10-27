---
tag: 01VVP10MWJ
kind: definition
name: Connected component
msc: [05C40]
defines: 0JG9W3KA6B
uses: [0J8XE7W68F]
sources:
  - url: https://en.wikipedia.org/wiki/Component_(graph_theory)
    locator: Definitions and examples
inventory: [TJ8VFMWKAW]
---

## Definition

Let $G$ be a [[graph|0JD5C82QMB]].
A connected component of $G$ is an equivalence class of the vertices of $G$ under [[reachability|0J8XE7W68F]].
The subgraph induced by a connected component is also called a connected component.

## Remarks

The connected components partition the vertex set. Each component, as an induced subgraph, is [[connected|0FFAYNMAJZ]].
A graph with $n$ vertices and $m$ edges has at least $n - m$ components.
A graph with no edges on $n$ vertices has $n$ components.

## Explanations

### L1 human

The connected components are the separate pieces of a graph.
Two vertices are in the same piece exactly when a walk joins them.
