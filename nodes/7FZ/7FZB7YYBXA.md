---
tag: 7FZB7YYBXA
kind: concept
name: k-vertex-connected graph
msc: [05C40]
specializes: [0KWFFMDF8T]
sources:
  - url: https://en.wikipedia.org/wiki/Vertex_connectivity
---

## Summary

A graph is $k$-vertex-connected, or $k$-connected, if it has more than $k$ vertices and stays [[connected|0KWFFMDF8T]] after the removal of any fewer than $k$ vertices.
The largest such $k$ is the vertex connectivity $\kappa(G)$, a measure of how robust a network is against the failure of nodes.
[[Menger's theorem|E6GYGZDBS7]] gives another view.
A graph with more than $k$ vertices is $k$-connected if and only if every two vertices are joined by $k$ internally disjoint paths.
The node [[k-vertex-connected graph|JJN72VZCZE]] gives the precise definition.

## Explanations

### L1 human

Think of a computer network in which some machines may break down.
The network is $2$-connected if the rest of the network can still talk after any single machine fails.
A ring of machines is $2$-connected: removing one machine leaves a chain, which is still in one piece.
A chain is only $1$-connected, since removing a machine in the middle cuts it in two.
