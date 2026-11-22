---
tag: GGFA8S4NZ2
kind: example
name: A Hermitian 2 × 2 matrix and its real eigenvalues
msc: ["15B57"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [0P17NGQQMQ]
uses: [0EKZCX4K3P]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_matrix
    locator: Properties
---

## Example

A matrix with complex entries can still have only real eigenvalues, and Hermitian matrices are the standard case.
Let
$$A = \begin{pmatrix} 2 & 1 - i \\ 1 + i & 3 \end{pmatrix}.$$

1. Conjugate each entry and transpose:
$$A^* = \begin{pmatrix} \overline{2} & \overline{1 + i} \\ \overline{1 - i} & \overline{3} \end{pmatrix} = \begin{pmatrix} 2 & 1 - i \\ 1 + i & 3 \end{pmatrix} = A.$$
So $A$ is [[Hermitian|0EKZCX4K3P]], and its diagonal entries $2$ and $3$ are real, as they must be.
2. For $x = (x_1, x_2)^{\mathsf{T}}$, expand $x^* A x$; the two cross terms are conjugates of each other, so
$$x^* A x = 2|x_1|^2 + 3|x_2|^2 + 2 \operatorname{Re}\big((1 - i)\, \overline{x_1} x_2\big),$$
which is a real number.
3. The trace is $5$, and the determinant is $2 \cdot 3 - (1 - i)(1 + i) = 6 - 2 = 4$. So the characteristic polynomial is
$$t^2 - 5t + 4 = (t - 1)(t - 4).$$
4. The eigenvalues are $1$ and $4$, and both are real.
5. For $\lambda = 4$, take $v = (1 - i, 2)^{\mathsf{T}}$ and multiply:
$$Av = \begin{pmatrix} 2(1 - i) + 2(1 - i) \\ (1 + i)(1 - i) + 6 \end{pmatrix} = \begin{pmatrix} 4 - 4i \\ 8 \end{pmatrix} = 4v.$$

## Remarks

The real eigenvalues agree with the [[spectral theorem for Hermitian matrices|0DGZBQWZWN]], which belongs to a later sub-area.
The same holds for every $2 \times 2$ Hermitian matrix $\begin{pmatrix} a & b \\ \overline{b} & d \end{pmatrix}$ with $a, d$ real.
Its characteristic polynomial $t^2 - (a + d) t + (ad - |b|^2)$ has discriminant
$$(a + d)^2 - 4(ad - |b|^2) = (a - d)^2 + 4|b|^2 \ge 0,$$
so both roots are real.

If you replace the entry $1 + i$ by $1 - i$, the matrix becomes symmetric but not Hermitian.
Its determinant is then $6 - (1 - i)^2 = 6 + 2i$, so the eigenvalues are no longer real.

## Explanations

### L1 human

The two entries off the diagonal, $1 - i$ and $1 + i$, are complex conjugates, and the diagonal numbers are real.
That mirror pattern is what makes the matrix Hermitian.
Although the matrix has complex entries, the numbers that it scales vectors by are the plain real numbers $1$ and $4$.

### L2 human

To find the eigenvalues of a $2 \times 2$ matrix, use $t^2 - (\operatorname{tr} A)\, t + \det A$.
For a Hermitian matrix both the trace and the determinant are real, because $(1 - i)(1 + i) = |1 + i|^2$.
Watch out: the determinant uses the product $b \overline{b} = |b|^2$, not $b^2$; with $b^2 = (1 - i)^2 = -2i$ you would get a wrong, complex determinant.
