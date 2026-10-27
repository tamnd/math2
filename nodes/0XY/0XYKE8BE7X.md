---
tag: 0XYKE8BE7X
kind: definition
name: Normal matrix
msc: [15B57, 15A21]
defines: 0MR0BYF0K2
uses: [0EX045E2BP]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_matrix
    locator: lead section
inventory: [A68TH0944V]
---

## Definition

Let $A$ be an $n \times n$ complex matrix.
The matrix $A$ is *normal* when
$$A A^* = A^* A,$$
where $A^*$ is the [[conjugate transpose|0DXKE10PHF]] of $A$.

## Remarks

Hermitian, skew-Hermitian and unitary matrices are normal.
A real matrix is normal when $A A^T = A^T A$; real symmetric and orthogonal matrices are examples.
The matrix $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ is not normal.
A matrix is normal if and only if its map on $\C^n$ is a [[normal operator|0C8BR8XRTR]] for the standard inner product.

## Explanations

### L1 human

A matrix is normal when it commutes with its conjugate transpose.
Normal matrices are exactly the matrices that a unitary change of basis makes diagonal.
They include the symmetric, the Hermitian and the unitary matrices.
