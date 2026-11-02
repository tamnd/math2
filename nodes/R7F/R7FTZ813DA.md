---
tag: R7FTZ813DA
kind: definition
name: Borel subgroup
msc: [20G07, 20G15]
defines: 5JSYA1JNCC
uses: [GA81VVQHEP, 0FXJ7YFMMX, 8SQK7RTB63, 0FCHE902D7]
sources:
  - url: https://en.wikipedia.org/wiki/Borel_subgroup
---

## Definition

Let $k$ be an algebraically closed field, and let $G$ be a [[linear algebraic group|GA81VVQHEP]] over $k$.
A *Borel subgroup* of $G$ is a subgroup $B \subseteq G$ such that:

1. $B$ is closed in the [[Zariski topology|8SQK7RTB63]];
2. $B$ is connected and [[solvable|0FXJ7YFMMX]];
3. $B$ is maximal among the subgroups with properties 1 and 2.

## Remarks

Over an arbitrary field $k$, a closed subgroup $B$ of $G$ is called a Borel subgroup if $B \times_k \bar{k}$ is a Borel subgroup of $G \times_k \bar{k}$.

Example: in $G = \mathrm{GL}_n$ the group $B$ of invertible upper triangular matrices is a Borel subgroup.
It is closed, cut out by $x_{ij} = 0$ for $i > j$.
It is connected and solvable, since its commutator subgroup consists of unipotent upper triangular matrices.
It is maximal: by the Lie–Kolchin theorem, a connected solvable subgroup $B' \supseteq B$ fixes some full flag, and the only full flag fixed by $B$ is the standard one, so $B' \subseteq B$.

Non-example: in $\mathrm{GL}_2$, the diagonal torus $T$ is closed, connected and solvable, but it fails clause 3, since $T \subsetneq B$ for the upper triangular group $B$.

All Borel subgroups of $G$ are conjugate, and $G / B$ is a projective variety.
