---
tag: 5FPWTYFJRA
kind: concept
name: Kruskal's algorithm
msc: [05C85, 05C05, 90C27]
specializes: [PSM6NKYJB8]
sources:
  - url: https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
same_as:
  wikidata: Q797860
  wikipedia: Kruskal's algorithm
---

## Summary

Kruskal's algorithm finds a [[minimum spanning tree|0JW7KT6PQW]] of a connected graph with weighted edges.
It is a [[greedy algorithm|PSM6NKYJB8]] that scans the edges from lightest to heaviest.
It keeps an edge whenever the edge does not close a cycle with the edges already kept.
With a disjoint-set structure to detect cycles, it runs in time $O(m \log m)$ on a graph with $m$ edges.

## Explanations

### L1 human

Think of towns to be joined by roads, where each possible road has a building cost.
Sort the roads from cheapest to most expensive.
Build each road in turn, unless its two towns are already joined by roads built before; then skip it.
For a triangle with costs $1$, $2$ and $3$, the algorithm builds the roads of cost $1$ and $2$ and skips the road of cost $3$.
The result joins all towns at the least total cost.
