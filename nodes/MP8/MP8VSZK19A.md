---
tag: MP8VSZK19A
kind: concept
name: Percolation threshold
msc: [60K35, 82B43, 82B26]
sources:
  - url: https://en.wikipedia.org/wiki/Percolation_threshold
same_as:
  wikidata: Q7167170
  wikipedia: Percolation threshold
---

## Summary

The percolation threshold of a graph, also called its critical probability, is a value $p_c$ of the parameter $p$ of [[percolation|BH7YPXCYDK]].
At $p_c$ an infinite open cluster starts to appear.
Below $p_c$ all open clusters are finite almost surely, and above $p_c$ there is an infinite open cluster almost surely.
It depends on the graph and on the choice of bond or site percolation.
Exact values are known only for a few graphs, such as $p_c = 1/2$ for bond percolation on the square lattice.

## Explanations

### L1 human

Open each edge of a large network with probability $p$.
For small $p$ the open pieces are small islands; for large $p$ they join into one huge network.
The threshold is the value of $p$ at which this switch happens.
On a tree in which every vertex has $3$ neighbours, the threshold is $1/2$.
Each step away from the root offers $2$ new edges, so the cluster can grow forever only if $2p$, the mean number of new open edges, exceeds $1$.
