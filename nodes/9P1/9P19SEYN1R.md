---
tag: 9P19SEYN1R
kind: concept
name: Ford–Fulkerson algorithm
msc: [05C21, 90C35, 05C85]
sources:
  - url: https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
same_as:
  wikidata: Q284695
  wikipedia: Ford–Fulkerson algorithm
---

## Summary

The Ford–Fulkerson algorithm computes a maximum flow from a source to a sink in a flow network.
It starts from the zero flow and repeatedly pushes extra flow along an augmenting path.
This is a path from source to sink in the residual network that still has spare capacity.
When no augmenting path is left, the flow is maximum, and this argument also proves the [[max-flow min-cut theorem|4HMR4KQ01T]].
With integer capacities it terminates and produces an integer maximum flow.

## Explanations

### L1 human

Picture water pipes from a source to a sink, each pipe with a maximum rate.
Find any route from source to sink where every pipe can carry more, and send as much extra water along it as the tightest pipe allows.
The residual network also lets the algorithm send water "backwards" through a pipe, which undoes an earlier poor choice.
For two parallel pipes of capacities $2$ and $3$ from source to sink, two augmentations give the maximum flow $5$.
When no route with spare room remains, no more water can get through.
