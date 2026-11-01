---
tag: MBASZABTJ1
kind: concept
name: Hamiltonian path
msc: [05C45]
specializes: [03NAMV1DHJ]
sources:
  - url: https://en.wikipedia.org/wiki/Hamiltonian_path
same_as:
  wikidata: Q273037
  wikipedia: Hamiltonian path
---

## Summary

A Hamiltonian path in a graph is a [[path|03NAMV1DHJ]] that visits every vertex exactly once.
It is the open form of a [[Hamiltonian cycle|0HF30P75G4]].
Deciding whether a graph has a Hamiltonian path is NP-complete, and no simple criterion like Euler's parity test for [[Eulerian trails|05NWGBHKSZ]] is known.
The node [[Hamiltonian path|AT8GWPWQWT]] gives the precise definition.

## Explanations

### L1 human

A Hamiltonian path is a tour that visits every city exactly once, without needing to come back home.
On a chessboard, a knight's tour that visits every square once is a Hamiltonian path in the knight's move graph.
The path graph $1 - 2 - 3 - 4$ is itself a Hamiltonian path, while a star with three arms has none.
