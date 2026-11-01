---
tag: PG8Z6F6DV9
kind: definition
name: Amenable group
msc: [43A07, 20F65]
defines: CEAT9BESKK
uses: [G5S1M9, 0KTW26C80J]
sources:
  - url: https://en.wikipedia.org/wiki/Amenable_group
---

## Definition

Let $G$ be a [[group|G5S1M9]], with no topology, and let $\mathcal{P}(G)$ be the set of all subsets of $G$.
The group $G$ is *amenable* if there is a function $\mu \colon \mathcal{P}(G) \to [0, 1]$ such that:

1. $\mu(G) = 1$.
2. $\mu(A \cup B) = \mu(A) + \mu(B)$ for all disjoint $A, B \subseteq G$.
3. $\mu(gA) = \mu(A)$ for all $g \in G$ and $A \subseteq G$.

Such a $\mu$ is a left-invariant finitely additive probability measure on $G$.

## Remarks

Example: a finite group $G$ is amenable, with $\mu(A) = \abs{A} / \abs{G}$; left translation is a bijection, so $\abs{gA} = \abs{A}$.

Non-example: the [[free group|0KTW26C80J]] $F_2$ on $a, b$ is not amenable.
Let $W(x)$ be the set of reduced words that begin with the letter $x$.
Then $F_2 = W(a) \sqcup a W(a^{-1})$ and $F_2 = W(b) \sqcup b W(b^{-1})$.
An invariant $\mu$ would give $\mu(W(a)) + \mu(W(a^{-1})) = 1$ and $\mu(W(b)) + \mu(W(b^{-1})) = 1$, but these four disjoint sets lie in $F_2$, so their total is at most $1$, a contradiction.

Equivalently, there is a left-invariant mean on $\ell^\infty(G)$, a positive linear functional $m$ with $m(1) = 1$ and $m(g \cdot f) = m(f)$.
For a locally compact group, one asks instead for a left-invariant mean on $L^\infty(G)$; for discrete groups the two notions agree.
For a countable group, amenability is equivalent to the Følner condition.
Subgroups, quotients and extensions of amenable groups are amenable, and abelian and solvable groups are amenable.
