---
tag: 009CY8JXFX
kind: statement
role: proposition
name: Scaling a row scales the determinant
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
uses: [0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Basic rules
---

## Statement

A common factor of one row can be taken out of the determinant.
Let $K$ be a commutative ring, let $n \ge 1$, let $A$ be an $n \times n$ matrix over $K$, and let $c \in K$.
Let $B$ be the matrix that results when one row of $A$ is multiplied by $c$.
Then $\det B = c \det A$, where $\det$ is the [[determinant|00KDZRW4C0]].

## Remarks

### A small check

Multiply the second row of $\begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$ by $4$:
$$\det \begin{pmatrix} 2 & 1 \\ 4 & 12 \end{pmatrix} = 24 - 4 = 20 = 4 \cdot (6 - 1).$$
The old determinant is $5$, and the new one is $4 \cdot 5$.
Read from right to left, the rule takes a factor out: since $(4, 12) = 4 (1, 3)$, the factor $4$ comes out of that row.

### Where it comes from and where it goes

The rule is the special case of [[linearity in each row|0PPG793642]] in which the row is multiplied by a scalar and nothing is added.
It describes the effect of the scaling [[row operation|04XWH28452]] on the determinant, one of the [[effects of row operations|09YB3WQG38]].
Applied to all $n$ rows, it gives the [[determinant of a scalar multiple|01EXSMK864]], $\det(cA) = c^n \det A$.
With $c = 0$ it shows that a [[zero row gives determinant 0|0FS6B46E5T]].

### Watch out

The factor comes out once for each row that is scaled, not once for the whole matrix.
Scaling one row of $I_2$ by $3$ gives determinant $3$, but scaling both rows gives $\det(3 I_2) = 9$.

## Explanations

### L1 human

Think of the rows as the edges of a box, and of the determinant as its volume.
If we stretch one edge by the factor $c$ and keep the others, the volume is multiplied by $c$.
The determinant behaves in the same way.
For example, doubling one row doubles the determinant, and halving it halves the determinant.

### L2 human

Here is a typical use: compute $\det \begin{pmatrix} 6 & 9 \\ 10 & 25 \end{pmatrix}$ with small numbers.
Take $3$ out of the first row and $5$ out of the second row:
$$\det \begin{pmatrix} 6 & 9 \\ 10 & 25 \end{pmatrix} = 3 \cdot 5 \det \begin{pmatrix} 2 & 3 \\ 2 & 5 \end{pmatrix} = 15 (10 - 6) = 60.$$
Check: $6 \cdot 25 - 9 \cdot 10 = 150 - 90 = 60$.
Factoring rows first keeps the numbers small, which helps in hand computations and in exact computations over the integers.
