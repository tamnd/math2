---
tag: NJY30DQG3H
kind: definition
name: Ordinal sum of posets
msc: [06A06]
defines: 6AJ7QQCTQQ
uses: [0QV2JS9RJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Partially_ordered_set
---

## Definition

Let $(P, \le_P)$ and $(Q, \le_Q)$ be [[partially ordered sets|0QV2JS9RJ3]] with $P \cap Q = \varnothing$.
The *ordinal sum* $P \oplus Q$ is the set $P \cup Q$ with the relation $\le$ given by $x \le y$ if and only if one of the following holds:

1. $x, y \in P$ and $x \le_P y$;
2. $x, y \in Q$ and $x \le_Q y$;
3. $x \in P$ and $y \in Q$.

## Remarks

If $P$ and $Q$ are not disjoint, first replace them by disjoint copies.
Example: with $P = \set{a}$ and $Q = \set{b, c}$ an antichain, $P \oplus Q$ has $a < b$ and $a < c$ by clause 3, and $b$, $c$ stay incomparable.
Non-example: in $Q \oplus P$ the element $a$ is above $b$ and $c$, so $Q \oplus P$ differs from $P \oplus Q$; the ordinal sum is not commutative.
The ordinal sum is associative, and the ordinal sum of two total orders is a total order.
For well-orders, it gives the sum of [[ordinal numbers|0YSCSX5YZC]], so $\omega \oplus \set{x}$ has order type $\omega + 1$.
