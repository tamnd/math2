---
tag: 0DGZBQWZWN
kind: statement
role: theorem
name: Spectral theorem for Hermitian matrices
msc: [15A18, 15B57]
uses: [06J4PXRG22, 0EKZCX4K3P, 0D6RMJ10M9]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_theorem
    locator: Hermitian maps and Hermitian matrices
---

## Statement

Let $A$ be a [[Hermitian|0P17NGQQMQ]] $n \times n$ complex matrix.
Then there are a [[unitary matrix|0AR68JTMDT]] $U$ and a real diagonal matrix $D$ with
$$A = U D U^*.$$
If $A$ is a real [[symmetric matrix|0VR671PHE5]], then $U$ can be chosen real, that is, [[orthogonal|0W02QESPJQ]]: $A = Q D Q^T$.

## Remarks

The diagonal entries of $D$ are the eigenvalues of $A$, and the columns of $U$ are orthonormal eigenvectors.
This is the matrix form of the [[spectral theorem|06J4PXRG22]].
For example, $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} = Q \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix} Q^T$ with $Q = \frac{1}{\sqrt 2} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$.

## Explanations

### L1 human

Every Hermitian matrix is diagonal after a unitary change of coordinates.
The new coordinate axes are perpendicular eigenvectors.
For real symmetric matrices, this is a rotation, possibly with a reflection, of the axes.
