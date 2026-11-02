---
tag: HD8CK28AJC
kind: definition
name: Algebraic lattice
msc: [06B23, 08A30]
defines: 3J0BTXSCVN
uses: [D7A0ZGZT5S, 9F7TYES4KE, 0R3H5PANRQ]
sources:
  - url: https://en.wikipedia.org/wiki/Compact_element
---

## Definition

Let $L$ be a [[complete lattice|D7A0ZGZT5S]].
It is an *algebraic lattice*, or compactly generated, if every $x \in L$ is the [[supremum|0R3H5PANRQ]] of the set $\set{c \in L : c \le x,\ c \text{ compact}}$ of [[compact elements|9F7TYES4KE]] below it.

## Remarks

Example: the lattice of subgroups of a group $G$, whose compact elements are the finitely generated subgroups.
Each subgroup $H$ is the join of the cyclic subgroups $\langle h \rangle$ for $h \in H$.
Non-example: the closed subsets of $[0, 1]$, ordered by inclusion, form a complete lattice in which the join of a family is the closure of its union.
A nonempty closed set $F$ is not compact: pick $p \in F$; the closed sets $C_n = [0, 1] \setminus (p - 1/n, p + 1/n)$ form a directed family whose join is $[0, 1] \supseteq F$, yet $p \notin C_n$ for every $n$.
So the only compact element is $\varnothing$, and no nonempty closed set is a join of compact elements.
Every algebraic lattice is a continuous lattice.
Some authors do not require completeness and speak of algebraic posets or algebraic dcpos instead.
