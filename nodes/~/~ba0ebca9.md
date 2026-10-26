---
tag: ~ba0ebca9
kind: definition
name: Edge set
msc: [05C99]
defines: ~068ae4cf
uses: [~3f82cef4]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_graph_theory
    locator: E
---

## Definition

Let $G$ be a [[graph|~3f82cef4]] with vertex set $V$ and adjacency relation $\sim$.
The edge set of $G$ is the set
$$E(G) = \{ \{u, v\} : u, v \in V,\ u \sim v \}$$
of unordered pairs of adjacent vertices.

## Remarks

Each edge is a $2$-element subset of $V$, because $\sim$ is irreflexive.
The number of edges $|E(G)|$ is the size of $G$, and the number of vertices $|V|$ is its order.
The [[handshaking lemma|~32eb3419]] relates $|E(G)|$ to the degrees of the vertices.

## Explanations

### L1 human

The edge set is the list of all lines of the graph, with each line given by its two end points.
A triangle on the vertices $a, b, c$ has the edge set $\{\{a, b\}, \{b, c\}, \{a, c\}\}$.
