---
tag: FM9VEAKSA7
kind: example
name: Least squares with dependent columns
msc: [65F20, 15A06]
topics: [8GQVME4SZZ]
audience: ug1
instance_of: [0BYTQ4X1HC]
illustrates: [V9AH43ZY91]
uses: [0W809K6AW0, 0PQ2GGY1QV, 0F0RPPJ2TT]
sources:
  - book: isbn:9780321982384
    locator: Section 6.5
  - url: https://en.wikipedia.org/wiki/Linear_least_squares
    locator: Basic formulation
---

## Example

Let $A = \begin{pmatrix} 1 & 2 \\ 1 & 2 \\ 1 & 2 \end{pmatrix}$ and $b = (1, 2, 6)$.
The second column is twice the first, so the columns are dependent.

1. The [[column space|0F0RPPJ2TT]] is the line $\R(1, 1, 1)$.
2. The projection of $b$ onto it is $p = \frac{1 + 2 + 6}{3} (1, 1, 1) = (3, 3, 3)$.
3. $A x = p$ means $x_1 + 2 x_2 = 3$. So the least-squares solutions form the line $\set{(3 - 2t, t) : t \in \R}$.
4. The [[null space|0PQ2GGY1QV]] of $A$ is $\R(-2, 1)$, and the solution set is $(3, 0) + \R(-2, 1)$, as [[existence and uniqueness|V9AH43ZY91]] predicts.
5. Normal equations: $A^{\mathsf{T}} A = \begin{pmatrix} 3 & 6 \\ 6 & 12 \end{pmatrix}$ has determinant $0$, and $A^{\mathsf{T}} b = (9, 18)$. Both equations reduce to $3 x_1 + 6 x_2 = 9$, the same line.
6. Every least-squares solution gives the same residual $b - p = (-2, -1, 3)$, with $\norm{b - p}^2 = 14$.
7. The solution of least norm is the one in the row space $\R(1, 2)$: $x = s(1, 2)$ with $5s = 3$, so $x = (3/5, 6/5)$, with $\norm{x}^2 = 9/5$.

## Remarks

The closest point $p$ is unique even though $\hat x$ is not.
If the second column is changed to $(0, 1, 2)$, the columns become independent, and the least-squares solution becomes unique.
The vector $(3/5, 6/5)$ is $A^+ b$ for the [[Moore-Penrose pseudoinverse|0YY8VX28JR]], as in the [[minimum-norm solution|QM2Y84VDX8]] theorem.

## Explanations

### L1 human

Both columns of $A$ point the same way, so they reach the same line of vectors.
There are many ways to combine them to get the closest point $(3, 3, 3)$.
So the best approximation is unique, but the recipe for it is not.

### L2 human

Here $A^{\mathsf{T}} A$ is singular, so the formula $(A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}} b$ cannot be used.
Row reduction of the normal equations still works and gives a line of solutions.
The typical fix is to choose the solution of least norm, or to drop a dependent column.
The trap is to report "no least-squares solution" when the normal matrix is singular.
