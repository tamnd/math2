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

We compute all nine [[cofactors|0W2QAVJQ1W]] of
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 10 \end{pmatrix}$$
over $\mathbb{Q}$, whose determinant is $-3$, and check them by two expansions.
Each minor is a [[2 by 2 determinant|0ZN2J42SK7]], and the signs follow the checkerboard
$$\begin{pmatrix} + & - & + \\ - & + & - \\ + & - & + \end{pmatrix}.$$

1. Row $1$: the minors are $M_{11} = 50 - 48 = 2$, $M_{12} = 40 - 42 = -2$ and $M_{13} = 32 - 35 = -3$.
   With the signs $+, -, +$, the cofactors are $C_{11} = 2$, $C_{12} = 2$ and $C_{13} = -3$.
2. Row $2$: the minors are
$$M_{21} = \det \begin{pmatrix} 2 & 3 \\ 8 & 10 \end{pmatrix} = -4, \qquad M_{22} = \det \begin{pmatrix} 1 & 3 \\ 7 & 10 \end{pmatrix} = -11, \qquad M_{23} = \det \begin{pmatrix} 1 & 2 \\ 7 & 8 \end{pmatrix} = -6.$$
   With the signs $-, +, -$, the cofactors are $C_{21} = 4$, $C_{22} = -11$ and $C_{23} = 6$.
3. Row $3$: the minors are $M_{31} = 12 - 15 = -3$, $M_{32} = 6 - 12 = -6$ and $M_{33} = 5 - 8 = -3$.
   With the signs $+, -, +$, the cofactors are $C_{31} = -3$, $C_{32} = 6$ and $C_{33} = -3$.
4. So the cofactor matrix is
$$\operatorname{cof} A = \begin{pmatrix} 2 & 2 & -3 \\ 4 & -11 & 6 \\ -3 & 6 & -3 \end{pmatrix}.$$
5. Check by the [[Laplace expansion|0C08BQ3M05]] along row $2$:
$$4 \cdot 4 + 5 \cdot (-11) + 6 \cdot 6 = 16 - 55 + 36 = -3 = \det A.$$
6. Check along column $3$, which pairs the entries $3, 6, 10$ with $C_{13}, C_{23}, C_{33}$:
$$3 \cdot (-3) + 6 \cdot 6 + 10 \cdot (-3) = -9 + 36 - 30 = -3.$$

## Remarks

Every row and every column of $\operatorname{cof} A$ gives $\det A$ when it is paired with the same row or column of $A$.
A row of $A$ paired with a different row of cofactors gives $0$.
For example, row $1$ of $A$ with row $2$ of the cofactors gives
$$1 \cdot 4 + 2 \cdot (-11) + 3 \cdot 6 = 0,$$
and this is the content of the [[adjugate identity|0528HKWZ1Z]].
Transposing $\operatorname{cof} A$ gives the adjugate, so $A^{-1} = -\tfrac{1}{3} (\operatorname{cof} A)^{\mathsf{T}}$.

If the last entry $10$ is changed to $9$, only the cofactors that use that entry change, namely $C_{11}$, $C_{12}$, $C_{21}$ and $C_{22}$.
For instance $C_{11}$ becomes $45 - 48 = -3$, and the row $3$ cofactors stay $-3, 6, -3$, since they never use row $3$.

## Explanations

### L1 human

Each of the nine entries has a cofactor: cover its row and column, take the $2 \times 2$ determinant of the four numbers left, and attach the checkerboard sign.
Multiplying the entries of one row by their cofactors and adding gives the determinant, here $-3$.
Any row or column works, and they all give the same answer.

### L2 human

The two checks, along a row and along a column, use six of the nine cofactors, and both give $-3$.
A third check is the product: the first row of $A$ times the first column of $(\operatorname{cof} A)^{\mathsf{T}}$ is $1 \cdot 2 + 2 \cdot 2 + 3 \cdot (-3) = -3$.
Watch out for row $2$: its signs start with minus, so $C_{21} = -M_{21} = 4$ and not $-4$.
