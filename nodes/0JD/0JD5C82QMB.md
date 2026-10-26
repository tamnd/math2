---
tag: 0JD5C82QMB
kind: definition
name: Graph
msc: [05C99]
defines: 00C0BR7D7H
sources:
  - url: https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)
    locator: Graph
---

## Definition

A graph, or simple graph, is a pair $G = (V, E)$ of a set $V$ and a set $E$ of $2$-element subsets of $V$.
The elements of $V$ are the vertices of $G$, and the elements of $E$ are its edges.
Two vertices $u$ and $v$ are adjacent if $\{u, v\} \in E$. The notation for this edge is $uv$, and the notation for adjacency is $u \sim v$.

Equivalently, a graph is a set $V$ with a relation $\sim$ on $V$ that is symmetric and irreflexive.
A graph is finite if $V$ is finite.

## Remarks

In a simple graph, no edge joins a vertex to itself, and two vertices are joined by at most one edge. A [[multigraph|01M5T0KDG7]] drops the second condition, and some variants allow loops.
In a [[directed graph|0R5HTV7REV]] the edges are ordered pairs.
The set $E$ is the [[edge set|0WNGQBPPQX]] of $G$.

## Explanations

### L1 human

A graph is a set of points with lines between some pairs of points.
For example, the people at a party are vertices, and two people are joined by an edge when they know each other.
