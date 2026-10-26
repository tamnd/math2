---
tag: 01R1HPEK6S
kind: statement
role: theorem
name: A graph is bipartite iff it has no odd cycle
msc: [05C75]
uses: [07CT9RDY7Q, 07DVHJ8N0A]
sources:
  - url: https://en.wikipedia.org/wiki/Bipartite_graph
    locator: Characterization
---

## Statement

Let $G$ be a [[graph|0JD5C82QMB]].
Then $G$ is [[bipartite|07DVHJ8N0A]] if and only if $G$ has no [[cycle|07CT9RDY7Q]] of odd length.

## Remarks

One direction is easy. A cycle in a bipartite graph alternates between the two parts, so its length is even.
For the converse, work in each component. Colour a vertex by the parity of its distance to a fixed vertex. An edge between two vertices of the same colour would give an odd closed walk, and then an odd cycle.
A graph is also bipartite if and only if its chromatic number is at most $2$.

## Explanations

### L1 human

Walking around a cycle in a bipartite graph, you switch sides at every step.
To come back to the start you need an even number of steps, so odd cycles are impossible.
