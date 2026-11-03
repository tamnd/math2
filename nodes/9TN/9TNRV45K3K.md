---
tag: 9TNRV45K3K
kind: concept
name: UPGMA
msc: [92B10, 92D15, 62H30]
specializes: [D9Y3A9RH6J]
sources:
  - url: https://en.wikipedia.org/wiki/UPGMA
same_as:
  wikidata: Q1779497
  wikipedia: UPGMA
---

## Summary

UPGMA (unweighted pair group method with arithmetic mean) is an agglomerative clustering method that builds a rooted tree from a table of pairwise distances.
At each step it merges the two closest clusters and measures distances between clusters by the average distance between their members.
In phylogenetics it gives a rooted [[phylogenetic tree|RK58WSHJSG]] in which all leaves are at the same height.
It recovers the right tree when the distances form an [[ultrametric|A6DPR620B5]], that is, when evolution runs at a constant rate.

## Explanations

### L1 human

Imagine you know how different each pair of species is, and you want a family tree.
UPGMA first joins the two most similar species into one group.
Then it treats that group as a single new species whose distance to every other species is the average of its members' distances.
It repeats until everything is in one group.
For example, let $a$ and $b$ be at distance $2$, and let $c$ be at distance $6$ from $a$ and $8$ from $b$.
Then $a$ and $b$ join first, and the group $\set{a, b}$ is at distance $7$ from $c$.
