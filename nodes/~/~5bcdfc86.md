---
tag: ~5bcdfc86
kind: statement
role: theorem
name: A tree on n vertices has n − 1 edges
msc: [05C05]
uses: [~ba0ebca9, ~29e53124]
sources:
  - url: https://en.wikipedia.org/wiki/Tree_(graph_theory)
    locator: Properties
---

## Statement

Let $T$ be a finite [[tree|~29e53124]] with $n$ vertices.
Then $T$ has exactly $n - 1$ edges.

## Remarks

A tree has at least one vertex, because it is connected. Thus $n \ge 1$.
Proof by induction on $n$: for $n \ge 2$ delete a leaf, which exists by the [[leaf lemma|~e506686f]]. The rest is a tree with $n - 1$ vertices.
A consequence: the sum of the degrees in a tree is $2n - 2$.

## Explanations

### L1 human

Build a tree by adding one vertex at a time, each joined to the tree by one new edge.
You start with $1$ vertex and $0$ edges, so at the end there is always one edge fewer than vertices.
