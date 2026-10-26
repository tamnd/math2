---
tag: 0EKZCX4K3P
kind: definition
name: Hermitian matrix
msc: [15B57]
defines: 0P17NGQQMQ
uses: [0EX045E2BP, 0CP7YY6NAG]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_matrix
    locator: lead section
---

## Definition

Let $A = (a_{ij})$ be an $n \times n$ complex [[square matrix|0JXZKX526R]].
The matrix $A$ is *Hermitian* when $A^* = A$, where $A^*$ is the [[conjugate transpose|0DXKE10PHF]] of $A$.
Equivalently, $a_{ij} = \overline{a_{ji}}$ for all $i$ and $j$.

## Remarks

The diagonal entries of a Hermitian matrix are real.
A real matrix is Hermitian if and only if it is [[symmetric|0VR671PHE5]].
The eigenvalues of a Hermitian matrix are real, and $\C^n$ has an orthonormal basis of eigenvectors, by the [[spectral theorem for Hermitian matrices|0DGZBQWZWN]].
The matrix $\begin{pmatrix} 2 & 1 - i \\ 1 + i & 3 \end{pmatrix}$ is Hermitian.

## Explanations

### L1 human

A Hermitian matrix is the complex version of a symmetric matrix.
The entry across the diagonal is the complex conjugate of the entry here.
In quantum mechanics, observable quantities are Hermitian matrices or operators.
