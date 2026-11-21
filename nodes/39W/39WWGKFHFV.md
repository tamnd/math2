---
tag: 39WWGKFHFV
kind: example
name: A triangular system with a zero on the diagonal
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
uses: [0ATFVE08MW, 0N4XY7Z3NN, 0J0BBCMJ5W]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: Forward and back substitution
---

## Example

A zero on the diagonal stops back substitution, and the right side then decides between no solution and infinitely many.
Let $U = \begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix}$ over $\mathbb{R}$.
It is [[upper triangular|0N4XY7Z3NN]], but $u_{22} = 0$, so the formula $x_2 = b_2 / u_{22}$ of [[back substitution|0ATFVE08MW]] fails.

1. Take $b = (2, 1)$. Row 2 reads $0 = 1$, which is false, so the system has no solution.
2. Take $b = (2, 0)$. Row 2 reads $0 = 0$, which gives no condition on $x_2$.
3. In this case column 2 has no [[pivot|0J0BBCMJ5W]], so $x_2$ is a free variable, and we put $x_2 = t$.
4. Row 1 then gives $x_1 = 2 - t$.
5. Check: $(2 - t) + t = 2$ and $0 \cdot (2 - t) + 0 \cdot t = 0$ for every $t$.

So the solution set for $b = (2, 0)$ is $\{(2 - t, t) : t \in \mathbb{R}\}$, a line.

## Remarks

A zero on the diagonal of a triangular matrix means that the matrix is not invertible, since the determinant is the product of the diagonal entries.
Then there is no solution or there are infinitely many, depending on $b$.
Here the two cases are $b_2 \neq 0$ and $b_2 = 0$.

## Explanations

### L1 human

The second equation has no unknown in it.
If its right side is not zero, it is false, and there is no solution.
If its right side is zero, the second unknown can be any number.

### L2 human

1. Look at each diagonal entry before dividing.
2. A zero row with a nonzero right side means no solution.
3. A zero row with a zero right side gives a free variable.
4. Solve the other rows for the pivot variables in terms of the free variables.

This reading applies to any echelon form that is not square or not invertible.
Watch out: in floating point arithmetic, division by $0$ usually gives an infinite or undefined value without an error, so a program should test the diagonal first.
