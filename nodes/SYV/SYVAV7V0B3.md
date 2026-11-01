---
tag: SYVAV7V0B3
kind: definition
name: Dual matroid
msc: [05B35]
defines: 6QF83CFK2G
uses: [PX31ZNYS3Z, QTSQR7130G, SYRCTH853H]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_matroid
---

## Definition

Let $M$ be a [[matroid|PX31ZNYS3Z]] on a finite ground set $E$, and let $\mathcal{B}$ be its set of [[bases|QTSQR7130G]].
The *dual matroid* $M^*$ is the matroid on $E$ whose set of bases is
$$\mathcal{B}^* = \set{E \setminus B : B \in \mathcal{B}}.$$

## Remarks

It is a theorem that $\mathcal{B}^*$ satisfies the basis exchange property, so $M^*$ is indeed a matroid.
Its independent sets are the subsets of $E$ disjoint from some basis of $M$.
Its [[rank function|SYRCTH853H]] is $r^*(A) = \abs{A} - r(E) + r(E \setminus A)$, where $r$ is the rank function of $M$, and $(M^*)^* = M$.
The bases of $M^*$ are the cobases of $M$, and the circuits of $M^*$ are the cocircuits of $M$.

Example: for the uniform matroid $U_{k,n}$, whose bases are the $k$-element subsets of $\set{1, \dots, n}$, the dual has as bases the $(n-k)$-element subsets, so $U_{k,n}^* = U_{n-k,n}$.

Non-example: the complements of the independent sets of $M$ are in general not the independent sets of $M^*$.
For $M = U_{1,2}$ on $\set{1, 2}$, the complement of $\emptyset$ is $\set{1, 2}$, which is not independent in $M^* = U_{1,2}$.
