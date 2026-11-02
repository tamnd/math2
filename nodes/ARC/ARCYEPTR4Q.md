---
tag: ARCYEPTR4Q
kind: definition
name: Subalgebra lattice
msc: [08A30, 06B23]
defines: T0TNG7AGXT
uses: [QJGPT2W0FT, 2TQD8NMG9P, D7A0ZGZT5S, 3J0BTXSCVN, 9F7TYES4KE, WR4WF1K2KW]
sources:
  - url: https://en.wikipedia.org/wiki/Compact_element
---

## Definition

Let $\mathbf{A}$ be an [[algebra|QJGPT2W0FT]] with universe $A$.
A *subuniverse* of $\mathbf{A}$ is a subset of $A$ closed under all fundamental operations, as for a subalgebra.
Let $\operatorname{Sub} \mathbf{A}$ be the set of all subuniverses of $\mathbf{A}$.
The *subalgebra lattice* of $\mathbf{A}$ is the partially ordered set $(\operatorname{Sub} \mathbf{A}, \subseteq)$.
Its meet and join are
$$B \wedge C = B \cap C, \qquad B \vee C = \operatorname{Sg}(B \cup C),$$
where $\operatorname{Sg}$ is the [[generated subuniverse|2TQD8NMG9P]].

## Remarks

The intersection of any family of subuniverses is a subuniverse, so $\operatorname{Sub} \mathbf{A}$ is a [[complete lattice|D7A0ZGZT5S]].
It is an [[algebraic lattice|3J0BTXSCVN]].
Its [[compact elements|9F7TYES4KE]] are the subuniverses $\operatorname{Sg}(X)$ with $X$ finite, that is, the [[finitely generated|WR4WF1K2KW]] ones.

Example: for the group $(\Z, +, -, 0)$ the subuniverses are the sets $n\Z$ with $n \ge 0$.
Here $m\Z \subseteq n\Z$ if and only if $n$ divides $m$, and $m\Z \vee n\Z = d\Z$ with $d = \gcd(m, n)$.

Non-example: the lattice of all subsets of $\Z$ is not the subalgebra lattice of this group.
The subset $\set{1}$ is not closed under addition, so it is not a subuniverse.

When the signature has no constant symbols, the empty set is a subuniverse and is the least element of $\operatorname{Sub} \mathbf{A}$.
Some authors exclude it and call only nonempty subuniverses subalgebras.
