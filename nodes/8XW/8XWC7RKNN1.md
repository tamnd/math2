---
tag: 8XWC7RKNN1
kind: example
name: Inverse of a 2 × 2 matrix
msc: [08A02, 15A09]
topics: [BAZT8JJ70S, P8J6QR66TJ]
audience: school
instance_of: [0ZNZH0EXFX, 0EB9N0S33C]
uses: [0EB9N0S33C, 00KDZRW4C0, 06DW9BAWB1, 032Q9FB8MT]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Inversion of 2 × 2 matrices
  - book: isbn:9780321982384
    locator: Section 2.2
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

A numerical case: let $A = \begin{pmatrix} 4 & 7 \\ 2 & 6 \end{pmatrix}$.

6. $\delta = 4 \cdot 6 - 7 \cdot 2 = 24 - 14 = 10$.
7. $A^{-1} = \tfrac{1}{10}\begin{pmatrix} 6 & -7 \\ -2 & 4 \end{pmatrix} = \begin{pmatrix} 3/5 & -7/10 \\ -1/5 & 2/5 \end{pmatrix}$.
8. Check: $A \cdot \begin{pmatrix} 6 & -7 \\ -2 & 4 \end{pmatrix} = \begin{pmatrix} 24 - 14 & -28 + 28 \\ 12 - 12 & -14 + 24 \end{pmatrix} = 10 I_2$, so $AA^{-1} = I_2$.
9. Check: $\begin{pmatrix} 6 & -7 \\ -2 & 4 \end{pmatrix} A = \begin{pmatrix} 24 - 14 & 42 - 42 \\ -8 + 8 & -14 + 24 \end{pmatrix} = 10 I_2$, so $A^{-1}A = I_2$.

We solve the system $4x + 7y = 1$, $2x + 6y = 3$, which is $A(x, y)^{\mathsf{T}} = (1, 3)^{\mathsf{T}}$.

10. $(x, y)^{\mathsf{T}} = A^{-1}(1, 3)^{\mathsf{T}} = \tfrac{1}{10}(6 - 21, \; -2 + 12)^{\mathsf{T}} = \tfrac{1}{10}(-15, 10)^{\mathsf{T}} = (-\tfrac{3}{2}, 1)^{\mathsf{T}}$.
11. Check: $4 \cdot (-\tfrac{3}{2}) + 7 \cdot 1 = -6 + 7 = 1$ and $2 \cdot (-\tfrac{3}{2}) + 6 \cdot 1 = -3 + 6 = 3$.

A case where the formula fails: let $C = \begin{pmatrix} 2 & 4 \\ 3 & 6 \end{pmatrix}$.

12. $\delta = 2 \cdot 6 - 4 \cdot 3 = 0$, so the formula would divide by $0$.
13. $C(2, -1)^{\mathsf{T}} = (4 - 4, \; 6 - 6)^{\mathsf{T}} = 0$. If $DC = I_2$, then $(2, -1)^{\mathsf{T}} = DC(2, -1)^{\mathsf{T}} = 0$, which is false. So $C$ is singular.

## Remarks

If $\delta = 0$, then $A$ has no inverse.
Indeed, $\det(AB) = \det A \det B$ for all $2 \times 2$ matrices, so $AB = I_2$ would give $0 \cdot \det B = 1$, which is impossible.
Matrix multiplication is associative, so the inverse is [[unique|~139b320d]], and the formula gives the only inverse.
For square matrices, one of the checks is enough, because [[a one-sided inverse of a square matrix is two-sided|0753Y2X5K6]].
The same formula works over each commutative ring when $\delta$ is a unit; it is the case $n = 2$ of the [[inverse via the adjugate|0ENVM493VK]].
The invertible $2 \times 2$ matrices form the [[general linear group|0FCHE902D7]] $\mathrm{GL}_2(\mathbb{R})$.

## Explanations

### L1 human

To invert a $2 \times 2$ matrix, exchange the two numbers on the main diagonal and change the sign of the other two numbers.
Then divide by the determinant $ad - bc$.
When we multiply the result by the matrix, we get the identity matrix.
If the determinant is $0$, we cannot divide, and the matrix has no inverse.

### L2 human

The computation in steps 1 and 3 shows the idea.
The product with the adjusted matrix is $\delta$ times the identity, and the division by $\delta$ makes it the identity.
The typical use is to solve a system of two linear equations $A\mathbf{x} = \mathbf{y}$ as $\mathbf{x} = A^{-1}\mathbf{y}$, as in steps 10 and 11.
A trap is to forget the factor $1/\delta$, or to change the signs on the main diagonal and not on the other diagonal.
