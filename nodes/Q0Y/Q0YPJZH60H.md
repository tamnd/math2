---
tag: Q0YPJZH60H
kind: definition
name: Tridiagonal matrix
msc: [15B99, 65F05]
defines: DARX1KZRHZ
uses: [0B1261B5ED, 0JXZKX526R]
sources:
  - url: https://en.wikipedia.org/wiki/Tridiagonal_matrix
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] and let $A = (a_{ij})$ be an $n \times n$ [[square matrix|0JXZKX526R]] over $R$.
The matrix $A$ is *tridiagonal* when $a_{ij} = 0$ for all $i, j$ with $\abs{i - j} > 1$.

## Remarks

Example: $\begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{pmatrix}$ is tridiagonal, because the only entries with $\abs{i - j} > 1$ are $a_{13}$ and $a_{31}$, and both are $0$.
Non-example: $\begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ is not tridiagonal, because $a_{13} = 1$ and $\abs{1 - 3} = 2$.
A tridiagonal matrix is often written with diagonal $a_1, \dots, a_n$, superdiagonal $b_1, \dots, b_{n-1}$ and subdiagonal $c_1, \dots, c_{n-1}$.
Then the leading principal minors $f_k$ satisfy $f_k = a_k f_{k-1} - b_{k-1} c_{k-1} f_{k-2}$, with $f_0 = 1$ and $f_{-1} = 0$.
Equivalently, $A$ is tridiagonal when it is both upper and lower [[Hessenberg|YCEEWJTX56]].
