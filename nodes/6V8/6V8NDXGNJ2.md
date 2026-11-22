---
tag: 6V8NDXGNJ2
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

The matrix
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$$
over $\mathbb{Q}$ is singular, and [[row reduction|0Z83DHFMYM]] of the [[augmented matrix|0T6MWGZSXA]] $[A \mid I_3]$ shows this in three operations.

The operations $R_2 \to R_2 - 4R_1$ and $R_3 \to R_3 - 7R_1$ clear the first column:
$$\left(\begin{array}{ccc|ccc} 1 & 2 & 3 & 1 & 0 & 0 \\ 4 & 5 & 6 & 0 & 1 & 0 \\ 7 & 8 & 9 & 0 & 0 & 1 \end{array}\right) \to \left(\begin{array}{ccc|ccc} 1 & 2 & 3 & 1 & 0 & 0 \\ 0 & -3 & -6 & -4 & 1 & 0 \\ 0 & -6 & -12 & -7 & 0 & 1 \end{array}\right).$$
Then $R_3 \to R_3 - 2R_2$ gives
$$\left(\begin{array}{ccc|ccc} 1 & 2 & 3 & 1 & 0 & 0 \\ 0 & -3 & -6 & -4 & 1 & 0 \\ 0 & 0 & 0 & 1 & -2 & 1 \end{array}\right),$$
since $-7 - 2(-4) = 1$, $0 - 2 \cdot 1 = -2$ and $1 - 0 = 1$.
The left block has a zero row, so the reduced row echelon form of $A$ is not $I_3$, and $A$ is singular.

The right block tells us more.
It is the product $E$ of the operations used, and the left block is $EA$, so the zero row says $(1, -2, 1)A = 0$.
Check:
$$(1, -2, 1)A = (1 - 8 + 7, \; 2 - 10 + 8, \; 3 - 12 + 9) = (0, 0, 0).$$
This vector also proves directly that $A$ has no inverse.
If $AB = I_3$ for some $B$, then
$$(1, -2, 1) = (1, -2, 1)AB = 0 \cdot B = 0,$$
which is false.

## Remarks

### Rows and columns

The relation $(1, -2, 1)A = 0$ says that row 1 minus twice row 2 plus row 3 of $A$ is zero, a dependence among the rows.
Here the column vector $(1, -2, 1)^{\mathsf{T}}$ also solves $Ax = 0$, since
$$A \begin{pmatrix} 1 \\ -2 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 - 4 + 3 \\ 4 - 10 + 6 \\ 7 - 16 + 9 \end{pmatrix} = 0.$$
That is special to this matrix, whose rows and columns are both arithmetic progressions.
For a general singular matrix, a vector $y$ with $yA = 0$ and a vector $x$ with $Ax = 0$ are different.

### No zero entries needed

None of the entries of $A$ is $0$, and no row is a multiple of another, yet $A$ is singular.
A zero row in the left block always means that $A$ is singular, by [[invertibility and row reduction|1ZK55FS2BF]], and elimination is how the hidden dependence comes to light.

## Explanations

### L1 human

When we row reduce, a full row of zeros appears on the left.
This means that one row of $A$ is a combination of the others, and then $A$ has no inverse.
Here row 1 plus row 3 equals twice row 2.

### L2 human

The point of the example is that the method needs no separate test for singularity: the zero row shows up on its own.
The right part of that zero row is useful, because it lists the coefficients of the dependence, here $R_1 - 2R_2 + R_3 = 0$.
A trap: you might expect a singular matrix to have zero entries or equal rows, and this one has neither.
