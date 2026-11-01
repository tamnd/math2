---
tag: JS3695KMCC
kind: definition
name: Unimodular matrix
msc: [15B36, 11C20]
defines: R6RBQHW191
uses: [0JXZKX526R, 00KDZRW4C0, 0EB9N0S33C]
sources:
  - url: https://en.wikipedia.org/wiki/Unimodular_matrix
---

## Definition

Let $n \ge 1$ and let $A$ be an $n \times n$ [[square matrix|0JXZKX526R]] with entries in $\Z$.
The matrix $A$ is *unimodular* when its [[determinant|00KDZRW4C0]] is $1$ or $-1$.

## Remarks

Example: $\begin{pmatrix} 2 & 3 \\ 1 & 2 \end{pmatrix}$ is unimodular, because its determinant is $4 - 3 = 1$.
Non-example: $\begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$ is not unimodular, because its determinant is $2$; its inverse $\begin{pmatrix} 1/2 & 0 \\ 0 & 1 \end{pmatrix}$ is not an integer matrix.
An integer square matrix is unimodular exactly when it is [[invertible|0EB9N0S33C]] and its inverse has integer entries.
This follows from $\det(A)\det(A^{-1}) = 1$ and from the formula of the inverse by the adjugate.
More generally, over a commutative ring $R$, a square matrix is called unimodular when its determinant is a [[unit|0XVEZDE9J8]] of $R$.
