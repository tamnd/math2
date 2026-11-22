---
tag: DAYPSS15ET
kind: example
name: Inverting a 3 × 3 matrix by the block formula
msc: ["15A09"]
topics: [P8J6QR66TJ]
audience: ug2
instance_of: [6HWFBXYPZP]
uses: [5QTK7JWXF3, CA1J41NWGS, 8XWC7RKNN1, 032Q9FB8MT]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Blockwise inversion
---

## Example

The block inverse formula inverts a $3 \times 3$ matrix from one $2 \times 2$ inverse and one number, the Schur complement.
Let
$$M = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 1 & 0 \\ 1 & 2 & 3 \end{pmatrix}$$
over $\mathbb{Q}$, with blocks $A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$, $B = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$, $C = (1, 2)$ and $D = (3)$.

1. $\det A = 2 - 1 = 1$, and the [[$2 \times 2$ formula|8XWC7RKNN1]] gives $A^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$.
2. $A^{-1}B = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$, the first column of $A^{-1}$, and $CA^{-1} = (1 - 2,\ -1 + 4) = (-1, 3)$.
3. The [[Schur complement|CA1J41NWGS]] is $S = D - CA^{-1}B = 3 - (-1) = 4$. It is invertible, so $M$ is invertible by the [[block inverse formula|5QTK7JWXF3]], and $\det M = \det A \cdot S = 4$.
4. The product $A^{-1}B \cdot CA^{-1}$ is a column times a row, the rank one matrix $\begin{pmatrix} 1 \\ -1 \end{pmatrix} (-1, 3) = \begin{pmatrix} -1 & 3 \\ 1 & -3 \end{pmatrix}$.

The four blocks of $M^{-1}$ are
$$A^{-1} + \tfrac{1}{4} \begin{pmatrix} -1 & 3 \\ 1 & -3 \end{pmatrix} = \begin{pmatrix} 3/4 & -1/4 \\ -3/4 & 5/4 \end{pmatrix}, \quad -\tfrac14 A^{-1}B = \begin{pmatrix} -1/4 \\ 1/4 \end{pmatrix}, \quad -\tfrac14 CA^{-1} = (1/4, -3/4), \quad S^{-1} = \tfrac14.$$
So
$$M^{-1} = \frac{1}{4} \begin{pmatrix} 3 & -1 & -1 \\ -3 & 5 & 1 \\ 1 & -3 & 1 \end{pmatrix}.$$
Check: row 1 of $4M^{-1}$ times $M$ is $(6 - 1 - 1,\ 3 - 1 - 2,\ 3 - 0 - 3) = (4, 0, 0)$, row 2 gives $(-6 + 5 + 1,\ -3 + 5 + 2,\ -3 + 0 + 3) = (0, 4, 0)$, and row 3 gives $(2 - 3 + 1,\ 1 - 3 + 2,\ 1 + 0 + 3) = (0, 0, 4)$.
So $M^{-1} M = I_3$.

## Remarks

### The same number as a pivot

The Schur complement $S = 4$ is also the last pivot in elimination on $M$.
The steps $R_2 \to R_2 - \tfrac{1}{2} R_1$ and $R_3 \to R_3 - \tfrac{1}{2} R_1$ give rows $(0, \tfrac12, -\tfrac12)$ and $(0, \tfrac32, \tfrac52)$, and then $R_3 \to R_3 - 3R_2$ gives $(0, 0, 4)$.
The pivots $2$, $\tfrac12$ and $4$ have product $4 = \det M$.

### Watch out

The upper left block of $M^{-1}$ is not $A^{-1}$.
The correction term $\tfrac14 \begin{pmatrix} -1 & 3 \\ 1 & -3 \end{pmatrix}$ changes every entry, because $B$ and $C$ are both nonzero.

## Explanations

### L1 human

We split the matrix into a $2 \times 2$ block, a column, a row and a single number.
We invert the small block, compute one number $S$, and build the inverse from these pieces.
Multiplying back confirms the answer.

### L2 human

The method pays off when $A^{-1}$ is already known, or easy, as for a diagonal $A$.
Then the whole work is one Schur complement and its inverse, here a single division by $4$.
