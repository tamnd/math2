---
tag: SC5QB5F4TE
kind: concept
name: Extremal graph theory
msc: [05C35]
sources:
  - url: https://en.wikipedia.org/wiki/Extremal_graph_theory
same_as:
  wikidata: Q739245
  wikipedia: Extremal graph theory
---

## Summary

Extremal graph theory studies how large or small a [[graph|00C0BR7D7H]] can be when it must have, or must avoid, a given structure.
Its basic quantity is the extremal number $\mathrm{ex}(n, H)$, the largest number of edges of a graph on $n$ vertices with no [[subgraph|0WBFFC8XZ9]] isomorphic to $H$.
[[Turán's theorem|0JG1KZSPFZ]] computes it for complete graphs, and the [[Erdős–Stone theorem|XZF9BFJFXB]] gives it asymptotically for every non-bipartite $H$.
For bipartite $H$ the question leads to the [[Zarankiewicz problem|KT9WJFRQ3F]], which is still largely open.

## Explanations

### L1 human

Extremal graph theory asks questions of the form "how many edges can you draw before a certain pattern is forced to appear?".
For example, a graph on $n$ vertices without a triangle has at most $n^2/4$ edges.
The best graph puts the vertices in two equal groups and joins every vertex of one group to every vertex of the other.
Results of this kind show that density alone forces structure.
