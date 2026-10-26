---
tag: ~e95ddbc1
kind: definition
name: Subgraph
msc: [05C99]
defines: ~0fc015ca
uses: [~3f82cef4]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_graph_theory
    locator: S
---

## Definition

Let $G = (V, E)$ be a [[graph|~3f82cef4]].
A subgraph of $G$ is a graph $H = (V', E')$ with $V' \subseteq V$ and $E' \subseteq E$.
Each edge of $E'$ has both ends in $V'$, because $H$ is a graph.

## Remarks

A subgraph is spanning if $V' = V$.
An [[induced subgraph|~841cfb35]] keeps all edges of $G$ between the chosen vertices.
In the cycle $C_4$ with vertices $1, 2, 3, 4$, the path $1 - 2 - 3$ is a subgraph.

## Explanations

### L1 human

To get a subgraph, delete some vertices and some edges of a graph.
When you delete a vertex, you must also delete the edges at that vertex.
