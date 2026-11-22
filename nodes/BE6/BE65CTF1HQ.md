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

Let $v = \frac{1}{3}(1, 2, 2)$.
It is a unit vector, because $\frac{1}{9}(1 + 4 + 4) = 1$.
We compute the Householder matrix $H = I_3 - 2vv^{\mathsf{T}}$, the matrix of the [[reflection|025158VEYZ]] in the plane $x + 2y + 2z = 0$, and we check its properties.

1. The outer product is
$$vv^{\mathsf{T}} = \frac{1}{9}\begin{pmatrix} 1 & 2 & 2 \\ 2 & 4 & 4 \\ 2 & 4 & 4 \end{pmatrix}.$$
2. Subtract twice this from $I_3$, entry by entry; for example the entry $(1, 1)$ is $1 - \frac{2}{9} = \frac{7}{9}$ and the entry $(2, 3)$ is $-\frac{8}{9}$:
$$H = \frac{1}{9}\begin{pmatrix} 7 & -4 & -4 \\ -4 & 1 & -8 \\ -4 & -8 & 1 \end{pmatrix}.$$
3. The matrix $H$ is symmetric. Its first column has length $\frac{1}{9}\sqrt{49 + 16 + 16} = 1$, and the other two columns have length $\frac{1}{9}\sqrt{16 + 1 + 64} = 1$.
4. The dot products of the columns are $\frac{1}{81}(-28 - 4 + 32) = 0$ for columns $1$ and $2$, $\frac{1}{81}(-28 + 32 - 4) = 0$ for columns $1$ and $3$, and $\frac{1}{81}(16 - 8 - 8) = 0$ for columns $2$ and $3$. So $H$ is [[orthogonal|0QRBVFJ50X]].
5. The normal vector is reversed:
$$Hv = \frac{1}{27}(7 - 8 - 8, \ -4 + 2 - 16, \ -4 - 16 + 2) = \frac{1}{27}(-9, -18, -18) = -v.$$
6. The vector $w = (2, -1, 0)$ lies in the mirror, because $2 - 2 + 0 = 0$, and it is fixed: $Hw = \frac{1}{9}(14 + 4, \ -8 - 1, \ -8 + 8) = (2, -1, 0)$.
7. The vector $w' = (2, 0, -1)$ also lies in the mirror, and $v, w, w'$ is a basis of $\R^3$. In this basis the matrix of $H$ is $\operatorname{diag}(-1, 1, 1)$, so [[the determinant|0C3CFHDN6R]] is $\det H = -1$.

## Remarks

The example checks parts 1, 3 and 4 of [[the reflection theorem|FEER10D15S]] on one matrix.
Part 5 of the same theorem is visible too.
The first column of $H$ is $\frac{1}{9}(7, -4, -4)$, so $H$ sends $3e_1 = (3, 0, 0)$ to $\frac{1}{3}(7, -4, -4)$.
Both vectors have length $3$, and their difference is $\frac{1}{3}(2, 4, 4) = 2v$, a normal vector of the mirror, as the swap rule predicts.

The trace gives a quick test.
It is $\frac{1}{9}(7 + 1 + 1) = 1$, the sum of the eigenvalues $-1$, $1$ and $1$ of a reflection of $\R^3$.
All entries of $9H$ are integers because $3v$ has integer entries.
In the same way, every vector $(a, b, c)$ of integers gives a reflection with rational entries, $I - \frac{2}{a^2 + b^2 + c^2}(a, b, c)^{\mathsf{T}}(a, b, c)$, and the vector need not have length $3$.

## Explanations

### L1 human

The vector $(1, 2, 2)$ points straight out of a flat mirror through the origin.
The matrix $H$ sends each point of space to its mirror image.
The vector $(1, 2, 2)$ itself goes to $(-1, -2, -2)$.
Vectors that lie in the mirror, such as $(2, -1, 0)$, stay where they are.

### L2 human

The worked computation is in the Example above.
A typical use of a matrix like this is to write down a symmetric orthogonal matrix with rational entries in a few lines.
Watch out: the formula $I - 2vv^{\mathsf{T}}$ needs a unit vector $v$.
With $u = (1, 2, 2)$ in place of $v$, the matrix $I - 2uu^{\mathsf{T}}$ has entry $(1, 1)$ equal to $-1$ and first column $(-1, -4, -4)$, of length $\sqrt{33}$, so it is not orthogonal.
The correct formula for this $u$ is $I - \frac{2}{9}uu^{\mathsf{T}}$, which is the same $H$.
