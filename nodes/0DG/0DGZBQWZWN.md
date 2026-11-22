---
tag: 0DGZBQWZWN
kind: statement
role: theorem
name: Spectral theorem for Hermitian matrices
msc: ["15A18", "15B57"]
topics: [3YM9EK6VMB]
audience: ug1
about: [0P17NGQQMQ, 0VR671PHE5]
uses: [0C4NT4GT3X, 06J4PXRG22, 0EKZCX4K3P, 0N28QN4CYA, 0D6RMJ10M9, 0QRBVFJ50X]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.IsHermitian.spectral_theorem
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_theorem
    locator: Hermitian maps and Hermitian matrices
  - url: https://en.wikipedia.org/wiki/Hermitian_matrix
    locator: Eigendecomposition
  - book: isbn:9780134860244
    locator: Section 6.4
  - book: isbn:9783031410253
    locator: Chapter 7
---

## Statement

A Hermitian matrix is a real diagonal matrix seen in a different orthonormal basis, and a real symmetric matrix is a real diagonal matrix seen in a different real orthonormal basis.

1. Let $A$ be a [[Hermitian|0EKZCX4K3P]] $n \times n$ complex matrix, so $A^* = A$. Then there are a [[unitary matrix|0D6RMJ10M9]] $U$ and a real diagonal matrix $D$ with $A = U D U^*$.
2. Let $A$ be a real [[symmetric|0N28QN4CYA]] $n \times n$ matrix. Then there are a real [[orthogonal matrix|0QRBVFJ50X]] $Q$ and a real diagonal matrix $D$ with $A = Q D Q^{\mathsf{T}}$.

The diagonal entries of $D$ are the eigenvalues of $A$, repeated by multiplicity, and the columns of $U$, or of $Q$, form an orthonormal basis of eigenvectors.

## Remarks

### A first case

Take the Hermitian matrix $A = \begin{pmatrix} 1 & 2i \\ -2i & 1 \end{pmatrix}$, worked out in [[the Hermitian 2 by 2 example|4119199XBW]].
Its characteristic polynomial is
$$(1 - t)^2 - (2i)(-2i) = (1 - t)^2 - 4,$$
with the real roots $3$ and $-1$.
The unit eigenvectors $u_1 = \tfrac{1}{\sqrt{2}}(i, 1)$ for $3$ and $u_2 = \tfrac{1}{\sqrt{2}}(1, i)$ for $-1$ are orthogonal, so
$$A = U \begin{pmatrix} 3 & 0 \\ 0 & -1 \end{pmatrix} U^*, \qquad U = \tfrac{1}{\sqrt{2}} \begin{pmatrix} i & 1 \\ 1 & i \end{pmatrix}.$$
Check: $D$ has trace $2$ and determinant $-3$, and $A$ has trace $2$ and determinant $1 - (2i)(-2i) = 1 - 4 = -3$.
A real case is [[the symmetric 3 by 3 matrix with eigenvalues 3, 4 and 6|2P021RCC4Y]].

### Why each hypothesis is needed

The condition $A^* = A$ cannot be replaced by $A^{\mathsf{T}} = A$ for complex matrices.
[[The complex symmetric matrix|DAZBNZXZK7]] $\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$ has the eigenvalues $1 \pm i$, so no real $D$ is possible.
That matrix happens to be normal, so it still has the form $U D U^*$ by [[the complex spectral theorem|04CW1P44VD]], but with $D = \operatorname{diag}(1 + i, 1 - i)$.

In part 2, symmetry is needed for a real orthogonal $Q$.
[[The matrix $\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$|5RQ7EC5RC6]] is real with the real eigenvalues $1$ and $2$, but its eigenvectors $(1, 0)$ and $(1, 1)$ are not orthogonal, so it is not orthogonally diagonalizable.
Real eigenvalues alone are not enough.

### What it gives you

