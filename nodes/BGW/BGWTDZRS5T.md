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

Even when the rows and the columns live in the same space, they can span different subspaces.
Let $A = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ over $\mathbb{R}$.

1. The rows are $(1, 1)$ and $(0, 0)$, so the [[row space|0EP73HK4C4]] is the line $\{(t, t) : t \in \mathbb{R}\}$.
2. The columns are $(1, 0)$ and $(1, 0)$, so the [[column space|0F0RPPJ2TT]] is the line $\{(t, 0) : t \in \mathbb{R}\}$.
3. The vector $(1, 0)$ is in the column space, but it is not in the row space, since $(t, t) = (1, 0)$ would need $t = 1$ and $t = 0$ at once.
4. So the column space is not the row space, although both are lines through the origin in $\mathbb{R}^2$.

Column operations change the row space as well.

5. Subtract column 1 from column 2; the result is $B = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$.
6. The row space of $B$ is the line $\{(t, 0)\}$, which differs from the row space $\{(t, t)\}$ of $A$.

## Remarks

The example shows that only the dimensions of the two spaces are tied together.
Both are lines here, of dimension $1$, as the theorem that [[row rank equals column rank|0TZAG60ZYT]] requires.
The subspaces themselves depend on which side we read the matrix from.

The two spaces do agree in some cases.
For a symmetric matrix, the rows are the columns, so the row space equals the column space.
For an invertible $n \times n$ matrix, both spaces are all of $\mathbb{R}^n$.
If we change the second row of $A$ to $(1, 1)$, the matrix becomes symmetric, and both spaces are the line through $(1, 1)$.

## Explanations

### L1 human

The rows and the columns of a square matrix can point in different directions.
Here every row points along $(1, 1)$, while every column points along $(1, 0)$.
So the row space and the column space are two different lines.

### L2 human

Only their dimensions agree, and that is the content of the rank theorem.
Row operations keep the row space and column operations keep the column space, but not the other way round, as step 6 shows.
Watch out: over $\mathbb{R}$ the row space is orthogonal to the null space, and the column space is orthogonal to the null space of $A^{\mathsf{T}}$, so the two pictures need two different null spaces.
