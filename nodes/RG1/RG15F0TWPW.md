---
tag: RG15F0TWPW
kind: concept
name: Compact-open topology
msc: [54C35]
specializes: [0CQHFPGJ45]
sources:
  - url: https://en.wikipedia.org/wiki/Compact-open_topology
same_as:
  wikidata: Q1669863
  wikipedia: Compact-open topology
---

## Summary

The compact-open topology is a standard topology on the set $C(X, Y)$ of continuous maps between two topological spaces.
Its basic open sets ask that the maps send a given compact set into a given open set.
When $Y$ is a metric space, it is the topology of uniform convergence on compact sets.
It is the usual topology on mapping spaces in homotopy theory.

## Explanations

### L1 human

To say that two continuous maps are close, you can look at them on a compact piece of the source.
The compact-open topology says a map is near $f$ when it sends each chosen compact piece into an open target region that $f$ also sends it into.
For maps from $[0, 1]$ to $\R$, this is the same as being uniformly close on all of $[0, 1]$.
For maps from $\R$ to $\R$, it means being uniformly close on each bounded closed interval, but not necessarily on all of $\R$.
