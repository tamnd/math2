---
tag: 0V05FC4GKQ
kind: definition
name: Induced subgraph
msc: [05C99]
defines: 0EREPBVG2G
uses: [0P11X5HKAX]
sources:
  - url: https://en.wikipedia.org/wiki/Induced_subgraph
    locator: Definition
---

## Definition

Let $G = (V, E)$ be a [[graph|0JD5C82QMB]] and let $S \subseteq V$.
The subgraph induced by $S$ is the graph $G[S]$ with vertex set $S$ and edge set
$$\{ \{u, v\} \in E : u, v \in S \}.$$
A subgraph of this form is an induced subgraph.

## Remarks

An induced subgraph is a [[subgraph|0P11X5HKAX]] that keeps every edge of $G$ between its vertices.
In $K_4$, every subgraph induced by $3$ vertices is a triangle. A path on these $3$ vertices is a subgraph, but it is not induced.
A [[clique|0G52BPNPKG]] induces a complete graph, and an [[independent set|0KZJ82WEPP]] induces a graph with no edges.

## Explanations

### L1 human

Choose some vertices and keep all the edges between them.
The result is the induced subgraph on those vertices.
