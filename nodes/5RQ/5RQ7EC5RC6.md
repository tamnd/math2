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

A tempting claim says that a real matrix with real eigenvalues can be diagonalized by an orthogonal matrix.
The matrix
$$A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$$
on $\mathbb{R}^2$ with the dot product refutes it: its eigenvalues are real, it is even diagonalizable, but no orthogonal matrix $Q$ makes $Q^{\mathsf{T}} A Q$ diagonal.

1. Real eigenvalues. $A$ is upper triangular, so its eigenvalues are its diagonal entries $1$ and $2$.
2. The first eigenspace. The matrix $A - I$ has the rows $(0, 1)$ and $(0, 1)$, so its kernel is the line spanned by $(1, 0)$.
3. The second eigenspace. The matrix $A - 2I$ has the rows $(-1, 1)$ and $(0, 0)$, so its kernel is the line spanned by $(1, 1)$. Check: $A(1, 1) = (2, 2)$.
4. Diagonalizable. The vectors $(1, 0)$ and $(1, 1)$ are independent, so they form a basis of eigenvectors, and $A$ is [[diagonalizable|07SQCNV233]].
5. No orthonormal eigenbasis. Every eigenvector is a nonzero multiple of $(1, 0)$ or of $(1, 1)$, because each eigenspace is a line. For nonzero $a$ and $b$, the dot product $a(1, 0) \cdot b(1, 1) = ab$ is not $0$, so an eigenvector from one line is never orthogonal to one from the other line. Two eigenvectors from the same line are never orthogonal either.
6. No orthogonal $Q$. If $Q^{\mathsf{T}} A Q = D$ were diagonal with $Q$ [[orthogonal|0QRBVFJ50X]], then $AQ = QD$, and the columns of $Q$ would be an orthonormal basis of eigenvectors. Step 5 rules this out.
7. The reason. $A^{\mathsf{T}}$ has the rows $(1, 0)$ and $(1, 2)$, so $A^{\mathsf{T}} \neq A$ and $A$ is not [[symmetric|0N28QN4CYA]]. This agrees with the [[real spectral theorem|06J4PXRG22]], which makes symmetry the exact condition.

## Remarks

The two eigenlines meet at an angle of $45$ degrees, since $\cos \theta = \frac{(1, 0) \cdot (1, 1)}{1 \cdot \sqrt{2}} = \frac{1}{\sqrt{2}}$.
If you replace the entry $1$ in the corner by $c$, the second eigenline is spanned by $(c, 1)$, and the angle shrinks toward $0$ as $c$ grows.
Only $c = 0$ makes the eigenlines perpendicular, and that is exactly the case where the matrix is symmetric.

The matrix is not [[normal|0ENZN5G4CV]] either, since
$$A A^{\mathsf{T}} = \begin{pmatrix} 2 & 2 \\ 2 & 4 \end{pmatrix} \neq \begin{pmatrix} 1 & 1 \\ 1 & 5 \end{pmatrix} = A^{\mathsf{T}} A.$$
So even over $\mathbb{C}$ there is no orthonormal basis of eigenvectors, by the [[complex spectral theorem|04CW1P44VD]].
What real eigenvalues do give is a triangular form: by the [[Schur decomposition|V1JG4C7R7B]], a real matrix whose eigenvalues are all real is orthogonally similar to an upper triangular matrix, and $A$ is already one.
A sharper trap is the [[shear|BF9MKKHH4Z]] with rows $(1, 1)$ and $(0, 1)$: its only eigenvalue $1$ is real, but it has no basis of eigenvectors at all.

## Explanations

### L1 human

This matrix stretches two directions, one by $1$ and one by $2$.
The two directions are $(1, 0)$ and $(1, 1)$, and they make an angle of $45$ degrees.
A symmetric matrix always has perpendicular stretch directions, so this matrix cannot be symmetric, and no rotation of the axes makes it diagonal.

### L2 human

To test whether a real matrix is orthogonally diagonalizable, first check whether $A^{\mathsf{T}} = A$, because the real spectral theorem makes this the exact condition.
Here $A^{\mathsf{T}} \neq A$, so the answer is no before any eigenvector is computed.
The direct check of steps 2 to 5 gives the same answer, because the eigenspaces are lines that are not perpendicular.
Watch out: being diagonalizable, having real eigenvalues and being triangular are all weaker than being symmetric.
