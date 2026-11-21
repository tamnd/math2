---
tag: YSF9M0E66C
kind: example
name: A 2 × 2 matrix with proportional rows is singular
msc: ["15A09"]
topics: [P8J6QR66TJ]
audience: school
not_instance_of:
  - target: 0EB9N0S33C
    note: the matrix sends the nonzero vector (2, -1) to 0, so no matrix B can satisfy BA = I
uses: [0TWTS88TWN, 0CCQV3884B, 073E4XC016]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Definition
---

## Example

Let $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ over $\mathbb{R}$, whose second row is twice the first.
We show that $A$ has neither a left inverse nor a right inverse, so it is not [[invertible|0TWTS88TWN]].

1. Take $x = (2, -1)^{\mathsf{T}}$. The [[matrix-vector product|0CCQV3884B]] is
$$Ax = \begin{pmatrix} 1 \cdot 2 + 2 \cdot (-1) \\ 2 \cdot 2 + 4 \cdot (-1) \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}.$$
2. Suppose some $2 \times 2$ matrix $B$ satisfies $BA = I_2$.
3. Then $x = I_2 x = (BA)x = B(Ax) = B0 = 0$, by [[associativity|073E4XC016]].
4. This contradicts $x \ne 0$, so $A$ has no left inverse.
5. Each column of a product $AB$ is $A$ times a column of $B$, so it has the form $(t, 2t)^{\mathsf{T}}$. The first column of $I_2$ is $(1, 0)^{\mathsf{T}}$, which is not of this form, so $A$ has no right inverse either.

## Remarks

The argument of step 3 works for every square matrix: if a nonzero vector goes to $0$, there is no left inverse.
The [[2 × 2 formula|8XWC7RKNN1]] gives the same verdict, since $ad - bc = 1 \cdot 4 - 2 \cdot 2 = 0$.
Row reduction sees it too: the step $R_2 \leftarrow R_2 - 2R_1$ makes the second row $(0, 0)$, so the reduced row echelon form is not $I_2$.

Change one entry and the picture changes.
With $4$ replaced by $5$, the rows $(1, 2)$ and $(2, 5)$ are no longer proportional, $ad - bc = 5 - 4 = 1$, and the matrix is invertible with inverse $\begin{pmatrix} 5 & -2 \\ -2 & 1 \end{pmatrix}$.

## Explanations

### L1 human

This matrix squashes the whole plane onto the line through $(1, 2)$.
The point $(2, -1)$ and the origin both land on the origin.
After the squash we cannot tell which point we started from, so no matrix can undo it.

### L2 human

The test for singularity is to find one nonzero vector $x$ with $Ax = 0$.
Here the proportional rows suggest it, and so do the columns: $2 \cdot (\text{column } 1) - (\text{column } 2) = (2 - 2, 4 - 4) = 0$.
Watch out: a matrix with no zero entries can still be singular, as this one is.
