---
tag: 4AVF0RN7HV
kind: concept
name: Graph enumeration
msc: [05C30, 05A16]
sources:
  - url: https://en.wikipedia.org/wiki/Graph_enumeration
same_as:
  wikidata: Q5597086
  wikipedia: Graph enumeration
---

## Summary

Graph enumeration is the part of combinatorics that counts [[graphs|00C0BR7D7H]] with a given property, either as labelled graphs or up to [[isomorphism|0F7QKGJS6B]].
There are $2^{\binom{n}{2}}$ labelled graphs on $n$ given vertices, and [[Cayley's formula|0M2SSGSYPE]] counts the labelled trees.
Unlabelled counts are harder, and tools such as the [[Pólya enumeration theorem|MPYQ39P01F]] and generating functions are used for them.
It is a central part of [[enumerative combinatorics|EX382NQTGP]].

## Explanations

### L1 human

Graph enumeration asks "how many graphs of this kind are there?".
There are two ways to count.
In labelled counting the vertices have names, so two drawings with different names count as different graphs.
In unlabelled counting only the shape matters.
For three vertices there are $8$ labelled graphs but only $4$ shapes: no edge, one edge, a path with two edges, and a triangle.
