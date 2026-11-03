---
tag: E4Y32N7GRR
kind: concept
name: Centrality
msc: [91D30, 05C82]
sources:
  - url: https://en.wikipedia.org/wiki/Centrality
same_as:
  wikidata: Q5062194
  wikipedia: Centrality
---

## Summary

A centrality measure assigns to each vertex of a [[graph|00C0BR7D7H]] a number that says how important or central the vertex is in the network.
Different notions of importance give different measures.
Degree centrality counts direct links, and closeness centrality rewards short distances to all others.
Betweenness centrality rewards lying on many shortest paths, and eigenvector centrality rewards links to other important vertices.
Centrality is a basic tool of social network analysis and of network science in general.

## Explanations

### L1 human

In a group of friends, who is the most central person?
It could be the one with the most friends, the one who can reach everyone through few introductions, or the one through whom news must pass.
Each answer is a different centrality measure.
In a star, where one person knows everyone and nobody else knows each other, all these measures agree that the person in the middle is the most central.
