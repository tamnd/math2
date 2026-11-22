---
tag: RMXFKRW9WQ
kind: example
name: A matrix with determinant on the unit circle that is not unitary
msc: ["15B57", "20G20"]
topics: [AZS5BPF5H3]
audience: ug2
not_instance_of:
  - target: VW5H9XFNJB
    note: the determinant is i, but the second column has length the square root of two
uses: [0D6RMJ10M9, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Unitary_group
    locator: lead section
---

## Example

Let
$$A = \begin{pmatrix} i & 1 \\ 0 & 1 \end{pmatrix}.$$
We show that $\lvert \det A \rvert = 1$ and that the eigenvalues lie on the unit circle, but that $A$ is not in the [[unitary group|VW5H9XFNJB]] $U(2)$.

1. The matrix is upper triangular, so $\det A = i \cdot 1 = i$, and $\lvert \det A \rvert = 1$.
2. The eigenvalues of a triangular matrix are its diagonal entries, here $i$ and $1$, and both lie on the unit circle.
3. Conjugate and transpose:
$$A^* = \begin{pmatrix} -i & 0 \\ 1 & 1 \end{pmatrix}.$$
4. Multiply, row of $A^*$ by column of $A$:
$$A^* A = \begin{pmatrix} (-i)(i) & (-i) \cdot 1 + 0 \\ 1 \cdot i + 0 & 1 + 1 \end{pmatrix} = \begin{pmatrix} 1 & -i \\ i & 2 \end{pmatrix} \ne I_2.$$
5. So $A$ is not [[unitary|0D6RMJ10M9]]. The entry $2$ says that the second column $(1, 1)$ has squared length $2$.

## Remarks

The example shows that neither the [[determinant|0C3CFHDN6R]] nor the eigenvalues detect unitary matrices.
Both are necessary conditions, and both are far from sufficient.

The eigenvectors show what goes wrong.
For the eigenvalue $i$ an eigenvector is $(1, 0)$.
For the eigenvalue $1$ we solve $(i - 1) x_1 + x_2 = 0$ and get $(1, 1 - i)$.
Their inner product is $1 \cdot 1 + 0 \cdot \overline{(1 - i)} = 1 \ne 0$, while for a unitary matrix eigenvectors of different eigenvalues are orthogonal.
The matrix is not even normal, since
$$A A^* = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \ne A^* A.$$

## Explanations

### L1 human

The determinant of this matrix has size $1$, so in a sense it keeps areas.
But it stretches some vectors: $(0, 1)$ goes to $(1, 1)$, which is longer.
So the matrix does not keep lengths, and it is not unitary.

### L2 human

The typical way to show that a matrix is not unitary is to find one column whose length is not $1$, or two columns that are not orthogonal.
Here the second column fails at once, since $\lvert 1 \rvert^2 + \lvert 1 \rvert^2 = 2$.
Watch out: the test $\lvert \det A \rvert = 1$ is necessary for a unitary matrix, but it is not sufficient.
Scaling the second column to $\frac{1}{\sqrt{2}}(1, 1)$ would not help either, because that column is still not orthogonal to the first column $(i, 0)$.
