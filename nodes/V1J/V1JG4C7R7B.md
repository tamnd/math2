---
tag: V1JG4C7R7B
kind: statement
role: theorem
name: Schur decomposition
aliases: [schur-unitary-triangularization, real-schur-form]
msc: ["15A23", "15A21"]
topics: [3YM9EK6VMB]
audience: ug1
uses: [0JXZKX526R, 0AR68JTMDT, 0N4XY7Z3NN, 0DXKE10PHF, 0BQAA2BK3Q, 0FWJ0VW561, 0QRBVFJ50X]
about: [0AR68JTMDT, 0N4XY7Z3NN]
sources:
  - url: https://en.wikipedia.org/wiki/Schur_decomposition
  - url: https://en.wikipedia.org/wiki/Schur_decomposition
    locator: Statement
  - url: https://en.wikipedia.org/wiki/Schur_decomposition
    locator: Proof
  - book: isbn:9783031410253
    locator: Chapter 6
  - book: isbn:9780134860244
    locator: Section 6.4
same_as:
  wikidata: Q1064218
  wikipedia: Schur decomposition
---

## Statement

Every complex square matrix becomes upper triangular in a suitable orthonormal basis, so we can triangularize without giving up lengths and angles.

1. Operator form. Let $V$ be a finite-dimensional complex inner product space, and let $T \colon V \to V$ be linear. Then $V$ has an [[orthonormal basis|0FWJ0VW561]] $e_1, \dots, e_n$ in which the matrix of $T$ is upper triangular. Equivalently, $T e_k \in \operatorname{span}(e_1, \dots, e_k)$ for $k = 1, \dots, n$.
2. Matrix form. Let $A$ be an $n \times n$ complex [[square matrix|0JXZKX526R]]. Then there are a [[unitary matrix|0AR68JTMDT]] $Q$ and an [[upper triangular matrix|0N4XY7Z3NN]] $U$ with $A = Q U Q^*$, where $Q^*$ is the [[conjugate transpose|0DXKE10PHF]] of $Q$. The diagonal entries of $U$ are the [[eigenvalues|0BQAA2BK3Q]] of $A$, each repeated as often as its algebraic multiplicity.
3. Real Schur form. Let $A$ be an $n \times n$ real matrix. Then there are a real [[orthogonal matrix|0QRBVFJ50X]] $Q$ and a real block upper triangular matrix $M$ with $A = Q M Q^{\mathsf{T}}$, in which each diagonal block is $1 \times 1$ or is a $2 \times 2$ block with no real eigenvalue.

In part 3, the $1 \times 1$ blocks are the real eigenvalues of $A$, and each $2 \times 2$ block carries one pair of conjugate non-real eigenvalues.
If every eigenvalue of the real matrix $A$ is real, then $M$ has only $1 \times 1$ blocks, so $A$ is orthogonally similar to a real upper triangular matrix.

## Remarks

### A first case

Take $A = \begin{pmatrix} 1 & 2 \\ -2 & 5 \end{pmatrix}$, worked out in [[the Schur form of a real matrix with a repeated eigenvalue|HFW74NJ8G3]].
Its characteristic polynomial is $(1 - t)(5 - t) + 4 = (t - 3)^2$, and $A(1, 1) = (3, 3)$, so $q_1 = \tfrac{1}{\sqrt{2}}(1, 1)$ is a unit eigenvector.
Complete it with $q_2 = \tfrac{1}{\sqrt{2}}(-1, 1)$ and let $Q$ have the columns $q_1, q_2$.
Then
$$Q^{\mathsf{T}} A Q = \begin{pmatrix} 3 & 4 \\ 0 & 3 \end{pmatrix}.$$
Check: the sum of the squares of the entries is $1 + 4 + 4 + 25 = 34$ for $A$ and $9 + 16 + 9 = 34$ for the triangular form, as it must be for an orthogonal change of basis.
The matrix $A$ has only one line of eigenvectors, so no basis at all makes it diagonal, but Schur still makes it triangular.

### Why each hypothesis is needed

Part 1 needs a complex space.
[[The rotation by a right angle|1CF483TZZA]] on $\mathbb{R}^2$ has the eigenvalues $\pm i$ and no real eigenvector.
A triangular real matrix has a real eigenvector, namely its first basis vector, so no real basis makes the rotation triangular.
This is why part 3 keeps $2 \times 2$ blocks, and why the real triangular form exists only when all the eigenvalues are real.

Finite dimension is needed for the induction, which starts from one eigenvalue.
In infinite dimension an operator can have no eigenvalue at all, and the statement has no direct analogue.

