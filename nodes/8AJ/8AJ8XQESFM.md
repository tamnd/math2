---
tag: 8AJ8XQESFM
kind: definition
name: Special unitary group
msc: ["15B57", "20G20"]
topics: [AZS5BPF5H3]
audience: ug2
defines: ZRYYPHWESP
uses: [0D6RMJ10M9, 0C3CFHDN6R]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.specialUnitaryGroup
    match: variant
sources:
  - url: https://en.wikipedia.org/wiki/Special_unitary_group
    locator: lead section
---

## Definition

Let $n \ge 1$.
The *special unitary group* is the set
$$SU(n) = \set{U \in M_n(\C) : U^*U = I_n \text{ and } \det U = 1}$$
of complex [[unitary matrices|0D6RMJ10M9]] with [[determinant|0C3CFHDN6R]] $1$, with matrix multiplication as the group operation.

## Notation

- Books write $SU(n)$, $SU_n$ or $SU(n, \C)$.
- Mathlib writes `Matrix.specialUnitaryGroup n ℂ` for an index type `n`. It is defined as the matrices in `Matrix.unitaryGroup n ℂ` with determinant `1`.

## Remarks

- $SU(n)$ is closed under products and inverses, because the determinant is multiplicative. So it is a group.
- For a unitary matrix, $\abs{\det U} = 1$ always holds. The condition $\det U = 1$ is stronger: it also fixes the argument of $\det U$.
- Examples and non-examples are in the node on the [[concept|ZRYYPHWESP]].

## Explanations

### L1 human

A special unitary matrix is a unitary matrix whose determinant is exactly $1$.
For a unitary matrix, the determinant is always a point on the unit circle.
The special ones have the point $1$.

### L2 human

Worked check for $U = \operatorname{diag}(i, -i)$:

1. $U^*U = \operatorname{diag}(-i \cdot i, i \cdot (-i)) = \operatorname{diag}(1, 1) = I_2$.
2. $\det U = i \cdot (-i) = 1$.
3. So $U \in SU(2)$.

A trap: $\operatorname{diag}(i, i)$ is unitary, but its determinant is $-1$.
