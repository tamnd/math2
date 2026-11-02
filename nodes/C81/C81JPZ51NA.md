---
tag: C81JPZ51NA
kind: concept
name: Laman graph
msc: [52C25, 05C10]
specializes: [00C0BR7D7H]
sources:
  - url: https://en.wikipedia.org/wiki/Laman_graph
same_as:
  wikidata: Q4253458
  wikipedia: Laman graph
---

## Summary

A Laman graph is a [[graph|00C0BR7D7H]] with $2n - 3$ edges on $n$ vertices in which no set of $k \ge 2$ vertices spans more than $2k - 3$ edges.
These are exactly the graphs that are minimally rigid in the plane for generic positions of the vertices.
So they reduce a question of [[rigidity of frameworks|V5YS9BZX0N]] in the plane to a count of edges, which can be checked by efficient algorithms.

## Explanations

### L1 human

A point in the plane has two degrees of freedom, and a rigid shape in the plane can still slide and turn in three ways.
So $n$ points need $2n - 3$ bars to be held rigid, and no part may waste bars on a piece that is already rigid.
A triangle has $3$ vertices and $3 = 2 \cdot 3 - 3$ edges, and it is a Laman graph.
The complete graph on $4$ vertices has $6 > 5$ edges, so it has one bar too many.
