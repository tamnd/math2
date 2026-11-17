---
tag: 8XWC7RKNN1
kind: example
name: An invertible 2 × 2 matrix has the inverse given by the determinant formula
msc: [08A02, 15A09]
topics: [BAZT8JJ70S]
audience: school
instance_of: [0ZNZH0EXFX]
uses: [0EB9N0S33C, 00KDZRW4C0, 06DW9BAWB1, 032Q9FB8MT]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Inversion of 2 × 2 matrices
---

## Example

Let $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ be a real matrix with [[determinant|00KDZRW4C0]] $\delta = ad - bc \neq 0$.
Let $B = \dfrac{1}{\delta}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$.
We check that $B$ is an [[inverse|0ZNZH0EXFX]] of $A$ for [[matrix multiplication|032Q9FB8MT]], with the [[identity matrix|06DW9BAWB1]] $I_2$ as the identity.

1. $\begin{pmatrix} a & b \\ c & d \end{pmatrix}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix} = \begin{pmatrix} ad - bc & -ab + ba \\ cd - dc & -cb + da \end{pmatrix} = \begin{pmatrix} \delta & 0 \\ 0 & \delta \end{pmatrix}$.
2. Divide by $\delta$, which is allowed because $\delta \neq 0$. So $AB = I_2$, and $B$ is a right inverse of $A$.
3. $\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}\begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} da - bc & db - bd \\ -ca + ac & -cb + ad \end{pmatrix} = \begin{pmatrix} \delta & 0 \\ 0 & \delta \end{pmatrix}$.
4. In the same way, $BA = I_2$, and $B$ is a left inverse of $A$.
5. By steps 2 and 4, $B$ is a two-sided inverse of $A$, so $A$ is an [[invertible matrix|0EB9N0S33C]] and $A^{-1} = B$.

A numerical check with $A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}$, where $\delta = 6 - 5 = 1$ and $B = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$:

6. $AB = \begin{pmatrix} 6 - 5 & -2 + 2 \\ 15 - 15 & -5 + 6 \end{pmatrix} = I_2$.
7. $BA = \begin{pmatrix} 6 - 5 & 3 - 3 \\ -10 + 10 & -5 + 6 \end{pmatrix} = I_2$.

## Remarks

If $\delta = 0$, then $A$ has no inverse.
Indeed, $\det(AB) = \det A \det B$ for all $2 \times 2$ matrices, so $AB = I_2$ would give $0 \cdot \det B = 1$, which is impossible.
Matrix multiplication is associative, so the inverse is unique, and the formula gives the only inverse.
For square matrices, one of the checks is enough, because [[a one-sided inverse of a square matrix is two-sided|0753Y2X5K6]].
The invertible $2 \times 2$ matrices form the [[general linear group|0FCHE902D7]] $\mathrm{GL}_2(\mathbb{R})$.

## Explanations

### L1 human

To invert a $2 \times 2$ matrix, exchange the two numbers on the main diagonal, change the sign of the other two numbers, and divide by the determinant $ad - bc$.
When we multiply the result by the matrix, we get the identity matrix.
If the determinant is $0$, we cannot divide, and the matrix has no inverse.

### L2 human

The computation in steps 1 and 3 shows the idea: the product with the adjusted matrix is $\delta$ times the identity, and the division by $\delta$ makes it the identity.
The typical use is to solve a system of two linear equations $A\mathbf{x} = \mathbf{y}$ as $\mathbf{x} = A^{-1}\mathbf{y}$.
A trap is to forget the factor $1/\delta$, or to change the signs on the main diagonal and not on the other diagonal.
