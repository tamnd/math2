---
tag: 0MKABWDRNC
kind: definition
name: Upper triangular matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
defines: 0N4XY7Z3NN
uses: [0CP7YY6NAG]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: lead section
inventory: [1W8C1QV0S3]
---

## Definition

Let $R$ be a ring and let $n \ge 0$ be an integer.
A [[square matrix|0CP7YY6NAG]] $U = (u_{ij})$ of order $n$ over $R$ is *upper triangular* when $u_{ij} = 0$ for all $i > j$.
It is *strictly upper triangular* when $u_{ij} = 0$ for all $i \ge j$.
It is *lower triangular* when $u_{ij} = 0$ for all $i < j$, and *strictly lower triangular* when $u_{ij} = 0$ for all $i \le j$.

## Notation

- A matrix is *triangular* when it is upper or lower triangular.
- The [[lower triangular matrix|00J3KZP8Y0]] has its own page.

## Remarks

- Sums and products of upper triangular matrices of the same order are upper triangular, by the [[product theorem|45RET2Y995]].
- The [[determinant of a triangular matrix|0K1KKMFHYH]] is the product of its diagonal entries.
- The diagonal entries of an upper triangular matrix over a field are its [[eigenvalues|0BQAA2BK3Q]].
- A system $Ux = b$ with $U$ upper triangular and invertible is solved by [[back substitution|0ATFVE08MW]].

## Explanations

### L1 human

An upper triangular matrix has only zeros below the main diagonal.
For example, $\begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix}$ is upper triangular.

### L2 human

The condition $u_{ij} = 0$ for $i > j$ says that row $i$ starts with at least $i - 1$ zeros.
The strict condition asks for at least $i$ zeros, so the diagonal is zero too.
