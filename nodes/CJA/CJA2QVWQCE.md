---
tag: CJA2QVWQCE
kind: example
name: Stopping at an echelon form does not give the inverse
msc: ["15A09"]
topics: [P8J6QR66TJ]
audience: ug1
not_instance_of:
  - target: 0Z83DHFMYM
    note: the reduction stops at an echelon form, so the right block is the record E of the operations with EA in echelon form, and E is not the inverse of A
uses: [0Z83DHFMYM, 0VYCDGMJJJ, 0T6MWGZSXA, 032Q9FB8MT]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_elimination
    locator: Finding the inverse of a matrix
---

## Example

If the reduction of $[A \mid I_n]$ stops at an echelon form, the right block is not the inverse.
Take
$$A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}, \qquad A^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$$
over $\mathbb{Q}$.
One operation, $R_2 \to R_2 - \tfrac{1}{2} R_1$, brings the left block to an [[echelon form|0VYCDGMJJJ]]:
$$\left(\begin{array}{cc|cc} 2 & 1 & 1 & 0 \\ 1 & 1 & 0 & 1 \end{array}\right) \to \left(\begin{array}{cc|cc} 2 & 1 & 1 & 0 \\ 0 & \tfrac{1}{2} & -\tfrac{1}{2} & 1 \end{array}\right).$$
The left block $U = \begin{pmatrix} 2 & 1 \\ 0 & \tfrac{1}{2} \end{pmatrix}$ has two pivots, so $A$ is invertible.
But the right block
$$E = \begin{pmatrix} 1 & 0 \\ -\tfrac{1}{2} & 1 \end{pmatrix}$$
is not $A^{-1}$.
Check: it is the record of the one operation, and
$$EA = \begin{pmatrix} 2 & 1 \\ -1 + 1 & -\tfrac{1}{2} + 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 0 & \tfrac{1}{2} \end{pmatrix} = U \ne I_2.$$

To reach the inverse, finish the job.
The operation $R_1 \to R_1 - 2R_2$ changes row 1 to $(2, 0 \mid 2, -2)$, and the scalings $R_1 \to \tfrac{1}{2} R_1$ and $R_2 \to 2R_2$ give
$$\left(\begin{array}{cc|cc} 1 & 0 & 1 & -1 \\ 0 & 1 & -1 & 2 \end{array}\right).$$
Now the right block is $A^{-1}$.

## Remarks

### The general rule

At every stage of the [[reduction of $[A \mid I_n]$|0Z83DHFMYM]], the right block is the product $E$ of the elementary matrices used so far, and the left block is $EA$.
So the right block equals $A^{-1}$ exactly when the left block is $I_n$.
An echelon form is enough to decide invertibility, by counting pivots, but not to read off the inverse.

### The stopped computation is still useful

The equation $EA = U$ gives $A = E^{-1}U$ with
$$E^{-1} = \begin{pmatrix} 1 & 0 \\ \tfrac{1}{2} & 1 \end{pmatrix}.$$
That is a lower triangular matrix times an upper triangular one, an LU factorization of $A$.
Check: $E^{-1}U = \begin{pmatrix} 2 & 1 \\ 1 & \tfrac{1}{2} + \tfrac{1}{2} \end{pmatrix} = A$.
To solve one system $Ax = b$, the echelon form and back substitution are cheaper than the full inverse.

## Explanations

### L1 human

If we stop the row steps too early, the right half is not yet the inverse.
We must continue until the left half is exactly the identity matrix.

### L2 human

The point is that the method of [[computing the inverse by row reduction|0Z83DHFMYM]] has a fixed end: the identity on the left.
A typical use of the stopped form is to solve one system by back substitution.
A trap: two pivots in an echelon form tell you that the inverse exists, which tempts you to read it off too early.
