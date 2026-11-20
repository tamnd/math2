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

Let $A = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ over $\R$.

1. $A(x, y) = (x + y, 0)$. So the [[null space|0PQ2GGY1QV]] of $A$ is the line $x + y = 0$, spanned by $(1, -1)$.
2. The [[transpose|0W809K6AW0]] is $A^\top = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$, and $A^\top(x, y) = (x, x)$.
3. So the null space of $A^\top$ is the line $x = 0$, spanned by $(0, 1)$.
4. The vector $(1, -1)$ is not in the null space of $A^\top$, since $A^\top(1, -1) = (1, 1) \ne 0$.
5. So the left null space of $A$ is not the null space of $A$, although both are lines in $\R^2$.

The solution set of a system with a nonzero right side is not a null space either.

6. The set $\{x : Ax = (1, 0)\}$ is the line $x + y = 1$. It does not contain $(0, 0)$, so it is not a subspace.

## Remarks

- The two null spaces have the same dimension here because $A$ is square. For an $m \times n$ matrix of rank $r$, they have dimensions $n - r$ and $m - r$.
- For a symmetric matrix, $A^\top = A$, so the two null spaces agree.

## Explanations

### L1 human

The null space of $A$ and the null space of its transpose are different spaces in general.
One describes relations among the columns, the other relations among the rows.

### L2 human

$\operatorname{Null}(A)$ is orthogonal to the rows of $A$, and $\operatorname{Null}(A^\top)$ is orthogonal to the columns of $A$.
Here the row is $(1, 1)$ and the column is $(1, 0)$, so the two null spaces are the lines orthogonal to these.
