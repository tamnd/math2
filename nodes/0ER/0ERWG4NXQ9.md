---
tag: 0ERWG4NXQ9
kind: statement
role: theorem
name: QR decomposition
msc: [15A23, 65F25]
uses: [0D6RMJ10M9, 0MKABWDRNC, 0VT6P0GNQR]
sources:
  - url: https://en.wikipedia.org/wiki/QR_decomposition
    locator: Square matrix
same_as:
  wikidata: Q653242
  wikipedia: QR decomposition
---

## Statement

Let $A$ be an $n \times n$ complex matrix.
Then there are a [[unitary matrix|0AR68JTMDT]] $Q$ and an [[upper triangular matrix|0N4XY7Z3NN]] $R$ with
$$A = QR.$$
If $A$ is real, then $Q$ and $R$ can be chosen real, with $Q$ orthogonal.
If $A$ is invertible and the diagonal entries of $R$ are required to be positive, then $Q$ and $R$ are unique.

## Remarks

For an invertible $A$, the [[Gram–Schmidt process|0VT6P0GNQR]] applied to the columns of $A$ gives the columns of $Q$.
A rectangular $m \times n$ matrix with $m \ge n$ has a decomposition $A = QR$ with $Q$ unitary $m \times m$ and $R$ upper triangular $m \times n$.
Householder reflections and Givens rotations compute it stably.
It is used to solve least squares problems and in the QR algorithm for eigenvalues.

## Explanations

### L1 human

The QR decomposition writes a matrix as a rotation, possibly with reflections, times a triangular matrix.
The columns of $Q$ are orthonormal, and $R$ records how to rebuild the columns of $A$ from them.
It is the matrix form of the Gram–Schmidt process.
