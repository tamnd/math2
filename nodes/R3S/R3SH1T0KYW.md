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

Let
$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \qquad B = \begin{pmatrix} 0 & 1 \\ -1 & 2 \end{pmatrix}.$$

1. By [[scalar multiplication|0K28YXMS7Q]], $2A = \begin{pmatrix} 2 & 4 \\ 6 & 8 \end{pmatrix}$ and $3B = \begin{pmatrix} 0 & 3 \\ -3 & 6 \end{pmatrix}$.
2. By [[subtraction|0BVXADM10P]] entry by entry, $2A - 3B = \begin{pmatrix} 2 - 0 & 4 - 3 \\ 6 + 3 & 8 - 6 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 9 & 2 \end{pmatrix}$.
3. Check with the rule $(2A - 3B)_{ij} = 2a_{ij} - 3b_{ij}$ at $(2, 1)$: $2 \cdot 3 - 3 \cdot (-1) = 9$.
4. Check commutativity: $A + B = \begin{pmatrix} 1 & 3 \\ 2 & 6 \end{pmatrix} = B + A$.
5. Check distributivity: $2(A + B) = \begin{pmatrix} 2 & 6 \\ 4 & 12 \end{pmatrix} = 2A + 2B$, since $2B = \begin{pmatrix} 0 & 2 \\ -2 & 4 \end{pmatrix}$.

## Remarks

In terms of the [[matrix units|A4HTT7JFD1]], $2A - 3B = 2E_{11} + E_{12} + 9E_{21} + 2E_{22}$.
The same combination of the linear maps $x \mapsto Ax$ and $x \mapsto Bx$ has the matrix $2A - 3B$.

## Explanations

### L1 human

We first multiply each matrix by its number, and then we subtract position by position.
Each entry of the answer uses only the entries of $A$ and $B$ in the same position.

### L2 human

The matrices of one size behave like vectors with four coordinates.
Here the coordinates of $2A - 3B$ are $2(1, 2, 3, 4) - 3(0, 1, -1, 2) = (2, 1, 9, 2)$.
