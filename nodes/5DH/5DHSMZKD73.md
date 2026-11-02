---
tag: 5DHSMZKD73
kind: definition
name: Ring with involution
msc: [16W10, 46K05]
defines: 7W52X4N3NJ
uses: [0894J980RK, 0EX045E2BP]
sources:
  - url: https://en.wikipedia.org/wiki/*-algebra
---

## Definition

Let $R$ be a [[ring|0894J980RK]] with unit $1$.
An *involution* on $R$ is a map $R \to R$, $a \mapsto a^*$, such that for all $a, b \in R$:

1. $(a + b)^* = a^* + b^*$.
2. $(ab)^* = b^* a^*$.
3. $1^* = 1$.
4. $(a^*)^* = a$.

A *ring with involution*, or *$*$-ring*, is a ring together with an involution.

## Remarks

Clause 3 follows from the others: $1^* a = (a^* \cdot 1)^* = a$ and likewise $a 1^* = a$ for all $a$, so $1^*$ is a unit element and equals $1$.
An element $a$ is *self-adjoint* or *Hermitian* if $a^* = a$.
Example: $R = M_n(\C)$ with $A^* = \overline{A}^{\,T}$, the [[conjugate transpose|0EX045E2BP]].
Clauses 1, 3 and 4 are clear, and clause 2 holds because $(AB)^T = B^T A^T$ and conjugation is multiplicative.
Example: the transpose on $M_n(F)$ for a field $F$, and $g \mapsto g^{-1}$ extended linearly on a group ring $\Z[G]$.
Non-example: the identity map on $M_2(\R)$ satisfies clauses 1, 3 and 4 but fails clause 2, since $AB \ne BA$ for some matrices $A, B$.
If $R$ is an algebra over a commutative $*$-ring $K$, a *$*$-algebra* also asks $(\lambda a)^* = \lambda^* a^*$ for $\lambda \in K$.
