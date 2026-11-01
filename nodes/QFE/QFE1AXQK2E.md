---
tag: QFE1AXQK2E
kind: definition
name: Graph minor
msc: [05C83]
defines: VYQ32ZBPEE
uses: [0JD5C82QMB, 0P11X5HKAX, 0FFAYNMAJZ, 00CT0PTH74]
sources:
  - url: https://en.wikipedia.org/wiki/Graph_minor
---

## Definition

Let $G$ and $H$ be finite [[graphs|0JD5C82QMB]].
Let $uv$ be an edge of $G$.
The contraction $G / uv$ is obtained from $G$ by removing $u$ and $v$ and adding a new vertex $w$.
The new vertex $w$ is adjacent to each other vertex that was adjacent to $u$ or to $v$.
The graph $H$ is a minor of $G$ if finitely many edge contractions turn a [[subgraph|0P11X5HKAX]] of $G$ into a graph [[isomorphic|00CT0PTH74]] to $H$.

## Remarks

Equivalently, there are pairwise disjoint nonempty sets $B_x \subseteq V(G)$, one for each vertex $x$ of $H$, with two properties.
Each $B_x$ induces a [[connected|0FFAYNMAJZ]] subgraph of $G$.
For each edge $xy$ of $H$, some edge of $G$ joins $B_x$ to $B_y$.
The sets $B_x$ are called branch sets.
Example: $K_5$ is a minor of the [[Petersen graph|0NR95CTFCZ]].
Take as branch sets the five spokes, each made of an outer vertex and its inner neighbour.
Then the outer $5$-cycle and the inner pentagram join every two branch sets.
Non-example: the triangle $K_3$ is not a minor of any tree, because deleting and contracting edges of a forest always gives a forest.
Every subgraph is a minor, but a minor need not be a subgraph.
For example, $K_3$ is a minor of every cycle $C_n$ with $n \ge 3$ but a subgraph only of $C_3$.
