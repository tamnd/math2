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

Let $A$ be the $3 \times 4$ matrix with rows $(1, 2, 0, 1)$, $(2, 4, 1, 4)$ and $(3, 6, 1, 5)$.
The left null space of $A$ is the [[null space|0PQ2GGY1QV]] of the [[transpose|0W809K6AW0]]
$$A^\top = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 0 & 1 & 1 \\ 1 & 4 & 5 \end{pmatrix}.$$

1. Subtract $2$ times row 1 from row 2, and row 1 from row 4. The rows become $(1, 2, 3)$, $(0, 0, 0)$, $(0, 1, 1)$, $(0, 2, 2)$.
2. Subtract $2$ times row 3 from row 4, and move the zero row down. The rows are $(1, 2, 3)$, $(0, 1, 1)$, $(0, 0, 0)$, $(0, 0, 0)$.
3. Subtract $2$ times row 2 from row 1. The [[reduced row echelon form|0NNR68BFRY]] has the nonzero rows $(1, 0, 1)$ and $(0, 1, 1)$.
4. The free variable is $y_3$, and $y_1 = -y_3$, $y_2 = -y_3$. With $y_3 = 1$ this gives the basis vector $s = (-1, -1, 1)$.
5. Check $A^\top s = (-1 - 2 + 3,\ -2 - 4 + 6,\ 0 - 1 + 1,\ -1 - 4 + 5) = (0, 0, 0, 0)$.
6. So the left null space is the line spanned by $(-1, -1, 1)$, of dimension $1 = 3 - 2 = m - \rank A$.
7. In terms of $A$: $s^\top A = 0$ says $-(\text{row } 1) - (\text{row } 2) + (\text{row } 3) = 0$, that is, row 3 is the sum of rows 1 and 2.

## Remarks

- Each vector of the left null space gives a condition for $Ax = b$ to be solvable: $s \cdot b = 0$. Here this is $b_3 = b_1 + b_2$, the equation of the column space.
- The rank of $A^\top$ is $2$, the same as the rank of $A$.

## Explanations

### L1 human

The left null space lists the ways to combine the rows of $A$ into the zero row.
Here row 3 is the sum of rows 1 and 2, and that is the only relation up to a multiple.

### L2 human

The left null space lives in $\R^3$, the space of the columns, while the null space lives in $\R^4$.
Over $\R$ it is the orthogonal complement of the column space.
Its vectors give the equations that a right side $b$ must satisfy for $Ax = b$ to have a solution.
