---
tag: CD2XB4Y1SF
kind: concept
name: Treewidth
msc: [05C83, 05C75, 05C85]
sources:
  - url: https://en.wikipedia.org/wiki/Treewidth
same_as:
  wikidata: Q5067368
  wikipedia: Treewidth
---

## Summary

Treewidth is a number that measures how close a graph is to a [[tree|0MJ0JS72DZ]].
It is defined through tree decompositions, which arrange overlapping sets of vertices along a tree.
Forests have treewidth at most $1$, and the complete graph $K_n$ has treewidth $n - 1$.
Treewidth is central in the theory of [[graph minors|VYQ32ZBPEE]].
Many problems that are hard in general can be solved efficiently on graphs of bounded treewidth.

## Explanations

### L1 human

A tree is easy to handle because removing any vertex that is not a leaf splits it into separate pieces.
A graph of small treewidth has the same property in a fuzzy way.
It can be cut into pieces by removing small sets of vertices, again and again, in a tree-like pattern.
For example, a cycle is not a tree, but it has treewidth $2$, so it is almost as simple as a tree.
A large square grid has large treewidth, because no small set of vertices splits it into small pieces.
