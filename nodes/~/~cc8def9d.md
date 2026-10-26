---
tag: ~cc8def9d
kind: definition
name: K-colourable graph
msc: [05C15]
defines: ~7ec8a7b4
uses: [~ed132083]
sources:
  - url: https://en.wikipedia.org/wiki/Graph_coloring
    locator: Vertex coloring
---

## Definition

Let $k$ be a natural number.
A [[graph|~3f82cef4]] $G$ is $k$-colourable if it has a [[colouring|~ed132083]] with the set of colours $\{1, 2, \dots, k\}$.

## Remarks

A $k$-colourable graph is also $(k+1)$-colourable.
A graph is $2$-colourable if and only if it is [[bipartite|~729625d7]].
The [[complete graph|~b29ee1b7]] $K_n$ is $k$-colourable if and only if $k \ge n$.

## Explanations

### L1 human

A graph is $k$-colourable when $k$ colours are enough to colour it properly.
A triangle needs three colours, so it is $3$-colourable but not $2$-colourable.
