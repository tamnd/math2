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

Take
$$A = \begin{pmatrix} 1 & 2 \\ 1 & 2 \\ 1 & 2 \end{pmatrix}, \qquad b = \begin{pmatrix} 1 \\ 2 \\ 6 \end{pmatrix}.$$
The second column is twice the first, so the columns are dependent.
We find all least-squares solutions of $Ax = b$, and then the shortest one.

1. Both columns are multiples of $(1, 1, 1)$, so the [[column space|0F0RPPJ2TT]] is the line $\R(1, 1, 1)$.
2. The projection of $b$ onto this line is
$$p = \frac{1 + 2 + 6}{3} (1, 1, 1) = (3, 3, 3).$$
3. The equation $Ax = p$ reads $x_1 + 2x_2 = 3$ in each row, so the least-squares solutions form the line $\{(3 - 2t, t) : t \in \R\}$.
4. The [[null space|0PQ2GGY1QV]] of $A$ is $\R(-2, 1)$, so this line is $(3, 0) + \operatorname{Nul}(A)$, as [[existence and uniqueness|V9AH43ZY91]] predicts.
5. The normal equations give the same line, since
$$A^{\mathsf{T}} A = \begin{pmatrix} 3 & 6 \\ 6 & 12 \end{pmatrix}, \qquad A^{\mathsf{T}} b = \begin{pmatrix} 9 \\ 18 \end{pmatrix},$$
and both rows reduce to $3x_1 + 6x_2 = 9$.
6. The matrix $A^{\mathsf{T}} A$ has determinant $36 - 36 = 0$, so the formula $(A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}} b$ cannot be used.
7. Every least-squares solution gives the same residual $b - p = (-2, -1, 3)$, with $\norm{b - p}^2 = 4 + 1 + 9 = 14$.
8. The row space of $A$ is $\R(1, 2)$, so the solution in the row space has the form $x = s(1, 2)$, and then $x_1 + 2x_2 = 5s = 3$ gives $s = 3/5$.
9. So the shortest least-squares solution is $x = (3/5, 6/5)$, with $\norm{x}^2 = 9/25 + 36/25 = 9/5$.

Check: $(3/5, 6/5) \cdot (-2, 1) = -6/5 + 6/5 = 0$, so this solution is orthogonal to the null space.

## Remarks

The example separates two questions that look alike.
The closest point $p = (3, 3, 3)$ is unique, because it depends only on the column space.
The coefficients $\hat x$ are not unique, because many combinations of two parallel columns give the same vector.

Change one number and the picture changes.
If the second column becomes $(0, 1, 2)$, the columns are independent, $A^{\mathsf{T}} A$ becomes invertible, and the least-squares solution is unique.
The shortest solution $(3/5, 6/5)$ found in step 9 is $A^+ b$ for the [[Moore-Penrose pseudoinverse|0YY8VX28JR]], as the [[minimum-norm solution|QM2Y84VDX8]] theorem describes.

## Explanations

### L1 human

Both columns of $A$ point the same way, so together they only reach one line of vectors.
The point of that line nearest to $b$ is $(3, 3, 3)$, and there is only one such point.
But you can reach it as $3$ times the first column, or as $1.5$ times the second column, or by many other mixtures.
So the best approximation is unique, while the recipe for it is not.

### L2 human

The singular matrix $A^{\mathsf{T}} A$ is the warning sign in this example.
Row reduction of the normal equations still works and gives a whole line of solutions.
There are two standard ways to get one answer: choose the solution of least norm, as in step 9, or drop the dependent column and fit with the first column alone, which gives $x_1 = 3$.
A common mistake is to report "no least-squares solution" when the normal matrix is singular, but a least-squares solution always exists.
