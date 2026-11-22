---
tag: GS2PYPBGGJ
kind: example
name: The left null space is not the null space
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
not_instance_of:
  - target: 0PHDYNR24D
    note: for the matrix with rows (1, 1) and (0, 0), the null space of the transpose is the line through (0, 1), which is not the null space, the line through (1, -1)
uses: [0PQ2GGY1QV, 0W809K6AW0]
sources:
  - url: https://en.wikipedia.org/wiki/Row_and_column_spaces
    locator: Relation to the left null space
---

## Example

A matrix and its transpose can have different null spaces, even when the matrix is square.
Let $A = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ over $\mathbb{R}$.

1. We have $A(x, y) = (x + y, 0)$, so the [[null space|0PQ2GGY1QV]] of $A$ is the line $x + y = 0$, spanned by $(1, -1)$.
2. The [[transpose|0W809K6AW0]] is $A^{\mathsf{T}} = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$, and $A^{\mathsf{T}}(x, y) = (x, x)$.
3. So the null space of $A^{\mathsf{T}}$, the left null space of $A$, is the line $x = 0$, spanned by $(0, 1)$.
4. The vector $(1, -1)$ is not in the left null space, since $A^{\mathsf{T}}(1, -1) = (1, 1) \ne 0$.
5. So the left null space of $A$ is not its null space, although both are lines in $\mathbb{R}^2$.

The solution set of a system with a nonzero right side is not a null space either.

6. The set $\{x : Ax = (1, 0)\}$ is the line $x + y = 1$, and it does not contain $(0, 0)$, so it is not a subspace.

## Remarks

The example shows that the two null spaces answer different questions.
The null space of $A$ is orthogonal to the rows of $A$, here to $(1, 1)$, so it is the line through $(1, -1)$.
The left null space is orthogonal to the columns of $A$, here to $(1, 0)$, so it is the line through $(0, 1)$.

The two lines have the same dimension only because $A$ is square.
For an $m \times n$ matrix of rank $r$, the null space has dimension $n - r$ and the left null space has dimension $m - r$, so for the $1 \times 2$ matrix $\begin{pmatrix} 1 & 1 \end{pmatrix}$ they are a line in $\mathbb{R}^2$ and the zero subspace of $\mathbb{R}^1$.
For a symmetric matrix, $A^{\mathsf{T}} = A$, so the two null spaces agree; if we change the second row of $A$ to $(1, 1)$, both become the line through $(1, -1)$.

## Explanations

### L1 human

The null space of $A$ and the null space of its transpose are different spaces in general.
One lists the relations among the columns, and the other lists the relations among the rows.
Here the two columns are equal, which gives the relation $(1, -1)$, while the second row is zero, which gives the relation $(0, 1)$.

### L2 human

To find the left null space, solve $A^{\mathsf{T}} y = 0$, or equivalently $y^{\mathsf{T}} A = 0$.
Here $y^{\mathsf{T}} A = (y_1, y_1)$, so the condition is $y_1 = 0$, and $y_2$ is free.
Watch out: writing $yA$ with $y$ as a column has no meaning for a $2 \times 2$ matrix, so keep the transpose in the notation.
