---
tag: 0E3X2G1ZQB
kind: object
name: Algebra of endomorphisms
msc: [15A04, 16S50]
instance_of: [0X9MBPP2Z3]
sources:
  - url: https://en.wikipedia.org/wiki/Endomorphism_ring
    locator: lead section
---

## Description

Let $F$ be a field and let $V$ be a vector space over $F$.
The *algebra of endomorphisms* $\End_F(V)$ is the set of [[endomorphisms|0J7H0YBFDJ]] of $V$, with pointwise addition, scalar multiplication, and composition as multiplication.
It is an associative algebra over $F$, with the identity map $\id_V$ as unit.
Thus $S(T + U) = ST + SU$, $(S + T)U = SU + TU$ and $a(ST) = (aS)T = S(aT)$ for all $S, T, U \in \End_F(V)$ and $a \in F$.

## Remarks

If $\dim V = n$, then the choice of a basis gives an algebra isomorphism $\End_F(V) \cong M_n(F)$.
For $\dim V \ge 2$, the algebra is not commutative.
Its group of units is the group $GL(V)$ of linear isomorphisms $V \to V$.

## Explanations

### L1 human

The endomorphisms of a space can be added, scaled and composed.
Composition plays the role of multiplication.
This makes them a ring that is also a vector space, like the square matrices.
