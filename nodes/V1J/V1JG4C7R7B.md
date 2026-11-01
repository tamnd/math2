---
tag: V1JG4C7R7B
kind: statement
role: theorem
name: Schur decomposition
msc: [15A23, 15A21]
uses: [0JXZKX526R, 0AR68JTMDT, 0N4XY7Z3NN, 0DXKE10PHF, 0BQAA2BK3Q]
about: [0AR68JTMDT, 0N4XY7Z3NN]
sources:
  - url: https://en.wikipedia.org/wiki/Schur_decomposition
same_as:
  wikidata: Q1064218
  wikipedia: Schur decomposition
---

## Statement

Let $A$ be an $n \times n$ complex [[square matrix|0JXZKX526R]].
Then there are a [[unitary matrix|0AR68JTMDT]] $Q$ and an [[upper triangular matrix|0N4XY7Z3NN]] $T$ such that
$$A = Q T Q^*,$$
where $Q^*$ is the [[conjugate transpose|0DXKE10PHF]] of $Q$.
The diagonal entries of $T$ are the [[eigenvalues|0BQAA2BK3Q]] of $A$, each repeated as often as its algebraic multiplicity.

## Remarks

The proof is by induction on $n$.
Over $\C$, the matrix $A$ has an eigenvector $v$ of norm $1$.
Extend $v$ to an orthonormal basis; in this basis the first column of the matrix of $A$ is $(\lambda, 0, \dots, 0)^T$.
Apply the induction hypothesis to the lower right $(n-1) \times (n-1)$ block.

The order of the eigenvalues on the diagonal of $T$ can be chosen freely.
If $A$ is a [[normal matrix|0MR0BYF0K2]], then $T$ is normal and triangular, hence diagonal; this gives the [[spectral theorem for normal matrices|04CW1P44VD]].
The complex field matters.
A real matrix with non-real eigenvalues has no factorisation $A = QTQ^T$ with $Q$ real orthogonal and $T$ real upper triangular.
Indeed, the diagonal of such a $T$ would hold the eigenvalues of $A$.
The real Schur form uses an orthogonal $Q$ and a block upper triangular $T$ with diagonal blocks of size $1$ or $2$ instead.

## Explanations

### L1 human

Every complex square matrix becomes upper triangular after a change to a suitable orthonormal basis.
The eigenvalues then sit on the diagonal.
Unlike diagonalisation, this always works, and the change of basis keeps all lengths and angles.

### L2 human

The Schur decomposition is the unitary form of [[triangularisation|0363JMQ42Y]].
It is stable to compute, and the [[QR algorithm|B6F8YWHYZ5]] for eigenvalues computes it.
It gives quick proofs that the trace is the sum and the determinant is the product of the eigenvalues.
It is also the standard route to the spectral theorem for normal matrices.
