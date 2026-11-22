---
tag: CECRXV7KAZ
kind: example
name: Two vectors in R³ have no determinant in a basis
msc: [15A15, 15A75]
topics: [DTBK11SR77]
audience: ug2
not_instance_of:
  - target: 05CJSSXPR3
    note: two vectors in R^3 have a 3 × 2 coordinate matrix, so they have no determinant in a basis of R^3
uses: [0V94H674MB]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Determinant of n vectors
---

## Example

Let $V = \mathbb{R}^3$ with the standard basis $E$, and let $v_1 = (1, 0, 0)$ and $v_2 = (0, 1, 0)$.
The expression $\det_E(v_1, v_2)$ is not defined, and we check which condition fails.

1. The [[definition|0V94H674MB]] needs exactly $\dim V = 3$ vectors, and we have $2$.
2. The coordinate matrix of $v_1, v_2$ has $3$ rows and $2$ columns:
$$\begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix}.$$
   A $3 \times 2$ matrix has no determinant.
3. Could a third vector fix this?
   With $v_3 = (0, 0, 1)$ the matrix becomes $I_3$, and $\det_E(v_1, v_2, v_3) = 1$.
4. With $v_3 = (1, 1, 0) = v_1 + v_2$ instead, the three vectors are dependent, and $\det_E(v_1, v_2, v_3) = 0$.
5. So the value with a third vector depends on that vector, and no value belongs to $v_1, v_2$ alone.

## Remarks

The two vectors do span a unit square, so they have an area, but it is a $2$-dimensional measurement inside a $3$-dimensional space, and $\det_E$ measures $3$-dimensional volume.
That area comes from the Gram determinant.
Let $A$ be the $3 \times 2$ matrix above, so that $A^{\mathsf{T}} A$ is the $2 \times 2$ matrix of dot products $v_i \cdot v_j$.
Here $A^{\mathsf{T}} A = I_2$, and the area is $\sqrt{\det(A^{\mathsf{T}} A)} = 1$.
The [[Cauchy-Binet formula|08WE2W7DYS]] writes $\det(A^{\mathsf{T}} A)$ as the sum of the squares of the three $2 \times 2$ minors of $A$, here $1^2 + 0^2 + 0^2 = 1$.
None of this is a determinant of the pair in a basis of $\mathbb{R}^3$.

## Explanations

### L1 human

A determinant in a basis of space needs three vectors.
With two vectors, the coordinate matrix is not square, so there is no determinant.
Two arrows in space make a flat parallelogram, and a flat shape has no volume to measure.

### L2 human

Steps 3 and 4 show that a third vector can give the value $1$ or the value $0$, so the pair alone fixes no number.
Watch out: do not delete a row of the $3 \times 2$ matrix to make it square.
For the vectors $(1, 0, 1)$ and $(0, 1, 1)$, deleting the third row gives determinant $1$, while deleting the first row gives $\det \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix} = -1$, so the answer depends on the row you delete.
