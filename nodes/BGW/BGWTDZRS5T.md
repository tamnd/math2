---
tag: BGWTDZRS5T
kind: example
name: The column space of a square matrix is not its row space
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
not_instance_of:
  - target: 069MCGX635
    note: for the matrix with rows (1, 1) and (0, 0), the column space is the line through (1, 0), but the row space is the line through (1, 1)
uses: [0EP73HK4C4, 0F0RPPJ2TT]
sources:
  - url: https://en.wikipedia.org/wiki/Row_and_column_spaces
    locator: Row space
---

## Example

Let $A = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ over $\R$.

1. The rows are $(1, 1)$ and $(0, 0)$. So the [[row space|0EP73HK4C4]] is the line $\{(t, t) : t \in \R\}$.
2. The columns are $(1, 0)$ and $(1, 0)$. So the [[column space|0F0RPPJ2TT]] is the line $\{(t, 0) : t \in \R\}$.
3. The vector $(1, 0)$ is in the column space. It is not in the row space, since $(t, t) = (1, 0)$ needs $t = 1$ and $t = 0$.
4. So the column space is not the row space, although both are lines in $\R^2$.

Column operations also change the row space.

5. Subtract column 1 from column 2. The result is $B = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$.
6. The row space of $B$ is the line $\{(t, 0)\}$. It differs from the row space $\{(t, t)\}$ of $A$.

## Remarks

- The two spaces have the same dimension, $1$, as the theorem that [[row rank equals column rank|0TZAG60ZYT]] says.
- For a symmetric matrix, the row space and the column space are equal, since the rows are the columns.

## Explanations

### L1 human

The rows and the columns of a square matrix can point in different directions.
So the row space and the column space are in general two different subspaces.

### L2 human

Only their dimensions agree.
Row operations keep the row space and column operations keep the column space, but not the other way round.
