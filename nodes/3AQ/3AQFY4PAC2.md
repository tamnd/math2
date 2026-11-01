---
tag: 3AQFY4PAC2
kind: definition
name: Triangular matrix
msc: [15B99, 15A23]
defines: GTG8MJGDKC
uses: [0B1261B5ED, 0JXZKX526R, 0N4XY7Z3NN, 00J3KZP8Y0]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] and let $A = (a_{ij})$ be an $n \times n$ [[square matrix|0JXZKX526R]] over $R$.
The matrix $A$ is *upper triangular* when $a_{ij} = 0$ for all $i > j$.
It is *lower triangular* when $a_{ij} = 0$ for all $i < j$.
It is *triangular* when it is upper triangular or lower triangular.

## Remarks

Example: $\begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix}$ is triangular, because its entries below the diagonal, in positions $(2,1)$, $(3,1)$, $(3,2)$, are zero.
Non-example: $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ is not triangular, because $a_{21} = 3 \ne 0$ and $a_{12} = 2 \ne 0$.
A matrix is both upper and lower triangular exactly when it is diagonal.
A triangular matrix is *strictly* triangular when its diagonal entries are also zero, and *unit* triangular when they are all $1$.
See also [[upper triangular matrix|0N4XY7Z3NN]] and [[lower triangular matrix|00J3KZP8Y0]].
