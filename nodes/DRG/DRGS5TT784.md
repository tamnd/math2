---
tag: DRGS5TT784
kind: definition
name: Extremal graph theory
msc: [05C35]
defines: SC5QB5F4TE
uses: [00C0BR7D7H, 0WBFFC8XZ9, 0F7QKGJS6B]
sources:
  - url: https://en.wikipedia.org/wiki/Extremal_graph_theory
---

## Definition

Let $H$ be a finite simple [[graph|00C0BR7D7H]] with at least one edge, and let $n \ge 1$ be an integer.
A graph $G$ is *$H$-free* if no [[subgraph|0WBFFC8XZ9]] of $G$ is [[isomorphic|0F7QKGJS6B]] to $H$.
The *extremal number* $\mathrm{ex}(n, H)$ is the largest number of edges of an $H$-free graph with $n$ vertices.
An $H$-free graph with $n$ vertices and $\mathrm{ex}(n, H)$ edges is an *extremal graph* for $H$.
Extremal graph theory is the study of $\mathrm{ex}(n, H)$, of the extremal graphs, and of similar maximum and minimum problems for graphs.

## Remarks

Example: $\mathrm{ex}(4, K_3) = 4$.
The $4$-cycle has $4$ edges and no triangle.
A graph on $4$ vertices with $5$ edges is $K_4$ minus one edge, and it contains a triangle.

Non-example: $K_4$ is not counted for $\mathrm{ex}(4, K_3)$, because it is not $K_3$-free.

The maximum exists, since the empty graph on $n$ vertices is $H$-free and the number of edges is at most $\binom{n}{2}$.
For complete graphs, [[Turán's theorem|0JG1KZSPFZ]] says that $\mathrm{ex}(n, K_{r+1})$ is the number of edges of the [[Turán graph|0VTCABADBE]] $T(n, r)$.
