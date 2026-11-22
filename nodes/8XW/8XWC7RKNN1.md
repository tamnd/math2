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

Every $2 \times 2$ matrix with nonzero $ad - bc$ has an inverse that you can write down at once.
Let $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ be a real matrix with [[determinant|00KDZRW4C0]] $\delta = ad - bc \neq 0$, and let
$$B = \frac{1}{\delta}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}.$$
In words: swap the two diagonal entries, change the sign of the other two, and divide by $\delta$.
We check that $B$ is an [[inverse|0ZNZH0EXFX]] of $A$ for [[matrix multiplication|032Q9FB8MT]], with the [[identity matrix|06DW9BAWB1]] $I_2$ as the identity.

1. Multiply $A$ by the matrix in the bracket, row by column:
$$\begin{pmatrix} a & b \\ c & d \end{pmatrix}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix} = \begin{pmatrix} ad - bc & -ab + ba \\ cd - dc & -cb + da \end{pmatrix} = \begin{pmatrix} \delta & 0 \\ 0 & \delta \end{pmatrix}.$$
2. Divide by $\delta$, which is allowed because $\delta \neq 0$. This gives $AB = I_2$.
3. Multiply in the other order:
$$\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}\begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} da - bc & db - bd \\ -ca + ac & -cb + ad \end{pmatrix} = \begin{pmatrix} \delta & 0 \\ 0 & \delta \end{pmatrix}.$$
4. Dividing by $\delta$ again gives $BA = I_2$.
5. By steps 2 and 4, $A$ is an [[invertible matrix|0EB9N0S33C]] and $A^{-1} = B$.

## Remarks

### A case with numbers

Take $A = \begin{pmatrix} 4 & 7 \\ 2 & 6 \end{pmatrix}$, so that $\delta = 4 \cdot 6 - 7 \cdot 2 = 24 - 14 = 10$.
The formula gives
$$A^{-1} = \frac{1}{10}\begin{pmatrix} 6 & -7 \\ -2 & 4 \end{pmatrix} = \begin{pmatrix} 3/5 & -7/10 \\ -1/5 & 2/5 \end{pmatrix}.$$
Check: $\begin{pmatrix} 4 & 7 \\ 2 & 6 \end{pmatrix}\begin{pmatrix} 6 & -7 \\ -2 & 4 \end{pmatrix} = \begin{pmatrix} 24 - 14 & -28 + 28 \\ 12 - 12 & -14 + 24 \end{pmatrix} = 10 I_2$.

### Solving a system with it

The system $4x + 7y = 1$, $2x + 6y = 3$ is $A(x, y)^{\mathsf{T}} = (1, 3)^{\mathsf{T}}$ for the same $A$.
Multiply the right side by $A^{-1}$:
$$\begin{pmatrix} x \\ y \end{pmatrix} = \frac{1}{10}\begin{pmatrix} 6 - 21 \\ -2 + 12 \end{pmatrix} = \frac{1}{10}\begin{pmatrix} -15 \\ 10 \end{pmatrix} = \begin{pmatrix} -3/2 \\ 1 \end{pmatrix}.$$
Check: $4 \cdot (-\tfrac{3}{2}) + 7 = -6 + 7 = 1$ and $2 \cdot (-\tfrac{3}{2}) + 6 = -3 + 6 = 3$.

### When the formula fails

Take $C = \begin{pmatrix} 2 & 4 \\ 3 & 6 \end{pmatrix}$, so that $\delta = 2 \cdot 6 - 4 \cdot 3 = 0$ and the formula would divide by $0$.
Here no inverse exists at all.
The vector $(2, -1)$ goes to $C(2, -1)^{\mathsf{T}} = (4 - 4, 6 - 6)^{\mathsf{T}} = 0$.
If $DC = I_2$ for some $D$, then $(2, -1)^{\mathsf{T}} = D C (2, -1)^{\mathsf{T}} = D 0 = 0$, which is false.

The same holds for every matrix with $\delta = 0$.
The determinant is multiplicative, so $AB = I_2$ would give $\det A \det B = 1$, which is impossible when $\det A = 0$.

### What else it shows

The inverse is [[unique|FMCX4D7RD4]], so the formula gives the only inverse.
For square matrices one of the two checks is enough, because [[a one-sided inverse of a square matrix is two-sided|0753Y2X5K6]].
The formula works over any commutative ring when $\delta$ is a unit, and it is the case $n = 2$ of the [[inverse via the adjugate|0ENVM493VK]].
The invertible $2 \times 2$ real matrices form the [[general linear group|0FCHE902D7]] $\mathrm{GL}_2(\mathbb{R})$.

### Watch out

Two slips are common: forgetting the factor $1/\delta$, and changing the signs on the main diagonal instead of the other one.
For $A = \begin{pmatrix} 4 & 7 \\ 2 & 6 \end{pmatrix}$, the wrong matrix $\begin{pmatrix} -6 & 7 \\ 2 & -4 \end{pmatrix}$ gives the product $A \begin{pmatrix} -6 & 7 \\ 2 & -4 \end{pmatrix} = \begin{pmatrix} -10 & 0 \\ 0 & -10 \end{pmatrix}$, which is $-10 I_2$ and not $I_2$.

## Explanations

### L1 human

To invert a $2 \times 2$ matrix, exchange the two numbers on the main diagonal and change the sign of the other two numbers.
Then divide every entry by the number $ad - bc$.
When we multiply the result by the matrix, we get the identity matrix.
If $ad - bc$ is $0$, we cannot divide, and the matrix has no inverse.

### L2 human

The computation in steps 1 and 3 shows why the formula works.
The product with the swapped-and-signed matrix is $\delta$ times the identity, and the division by $\delta$ turns it into the identity.
The typical use is to solve a system of two equations $Ax = y$ as $x = A^{-1} y$, as in the system above.
Before you use the formula, compute $\delta$: when it is $0$, the system has either no solution or infinitely many, and no inverse can help.
