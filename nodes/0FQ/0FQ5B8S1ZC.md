---
tag: 0FQ5B8S1ZC
kind: definition
name: Spanning tree
msc: [05C05]
defines: 0S4ZEZM7KE
uses: [0P11X5HKAX, 0MJ0JS72DZ]
sources:
  - url: https://en.wikipedia.org/wiki/Spanning_tree
    locator: Definitions
inventory: [B62FGDTWP5]
---

## Definition

Let $G$ be a [[graph|0JD5C82QMB]].
A spanning tree of $G$ is a [[subgraph|0P11X5HKAX]] $T$ of $G$ that contains every vertex of $G$ and is a [[tree|0MJ0JS72DZ]].

## Remarks

A graph has a spanning tree if and only if it is connected. The node [[every connected graph has a spanning tree|04XPQT2XTC]] gives one direction.
A spanning tree of a finite connected graph with $n$ vertices has $n - 1$ edges.
The complete graph $K_n$ has $n^{n-2}$ spanning trees, by [[Cayley's formula|0M2SSGSYPE]]. A [[minimum spanning tree|0Z367CGNRM]] has the least total weight.

## Explanations

### L1 human

A spanning tree keeps all the vertices of a graph and just enough edges to stay connected without any loop.
For a road network, it is a smallest set of roads that still links all towns.
