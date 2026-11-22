---
tag: 3WRXFFFDV1
kind: example
name: The Schur complement of a pivot is the matrix left after one elimination step
msc: ["15A09", "15A23"]
topics: [P8J6QR66TJ]
audience: ug2
instance_of: [6HWFBXYPZP]
uses: [CA1J41NWGS, B61PAXBBHQ, 0KA7A4ENVJ]
sources:
  - url: https://en.wikipedia.org/wiki/Schur_complement
    locator: Background
---

## Example

One step of Gaussian elimination with the first pivot leaves, in the lower right corner, exactly the Schur complement of that pivot.
Let
$$M = \begin{pmatrix} 2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{pmatrix},$$
with the $1 \times 1$ block $A = (2)$, $B = (1, 1)$, $C = \begin{pmatrix} 4 \\ 8 \end{pmatrix}$ and $D = \begin{pmatrix} 3 & 3 \\ 7 & 9 \end{pmatrix}$.
The [[Schur complement|CA1J41NWGS]] is
$$CA^{-1}B = \tfrac12 \begin{pmatrix} 4 \\ 8 \end{pmatrix} (1, 1) = \begin{pmatrix} 2 & 2 \\ 4 & 4 \end{pmatrix}, \qquad M/A = D - CA^{-1}B = \begin{pmatrix} 1 & 1 \\ 3 & 5 \end{pmatrix}.$$
Now do one elimination step on $M$: $R_2 \to R_2 - 2R_1$ gives $(0, 1, 1)$, and $R_3 \to R_3 - 4R_1$ gives $(0, 3, 5)$.
The lower right $2 \times 2$ block after this step is $\begin{pmatrix} 1 & 1 \\ 3 & 5 \end{pmatrix}$, which is $M/A$.
By the [[determinant formula|0KA7A4ENVJ]],
$$\det M = 2 \cdot \det(M/A) = 2 (5 - 3) = 4.$$
Check: this agrees with the [[worked LU example|B61PAXBBHQ]], where the pivots of $M$ are $2$, $1$ and $2$, with product $4$.

## Remarks

### The general reason

The row operation $R_i \to R_i - (m_{i1}/m_{11}) R_1$ subtracts $c_i\, a^{-1}\, b$ from the part of row $i$ to the right of column 1, where $a = m_{11}$, $b$ is the rest of row 1 and $c_i = m_{i1}$.
Taken over all $i \ge 2$, these subtractions remove exactly the block $C A^{-1} B$ from $D$.
So Gaussian elimination is the repeated formation of Schur complements of $1 \times 1$ pivots.
Elimination on $M/A$ continues with the pivot $1$ and leaves the Schur complement $5 - 3 \cdot 1 \cdot 1 = 2$, the last pivot.

### Try it

Find the Schur complement of the pivot $1$ in $N = \begin{pmatrix} 1 & 2 \\ 3 & 10 \end{pmatrix}$, and compare it with one step of elimination.
Answer: $N/(1) = 10 - 3 \cdot 2 = 4$, and $R_2 \to R_2 - 3R_1$ gives the row $(0, 4)$.
Check: $\det N = 10 - 6 = 4 = 1 \cdot 4$.

## Explanations

### L1 human

One step of elimination with the first pivot leaves a smaller matrix in the lower right corner.
That smaller matrix is exactly the Schur complement of the pivot.
So the Schur complement is "what is left to do" after the first pivot.

### L2 human

This explains the quotient notation $M/A$.
Each step of elimination divides out one pivot and keeps the rest.
The determinant is the product of the pivots, which matches $\det M = \det A \det(M/A)$ step by step.
