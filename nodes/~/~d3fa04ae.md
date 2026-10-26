---
tag: ~d3fa04ae
kind: definition
name: Minimum spanning tree
msc: [05C05]
defines: ~b1fab929
uses: [~3859990e]
sources:
  - url: https://en.wikipedia.org/wiki/Minimum_spanning_tree
    locator: lead section
---

## Definition

Let $G$ be a finite [[connected|~c1305259]] [[graph|~3f82cef4]] with edge set $E$, and let $w : E \to \mathbb{R}$ be a weight function.
The weight of a subgraph is the sum of the weights of its edges.
A minimum spanning tree of $(G, w)$ is a [[spanning tree|~3859990e]] of $G$ whose weight is the smallest among all spanning trees of $G$.

## Remarks

A minimum spanning tree exists, because a finite graph has finitely many spanning trees. It is unique when all weights are distinct.
Kruskal's algorithm and Prim's algorithm find a minimum spanning tree with greedy choices.

## Explanations

### L1 human

Suppose that each road between towns has a cost to build.
A minimum spanning tree is the cheapest set of roads that links all towns.
