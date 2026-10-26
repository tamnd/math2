---
tag: ~b61be5cb
kind: definition
name: Irreducible element
msc: [13A05]
defines: ~88af24d9
uses: [~6bd4a5ff, ~11c1c339]
sources:
  - url: https://en.wikipedia.org/wiki/Irreducible_element
    locator: Definition in an integral domain
---

## Definition

Let $R$ be an [[integral domain|~6bd4a5ff]].
An element $p \in R$ is irreducible if it has these three properties.

1. $p \neq 0$.
2. $p$ is not a [[unit|~11c1c339]].
3. If $p = a b$ with $a, b \in R$, then $a$ is a unit or $b$ is a unit.

## Remarks

The irreducible elements of $\mathbb{Z}$ are the numbers $p$ and $-p$ with $p$ prime.
In $\mathbb{Z}[i]$, the number $3$ is irreducible, but $5 = (2 + i)(2 - i)$ is not.
Every [[prime element|~363b219f]] is irreducible. The converse [[can fail|~eb44d6b3]].
For polynomials over a field, the irreducible elements are the [[irreducible polynomials|~25830f16]].

## Explanations

### L1 human

An irreducible element cannot be split into smaller factors.
The only factorizations are trivial ones, with a unit as one factor, like $7 = (-1)(-7)$.
In the integers, the irreducible elements are the primes and their negatives.
