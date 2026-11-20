---
tag: 5RQ7EC5RC6
kind: counterexample
name: A real matrix with real eigenvalues that is not orthogonally diagonalizable
msc: ["15A18", "15A21"]
topics: [3YM9EK6VMB]
audience: ug1
uses: [06J4PXRG22, 04CW1P44VD, 0N28QN4CYA, 0ENZN5G4CV, 0QRBVFJ50X, 07SQCNV233]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_theorem
    locator: Hermitian maps and Hermitian matrices
  - book: isbn:9783031410253
    locator: Chapter 7
---

## Counterexample

Let $A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$ act on $\mathbb{R}^2$ with the dot product.
The matrix is real, and its eigenvalues $1$ and $2$ are real.
But no orthogonal matrix $Q$ makes $Q^T A Q$ diagonal.

1. $A$ is upper triangular, so its eigenvalues are the diagonal entries $1$ and $2$.
2. The kernel of $A - I = \begin{pmatrix} 0 & 1 \\ 0 & 1 \end{pmatrix}$ is the line spanned by $(1, 0)$.
3. The kernel of $A - 2I = \begin{pmatrix} -1 & 1 \\ 0 & 0 \end{pmatrix}$ is the line spanned by $(1, 1)$.
4. So $(1, 0)$ and $(1, 1)$ form a basis of eigenvectors, and $A$ is [[diagonalizable|07SQCNV233]].
5. Every eigenvector is a nonzero multiple of $(1, 0)$ or of $(1, 1)$, because the two eigenspaces are lines.
6. The dot product $(1, 0) \cdot (1, 1) = 1$ is not $0$. So a vector of the first line and a vector of the second line are never orthogonal, unless one of them is $0$.
7. So $\mathbb{R}^2$ has no orthonormal basis of eigenvectors of $A$. Then no [[orthogonal matrix|0QRBVFJ50X]] $Q$ makes $Q^T A Q$ diagonal, because its columns would be such a basis.
8. This agrees with [[the real spectral theorem|06J4PXRG22]]: $A^T = \begin{pmatrix} 1 & 0 \\ 1 & 2 \end{pmatrix} \neq A$, so $A$ is not [[symmetric|0N28QN4CYA]].

## Remarks

- The matrix is not [[normal|0ENZN5G4CV]] either: $A A^T = \begin{pmatrix} 2 & 2 \\ 2 & 4 \end{pmatrix}$ and $A^T A = \begin{pmatrix} 1 & 1 \\ 1 & 5 \end{pmatrix}$. So also over $\mathbb{C}$ there is no orthonormal eigenbasis, by [[the complex spectral theorem|04CW1P44VD]].
- A second trap matrix is [[the shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$|BF9MKKHH4Z]]. Its only eigenvalue $1$ is real, but it has no basis of eigenvectors at all.
- The example refutes the claim "a real matrix with real eigenvalues is orthogonally diagonalizable". Real eigenvalues give only a real orthogonal triangular form, by [[the Schur decomposition|V1JG4C7R7B]].

## Explanations

### L1 human

This matrix stretches two directions, by $1$ and by $2$.
The two directions are $(1, 0)$ and $(1, 1)$, and they make an angle of $45$ degrees.
A symmetric matrix always has perpendicular stretch directions, so this matrix is not symmetric.

### L2 human

How to test whether a real matrix is orthogonally diagonalizable:

1. Check whether $A^T = A$. By the real spectral theorem, this is the exact condition.
2. Here $A^T \neq A$, so the answer is no, before any computation of eigenvectors.
3. A direct check gives the same answer: the eigenspaces are lines that are not perpendicular.

A trap: diagonalizable, real eigenvalues and triangular are all weaker than symmetric.
