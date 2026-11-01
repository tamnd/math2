---
tag: HV2QBDHTDD
kind: concept
name: Schreier coset graph
msc: ["20F65", "05C25"]
specializes: [0KFYGSHHF5]
sources:
  - url: https://en.wikipedia.org/wiki/Schreier_coset_graph
same_as:
  wikidata: Q7432869
  wikipedia: Schreier coset graph
---

## Summary

Let $G$ be a [[group|G5S1M9]], $H$ a [[subgroup|0X1JXT47GA]] and $S$ a set of elements of $G$.
The Schreier coset graph is a [[directed graph|0KFYGSHHF5]] whose vertices are the [[right cosets|0NE1DK7H4T]] of $H$, with an edge labelled $s$ from $Hg$ to $Hgs$.
For $H = \set{1}$ it is the [[Cayley graph|0GYQK9NDJF]] of $G$ with respect to $S$.
It shows how the generators permute the cosets of $H$.
It is used in coset enumeration and to find generators of subgroups, as in the Reidemeister–Schreier method.

## Explanations

### L1 human

Group the elements of $G$ into the right cosets of $H$, and draw one dot for each coset.
Each generator $s$ moves a coset $Hg$ to the coset $Hgs$; draw an arrow for this move.
For example, in $\Z$ with $H = 3\Z$ and the generator $1$, there are three dots $3\Z$, $1 + 3\Z$ and $2 + 3\Z$, and the arrows form a triangle.
Paths in the graph that start and end at the dot $H$ spell words that represent elements of $H$.
