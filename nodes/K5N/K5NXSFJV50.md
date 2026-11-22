---
tag: K5NXSFJV50
kind: example
name: Diagonalizing a 3 × 3 matrix with a repeated eigenvalue
msc: ["15A20", "15A18"]
topics: [Z6S6PWMJPH]
audience: ug1
instance_of: [07SQCNV233, D0AP2R7272]
illustrates: [CDB8KCNNG9]
uses: [0Y17PEKF24, 039HF58KQ5, 0AYEPBQMAW, 0TWTS88TWN]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonalizable_matrix
    locator: Examples
  - book: isbn:9780321982384
    locator: Section 5.3
---

## Example

Let $A = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix}$ over $\R$.
We show that $A$ is diagonalizable, although one of its eigenvalues is repeated.

1. Write $A = I + J$, where $J$ is the $3 \times 3$ matrix of all ones.
   Each row of $J$ adds up the coordinates, so $J(1, 1, 1) = (3, 3, 3)$, and $J v = 0$ for every $v = (x, y, z)$ with $x + y + z = 0$.
2. Since $A w = w + J w$ for every vector $w$, we get $A(1, 1, 1) = 4(1, 1, 1)$, and $A v = v$ for every $v$ in the plane $x + y + z = 0$.
3. So $4$ and $1$ are eigenvalues, and the [[characteristic polynomial|0VSSPAFM2C]] is $(t - 4)(t - 1)^2$.
   Check: its constant term is $-4$, and $(-1)^3 \det A = -4$, since $\det A = 4$.
4. The [[eigenspace|0G0RFPG8HR]] of $1$ is $\ker(A - I) = \ker J$, the plane $x + y + z = 0$, with the basis $(1, -1, 0)$ and $(1, 0, -1)$.
   Its dimension $2$ equals the algebraic multiplicity $2$ of the eigenvalue $1$.
5. The eigenspace of $4$ is the line spanned by $(1, 1, 1)$.
6. Put the three eigenvectors as the columns of $P$, and the eigenvalues in the same order in $D$:
$$P = \begin{pmatrix} 1 & 1 & 1 \\ 1 & -1 & 0 \\ 1 & 0 & -1 \end{pmatrix}, \qquad D = \begin{pmatrix} 4 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad P^{-1} = \frac{1}{3} \begin{pmatrix} 1 & 1 & 1 \\ 1 & -2 & 1 \\ 1 & 1 & -2 \end{pmatrix}.$$
   Here $\det P = 3$, and the product of $P$ with the matrix in the parentheses of $P^{-1}$ is $3I$.
7. Multiply back.
   First $P D$ scales the first column of $P$ by $4$, and then
$$P D P^{-1} = \begin{pmatrix} 4 & 1 & 1 \\ 4 & -1 & 0 \\ 4 & 0 & -1 \end{pmatrix} \cdot \frac{1}{3} \begin{pmatrix} 1 & 1 & 1 \\ 1 & -2 & 1 \\ 1 & 1 & -2 \end{pmatrix} = \frac{1}{3} \begin{pmatrix} 6 & 3 & 3 \\ 3 & 6 & 3 \\ 3 & 3 & 6 \end{pmatrix} = A.$$
8. So $A$ is [[diagonalizable|07SQCNV233]] over $\R$, with the repeated eigenvalue $1$.

## Remarks

A repeated eigenvalue does not stop diagonalization.
What matters is that the eigenspace of $1$ is as large as the multiplicity of $1$, which is the [[test by multiplicities|CDB8KCNNG9]].
The matrix is symmetric, so the [[real spectral theorem|06J4PXRG22]] even gives an orthonormal basis of eigenvectors.
To get it, replace the basis of the plane by an orthogonal one such as $(1, -1, 0)$ and $(1, 1, -2)$, and divide each vector by its length.

Now change one entry and compare.
The matrix $B = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 4 \end{pmatrix}$ has the same characteristic polynomial $(t - 4)(t - 1)^2$.
But $B - I = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 3 \end{pmatrix}$ has rank $2$, so the eigenspace of $1$ is only the line spanned by $e_1$.
Then $B$ has at most two independent eigenvectors, and it is not diagonalizable.

## Explanations

### L1 human

This matrix stretches the diagonal direction through $(1, 1, 1)$ by a factor $4$.
It does not move any arrow in the flat plane where the three coordinates add up to $0$.
A plane gives two independent directions, and the diagonal line gives a third one.
Three independent directions in space are enough to serve as axes, so the matrix can be made diagonal.

### L2 human

Let us check the inverse of step 6, since the whole result rests on it.
Write $Q = 3 P^{-1}$, the integer matrix in the parentheses.
Row $1$ of $P$ is $(1, 1, 1)$, and its products with the columns of $Q$ are $1 + 1 + 1 = 3$, then $1 - 2 + 1 = 0$, then $1 + 1 - 2 = 0$.
Row $2$ of $P$ is $(1, -1, 0)$, and its products are $1 - 1 = 0$, then $1 + 2 = 3$, then $1 - 1 = 0$.
Row $3$ of $P$ is $(1, 0, -1)$, and its products are $1 - 1 = 0$, then $1 - 1 = 0$, then $1 + 2 = 3$.
So $P Q = 3I$ and $P^{-1} = \tfrac{1}{3} Q$.
Watch out: from "three eigenvalues $4, 1, 1$" alone you cannot conclude that $A$ is diagonalizable, because the matrix $B$ of the remarks has the same three eigenvalues and is not.
