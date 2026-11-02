---
tag: 2YHG0X6EA0
kind: definition
name: Disjoint union of posets
msc: [06A06]
defines: TZWMEM7GKA
uses: [0QV2JS9RJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Disjoint_union
---

## Definition

Let $(P, \le_P)$ and $(Q, \le_Q)$ be [[partially ordered sets|0QV2JS9RJ3]] with $P \cap Q = \varnothing$.
The *disjoint union* $P + Q$ is the set $P \cup Q$ with the following relation $\le$.
For $x, y \in P \cup Q$, $x \le y$ holds if and only if either $x, y \in P$ and $x \le_P y$, or $x, y \in Q$ and $x \le_Q y$.

## Remarks

If $P$ and $Q$ are not disjoint, first replace them by disjoint copies, such as $P \times \set{0}$ and $Q \times \set{1}$.
The same construction works for any family of pairwise disjoint posets.
Example: if $P$ is the chain $a < b$ and $Q$ is the chain $c < d$, then $P + Q$ is the poset $\mathbf{2} + \mathbf{2}$ with exactly the strict relations $a < b$ and $c < d$.
Non-example: the poset with $a < b$, $c < d$ and also $a < d$ is not $P + Q$, since it relates an element of $P$ to an element of $Q$.
An antichain with $n$ elements is the disjoint union of $n$ one-element posets.
The width of $P + Q$ is the sum of the widths, and its height is the larger of the two heights.
