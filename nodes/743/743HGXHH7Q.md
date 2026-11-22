---
tag: 743HGXHH7Q
kind: example
name: Inverting a 3 × 3 matrix by row reduction
msc: ["15A09"]
topics: [P8J6QR66TJ]
audience: ug1
instance_of: [0Z83DHFMYM, 0EB9N0S33C]
uses: [0Z83DHFMYM, 0T6MWGZSXA, 098D6FQN3N, 032Q9FB8MT]
sources:
  - book: isbn:9780321982384
    locator: Section 2.2
  - url: https://en.wikipedia.org/wiki/Gaussian_elimination
    locator: Finding the inverse of a matrix
---

## Example

The $3 \times 3$ matrix
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{pmatrix}$$
over $\mathbb{Q}$ is invertible, and [[row reduction|0Z83DHFMYM]] of the [[augmented matrix|0T6MWGZSXA]] $[A \mid I_3]$ finds its inverse in five operations.

The first phase clears below the pivots.
The operation $R_3 \to R_3 - 5R_1$ and then $R_3 \to R_3 + 4R_2$ give
$$\left(\begin{array}{ccc|ccc} 1 & 2 & 3 & 1 & 0 & 0 \\ 0 & 1 & 4 & 0 & 1 & 0 \\ 5 & 6 & 0 & 0 & 0 & 1 \end{array}\right) \to \left(\begin{array}{ccc|ccc} 1 & 2 & 3 & 1 & 0 & 0 \\ 0 & 1 & 4 & 0 & 1 & 0 \\ 0 & -4 & -15 & -5 & 0 & 1 \end{array}\right) \to \left(\begin{array}{ccc|ccc} 1 & 2 & 3 & 1 & 0 & 0 \\ 0 & 1 & 4 & 0 & 1 & 0 \\ 0 & 0 & 1 & -5 & 4 & 1 \end{array}\right).$$
In the last step, $-15 + 4 \cdot 4 = 1$.
The left block is now upper triangular with pivots $1, 1, 1$, so $A$ is invertible, and no scaling is needed.

The last phase clears above the pivots, from right to left.
The operations $R_2 \to R_2 - 4R_3$, $R_1 \to R_1 - 3R_3$ and $R_1 \to R_1 - 2R_2$ give
$$\left(\begin{array}{ccc|ccc} 1 & 2 & 0 & 16 & -12 & -3 \\ 0 & 1 & 0 & 20 & -15 & -4 \\ 0 & 0 & 1 & -5 & 4 & 1 \end{array}\right) \to \left(\begin{array}{ccc|ccc} 1 & 0 & 0 & -24 & 18 & 5 \\ 0 & 1 & 0 & 20 & -15 & -4 \\ 0 & 0 & 1 & -5 & 4 & 1 \end{array}\right).$$
For example, the new row 2 is $(0, 1, 4 \mid 0, 1, 0) - 4(0, 0, 1 \mid -5, 4, 1) = (0, 1, 0 \mid 20, -15, -4)$.
So
$$A^{-1} = \begin{pmatrix} -24 & 18 & 5 \\ 20 & -15 & -4 \\ -5 & 4 & 1 \end{pmatrix}.$$

Check, row by row of $AA^{-1}$:
$$\begin{aligned} (1, 2, 3)&: \quad -24 + 40 - 15 = 1, \quad 18 - 30 + 12 = 0, \quad 5 - 8 + 3 = 0, \\ (0, 1, 4)&: \quad 20 - 20 = 0, \quad -15 + 16 = 1, \quad -4 + 4 = 0, \\ (5, 6, 0)&: \quad -120 + 120 = 0, \quad 90 - 90 = 0, \quad 25 - 24 = 1. \end{aligned}$$
So $AA^{-1} = I_3$, and for a square matrix this one product is enough.

## Remarks

### Why the entries are integers

The inverse of an integer matrix usually has fractions, and here it does not.
The reason is that $\det A = 1$.
Row replacements do not change the determinant, and the triangular left block after the first phase has determinant $1 \cdot 1 \cdot 1 = 1$.
A cofactor expansion along the first row agrees:
$$\det A = 1(0 - 24) - 2(0 - 20) + 3(0 - 5) = -24 + 40 - 15 = 1.$$
By the [[inverse via the adjugate|0ENVM493VK]], $A^{-1}$ is the adjugate divided by $\det A$, and the adjugate of an integer matrix has integer entries.

### What changes for a nearby matrix

If the entry $0$ in the corner is replaced by $1$, the first phase ends with the pivot $1 - 15 + 16 = 2$ in place of $1$.
The matrix is still invertible, the second phase must now scale row 3 by $\tfrac{1}{2}$, and the new inverse has fractions, since its determinant is $2$.

## Explanations

### L1 human

We put the identity matrix to the right of $A$ and use row steps until the left part is the identity.
The right part is then the inverse, and we check it by multiplying.
Here all the pivots were already $1$, so we never had to divide.

### L2 human

The computation shows the order of work: clear below the pivots from left to right, then clear above them from right to left.
Clearing above from right to left means that each clearing step uses a row whose left part is already a unit vector, so it cannot spoil the zeros made before.
A trap: the operation $R_3 \to R_3 + 4R_2$ uses the current rows 2 and 3, and the current row 3 is $(0, -4, -15 \mid -5, 0, 1)$, not the original one.
