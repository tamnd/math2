---
tag: 7YD2GRHXAB
kind: definition
name: Basis of a matroid
msc: [05B35]
defines: QTSQR7130G
uses: [PX31ZNYS3Z]
sources:
  - url: https://en.wikipedia.org/wiki/Basis_of_a_matroid
---

## Definition

Let $M = (E, \mathcal{I})$ be a [[matroid|PX31ZNYS3Z]].
A *basis* of $M$ is a set $B \in \mathcal{I}$ such that no set $A \in \mathcal{I}$ satisfies $B \subsetneq A$.

## Remarks

By the augmentation axiom, all bases of $M$ have the same number of elements.
The bases satisfy the exchange property: if $B_1, B_2$ are bases and $x \in B_1 \setminus B_2$, then there is $y \in B_2 \setminus B_1$ such that $(B_1 \setminus \set{x}) \cup \set{y}$ is a basis.
Conversely, a nonempty family of subsets of $E$ with this exchange property is the family of bases of exactly one matroid, whose independent sets are the subsets of bases.

Example: let $U_{2,3}$ be the uniform matroid on $\set{1, 2, 3}$, whose independent sets are the subsets with at most $2$ elements.
The set $\set{1, 2}$ is a basis of $U_{2,3}$.
It is independent, and its only proper superset $\set{1, 2, 3}$ has $3$ elements, so it is dependent.

Non-example: in $U_{2,3}$ the set $\set{1}$ is independent but not a basis, since $\set{1, 2}$ is a larger independent set.

In the graphic matroid of a connected graph, the bases are the [[spanning trees|0S4ZEZM7KE]].
In the matroid of the columns of a matrix, the bases are the sets of columns that form a basis of the column space.
