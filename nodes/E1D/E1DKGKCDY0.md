---
tag: E1DKGKCDY0
kind: definition
name: Neighbor joining
msc: [92B10, 92-08]
defines: M81NRAZVH0
uses: [5624H8KWKK, 5K1F0ZSN51]
sources:
  - url: https://en.wikipedia.org/wiki/Neighbor_joining
---

## Definition

Let $X$ be a set of $n \ge 3$ taxa and $d$ a symmetric matrix on $X$ with $d(i, i) = 0$ and $d(i, j) \ge 0$.
*Neighbor joining* is the [[algorithm|5K1F0ZSN51]] that builds an unrooted binary [[phylogenetic tree|5624H8KWKK]] on $X$ with edge lengths.
It repeats the following steps while the current set $X$ has $r \ge 3$ elements.

1. For $i \ne j$ in $X$ compute $Q(i, j) = (r - 2) d(i, j) - \sum_{k \in X} d(i, k) - \sum_{k \in X} d(j, k)$.
2. Choose a pair $\set{i, j}$ with $Q(i, j)$ minimal, and create a new node $u$ adjacent to $i$ and $j$.
3. Give the new edges the lengths $d(i, u) = \frac12 d(i, j) + \frac{1}{2(r - 2)} \Big( \sum_{k} d(i, k) - \sum_{k} d(j, k) \Big)$ and $d(j, u) = d(i, j) - d(i, u)$.
4. For each $k \ne i, j$ put $d(u, k) = \frac12 \big( d(i, k) + d(j, k) - d(i, j) \big)$, then replace $i$ and $j$ by $u$ in $X$.

When $r = 2$, join the last two nodes by an edge of length equal to their distance.

## Remarks

Example: let $d$ come from the tree $ab|cd$ with all five edges of length $1$, so $d(a, b) = d(c, d) = 2$ and the other distances are $3$.
Every row sum is $8$, so $Q(a, b) = Q(c, d) = 2 \cdot 2 - 16 = -12$ while $Q(a, c) = 2 \cdot 3 - 16 = -10$; the algorithm joins $a$ and $b$ with $d(a, u) = d(b, u) = 1$, as in the true tree.
Non-example: the rule "join the pair with the smallest $d(i, j)$" is not neighbor joining, since it skips the correction in clause 1.
This rule can fail when edge lengths are very unequal.
If $d$ is a tree metric, that is, it satisfies the four-point condition, neighbor joining returns the tree that realises it.
The algorithm takes $O(n^3)$ time; UPGMA is a simpler method that assumes a molecular clock.
