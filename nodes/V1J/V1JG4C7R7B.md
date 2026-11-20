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

1. Operator form. Let $V$ be a finite-dimensional complex inner product space, and let $T \colon V \to V$ be linear. Then $V$ has an [[orthonormal basis|0FWJ0VW561]] $e_1, \dots, e_n$ in which the matrix of $T$ is upper triangular. Equivalently, $T e_k \in \operatorname{span}(e_1, \dots, e_k)$ for $k = 1, \dots, n$.
2. Matrix form. Let $A$ be an $n \times n$ complex [[square matrix|0JXZKX526R]]. Then there are a [[unitary matrix|0AR68JTMDT]] $Q$ and an [[upper triangular matrix|0N4XY7Z3NN]] $U$ with
$$A = Q U Q^*,$$
where $Q^*$ is the [[conjugate transpose|0DXKE10PHF]] of $Q$.
The diagonal entries of $U$ are the [[eigenvalues|0BQAA2BK3Q]] of $A$, each repeated as often as its algebraic multiplicity.
3. Real Schur form. Let $A$ be an $n \times n$ real matrix. Then there are a real [[orthogonal matrix|0QRBVFJ50X]] $Q$ and a real block upper triangular matrix $M$ with $A = Q M Q^T$. Each diagonal block of $M$ is $1 \times 1$ or is a $2 \times 2$ block with no real eigenvalue.

In part 3, the $1 \times 1$ blocks are the real eigenvalues of $A$, and each $2 \times 2$ block carries a pair of conjugate non-real eigenvalues.

## Remarks

### Why each hypothesis is needed

- Part 1 needs a complex space. [[The rotation by a right angle|~369bb802]] on $\mathbb{R}^2$ has no eigenvalue, so no real basis makes its matrix triangular. The real Schur form of part 3 is the best possible over $\mathbb{R}$.
- A real matrix with only real eigenvalues has a real Schur form with only $1 \times 1$ blocks. So it is orthogonally similar to a real upper triangular matrix, as [[the Schur form of a defective matrix|~56036455]] shows.
- The theorem does not give a diagonal $U$. The matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ is already upper triangular, and it is not similar to a diagonal matrix.

### Consequences

- The trace of $A$ is the sum of the eigenvalues, and the determinant is their product, since $A$ and $U$ are similar.
- [[The complex spectral theorem|04CW1P44VD]]: if $A$ is normal, then $U$ is normal and upper triangular, hence diagonal.
- [[The real normal form|~abc653f3]]: if a real $A$ is normal, then $M$ is block diagonal, with $1 \times 1$ blocks and $2 \times 2$ blocks of the form $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$.
- The order of the eigenvalues on the diagonal of $U$ can be chosen freely. The proof picks an eigenvector for any eigenvalue at each step.

### Converse

Every matrix of the form $Q U Q^*$ is a complex square matrix, so the converse has no content.
The decomposition is not unique: for $A = I$, every unitary $Q$ works with $U = I$.

### Generalizations

- [[Triangularization|0363JMQ42Y]] over any field gives a triangular matrix similar to $A$ when the characteristic polynomial splits. Schur adds that the change of basis can be unitary.
- A commuting family of complex matrices can be triangularized by one unitary matrix.
- The generalized Schur decomposition treats pairs $(A, B)$ with $A = Q S Z^*$ and $B = Q T Z^*$, where $Q$ and $Z$ are unitary and $S$ and $T$ are upper triangular.

## Explanations

### L1 human

Every complex square matrix becomes upper triangular after a change to a suitable orthonormal basis.
The eigenvalues then sit on the diagonal.
Unlike diagonalization, this always works, and the change of basis keeps all lengths and angles.
For real matrices, some $2 \times 2$ blocks must stay on the diagonal, one for each pair of complex eigenvalues.

### L2 human

Worked example: [[a real matrix with a repeated eigenvalue|~56036455]].

1. Let $A = \begin{pmatrix} 1 & 2 \\ -2 & 5 \end{pmatrix}$. Its characteristic polynomial is $t^2 - 6t + 9 = (t - 3)^2$.
2. The eigenvalue $3$ has the eigenvector $(1, 1)$, since $A(1, 1) = (3, 3)$. Normalize it to $q_1 = \tfrac{1}{\sqrt{2}}(1, 1)$.
3. Extend by $q_2 = \tfrac{1}{\sqrt{2}}(-1, 1)$, and let $Q$ have the columns $q_1$ and $q_2$.
4. Then $Q^T A Q = \begin{pmatrix} 3 & 4 \\ 0 & 3 \end{pmatrix}$, an upper triangular matrix with the eigenvalue $3$ twice on the diagonal.

The typical use is to prove facts about eigenvalues with a triangular matrix, without diagonalizing.
The [[QR algorithm|B6F8YWHYZ5]] computes the Schur form, and it is the standard numerical method for eigenvalues.
A trap: the Schur form is not unique, and the entries above the diagonal depend on the choice of $Q$.

### L3 human

In terms of flags, part 1 says that every operator on a complex inner product space fixes a full flag $0 \subset V_1 \subset \dots \subset V_n = V$ with orthonormal steps.
The Gram-Schmidt process turns any invariant flag from [[triangularization|0363JMQ42Y]] into such an orthonormal flag.
Unitary similarity is a finer relation than similarity, and the entries above the diagonal of $U$ measure how far $A$ is from normal: $\sum \abs{u_{ij}}^2$ over $i < j$ is the same for every Schur form of $A$.
The real Schur form is the output of the real QR algorithm, and it avoids complex arithmetic.
