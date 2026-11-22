---
tag: M3YVJ6CFJ5
kind: example
name: Cholesky decomposition of a 3 × 3 matrix
msc: [15A23, 15B57]
topics: [SS4EVPKT3A]
audience: ug1
instance_of: [0KX66CZMBB]
illustrates: [0WKG8CYY6A, 0WKEF78PMV]
uses: [0EZSD6T9E0, 0QQCG3JWJ4]
sources:
  - url: https://en.wikipedia.org/wiki/Cholesky_decomposition
    locator: Example
---

## Example

Let
$$A = \begin{pmatrix} 4 & 2 & -2 \\ 2 & 10 & 2 \\ -2 & 2 & 6 \end{pmatrix}.$$
The matrix is real and symmetric.
We find the [[lower triangular|0EZSD6T9E0]] matrix $L = (l_{ij})$ with a positive diagonal and $A = L L^{\mathsf{T}}$, one column at a time, with the formulas of the [[Cholesky decomposition|0WKG8CYY6A]].

1. Column 1. The corner gives $l_{11} = \sqrt{a_{11}} = \sqrt 4 = 2$. Below it, $l_{21} = a_{21} / l_{11} = 2/2 = 1$ and $l_{31} = a_{31} / l_{11} = -2/2 = -1$.
2. Column 2. The diagonal entry subtracts the square already used in row 2, so $l_{22} = \sqrt{a_{22} - l_{21}^2} = \sqrt{10 - 1} = 3$. Below it, $l_{32} = (a_{32} - l_{31} l_{21}) / l_{22} = (2 - (-1)(1))/3 = 1$.
3. Column 3. The last entry is $l_{33} = \sqrt{a_{33} - l_{31}^2 - l_{32}^2} = \sqrt{6 - 1 - 1} = 2$.
4. The factor is
$$L = \begin{pmatrix} 2 & 0 & 0 \\ 1 & 3 & 0 \\ -1 & 1 & 2 \end{pmatrix}.$$
5. Multiply back. Entry $(i, j)$ of $L L^{\mathsf{T}}$ is the dot product of rows $i$ and $j$ of $L$. Row 1 of the product is $(2 \cdot 2,\ 2 \cdot 1,\ 2 \cdot (-1)) = (4, 2, -2)$.
6. Row 2 is $(1 \cdot 2,\ 1 \cdot 1 + 3 \cdot 3,\ 1 \cdot (-1) + 3 \cdot 1) = (2, 10, 2)$.
7. Row 3 is $((-1) \cdot 2,\ (-1) \cdot 1 + 1 \cdot 3,\ (-1)^2 + 1^2 + 2^2) = (-2, 2, 6)$.
8. So $L L^{\mathsf{T}} = A$. Each number under a square root in steps 1 to 3 was positive, so $A$ is [[positive definite|0QQCG3JWJ4]] by the converse part of the theorem.

## Remarks

The diagonal of $L$ also gives the leading principal minors of $A$.
The leading $k \times k$ block of $A$ is the product of the leading $k \times k$ blocks of $L$ and $L^{\mathsf{T}}$, so its determinant is $(l_{11} \cdots l_{kk})^2$:
$$\Delta_1 = 2^2 = 4, \qquad \Delta_2 = (2 \cdot 3)^2 = 36, \qquad \Delta_3 = (2 \cdot 3 \cdot 2)^2 = 144.$$
Check: $\Delta_2 = 4 \cdot 10 - 2 \cdot 2 = 36$, and the cofactor expansion of $\det A$ along the first row gives $4 \cdot 56 - 2 \cdot 16 - 2 \cdot 24 = 144$.
All three minors are positive, so [[Sylvester's criterion|0WKEF78PMV]] gives the same verdict, and the ratios $4$, $36/4 = 9$ and $144/36 = 4$ are the squares $l_{11}^2$, $l_{22}^2$ and $l_{33}^2$.

The factor solves systems quickly.
For $b = (4, 14, 6)$, forward substitution in $Ly = b$ gives $y_1 = 2$, then $2 + 3 y_2 = 14$ so $y_2 = 4$, then $-2 + 4 + 2 y_3 = 6$ so $y_3 = 2$.
Back substitution in $L^{\mathsf{T}} x = (2, 4, 2)$ gives $x_3 = 1$, then $3 x_2 + 1 = 4$ so $x_2 = 1$, then $2 x_1 + 1 - 1 = 2$ so $x_1 = 1$.
Check: the row sums of $A$ are $4$, $14$ and $6$, so $A(1, 1, 1) = b$.

If we change the corner $a_{33} = 6$ to $2$, steps 1 and 2 do not change, and step 3 needs $\sqrt{2 - 1 - 1} = 0$.
The new matrix is semidefinite but not definite, and it has no factor with a positive diagonal.
With $a_{33} = 1$ the number under the root is $-1$, and the matrix is not even semidefinite.

## Explanations

### L1 human

We write the matrix as a lower triangular matrix times its transpose.
The entries come one at a time, starting at the top left corner.
Each diagonal entry is a square root, and each entry below it is one division.
Multiplying the two triangles back together gives the matrix we started with.

### L2 human

The algorithm reads only the lower half of $A$, and it fills $L$ column by column.
At each diagonal step it takes the square root of $a_{jj}$ minus the squares already used in row $j$.
If that number is not positive, the matrix is not positive definite, and the algorithm stops.
Watch out for the correction terms.
In step 2 the product $l_{31} l_{21} = -1$ must be subtracted from $a_{32} = 2$, and if you forget it you get $l_{32} = 2/3$, and the product no longer equals $A$.
