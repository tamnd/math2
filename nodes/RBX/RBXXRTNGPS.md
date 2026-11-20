---
tag: RBXXRTNGPS
kind: example
name: Row reduction shows that a matrix is not invertible
msc: ["15A06", "15A09"]
topics: [DXSXFVDMXQ]
audience: school
not_instance_of:
  - target: 0EB9N0S33C
    note: The row reduction of [A | I] gives a zero row in the left block, so A has no inverse
uses: [098D6FQN3N, 0Z83DHFMYM, 0EB9N0S33C]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_elimination
    locator: Finding the inverse of a matrix
---

## Example

Let $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$ over $\R$.
We try to invert it by [[Gauss-Jordan elimination|098D6FQN3N]] on $[A \mid I]$.

1. The start is $\left[\begin{array}{rr|rr} 1 & 2 & 1 & 0 \\ 2 & 4 & 0 & 1 \end{array}\right]$.
2. $R_2 \leftarrow R_2 - 2R_1$ gives $(0, 0 \mid -2, 1)$.
3. The left block now has the zero row $(0, 0)$, so its RREF $\begin{bmatrix} 1 & 2 \\ 0 & 0 \end{bmatrix}$ is not $I$.
4. So $A$ is not [[invertible|0EB9N0S33C]].
5. Check: $\det A = 1 \cdot 4 - 2 \cdot 2 = 0$, and $A(2, -1) = (0, 0)$ with $(2, -1) \neq 0$.

## Remarks

The row $(0, 0 \mid -2, 1)$ says that $-2 \cdot (\text{row } 1) + (\text{row } 2) = 0$ for the rows of $A$.
The system $Ax = e_1$ has no solution, because its reduced augmented matrix has the row $(0, 0 \mid -2)$.

## Explanations

### L1 human

The second row of $A$ is twice the first row.
Row reduction makes the second row zero, so we cannot reach the identity matrix.
So $A$ has no inverse.

### L2 human

1. Reduce $[A \mid I]$ as usual.
2. If a zero row appears in the left block, stop.
3. The matrix is not invertible.
4. Confirm with a nonzero vector $x$ with $Ax = 0$.

The typical use is to test invertibility and to compute the inverse in one process.
A trap: the right block is not zero in that row, so the zero row is easy to miss if we look only at the whole row.
