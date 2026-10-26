---
tag: 06SCB3R6BN
kind: definition
name: Graph homomorphism
msc: [05C60]
defines: 052JJ9YVNM
uses: [0JD5C82QMB]
sources:
  - url: https://en.wikipedia.org/wiki/Graph_homomorphism
    locator: Definitions
---

## Definition

Let $G$ and $H$ be [[graphs|0JD5C82QMB]] with vertex sets $V(G)$ and $V(H)$.
A graph homomorphism from $G$ to $H$ is a map $f : V(G) \to V(H)$ such that $f(u) \sim f(v)$ in $H$ whenever $u \sim v$ in $G$.

## Remarks

A homomorphism maps edges to edges. It may map non-adjacent vertices to adjacent ones, and it may map several vertices to one vertex.
A homomorphism from $G$ to the complete graph $K_k$ is the same as a proper [[colouring|0874138YP6]] of $G$ with $k$ colours.
A bijective homomorphism whose inverse is also a homomorphism is a [[graph isomorphism|00CT0PTH74]].

## Explanations

### L1 human

A graph homomorphism is a map of vertices that sends each edge to an edge.
For example, mapping the vertices of a square alternately to the two ends of one edge is a homomorphism from $C_4$ to $K_2$.
