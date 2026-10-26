---
tag: 0BN2A6EBYA
kind: statement
role: proposition
name: Trees are bipartite
msc: [05C05]
uses: [0MJ0JS72DZ, 07DVHJ8N0A]
sources:
  - url: https://en.wikipedia.org/wiki/Bipartite_graph
    locator: Examples
---

## Statement

Let $T$ be a [[tree|0MJ0JS72DZ]].
Then $T$ is [[bipartite|07DVHJ8N0A]].

## Remarks

Proof: fix a vertex $r$. Put a vertex in $A$ if its [[distance|0WPZ5YPAGR]] to $r$ is even, and in $B$ if it is odd. The ends of an edge have distances that differ by $1$.
It also follows from the theorem that [[a graph is bipartite iff it has no odd cycle|01R1HPEK6S]], because a tree has no cycle at all.

## Explanations

### L1 human

Colour the vertices of a tree by levels, from a chosen root: even levels white, odd levels black.
Each edge goes between neighbouring levels, so it joins a white vertex and a black vertex.
