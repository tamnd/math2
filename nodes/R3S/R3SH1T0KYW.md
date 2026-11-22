---
tag: R3SH1T0KYW
kind: example
name: The linear combination 2A − 3B of two 2 × 2 matrices
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
instance_of: [0Y7H3SAVA1]
uses: [0BVXADM10P, 0K28YXMS7Q]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_addition
    locator: Entrywise sum
---

## Example

A linear combination of matrices is computed in two passes: scale each matrix, then add position by position.
Let
$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \qquad B = \begin{pmatrix} 0 & 1 \\ -1 & 2 \end{pmatrix}.$$

1. By [[scalar multiplication|0K28YXMS7Q]], every entry is multiplied by the scalar:
$$2A = \begin{pmatrix} 2 & 4 \\ 6 & 8 \end{pmatrix}, \qquad 3B = \begin{pmatrix} 0 & 3 \\ -3 & 6 \end{pmatrix}.$$
2. By [[subtraction|0BVXADM10P]] entry by entry,
$$2A - 3B = \begin{pmatrix} 2 - 0 & 4 - 3 \\ 6 + 3 & 8 - 6 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 9 & 2 \end{pmatrix}.$$
3. Check with the rule $(2A - 3B)_{ij} = 2a_{ij} - 3b_{ij}$ at $(2, 1)$: $2 \cdot 3 - 3 \cdot (-1) = 6 + 3 = 9$.
4. Check commutativity: both orders give the same sum,
$$A + B = \begin{pmatrix} 1 & 3 \\ 2 & 6 \end{pmatrix} = B + A.$$
5. Check distributivity: with $2B = \begin{pmatrix} 0 & 2 \\ -2 & 4 \end{pmatrix}$,
$$2A + 2B = \begin{pmatrix} 2 & 6 \\ 4 & 12 \end{pmatrix} = 2(A + B).$$

## Remarks

In terms of the [[matrix units|A4HTT7JFD1]], the result is $2A - 3B = 2E_{11} + E_{12} + 9E_{21} + 2E_{22}$.
The same combination of the linear maps $x \mapsto Ax$ and $x \mapsto Bx$ has the matrix $2A - 3B$, since $2Ax - 3Bx = (2A - 3B)x$.

Which scalar goes with which matrix matters, while the order of the terms does not.
Swapping the scalars gives
$$3A - 2B = \begin{pmatrix} 3 & 4 \\ 11 & 8 \end{pmatrix},$$
which differs from $2A - 3B$, while $-3B + 2A$ is the same matrix as $2A - 3B$ by commutativity.

## Explanations

### L1 human

We first multiply each matrix by its number, and then we subtract position by position.
Each entry of the answer uses only the entries of $A$ and $B$ in the same position.
For the top left entry this is $2 \cdot 1 - 3 \cdot 0 = 2$.

### L2 human

The matrices of one size behave like vectors with four coordinates.
Listing the entries row by row, the coordinates of $2A - 3B$ are
$$2(1, 2, 3, 4) - 3(0, 1, -1, 2) = (2, 1, 9, 2).$$
The typical use is to combine linear maps of the same shape, and the trap is to forget the sign on the second term, which would give $2A + 3B$ instead.
