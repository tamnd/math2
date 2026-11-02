---
tag: 8EPC35FTMX
kind: definition
name: Order complex
msc: [06A07, "05E45", 55U10]
defines: J32951135H
uses: [0QV2JS9RJ3, 0S8FE7ZMFM, V8GZ0W1ZZ5]
sources:
  - url: https://en.wikipedia.org/wiki/Poset_topology
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]].
The *order complex* $\Delta(P)$ of $P$ is the abstract [[simplicial complex|V8GZ0W1ZZ5]] with vertex set $P$ whose faces are the finite [[chains|0S8FE7ZMFM]] of $P$.
So the faces are the finite subsets $\set{x_0, x_1, \ldots, x_k} \subseteq P$ with $x_0 < x_1 < \cdots < x_k$.

## Remarks

$\Delta(P)$ is a simplicial complex because every subset of a chain is a chain.
A chain with $k + 1$ elements is a face of dimension $k$, so the dimension of $\Delta(P)$ is the length of the longest chain of $P$, when it is finite.
Topological properties of $P$, such as its homotopy type or homology, mean those of the geometric realization of $\Delta(P)$.
Example: let $P = \set{a, b, c, d}$ with $a < c$, $a < d$, $b < c$, $b < d$ and no other strict relations.
Its nonempty chains are the four points and the four pairs $\set{a, c}$, $\set{a, d}$, $\set{b, c}$, $\set{b, d}$.
So $\Delta(P)$ is a cycle of four edges, and its realization is a circle.
Non-example: for this $P$, the family of all subsets of $P$ is a simplicial complex on the vertex set $P$.
It is not $\Delta(P)$, since it contains $\set{a, b}$, which is not a chain.
The order complex of a chain with $n + 1$ elements is a full $n$-simplex.
