---
tag: BZ5GXNN7HC
kind: definition
name: Sperner property
msc: [06A07, 05D05]
defines: F02PJ2ZK9X
uses: [1C7TKGTB2F, 03HF498P1J, RA5SQ908G1]
sources:
  - url: https://en.wikipedia.org/wiki/Sperner_property_of_a_partially_ordered_set
---

## Definition

Let $P$ be a finite [[graded poset|1C7TKGTB2F]] with rank function $\rho$, and for each integer $i \ge 0$ let $P_i = \set{x \in P : \rho(x) = i}$ be the $i$-th rank level.
The poset $P$ has the *Sperner property* when every [[antichain|03HF498P1J]] $A \subseteq P$ satisfies $\abs{A} \le \max_i \abs{P_i}$.

## Remarks

Since each $P_i$ is an antichain, the condition says that the [[width|RA5SQ908G1]] of $P$ equals $\max_i \abs{P_i}$.

Example: the lattice of subsets of $\set{1, \ldots, n}$, ranked by size, has the Sperner property.
Check: by Sperner's theorem, an antichain has at most $\binom{n}{\floor{n/2}}$ members, which is the size of the middle level.

Non-example: let $P$ have elements $a_1, a_2, b$ of rank $0$ and $c, d_1, d_2$ of rank $1$, with the relations $a_1 < c$, $a_2 < c$, $b < d_1$, $b < d_2$ and no others.
Each level has $3$ elements, but $\set{a_1, a_2, d_1, d_2}$ is an antichain with $4$ elements.

A poset is strongly Sperner when, for every $k$, the largest union of $k$ antichains is no larger than the largest union of $k$ rank levels.
