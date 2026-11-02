---
tag: APD4NYG9TG
kind: definition
name: Order dimension
msc: [06A07]
defines: JC4J24MF93
uses: [0QV2JS9RJ3, W8DZ5KGGHN, T9CJHV6JW3]
sources:
  - url: https://en.wikipedia.org/wiki/Order_dimension
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]].
A *realizer* of $P$ is a set $\mathcal{R}$ of [[linear extensions|W8DZ5KGGHN]] of $\le$ with the following property.
For all $x, y \in P$, $x \le y$ holds if and only if $x \preceq y$ for every $\preceq$ in $\mathcal{R}$.
The *order dimension* $\dim P$ is the least cardinality of a realizer of $P$.

## Remarks

The set of all linear extensions is a realizer, by the [[Szpilrajn extension theorem|T9CJHV6JW3]], so the dimension is defined.
Example: an antichain $\set{a, b, c}$ has dimension $2$.
The orders $a \prec b \prec c$ and $c \prec b \prec a$ form a realizer, since each pair of distinct elements appears in both directions, and one linear order alone would make two elements comparable.
Non-example of a realizer: for the same antichain, the set $\set{a \prec b \prec c,\ b \prec a \prec c}$ is not a realizer, since $a$ precedes $c$ in both orders but $a \not\le c$.
A poset has dimension $1$ exactly when it is a total order.
Equivalently, $\dim P$ is the least $d$ such that $P$ embeds in a product of $d$ chains.
