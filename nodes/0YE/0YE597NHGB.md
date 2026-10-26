---
tag: 0YE597NHGB
kind: definition
name: Cayley graph
aliases: [cayley-diagram]
msc: [05C25, 20F65]
defines: 0GYQK9NDJF
uses: [0RG9SPQSWM, 0YSE802YCQ]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley_graph
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Cayley_graph
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Cayley_graph
    locator: Elementary properties
  - url: https://en.wikipedia.org/wiki/Cayley_graph
    locator: History
---

## Definition

Let $G$ be a [[group|G5S1M9]] and let $S$ be a [[generating set|0MBV2VHMXA]] of $G$.
The Cayley graph $\Gamma(G, S)$ is the directed graph with vertex set $G$.
For each $g \in G$ and $s \in S$, it has an edge with colour $s$ from $g$ to $g s$.

## Remarks

For $G = \mathbb{Z}$ and $S = \{1, -1\}$, the Cayley graph is an infinite path. For $\mathbb{Z}/n\mathbb{Z}$ with a generator and its inverse, it is the cycle $C_n$.
The Cayley graph of a free group with respect to a basis is a tree.
The [[left multiplication action|0K5TWJAGPD]] of $G$ on itself acts on $\Gamma(G, S)$, so each Cayley graph is vertex-transitive.
Arthur Cayley first considered these graphs for finite groups in 1878.

## Explanations

### L1 human

A Cayley graph draws a group as a network.
Each element is a point, and each generator gives an arrow from $g$ to $g s$.
Paths in the graph correspond to words in the generators.
