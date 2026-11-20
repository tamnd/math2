---
tag: 0GMPYM0NSR
kind: definition
name: Adjugate matrix
msc: ["15A09", "15A15"]
topics: [DTBK11SR77]
audience: ug1
defines: 07W9H8QF38
uses: [0W2QAVJQ1W, 0W809K6AW0]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.adjugate
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Adjugate_matrix
    locator: Definition
inventory: [WQ1C08GYW2]
---

## Definition

Let $K$ be a commutative ring, let $n \ge 2$, and let $A$ be an $n \times n$ matrix over $K$ with [[cofactors|0W2QAVJQ1W]] $C_{ij}$.
The *adjugate* of $A$ is the $n \times n$ matrix $\operatorname{adj}(A)$ with entries
$$\operatorname{adj}(A)_{ij} = C_{ji}.$$
So $\operatorname{adj}(A)$ is the [[transpose|0W809K6AW0]] of the matrix of cofactors $(C_{ij})$.
For $n = 1$ one sets $\operatorname{adj}(a) = (1)$.

## Remarks

For $n = 2$, $\operatorname{adj} \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$.
The adjugate satisfies $A \operatorname{adj}(A) = \det(A) I_n$, by the [[adjugate identity|0528HKWZ1Z]].
Older texts call it the *classical adjoint*; it is not the adjoint of an inner product space.
The convention for $n = 1$ makes the adjugate identity true for $n = 1$, and it agrees with Mathlib.

## Explanations

### L1 human

To build the adjugate, replace each entry by its cofactor, and then transpose.
The adjugate is almost the inverse: it is the inverse multiplied by the determinant.
For $2 \times 2$ matrices, swap the diagonal entries and negate the other two.