The trace and the determinant of a Hermitian matrix are real, since they are the sum and the product of the diagonal entries of $D$.
Polynomials are easy to compute, $p(A) = U p(D) U^*$, and the rank of $A$ is the number of nonzero diagonal entries of $D$.
Writing $u_j$ for column $j$ of $U$, the theorem says $A = \sum_j \lambda_j u_j u_j^*$, a sum of rank one matrices, which is [[the spectral decomposition|D5KVBA1K9R]].
The largest and the smallest eigenvalue are the maximum and the minimum of the [[Rayleigh quotient|06WHP8SE98]].

### The converse

The converse is true.
If $A = U D U^*$ with $U$ unitary and $D$ real diagonal, then $A^* = U D^* U^* = U D U^* = A$.
So a complex matrix is Hermitian exactly when it is unitarily diagonalizable with real eigenvalues.
In the same way, $Q D Q^{\mathsf{T}}$ is symmetric for every real orthogonal $Q$ and real diagonal $D$.

### Three spectral theorems

Books use the name "spectral theorem" for three related results.
[[The real spectral theorem|06J4PXRG22]] is about real symmetric matrices, this theorem is about Hermitian matrices, and [[the complex spectral theorem|04CW1P44VD]] is about normal matrices.
Part 2 is the matrix form of the real spectral theorem.
Some books call Hermitian matrices "symmetric" even over $\mathbb{C}$, so check which condition a book means before you apply its theorem.

### Watch out

The eigenvectors must be normalized, or $U$ is not unitary and $U^*$ is not the inverse of $U$.
For $A$ above, the unnormalized matrix $W = \begin{pmatrix} i & 1 \\ 1 & i \end{pmatrix}$ has $W^* W = 2I$, so $W^* A W = \operatorname{diag}(6, -2)$, twice the right answer.
When an eigenvalue is repeated, any basis of its eigenspace works only after Gram-Schmidt makes it orthonormal.

## Explanations

### L1 human

Every Hermitian matrix becomes diagonal after a change to suitable perpendicular complex axes, and the numbers on the diagonal are real.
For a real symmetric matrix, the change of axes is a rotation, possibly with a reflection.
For example, $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ stretches the direction $(1, 1)$ by $3$ and keeps the direction $(1, -1)$ as it is.
These two directions are perpendicular, and in them the matrix is just a stretch by $3$ and a stretch by $1$.

### L2 human

Here is a typical use: decide the shape of the curve $2x^2 + 2xy + 2y^2 = 3$.
The curve is $v^{\mathsf{T}} A v = 3$ with $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ and $v = (x, y)$.
The eigenvalues are $3$ for $(1, 1)$ and $1$ for $(1, -1)$, so part 2 gives
$$A = Q \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix} Q^{\mathsf{T}}, \qquad Q = \tfrac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}.$$
In the new coordinates $w = Q^{\mathsf{T}} v$ the equation is $3 w_1^2 + w_2^2 = 3$, an ellipse with semi-axes $1$ and $\sqrt{3}$.
Check: the point $(x, y) = \tfrac{1}{\sqrt{2}}(1, 1)$ has $w = (1, 0)$ and gives $2 \cdot \tfrac{1}{2} + 2 \cdot \tfrac{1}{2} + 2 \cdot \tfrac{1}{2} = 3$.
This is the principal axis method: change to eigenvector coordinates, solve the problem for the diagonal matrix $D$, and change back.

### L3 human

The Hermitian matrices are the self-adjoint elements of the algebra of complex $n \times n$ matrices.
The theorem says that the unitary group acts on them by conjugation, and that each orbit meets the real diagonal matrices in exactly one matrix, up to the order of the entries.
So the eigenvalues, listed in decreasing order, are a complete invariant for unitary similarity of Hermitian matrices.
In infinite dimension, compact self-adjoint operators have the same kind of diagonal form, and bounded ones need a [[projection-valued measure|X71XRPJR7D]].
The sub-area on positive operators and singular values applies the theorem to $A^* A$ to build the singular value decomposition.
