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

The special unitary group of degree $n$ is the group of complex unitary $n \times n$ matrices whose determinant equals $1$.
Let $n \ge 1$.
The *special unitary group* is the set
$$SU(n) = \{ U \in M_n(\C) : U^*U = I_n \text{ and } \det U = 1 \}$$
of complex [[unitary matrices|0D6RMJ10M9]] with [[determinant|0C3CFHDN6R]] $1$, with matrix multiplication as the group operation.

## Notation

Books write $SU(n)$, $SU_n$ or $SU(n, \C)$.
Mathlib writes `Matrix.specialUnitaryGroup n ℂ` for an index type `n`, and it defines this as the matrices in `Matrix.unitaryGroup n ℂ` with determinant `1`.

## Remarks

The definition has two conditions, and each one does its own job.
The condition $U^*U = I_n$ says that the columns are orthonormal for the complex inner product, so $U$ keeps lengths.
It already forces $\abs{\det U} = 1$, since $\abs{\det U}^2 = \det U^* \det U = 1$.
The condition $\det U = 1$ then fixes the argument of the determinant too, so it cuts the circle of possible determinants down to one point.

The set is a group because both conditions survive products and inverses.
Products of unitary matrices are unitary, and $\det(UV) = \det U \det V = 1$; the inverse $U^{-1} = U^*$ is unitary with $\det U^* = \overline{\det U} = 1$.

For an example, take $U = \operatorname{diag}(i, -i)$.
It is unitary, since $\overline{i} \cdot i = 1$ and $\overline{(-i)} \cdot (-i) = 1$, and $\det U = i \cdot (-i) = 1$, so $U \in SU(2)$.
For a failure, take $iI_2$: it is unitary, but $\det(iI_2) = i^2 = -1$, so it fails the second condition.
The matrix $\operatorname{diag}(2, \frac{1}{2})$ fails the first condition instead, although its determinant is $1$.
The [[concept page|ZRYYPHWESP]] gives more examples, the quaternion description of $SU(2)$ and the double cover of $SO(3)$.

## Explanations

### L1 human

A special unitary matrix is a unitary matrix whose determinant is exactly $1$.
For every unitary matrix, the determinant is a point on the unit circle of the complex plane.
The special ones are those whose point is $1$.

### L2 human

Here is a check of both conditions for $U = \frac{1}{5} \begin{pmatrix} 3 & -4i \\ -4i & 3 \end{pmatrix}$.
The columns have squared lengths $\frac{9 + 16}{25} = 1$, and their inner product is
$$\tfrac{1}{25}\big(3 \cdot \overline{(-4i)} + (-4i) \cdot 3\big) = \tfrac{1}{25}(12i - 12i) = 0,$$
so $U$ is unitary.
The determinant is $\frac{1}{25}\big(9 - (-4i)^2\big) = \frac{1}{25}(9 + 16) = 1$, so $U \in SU(2)$.
Watch out: $\operatorname{diag}(i, i)$ is unitary, but its determinant is $-1$.
