---
tag: KJ7X8CZWNT
kind: example
name: The left null space of a 3 × 4 matrix
msc: ["15A03", "15A06"]
topics: [S6559D61BP]
audience: ug1
instance_of: [0PHDYNR24D]
illustrates: [5NKND0CPKP]
uses: [0PQ2GGY1QV, 0W809K6AW0, 0NNR68BFRY]
sources:
  - url: https://en.wikipedia.org/wiki/Row_and_column_spaces
    locator: Relation to the left null space
---

## Example

The left null space of a matrix is the null space of its transpose, and it records the relations among the rows.
Let $A$ be the $3 \times 4$ matrix with rows $(1, 2, 0, 1)$, $(2, 4, 1, 4)$ and $(3, 6, 1, 5)$.
Its left null space is the [[null space|0PQ2GGY1QV]] of the [[transpose|0W809K6AW0]]
$$A^{\mathsf{T}} = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 0 & 1 & 1 \\ 1 & 4 & 5 \end{pmatrix}.$$

1. Subtract $2$ times row 1 from row 2, and row 1 from row 4; the rows become $(1, 2, 3)$, $(0, 0, 0)$, $(0, 1, 1)$ and $(0, 2, 2)$.
2. Subtract $2$ times row 3 from row 4, and move the zero rows to the bottom; the rows are $(1, 2, 3)$, $(0, 1, 1)$, $(0, 0, 0)$ and $(0, 0, 0)$.
3. Subtract $2$ times row 2 from row 1; the [[reduced row echelon form|0NNR68BFRY]] has the nonzero rows $(1, 0, 1)$ and $(0, 1, 1)$.
4. The free variable is $y_3$, with $y_1 = -y_3$ and $y_2 = -y_3$, so $y_3 = 1$ gives the basis vector $s = (-1, -1, 1)$.
5. Check with the rows of $A^{\mathsf{T}}$:
$$A^{\mathsf{T}} s = (-1 - 2 + 3,\ -2 - 4 + 6,\ 0 - 1 + 1,\ -1 - 4 + 5) = (0, 0, 0, 0).$$
6. So the left null space is the line in $\mathbb{R}^3$ spanned by $(-1, -1, 1)$, of dimension $1 = 3 - 2 = m - \operatorname{rank} A$.
7. In terms of $A$, the equation $s^{\mathsf{T}} A = 0$ says $-(\text{row } 1) - (\text{row } 2) + (\text{row } 3) = 0$, that is, row 3 is the sum of rows 1 and 2.

## Remarks

The example shows the two jobs of the left null space.
It lists the relations among the rows of $A$, and it gives the conditions on a right side.
If $Ax = b$, then $s \cdot b = s^{\mathsf{T}} A x = 0$, so every solvable right side satisfies $-b_1 - b_2 + b_3 = 0$, which is $b_3 = b_1 + b_2$.
This is the equation $w = u + v$ of the [[column space of the same matrix|AGHYPF25CY]], as the [[Fredholm alternative|4HH8C9V8JQ]] predicts.

The rank of $A^{\mathsf{T}}$ is $2$, the same as the rank of $A$, since both reduced forms have two pivots.
If we change the corner entry $5$ of $A$ to $6$, row 3 is no longer the sum of rows 1 and 2, the rank becomes $3$, and the left null space is $\{0\}$.

## Explanations

### L1 human

The left null space lists the ways to combine the rows of $A$ into a row of zeros.
Here row 3 is the sum of rows 1 and 2, so row 1 plus row 2 minus row 3 gives zero.
Up to a multiple, that is the only such combination.

### L2 human

The left null space lives in $\mathbb{R}^3$, the space of the columns, while the null space of $A$ lives in $\mathbb{R}^4$.
Over $\mathbb{R}$ it is the orthogonal complement of the column space.
Its vectors are the coefficients of the equations that a right side $b$ must satisfy for $Ax = b$ to have a solution.
Watch out: to compute it, row reduce $A^{\mathsf{T}}$, not $A$, because the reduced form of $A$ keeps the null space of $A$ and changes the relations among the rows.
