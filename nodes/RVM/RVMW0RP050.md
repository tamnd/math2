---
tag: RVMW0RP050
kind: definition
name: Hessenberg matrix
msc: [15B99, 65F15]
defines: YCEEWJTX56
uses: [0B1261B5ED, 0JXZKX526R]
sources:
  - url: https://en.wikipedia.org/wiki/Hessenberg_matrix
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] and let $A = (a_{ij})$ be an $n \times n$ [[square matrix|0JXZKX526R]] over $R$.
The matrix $A$ is *upper Hessenberg* when $a_{ij} = 0$ for all $i > j + 1$.
It is *lower Hessenberg* when $a_{ij} = 0$ for all $j > i + 1$.

## Remarks

Example: $\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 0 & 7 & 8 \end{pmatrix}$ is upper Hessenberg, because its only entry with $i > j + 1$ is $a_{31} = 0$.
Non-example: $\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$ is not upper Hessenberg, because $a_{31} = 7 \ne 0$.
Every [[upper triangular matrix|0N4XY7Z3NN]] is upper Hessenberg.
A matrix that is both upper and lower Hessenberg is a [[tridiagonal matrix|DARX1KZRHZ]].
An upper Hessenberg matrix is *unreduced* when all its subdiagonal entries $a_{i+1, i}$ are nonzero.
