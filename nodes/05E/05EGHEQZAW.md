---
tag: 05EGHEQZAW
kind: definition
name: Vector space
msc: [15A03]
defines: 000AYPA9AJ
sources:
  - url: https://en.wikipedia.org/wiki/Vector_space
    locator: Definition and basic properties
inventory: [FS3H3KZHNY]
---

## Definition

Let $F$ be a field.
A *vector space* over $F$ is a set $V$ with two maps: an addition $V \times V \to V$, $(u, v) \mapsto u + v$, and a scalar multiplication $F \times V \to V$, $(a, v) \mapsto av$.
These axioms must hold for all $u, v, w \in V$ and $a, b \in F$:

1. $u + (v + w) = (u + v) + w$.
2. $u + v = v + u$.
3. There is an element $0 \in V$ with $v + 0 = v$ for all $v \in V$.
4. For each $v \in V$ there is an element $-v \in V$ with $v + (-v) = 0$.
5. $a(bv) = (ab)v$.
6. $1v = v$, where $1$ is the unit of $F$.
7. $a(u + v) = au + av$.
8. $(a + b)v = av + bv$.

The elements of $V$ are *vectors*, and the elements of $F$ are *scalars*.

## Remarks

Axioms 1 to 4 say that $(V, +)$ is an abelian group.
The axioms give $0v = 0$ and $(-1)v = -v$ for all $v \in V$.
A vector space is a [[module|0NZ8JA25WK]] over a field; Mathlib uses `Module F V` for both.
Examples are the [[coordinate space|0XM8BZD76G]] $F^n$, [[spaces of matrices|0RE6X3BGPN]] and [[function spaces|0GZB2SN0PH]].

## Explanations

### L1 human

A vector space is a collection of objects that we can add together and stretch by numbers.
Arrows in the plane are the standard picture, but polynomials and functions also form vector spaces.
The eight axioms list the rules that make the usual algebra work.
