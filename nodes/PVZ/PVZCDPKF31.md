---
tag: PVZCDPKF31
kind: definition
name: Matroid
msc: [05B35]
defines: PX31ZNYS3Z
uses: [070R982G4B, 00E0YZCERH, 0CRMGPAH83]
sources:
  - url: https://en.wikipedia.org/wiki/Matroid
---

## Definition

Let $E$ be a [[finite set|070R982G4B]], called the ground set.
A *matroid* on $E$ is a pair $M = (E, \mathcal{I})$, where $\mathcal{I}$ is a family of subsets of $E$, called independent sets, such that:

1. $\emptyset \in \mathcal{I}$.
2. If $A \in \mathcal{I}$ and $B \subseteq A$, then $B \in \mathcal{I}$.
3. If $A, B \in \mathcal{I}$ and $\abs{A} > \abs{B}$, then there is $x \in A \setminus B$ with $B \cup \set{x} \in \mathcal{I}$.

A subset of $E$ that is not in $\mathcal{I}$ is *dependent*.

## Remarks

Example: let $E$ be the set of columns of a matrix over a field, and let $\mathcal{I}$ be the sets of columns that are [[linearly independent|0CRMGPAH83]].
Clauses 1 and 2 are clear.
For clause 3, if $\abs{A} > \abs{B}$, then $A$ spans a space of larger dimension than $B$.
So some $x \in A$ lies outside the span of $B$, and $B \cup \set{x}$ is independent.
Similarly, the edge sets of the forests of a graph form a matroid, the graphic matroid.
The uniform matroid $U_{k,n}$ has ground set $\set{1, \dots, n}$ and independent sets all subsets with at most $k$ elements.

Non-example: on $E = \set{1, 2, 3}$, let $\mathcal{I} = \set{\emptyset, \set{1}, \set{2}, \set{3}, \set{1, 2}}$.
Clauses 1 and 2 hold, but clause 3 fails for $A = \set{1, 2}$ and $B = \set{3}$: neither $\set{1, 3}$ nor $\set{2, 3}$ is independent.

Clause 3 is called the augmentation or exchange axiom.
Equivalent definitions use the [[bases|QTSQR7130G]], the [[rank function|SYRCTH853H]] or the circuits (minimal dependent sets).
Some authors allow an infinite ground set with extra conditions.
