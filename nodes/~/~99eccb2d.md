---
tag: ~99eccb2d
kind: example
name: Row reduction detects a singular 3 × 3 matrix
msc: ["15A09"]
topics: [P8J6QR66TJ]
audience: ug1
instance_of: [0Z83DHFMYM]
not_instance_of:
  - target: 0EB9N0S33C
    note: row reduction of [A | I] produces a zero row in the left block, and the row vector (1, -2, 1) satisfies (1, -2, 1)A = 0
uses: [0Z83DHFMYM, 0T6MWGZSXA, 032Q9FB8MT]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_elimination
    locator: Finding the inverse of a matrix
  - book: isbn:9780321982384
    locator: Section 2.2
---

## Example

Let $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$ over $\mathbb{Q}$.
We [[row reduce|0Z83DHFMYM]] the [[augmented matrix|0T6MWGZSXA]] $[A \mid I_3]$.

1. Start: $\left(\begin{array}{ccc|ccc} 1 & 2 & 3 & 1 & 0 & 0 \\ 4 & 5 & 6 & 0 & 1 & 0 \\ 7 & 8 & 9 & 0 & 0 & 1 \end{array}\right)$.
2. $R_2 \to R_2 - 4R_1$: row 2 becomes $(0, -3, -6 \mid -4, 1, 0)$.
3. $R_3 \to R_3 - 7R_1$: row 3 becomes $(0, -6, -12 \mid -7, 0, 1)$.
4. $R_3 \to R_3 - 2R_2$: row 3 becomes $(0, 0, 0 \mid 1, -2, 1)$.
5. The left block has a zero row, so its reduced row echelon form is not $I_3$, and $A$ is singular.
6. The right block is the product $E$ of the elementary matrices used, and the left block is $EA$. So row 3 of $EA$ is $(1, -2, 1)A$, which is $0$.
7. Check: $(1, -2, 1)A = (1 - 8 + 7, \; 2 - 10 + 8, \; 3 - 12 + 9) = (0, 0, 0)$.
8. If $AB = I_3$ for some $B$, then $(1, -2, 1) = (1, -2, 1)AB = 0 \cdot B = 0$, which is false. So $A$ has no right inverse, and $A$ is not invertible.

## Remarks

Here $(1, -2, 1)^{\mathsf{T}}$ also solves $Ax = 0$, since $A(1, -2, 1)^{\mathsf{T}} = (1 - 4 + 3, \; 4 - 10 + 6, \; 7 - 16 + 9)^{\mathsf{T}} = 0$.
This is a coincidence of this matrix: in general a vector $y$ with $yA = 0$ and a vector $x$ with $Ax = 0$ are different.
A zero row in the left block always means that the matrix is singular, by [[invertibility and row reduction|1ZK55FS2BF]].

## Explanations

### L1 human

When we row reduce, a full row of zeros appears on the left.
This means that one row of $A$ is a combination of the others, and then $A$ has no inverse.

### L2 human

The point of the example is that the method needs no separate test for singularity: the zero row shows up on its own.
The right block of the zero row is useful: it gives a combination of the rows of $A$ that is zero, here $R_1 - 2R_2 + R_3 = 0$.
A trap: none of the entries of $A$ is $0$, and the matrix still is singular.
