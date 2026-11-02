---
tag: RNTAAHTD0M
kind: definition
name: Semilattice
msc: [06A12]
defines: 74X7JRG2J7
uses: [0QV2JS9RJ3, J2T75ATRV5, 0XMEM406JM]
sources:
  - url: https://en.wikipedia.org/wiki/Semilattice
---

## Definition

Let $(S, \le)$ be a [[partially ordered set|0QV2JS9RJ3]].
$S$ is a *join-semilattice* if every two elements $x, y \in S$ have a [[join|J2T75ATRV5]] $x \vee y$ in $S$.
$S$ is a *meet-semilattice* if every two elements $x, y \in S$ have a meet $x \wedge y$ in $S$.

Algebraic form: a *semilattice* is a set $S$ with a binary operation $\cdot$ such that, for all $x, y, z \in S$:

1. $(x \cdot y) \cdot z = x \cdot (y \cdot z)$;
2. $x \cdot y = y \cdot x$;
3. $x \cdot x = x$.

## Remarks

The two forms are equivalent.
A join-semilattice gives the operation $x \cdot y = x \vee y$.
Conversely, a semilattice $(S, \cdot)$ becomes a join-semilattice for the order $x \le y \iff x \cdot y = y$, and a meet-semilattice for the order $x \le y \iff x \cdot y = x$.
So a semilattice is a commutative [[semigroup|0XMEM406JM]] in which every element is idempotent.
Example: the finite subsets of $\N$, ordered by $\subseteq$, form a join-semilattice, since the union of two finite sets is finite and is their join.
Example: $\set{a, b, 1}$ with $a < 1$ and $b < 1$ is a join-semilattice with $a \vee b = 1$.
It is not a meet-semilattice, since $a$ and $b$ have no common lower bound.
Non-example: a two-element antichain $\set{a, b}$ is not a join-semilattice, since $a$ and $b$ have no upper bound.
