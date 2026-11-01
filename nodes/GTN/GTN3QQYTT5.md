---
tag: GTN3QQYTT5
kind: concept
name: Line graph
msc: [05C76]
sources:
  - url: https://en.wikipedia.org/wiki/Line_graph
same_as:
  wikidata: Q1378376
  wikipedia: Line graph
---

## Summary

The line graph $L(G)$ of a [[graph|00C0BR7D7H]] $G$ has the edges of $G$ as its vertices.
Two of them are adjacent when they share an endpoint.
It turns questions about edges into questions about vertices.
For example, a matching of $G$ is an independent set of $L(G)$, and an edge colouring of $G$ is a vertex colouring of $L(G)$.
The node [[line graph|CJ57DT86S8]] gives the precise definition.

## Explanations

### L1 human

Draw a dot in the middle of each edge of a graph.
Join two of the new dots when their edges meet at a common vertex.
The new picture is the line graph.
For a star with three arms, the three arms all meet at the centre, so the line graph is a triangle.
