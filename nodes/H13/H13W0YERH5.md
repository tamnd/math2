---
tag: H13W0YERH5
kind: definition
name: Width of a poset
msc: [06A07]
defines: RA5SQ908G1
uses: [0QV2JS9RJ3, 03HF498P1J]
sources:
  - url: https://en.wikipedia.org/wiki/Dilworth's_theorem
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]].
The *width* of $P$ is the supremum of the cardinalities $\abs{A}$ of the [[antichains|03HF498P1J]] $A \subseteq P$.

## Remarks

Example: the set $\set{1, \ldots, 10}$ ordered by divisibility has width $5$.
The set $\set{6, 7, 8, 9, 10}$ is an antichain, and the five chains $\set{1, 2, 4, 8}$, $\set{3, 6}$, $\set{5, 10}$, $\set{7}$, $\set{9}$ cover the set, so no antichain has more than $5$ elements.
Non-example: the set $\set{2, 3, 4}$ has $3$ elements but is not an antichain there, since $2 \mid 4$, so it does not show that the width is at least $3$.
A nonempty poset has width $1$ exactly when it is a total order.
The width of an infinite poset can be infinite even when each antichain is finite.
[[Dilworth's theorem|GT224XDA4E]] says that a finite poset of width $w$ is a union of $w$ chains and of no fewer.