### What it gives you

The theorem gives a triangular matrix, and a triangular matrix shows its eigenvalues on the diagonal.
So the trace of $A$ is the sum of the eigenvalues and the determinant is their product, with multiplicity, because $A$ and $U$ are similar.

The main use of the theorem is [[the complex spectral theorem|04CW1P44VD]].
If $A$ is normal, then $U = Q^* A Q$ is normal too, and a normal upper triangular matrix is diagonal.
In the same way, for a real normal matrix the real Schur form becomes block diagonal, which is [[the real normal form|G6T1FNE3JC]].
The order of the eigenvalues on the diagonal of $U$ can be chosen freely, because the proof may start from any eigenvalue.

### The converse and uniqueness

Every matrix $Q U Q^*$ is a complex square matrix, so the converse has no content.
The decomposition is not unique.
For $A = I$, every unitary $Q$ works with $U = I$.
In the first case above, the choice $q_2 = \tfrac{1}{\sqrt{2}}(1, -1)$ gives the Schur form $\begin{pmatrix} 3 & -4 \\ 0 & 3 \end{pmatrix}$ instead.
What does not change is the sum $\sum_{i < j} \abs{u_{ij}}^2$ of the squares above the diagonal, since the total sum of squares and the diagonal are both fixed.
This sum is $0$ exactly when $A$ is normal, so it measures how far $A$ is from normal.

### Generalizations

[[Triangularization|0363JMQ42Y]] over any field gives a triangular matrix similar to $A$ whenever the characteristic polynomial splits, and Schur adds that over $\mathbb{C}$ the change of basis can be unitary.
A commuting family of complex matrices can be triangularized by one unitary matrix.
The generalized Schur decomposition treats a pair $(A, B)$ as $A = Q S Z^*$ and $B = Q T Z^*$, with $Q$ and $Z$ unitary and $S$ and $T$ upper triangular.

### Watch out

The theorem gives a triangular matrix, not a diagonal one.
The matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ is its own Schur form, and it is not similar to any diagonal matrix.
A second trap is to apply part 2 to a real matrix with non-real eigenvalues and expect a real $Q$.
For the rotation by a right angle, the unitary $Q$ must have non-real entries, and a real $Q$ gives only the real Schur form with one $2 \times 2$ block.

## History

Issai Schur published the unitary triangularization in 1909.

## Explanations

### L1 human

Every complex square matrix becomes a triangle of numbers after a change to suitable perpendicular axes of unit length.
The eigenvalues then sit on the diagonal.
Unlike diagonalization, this always works, and the change of axes keeps all lengths and angles.
For real matrices, some $2 \times 2$ blocks must stay on the diagonal, one for each pair of complex eigenvalues.

### L2 human

Here is the recipe for a $2 \times 2$ complex matrix, worked for $A = \begin{pmatrix} 2 & 1 \\ -1 & 0 \end{pmatrix}$.
The characteristic polynomial is $t^2 - 2t + 1 = (t - 1)^2$, and the kernel of $A - I = \begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix}$ is spanned by $(1, -1)$.
Take $q_1 = \tfrac{1}{\sqrt{2}}(1, -1)$ and the orthogonal unit vector $q_2 = \tfrac{1}{\sqrt{2}}(1, 1)$.
Then $A q_2 = \tfrac{1}{\sqrt{2}}(3, -1)$, so
$$q_1^{\mathsf{T}} A q_2 = \tfrac{1}{2}(3 + 1) = 2, \qquad q_2^{\mathsf{T}} A q_2 = \tfrac{1}{2}(3 - 1) = 1.$$
Since $A q_1 = q_1$, the first column of the new matrix is $(1, 0)$, and the Schur form is $\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$.
Check: the sum of squares is $4 + 1 + 1 + 0 = 6$ for $A$ and $1 + 4 + 1 = 6$ for the Schur form.
The typical use is to prove facts about eigenvalues with a triangular matrix when diagonalization is not available.
The [[QR algorithm|B6F8YWHYZ5]] computes the Schur form, and it is the standard numerical method for eigenvalues.

### L3 human

In the language of flags, part 1 says that every operator on a complex inner product space fixes a full flag $0 \subset V_1 \subset \dots \subset V_n = V$ whose steps are orthogonal.
The Gram-Schmidt process turns any invariant flag from [[triangularization|0363JMQ42Y]] into such an orthonormal flag, because it keeps each span $V_k$ the same.
Unitary similarity is a finer relation than similarity, and the part of $U$ above the diagonal carries the extra information.
The real Schur form is the output of the real QR algorithm, which avoids complex arithmetic.
