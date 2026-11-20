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

1. Let $A$ be a [[Hermitian|0EKZCX4K3P]] $n \times n$ complex matrix, so $A^* = A$.
Then there are a [[unitary matrix|0D6RMJ10M9]] $U$ and a real diagonal matrix $D$ with
$$A = U D U^*.$$
2. Let $A$ be a real [[symmetric|0N28QN4CYA]] $n \times n$ matrix.
Then there are a real [[orthogonal matrix|0QRBVFJ50X]] $Q$ and a real diagonal matrix $D$ with
$$A = Q D Q^T.$$

The diagonal entries of $D$ are the eigenvalues of $A$, repeated by multiplicity.
The columns of $U$, or of $Q$, are an orthonormal basis of eigenvectors.

## Remarks

### Why each hypothesis is needed

- The condition $A^* = A$ cannot be replaced by $A^T = A$ for complex matrices. [[The complex symmetric matrix|DAZBNZXZK7]] $\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$ has the eigenvalues $1 \pm i$, so no real $D$ is possible.
- A normal matrix that is not Hermitian still has the form $U D U^*$, by [[the complex spectral theorem|04CW1P44VD]]. But then $D$ is not real. The same matrix $\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$ is normal, with $D = \operatorname{diag}(1 + i, 1 - i)$.
- In part 2, the symmetry of $A$ is needed for a real orthogonal $Q$. [[The trap matrices|~3859cd16]] are real with real eigenvalues, but they are not orthogonally diagonalizable.

### Consequences

- The trace and the determinant of a Hermitian matrix are real, because they are the sum and the product of the diagonal entries of $D$.
- Powers and polynomials are easy to compute: $p(A) = U p(D) U^*$.
- The rank of $A$ is the number of nonzero diagonal entries of $D$.
- $A$ is the sum $\sum_j \lambda_j u_j u_j^*$ of rank one matrices, where $u_j$ is column $j$ of $U$. This is [[the spectral decomposition|~e55cbc04]].
- The largest and the smallest eigenvalue are the maximum and the minimum of the [[Rayleigh quotient|06WHP8SE98]].

### Converse

The converse is true.
If $A = U D U^*$ with $U$ unitary and $D$ real diagonal, then $A^* = U D^* U^* = U D U^* = A$.
So a complex matrix is Hermitian if and only if it is unitarily diagonalizable with real eigenvalues.
In the same way, $Q D Q^T$ is symmetric for every real orthogonal $Q$ and real diagonal $D$.

### Three spectral theorems

The name "spectral theorem" is used for three related results.
[[The real spectral theorem|06J4PXRG22]] is about real symmetric matrices, this page is about Hermitian matrices, and [[the complex spectral theorem|04CW1P44VD]] is about normal matrices.
Part 2 of this page is the matrix form of the real spectral theorem.
Some books call Hermitian matrices "symmetric", also over $\mathbb{C}$.
Check which condition a book means before you apply its theorem.

## Explanations

### L1 human

Every Hermitian matrix is diagonal after a unitary change of coordinates.
The new coordinate axes are perpendicular eigenvectors, and the numbers on the diagonal are real.
For a real symmetric matrix, the change of coordinates is a rotation of the axes, possibly with a reflection.
For example, $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ stretches the direction $(1, 1)$ by $3$ and keeps the direction $(1, -1)$.

### L2 human

Worked example: [[a Hermitian $2 \times 2$ matrix|~d6488332]].

1. Let $A = \begin{pmatrix} 1 & 2i \\ -2i & 1 \end{pmatrix}$. Then $A^* = A$.
2. The characteristic polynomial is $(1 - t)^2 - 4$, with the real roots $3$ and $-1$.
3. Unit eigenvectors are $u_1 = \tfrac{1}{\sqrt{2}}(i, 1)$ for $3$ and $u_2 = \tfrac{1}{\sqrt{2}}(1, i)$ for $-1$. They are orthogonal.
4. With $U = \tfrac{1}{\sqrt{2}} \begin{pmatrix} i & 1 \\ 1 & i \end{pmatrix}$, we get $A = U \operatorname{diag}(3, -1) U^*$.

A real example is [[the symmetric $3 \times 3$ matrix with eigenvalues $3$, $4$ and $6$|~1a3781ab]].
The typical use is to change to the eigenvector coordinates, solve the problem for the diagonal matrix $D$, and change back.
A trap: the eigenvectors must be normalized, or $U$ is not unitary and $U^*$ is not the inverse of $U$.

### L3 human

The Hermitian matrices are the self-adjoint elements of the algebra of complex $n \times n$ matrices.
The theorem says that the unitary group acts on them by conjugation, and each orbit meets the real diagonal matrices.
The orbit meets them in one diagonal matrix, up to the order of the entries.
In infinite dimension, compact self-adjoint operators have the same kind of diagonal form, and bounded ones need a [[projection-valued measure|X71XRPJR7D]].
