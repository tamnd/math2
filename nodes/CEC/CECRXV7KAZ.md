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
This is a non-example: $\det_E(v_1, v_2)$ is not defined.

1. The [[definition|0V94H674MB]] needs exactly $\dim V = 3$ vectors.
2. The coordinate matrix of $v_1, v_2$ is $3 \times 2$, and a $3 \times 2$ matrix has no determinant.
3. Check: the area of the square spanned by $v_1, v_2$ is $1$, but $\det_E$ measures $3$-dimensional volume.
4. Adding the vector $v_3 = (0, 0, 1)$ gives $\det_E(v_1, v_2, v_3) = \det I_3 = 1$.
5. Adding $v_3 = (1, 1, 0)$ instead gives $\det_E(v_1, v_2, v_3) = 0$, because $v_3 = v_1 + v_2$.
6. So the value with a third vector depends on that vector, and no value belongs to $v_1, v_2$ alone.

## Remarks

The $2$-dimensional area of $v_1, v_2$ inside $\mathbb{R}^3$ is the square root of the Gram determinant $\det(A^T A)$, with $A$ the $3 \times 2$ matrix.
Here $A^T A = I_2$, so the area is $1$.
This is the case $m < n$ of the [[Cauchy-Binet formula|08WE2W7DYS]], and it is not a determinant in a basis.

## Explanations

### L1 human

A determinant in a basis of $\mathbb{R}^3$ needs three vectors.
With two vectors, the coordinate matrix is not square, so there is no determinant.

### L2 human

Steps 4 and 5 show that a third vector can give the value $1$ or the value $0$.
A trap: do not delete a row of the $3 \times 2$ matrix to make it square; the result depends on the row you delete.
