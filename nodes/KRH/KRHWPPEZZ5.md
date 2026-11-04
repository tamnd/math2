---
tag: KRHWPPEZZ5
kind: proof
name: Proof that trees are bipartite
msc: [05C05]
proves: 0BN2A6EBYA
uses: [0MJ0JS72DZ, 0XNN9Z8E5A, 07DVHJ8N0A, 01R1HPEK6S]
sources:
  - url: https://en.wikipedia.org/wiki/Bipartite_graph
    locator: Examples
---

## Proof

1. A [[tree|0MJ0JS72DZ]] $T$ is [[acyclic|0XNN9Z8E5A]], so it has no cycle at all.
2. In particular, $T$ has no cycle of odd length.
3. By the theorem that [[a graph is bipartite iff it has no odd cycle|01R1HPEK6S]], $T$ is [[bipartite|07DVHJ8N0A]].

## Idea

The only obstruction to splitting the vertices into two sides is an odd cycle. A tree has no cycles, so nothing can go wrong. Concretely, colour each vertex by the parity of its distance to a fixed root.
