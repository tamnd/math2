---
tag: KZ1G2TB2Q3
kind: example
name: Solving two systems with the same coefficient matrix at once
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: ug1
instance_of: [0T6MWGZSXA]
uses: [0YCDZ7N8VD, 04XWH28452]
sources:
  - url: https://en.wikipedia.org/wiki/Augmented_matrix
    locator: lead section
---

## Example

Two systems with the same left sides need only one round of elimination.
We solve $Ax = b$ and $Ax = c$ over $\mathbb{R}$ for
$$A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \qquad b = \begin{pmatrix} 5 \\ 6 \end{pmatrix}, \qquad c = \begin{pmatrix} 1 \\ 0 \end{pmatrix}.$$

1. Put both right sides behind the bar of the [[augmented matrix|0YCDZ7N8VD]]:
$$\left[\begin{array}{cc|cc} 1 & 2 & 5 & 1 \\ 3 & 4 & 6 & 0 \end{array}\right].$$
2. The step $R_2 \leftarrow R_2 - 3R_1$ makes row 2 equal to $(0, -2 \mid -9, -3)$.
3. The step $R_2 \leftarrow -\tfrac12 R_2$ makes it $(0, 1 \mid \tfrac92, \tfrac32)$.
4. The step $R_1 \leftarrow R_1 - 2R_2$ makes row 1 equal to $(1, 0 \mid -4, -2)$.
5. The left block is now the identity, so each column behind the bar is a solution. The system $Ax = b$ has $x = (-4, \tfrac92)$, and $Ax = c$ has $x = (-2, \tfrac32)$.
6. Check the first: $-4 + 2 \cdot \tfrac92 = 5$ and $3 \cdot (-4) + 4 \cdot \tfrac92 = 6$.
7. Check the second: $-2 + 2 \cdot \tfrac32 = 1$ and $3 \cdot (-2) + 4 \cdot \tfrac32 = 0$.

## Remarks

Each [[elementary row operation|04XWH28452]] was chosen by looking at the left block only.
So the same steps serve every right side, and adding a column behind the bar costs only the arithmetic in that column.

If we add the right side $(0, 1)^{\mathsf{T}}$ as well, the two last columns are the columns of the identity.
The same three steps then turn that block into $A^{-1} = \begin{bmatrix} -2 & 1 \\ \tfrac32 & -\tfrac12 \end{bmatrix}$, whose first column is the solution $(-2, \tfrac32)$ found above.

## Explanations

### L1 human

Both systems have the same numbers on the left, so the same steps solve both.
We write both right sides behind the bar and do the steps once.
At the end, each column behind the bar holds one answer.

### L2 human

The typical use is to solve $AX = B$ for a matrix $X$, column by column.

1. Put all columns of $B$ behind the bar.
2. Reduce until the left block is the identity.
3. The right block is then $X$.

Watch out: a pivot that appears in a column right of the bar does not belong to $A$.
It means that one of the systems is inconsistent, and the other columns may still have solutions.
