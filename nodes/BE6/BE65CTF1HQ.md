---
tag: BE65CTF1HQ
kind: example
name: The Householder matrix of the vector one third of (1, 2, 2)
msc: ["15A04", "15B10", "65F25"]
topics: [AZS5BPF5H3]
audience: ug2
instance_of: [06BRDF3F0E, JDH0THTVGM]
illustrates: [FEER10D15S]
uses: [025158VEYZ, 0QRBVFJ50X, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Householder_transformation
    locator: Householder matrix
  - url: https://en.wikipedia.org/wiki/Householder_transformation
    locator: Properties
---

## Example

Let $v = \frac{1}{3}(1, 2, 2)$, a unit vector, because $\frac{1}{9}(1 + 4 + 4) = 1$.
We compute the Householder matrix $H = I_3 - 2vv^T$, the matrix of the [[reflection|025158VEYZ]] in the plane $x + 2y + 2z = 0$.

1. $vv^T = \frac{1}{9}\begin{pmatrix} 1 & 2 & 2 \\ 2 & 4 & 4 \\ 2 & 4 & 4 \end{pmatrix}$.
2. $H = I_3 - \frac{2}{9}\begin{pmatrix} 1 & 2 & 2 \\ 2 & 4 & 4 \\ 2 & 4 & 4 \end{pmatrix} = \frac{1}{9}\begin{pmatrix} 7 & -4 & -4 \\ -4 & 1 & -8 \\ -4 & -8 & 1 \end{pmatrix}$.
3. $H$ is symmetric. Its first column has length $\frac{1}{9}\sqrt{49 + 16 + 16} = 1$, and the other two columns have length $\frac{1}{9}\sqrt{16 + 1 + 64} = 1$.
4. The dot product of the columns $1$ and $2$ is $\frac{1}{81}(-28 - 4 + 32) = 0$. In the same way, the other two dot products are $\frac{1}{81}(-28 + 32 - 4) = 0$ and $\frac{1}{81}(16 - 8 - 8) = 0$. So $H$ is [[orthogonal|0QRBVFJ50X]].
5. $Hv = \frac{1}{27}(7 - 8 - 8, \ -4 + 2 - 16, \ -4 - 16 + 2) = \frac{1}{27}(-9, -18, -18) = -v$.
6. The vector $w = (2, -1, 0)$ lies in the mirror, because $2 - 2 + 0 = 0$. And $Hw = \frac{1}{9}(14 + 4, \ -8 - 1, \ -8 + 8) = (2, -1, 0) = w$.
7. In the basis $v$, $w$, $w' = (2, 0, -1)$, the matrix of $H$ is $\operatorname{diag}(-1, 1, 1)$, because $w'$ is also in the mirror. So [[the determinant|0C3CFHDN6R]] is $\det H = -1$.

## Remarks

- The example illustrates parts 1, 3 and 4 of [[the reflection theorem|FEER10D15S]].
- By part 5 of the same theorem, $H$ swaps $3e_1 = (3, 0, 0)$ and $(\frac{7}{3}, -\frac{4}{3}, -\frac{4}{3})$, two vectors of length $3$ whose difference is $2v$.
- The trace of $H$ is $\frac{1}{9}(7 + 1 + 1) = 1$, the sum of the eigenvalues $-1$, $1$ and $1$.
- All entries of $9H$ are integers, because $3v$ has integer entries.

## Explanations

### L1 human

The vector $(1, 2, 2)$ points straight out of a plane mirror through the origin.
The matrix $H$ sends each point to its mirror image.
The vector $(1, 2, 2)$ itself goes to its negative.
Vectors in the mirror, like $(2, -1, 0)$, stay where they are.

### L2 human

The worked computation is in the Example.
The typical use: a matrix of this form is a fast way to write down a symmetric orthogonal matrix with rational entries.
A trap: the formula $I - 2vv^T$ needs a unit vector $v$.
With $u = (1, 2, 2)$, the matrix $I - 2uu^T$ is not orthogonal, and the correct formula is $I - \frac{2}{9}uu^T$.
