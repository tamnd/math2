---
tag: 7NT7MRVZSQ
kind: concept
name: Network simplex algorithm
msc: [90C35, 90C49, 90C05]
specializes: [MH272QHWPM]
sources:
  - url: https://en.wikipedia.org/wiki/Network_simplex_algorithm
same_as:
  wikidata: Q1978970
  wikipedia: Network simplex algorithm
---

## Summary

The network simplex algorithm solves the [[minimum-cost flow problem|899795HN7H]].
It is the [[simplex algorithm|MH272QHWPM]] written in the language of graphs.
A basis is a [[spanning tree|0S4ZEZM7KE]] of the network.
A pivot sends flow around the one cycle that a new edge closes with the tree.
All its steps are simple graph operations, so it is very fast in practice.

## Explanations

### L1 human

In a network flow problem the basic solutions of the linear program correspond to spanning trees.
Edges outside the tree are either empty or full, and the flow on tree edges is then forced by the supplies.
Prices on the vertices tell whether adding an outside edge would lower the cost.
If it would, flow is pushed around the cycle that this edge forms with the tree until some edge becomes empty or full and leaves the tree.
For example, in a triangle with a cheap long way and an expensive short way, one pivot moves the flow to the cheaper route.
