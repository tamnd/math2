---
tag: NEMG5CNN3J
kind: proof
name: Proof of the recurrence for Bell numbers by the block of the last element
msc: [11B73]
proves: 0110GBHPPB
uses: [0WW85SQVS3, 09CCE86A6D, 0BFMR2FQ8B, 0EE2V3CHFK, 0GV2573FP4]
sources:
  - url: https://en.wikipedia.org/wiki/Bell_number
    locator: Summation formulas
---

## Proof

We sort the partitions by the elements outside the block of the last element.

1. Let $n$ be a natural number. Let $X = \set{1, \dots, n + 1}$, let $z = n + 1$, and let $Y = \set{1, \dots, n}$.
2. By the definition of the [[Bell numbers|0WW85SQVS3]], $B_m$ is the number of [[partitions|09CCE86A6D]] of an $m$-element set. So $B_{n+1}$ counts the partitions of $X$.
3. Let $P$ be a partition of $X$, and let $B$ be its block that contains $z$. Let $K = X \setminus B$. Then $K \subseteq Y$.
4. The other blocks $P \setminus \set{B}$ are nonempty, pairwise disjoint, and their union is $K$. So they form a partition of $K$.
5. Map $P$ to the pair $(K, P \setminus \set{B})$.
6. Conversely, let $K \subseteq Y$ and let $Q$ be a partition of $K$. The set $X \setminus K$ contains $z$, so it is nonempty. Then $Q \cup \set{X \setminus K}$ is a partition of $X$.
7. These two maps are inverse to each other. So the partitions of $X$ are in bijection with the pairs $(K, Q)$, where $K \subseteq Y$ and $Q$ is a partition of $K$.
8. For a fixed $K$ with $k$ elements, there are $B_k$ choices of $Q$.
9. By the [[number of $k$-element subsets|0BFMR2FQ8B]], $Y$ has $\binom{n}{k}$ subsets $K$ with $k$ elements, for $0 \le k \le n$.
10. By the [[rule of sum|0EE2V3CHFK]], grouping the pairs by $k = |K|$, and by the [[bijection principle|0GV2573FP4]],
$$B_{n+1} = \sum_{k=0}^{n} \binom{n}{k} B_k.$$

## Idea

In a partition of $\set{1, \dots, n + 1}$, the block of the last element leaves out some set $K$ of the first $n$ elements. Choose $K$ with $k$ elements in $\binom{n}{k}$ ways, then partition $K$ freely in $B_k$ ways.
