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

The adjugate of a square matrix is the transpose of its matrix of cofactors.
Let $K$ be a commutative ring, let $n \ge 2$, and let $A$ be an $n \times n$ matrix over $K$ with [[cofactors|0W2QAVJQ1W]] $C_{ij}$.
The *adjugate* of $A$ is the $n \times n$ matrix $\operatorname{adj}(A)$ with the entries
$$\operatorname{adj}(A)_{ij} = C_{ji} \qquad (1 \le i, j \le n).$$
So $\operatorname{adj}(A)$ is the [[transpose|0W809K6AW0]] of the cofactor matrix $(C_{ij})$.
For $n = 1$ we set $\operatorname{adj}(a) = (1)$ for every $a \in K$.

## Remarks

The definition has three parts, and each has a reason.
The cofactors carry the signs $(-1)^{i+j}$, and these signs are what make the [[adjugate identity|0528HKWZ1Z]] $A \operatorname{adj}(A) = \det(A) I_n$ true.
The transpose is needed because entry $(i, k)$ of $A \operatorname{adj}(A)$ must pair row $i$ of $A$ with the cofactors of row $k$, and those cofactors sit in column $k$ of the adjugate only after the transpose.
The ring must be commutative, so that the determinants that define the cofactors make sense and the Laplace expansion holds.

For $n = 2$, the cofactors of $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ are $d, -c, -b, a$, so
$$\operatorname{adj} \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}.$$
Without the transpose we would get $\begin{pmatrix} d & -c \\ -b & a \end{pmatrix}$, and for $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ its product with the matrix has the entry $1 \cdot (-3) + 2 \cdot 1 = -1$ in position $(1, 2)$, so it is not a multiple of $I_2$.

The convention for $n = 1$ makes the identity $a \cdot 1 = \det(a)$ true, and it agrees with Mathlib.
Older texts call the adjugate the *classical adjoint*, which is not the adjoint of an operator on an inner product space.
The [[concept page|07W9H8QF38]] gives the examples and the rules.

## Explanations

### L1 human

To build the adjugate, replace each entry by its cofactor, which is a signed smaller determinant.
Then flip the result across the main diagonal, so that rows become columns.
For a $2 \times 2$ matrix the two steps together swap the diagonal entries and change the sign of the other two.
