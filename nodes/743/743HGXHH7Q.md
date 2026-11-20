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

Let $A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{pmatrix}$ over $\mathbb{Q}$.
We [[row reduce|0Z83DHFMYM]] the [[augmented matrix|0T6MWGZSXA]] $[A \mid I_3]$.

1. Start: $\left(\begin{array}{ccc|ccc} 1 & 2 & 3 & 1 & 0 & 0 \\ 0 & 1 & 4 & 0 & 1 & 0 \\ 5 & 6 & 0 & 0 & 0 & 1 \end{array}\right)$.
2. $R_3 \to R_3 - 5R_1$: row 3 becomes $(0, -4, -15 \mid -5, 0, 1)$.
3. $R_3 \to R_3 + 4R_2$: row 3 becomes $(0, 0, 1 \mid -5, 4, 1)$. The left block is now upper triangular with pivots $1, 1, 1$, so $A$ is invertible.
4. $R_2 \to R_2 - 4R_3$: row 2 becomes $(0, 1, 0 \mid 20, -15, -4)$.
5. $R_1 \to R_1 - 3R_3$: row 1 becomes $(1, 2, 0 \mid 16, -12, -3)$.
6. $R_1 \to R_1 - 2R_2$: row 1 becomes $(1, 0, 0 \mid -24, 18, 5)$.
7. Result: $\left(\begin{array}{ccc|ccc} 1 & 0 & 0 & -24 & 18 & 5 \\ 0 & 1 & 0 & 20 & -15 & -4 \\ 0 & 0 & 1 & -5 & 4 & 1 \end{array}\right)$, so $A^{-1} = \begin{pmatrix} -24 & 18 & 5 \\ 20 & -15 & -4 \\ -5 & 4 & 1 \end{pmatrix}$.
8. Check row 1 of $AA^{-1}$: $(1, 2, 3)$ times the three columns of $A^{-1}$ gives $-24 + 40 - 15 = 1$, $18 - 30 + 12 = 0$ and $5 - 8 + 3 = 0$.
9. Check row 2: $(0, 1, 4)$ gives $20 - 20 = 0$, $-15 + 16 = 1$ and $-4 + 4 = 0$.
10. Check row 3: $(5, 6, 0)$ gives $-120 + 120 = 0$, $90 - 90 = 0$ and $25 - 24 = 1$.
11. So $AA^{-1} = I_3$. For a square matrix this one product is enough, and a direct computation of $A^{-1}A$ also gives $I_3$.

## Remarks

The determinant of $A$ is $1$.
Row replacements do not change the determinant, and the triangular left block of step 3 has determinant $1 \cdot 1 \cdot 1 = 1$.
A direct expansion agrees: $\det A = 1(0 - 24) - 2(0 - 20) + 3(0 - 5) = 1$.
So the inverse has integer entries, as the [[inverse via the adjugate|0ENVM493VK]] predicts for an integer matrix with determinant $1$.

## Explanations

### L1 human

We put the identity matrix to the right of $A$ and use row steps until the left part is the identity.
The right part is then the inverse, and we check it by multiplying.

### L2 human

The first phase (steps 2 and 3) clears below the pivots, and the last phase (steps 4 to 6) clears above them.
No scaling was needed, because all pivots were already $1$.
A trap: in step 3, the operation uses the new row 2 and the new row 3, not the rows of the original matrix.
