---
tag: PMGTV643X1
kind: statement
role: theorem
name: Petersen's theorem
msc: [05C70]
uses: [0JD5C82QMB, 0KA4S8R39M, 0D81KWH9ZM, 05ZPH8KF9K, 08J7R35B6Q]
about: [05ZPH8KF9K]
sources:
  - url: https://en.wikipedia.org/wiki/Petersen's_theorem
same_as:
  wikidata: Q7178199
  wikipedia: Petersen's theorem
---

## Statement

Let $G$ be a finite [[graph|0JD5C82QMB]] that is cubic, that is, [[$3$-regular|0KA4S8R39M]], and that has no [[bridge|0D81KWH9ZM]].
Then $G$ has a [[perfect matching|05ZPH8KF9K]].

## Remarks

The proof uses [[Tutte's theorem|08J7R35B6Q]].
It is enough to show that, for each set $S$ of vertices, the graph $G - S$ has at most $\abs{S}$ components with an odd number of vertices.
If $C$ is such an odd component, the degrees in $C$ add up to $3\abs{C}$, which is odd, so an odd number of edges joins $C$ to $S$.
This number is not $1$, since $G$ has no bridge, so it is at least $3$.
Since at most $3\abs{S}$ edges end in $S$, there are at most $\abs{S}$ odd components.
For example, the [[Petersen graph|0NR95CTFCZ]] is cubic and bridgeless, and its five spokes form a perfect matching.
The hypothesis on bridges is needed: there are cubic graphs with bridges that have no perfect matching.
The theorem also holds for cubic multigraphs without bridges, with the same proof.

## Explanations

### L1 human

In a cubic graph each vertex has exactly three edges.
If no single edge disconnects the graph, then the vertices can be paired off along edges, with every vertex in exactly one pair.
This is one of the oldest results of graph theory.

### L2 human

Petersen's theorem is a standard application of Tutte's theorem, by a counting argument on edges leaving odd components.
Removing a perfect matching from a bridgeless cubic graph leaves a $2$-factor, a disjoint union of cycles.
This is a starting point for edge colouring of cubic graphs.
A cubic graph has chromatic index $3$ exactly when it has a perfect matching whose complement consists of even cycles.
