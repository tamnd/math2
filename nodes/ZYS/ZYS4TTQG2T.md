---
tag: ZYS4TTQG2T
kind: definition
name: Height of a poset
msc: [06A07]
defines: MPR6MH4YSQ
uses: [0QV2JS9RJ3, 0S8FE7ZMFM]
sources:
  - url: https://en.wikipedia.org/wiki/Graded_poset
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]].
The *height* of $P$ is the supremum of the cardinalities $\abs{C}$ of the [[chains|0S8FE7ZMFM]] $C \subseteq P$.

## Remarks

Example: the subsets of $\set{1, 2, 3}$ ordered by inclusion have height $4$, as shown by the chain $\varnothing \subset \set{1} \subset \set{1, 2} \subset \set{1, 2, 3}$.
A chain of subsets has at most one subset of each size, so no chain is longer.
Non-example: the set $\set{\varnothing, \set{1}, \set{2}, \set{1, 2}}$ has $4$ elements but is not a chain, since $\set{1}$ and $\set{2}$ are incomparable.
Conventions differ: some authors call the height the largest *length* of a chain $x_0 < x_1 < \cdots < x_n$, which is $n$, one less than the number of elements.
In that second convention the height is the Krull dimension of the poset.
The height of an element $x$ is often defined as the height of the down-set $\set{y \in P : y \le x}$, with the same choice of convention.
