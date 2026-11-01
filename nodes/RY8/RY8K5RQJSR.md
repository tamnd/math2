---
tag: RY8K5RQJSR
kind: statement
role: theorem
name: Kurosh subgroup theorem
msc: ["20E06", "20E07"]
uses: [TM7QS7P7X9, 0X1JXT47GA, 0KTW26C80J, 0DXD4QSZ8A]
about: [TM7QS7P7X9, 0X1JXT47GA]
sources:
  - url: https://en.wikipedia.org/wiki/Kurosh_subgroup_theorem
same_as:
  wikidata: Q6446396
  wikipedia: Kurosh subgroup theorem
---

## Statement

Let $(A_i)_{i \in I}$ be a family of groups, and let $G = \mathop{*}_{i \in I} A_i$ be their [[free product|TM7QS7P7X9]].
Let $H$ be a [[subgroup|0X1JXT47GA]] of $G$.
Then there are a [[free group|0KTW26C80J]] $F$, groups $B_j$ for $j \in J$, and elements $g_j \in G$ with the following property.
Each $B_j$ is a subgroup of some factor $A_{i(j)}$, and
$$H = F * \mathop{*}_{j \in J} g_j B_j g_j^{-1}.$$
In words, $H$ is the free product of a free group and of [[conjugates|0DXD4QSZ8A]] of subgroups of the factors.

## Remarks

One proof uses [[Bass–Serre theory|6M731X66RD]].
The free product $G$ acts on a tree with trivial edge stabilisers, and the vertex stabilisers are the conjugates of the factors $A_i$.
The subgroup $H$ acts on the same tree, so it is the fundamental group of a [[graph of groups|DC1CQMD3WK]] with trivial edge groups.
Such a group is the free product of its vertex groups and of a free group, the fundamental group of the underlying graph.
A topological proof uses covering spaces of a wedge of spaces whose fundamental groups are the $A_i$.

Example: if every $A_i$ is infinite cyclic, then $G$ is free.
Each subgroup of $\Z$ is trivial or infinite cyclic, so each $g_j B_j g_j^{-1}$ is free, and $H$ is free.
This recovers the [[Nielsen–Schreier theorem|W97X7WX5G8]].
Another example: in $\Z/2 * \Z/3$, which is isomorphic to $PSL(2, \Z)$, every subgroup without elements of finite order is free.

## Explanations

### L1 human

A free product glues groups together with no relations between them.
The theorem says that every subgroup of such a product is again built in the same simple way.
It is a free product of pieces taken from the original factors, moved around by conjugation, together with a free group.

### L2 human

The theorem is the main structure result for subgroups of free products.
It generalises the Nielsen–Schreier theorem, which says that subgroups of free groups are free.
It implies that a subgroup that meets every conjugate of every factor only in the identity is free.
In Bass–Serre theory it is the special case of trees with trivial edge stabilisers; the general case describes subgroups of amalgamated products and [[HNN extensions|YEYERRY37K]].
