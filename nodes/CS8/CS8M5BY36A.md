---
tag: CS8M5BY36A
kind: example
name: The cofactor matrix of a 3 × 3 matrix
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
instance_of: [0XPKR18APA]
uses: [0W2QAVJQ1W, 0C08BQ3M05, 0ZN2J42SK7]
sources:
  - url: https://en.wikipedia.org/wiki/Minor_(linear_algebra)
    locator: Cofactor expansion of the determinant
---

## Example

Let $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 10 \end{pmatrix}$ over $\mathbb{Q}$, with $\det A = -3$.

1. The first minors of row $1$ are $M_{11} = 2$, $M_{12} = -2$, $M_{13} = -3$. With the signs $+, -, +$, the [[cofactors|0W2QAVJQ1W]] are $C_{11} = 2$, $C_{12} = 2$, $C_{13} = -3$.
2. Row $2$: $M_{21} = \det \begin{pmatrix} 2 & 3 \\ 8 & 10 \end{pmatrix} = -4$, $M_{22} = \det \begin{pmatrix} 1 & 3 \\ 7 & 10 \end{pmatrix} = -11$, $M_{23} = \det \begin{pmatrix} 1 & 2 \\ 7 & 8 \end{pmatrix} = -6$.
3. With the signs $-, +, -$, this gives $C_{21} = 4$, $C_{22} = -11$, $C_{23} = 6$.
4. Row $3$: $M_{31} = 12 - 15 = -3$, $M_{32} = 6 - 12 = -6$, $M_{33} = 5 - 8 = -3$. With the signs $+, -, +$, $C_{31} = -3$, $C_{32} = 6$, $C_{33} = -3$.
5. So the cofactor matrix is $C = \begin{pmatrix} 2 & 2 & -3 \\ 4 & -11 & 6 \\ -3 & 6 & -3 \end{pmatrix}$.
6. Check by the [[Laplace expansion|0C08BQ3M05]] along row $2$: $4 \cdot 4 + 5 \cdot (-11) + 6 \cdot 6 = 16 - 55 + 36 = -3 = \det A$.
7. Check along column $3$: $3 \cdot (-3) + 6 \cdot 6 + 10 \cdot (-3) = -9 + 36 - 30 = -3$.

## Remarks

Each row and each column of $C$ gives $\det A$ when it is paired with the same row or column of $A$.
Pairing row $1$ of $A$ with row $2$ of $C$ gives $1 \cdot 4 + 2 \cdot (-11) + 3 \cdot 6 = 0$; this is the [[adjugate identity|0528HKWZ1Z]].

## Explanations

### L1 human

Each of the nine entries has a cofactor: a $2 \times 2$ determinant with a checkerboard sign.
Multiplying the entries of one row by their cofactors and adding gives the determinant, here $-3$.

### L2 human

The two expansions, along a row and along a column, agree, which checks all six cofactors they use.
A trap: the signs in row $2$ start with minus, not plus.
