---
tag: 9HTB5KVS72
kind: definition
name: Locally finite poset
msc: [06A07, 06A11]
defines: TV1V4JDRDD
uses: [0QV2JS9RJ3, 070R982G4B]
sources:
  - url: https://en.wikipedia.org/wiki/Locally_finite_poset
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]].
For $x, y \in P$, the closed interval from $x$ to $y$ is $[x, y] = \set{z \in P : x \le z \le y}$.
The poset $P$ is *locally finite* when $[x, y]$ is a [[finite set|070R982G4B]] for all $x, y \in P$.

## Remarks

Example: $\N^k$ with the product order is locally finite.
Check: if $x \le y$, the interval $[x, y]$ is the box $\prod_{i=1}^k \set{x_i, \ldots, y_i}$, which has $\prod_i (y_i - x_i + 1)$ elements; if $x \not\le y$, it is empty.

Non-example: $\Q$ with the usual order is not locally finite, since $[0, 1]$ is infinite.

Every finite poset is locally finite.
The interval $[x, y]$ is empty unless $x \le y$, so only comparable pairs matter.
In Mathlib the class `LocallyFiniteOrder` provides the intervals as finite sets.
