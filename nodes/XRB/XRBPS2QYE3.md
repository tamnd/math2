---
tag: XRBPS2QYE3
kind: conjecture
name: Graph reconstruction conjecture
msc: [05C60]
uses: [0JD5C82QMB, 0V05FC4GKQ, 00CT0PTH74]
about: [00C0BR7D7H]
sources:
  - url: https://en.wikipedia.org/wiki/Reconstruction_conjecture
same_as:
  wikidata: Q7302789
  wikipedia: Reconstruction conjecture
history:
  posed_by: "Paul J. Kelly and Stanisław Ulam"
  first_stated: "1942"
---

## Statement

For a finite [[graph|0JD5C82QMB]] $G$ and a vertex $v$ of $G$, let $G - v$ be the [[induced subgraph|0V05FC4GKQ]] on the vertices other than $v$.
The deck of $G$ is the multiset of the [[isomorphism|00CT0PTH74]] classes of the graphs $G - v$, one for each vertex $v$.
Conjecture: if $G$ and $H$ are finite graphs with at least $3$ vertices and the same deck, then $G$ and $H$ are isomorphic.

## Remarks

The bound on the number of vertices is needed.
The graph with $2$ vertices and one edge and the graph with $2$ vertices and no edge have the same deck, made of two single vertices.
The conjecture is due to Kelly and Ulam, and it is open.
Many invariants can be read off the deck, for example the number of edges and the degree sequence.
Several classes of graphs are known to be reconstructible from their decks, among them regular graphs, disconnected graphs and trees.
Computer searches have confirmed the conjecture for all graphs with few vertices.

## Explanations

### L1 human

Take a graph and make one copy of it for each vertex, with that vertex and its edges erased.
Shuffle the copies and forget which vertex was erased in each.
The conjecture says that, as soon as there are at least three vertices, the shuffled pile of copies always determines the original graph.
