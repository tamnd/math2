---
tag: ~a94fe0ae
kind: definition
name: Dimension
msc: [15A03]
defines: ~3d1088d4
uses: [~6c1abb8a, ~f114c28f]
sources:
  - url: https://en.wikipedia.org/wiki/Dimension_(vector_space)
    locator: lead section
---

## Definition

Let $F$ be a field and let $V$ be a [[finite-dimensional|~d32e3615]] vector space over $F$.
The *dimension* of $V$ over $F$, written $\dim_F V$ or $\dim V$, is the number of vectors in a [[basis|~4af6ac42]] of $V$.
For an arbitrary vector space, the dimension is the cardinality of a basis.

## Remarks

The number is well defined, by the [[dimension theorem for vector spaces|~b8615729]].
The zero space $\{0\}$ has the empty basis and dimension $0$.
The dimension depends on the field: $\dim_\C \C = 1$, but $\dim_\R \C = 2$.
Mathlib writes `Module.finrank F V` for the dimension as a natural number, with value $0$ for infinite-dimensional spaces.

## Explanations

### L1 human

The dimension counts the independent directions in a space.
A line has dimension $1$, a plane has dimension $2$, and ordinary space has dimension $3$.
Every basis of a space has this same number of vectors.
