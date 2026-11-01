---
tag: GT224XDA4E
kind: statement
role: theorem
name: Dilworth's theorem
msc: [06A07, 05D99]
uses: [0QV2JS9RJ3, 0S8FE7ZMFM, 03HF498P1J, 0JP0ZF57PN]
about: [0S8FE7ZMFM, 03HF498P1J]
sources:
  - url: https://en.wikipedia.org/wiki/Dilworth%27s_theorem
same_as:
  wikidata: Q1134776
  wikipedia: Dilworth's theorem
---

## Statement

Let $(P, \le)$ be a finite [[partially ordered set|0QV2JS9RJ3]].
Let $w$ be the largest size of an [[antichain|03HF498P1J]] in $P$.
Then $P$ is the union of $w$ pairwise disjoint [[chains|0S8FE7ZMFM]], and $P$ is not the union of fewer than $w$ chains.

## Remarks

The easy half: a chain meets an antichain in at most one element, so any cover of $P$ by chains uses at least $w$ chains.
The hard half can be proved by induction on $\abs{P}$, by removing a maximal chain or by splitting $P$ along a maximum antichain.
Another proof builds a bipartite graph with two copies of $P$ and an edge from $x$ to $y$ when $x < y$; then [[Kőnig's theorem|0JP0ZF57PN]] on matchings gives the chain partition.
Example: in the set $\set{1, 2, \ldots, 10}$ ordered by divisibility, the set $\set{6, 7, 8, 9, 10}$ is an antichain of size $5$, and $\set{1, 2, 4, 8}$, $\set{3, 6}$, $\set{5, 10}$, $\set{7}$, $\set{9}$ are $5$ chains that cover it.
The number $w$ is called the width of $P$.
The theorem also holds for an infinite partially ordered set of finite width $w$.
The dual result, Mirsky's theorem, says that the largest size of a chain equals the least number of antichains that cover $P$.

## Explanations

### L1 human

In a partial order, some pairs of elements are comparable and others are not.
A chain is a set of elements that can all be lined up, and an antichain is a set of elements no two of which are comparable.
Dilworth's theorem says that the least number of chains needed to cover everything equals the largest number of pairwise incomparable elements.
So a big antichain is the only obstacle to covering with few chains.

### L2 human

Dilworth's theorem is one of the min-max theorems of combinatorics, like Kőnig's theorem and Menger's theorem, and each of these can be derived from the others.
It gives a quick proof of the [[Erdős–Szekeres theorem|0SNJM8HSD3]]: a sequence of $rs + 1$ distinct real numbers has an increasing subsequence of length $r + 1$ or a decreasing subsequence of length $s + 1$.
In algorithms, a minimum chain partition of a finite poset can be computed through a maximum matching in a bipartite graph.
