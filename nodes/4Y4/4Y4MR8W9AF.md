---
tag: 4Y4MR8W9AF
kind: definition
name: Association scheme
msc: ["05E30"]
defines: C338GKB4VJ
uses: [08QMKTWF9T, 070R982G4B, 08B9CX109G]
sources:
  - url: https://en.wikipedia.org/wiki/Association_scheme
---

## Definition

Let $X$ be a nonempty [[finite set|070R982G4B]] and let $d \ge 1$.
An *association scheme* with $d$ classes on $X$ is a [[partition|08QMKTWF9T]] of $X \times X$ into nonempty relations $R_0, R_1, \dots, R_d$ such that:

1. $R_0 = \set{(x, x) : x \in X}$.
2. For each $i$, the relation $R_i^T = \set{(y, x) : (x, y) \in R_i}$ is equal to $R_{i'}$ for some $i'$.
3. For all $i, j, k$ there is an integer $p^k_{ij}$ such that for every $(x, y) \in R_k$ the number of $z \in X$ with $(x, z) \in R_i$ and $(z, y) \in R_j$ equals $p^k_{ij}$.

The scheme is *symmetric* if $R_i^T = R_i$ for every $i$, and *commutative* if $p^k_{ij} = p^k_{ji}$ for all $i, j, k$.

## Remarks

Many authors, following Bose and Mesner, require the scheme to be symmetric in the definition.
In terms of the [[adjacency matrices|08B9CX109G]] $A_i$ of the relations, clause 3 says $A_i A_j = \sum_k p^k_{ij} A_k$.
So the $A_i$ span an algebra of matrices, the Bose–Mesner algebra, which is commutative exactly when the scheme is commutative.

Example: on any finite set $X$ with at least $2$ points, let $R_0$ be the diagonal and $R_1$ the set of pairs of distinct points.
Clauses 1 and 2 hold, and clause 3 holds with $p^0_{11} = \abs{X} - 1$ and $p^1_{11} = \abs{X} - 2$, while every other $p^k_{ij}$ is $0$ or $1$.

Non-example: let $X = \set{a, b, c}$ with $R_0$ the diagonal, $R_1$ the edges of the path $a - b - c$ in both directions, and $R_2 = \set{(a, c), (c, a)}$.
Clause 3 fails for $i = j = 1$, $k = 0$: for $(a, a)$ there is one $z$ with $(a, z), (z, a) \in R_1$, but for $(b, b)$ there are two.

A symmetric scheme with $2$ classes is the same as a [[strongly regular graph|C22WGRP3T8]] that is neither complete nor edgeless, with $R_1$ as its edge relation.
