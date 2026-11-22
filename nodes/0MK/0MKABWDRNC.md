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

We define the square matrices whose entries on one side of the main diagonal are all zero.
Let $R$ be a ring and let $n \ge 1$ be an integer.
A [[square matrix|0CP7YY6NAG]] $U = (u_{ij})$ of order $n$ over $R$ is *upper triangular* when $u_{ij} = 0$ for all $i > j$.
It is *strictly upper triangular* when $u_{ij} = 0$ for all $i \ge j$.
It is *lower triangular* when $u_{ij} = 0$ for all $i < j$, and *strictly lower triangular* when $u_{ij} = 0$ for all $i \le j$.
A matrix is *triangular* when it is upper triangular or lower triangular.

## Notation

Upper triangular matrices are often written $U$ or $R$, and lower triangular ones $L$.
A triangular matrix with all diagonal entries equal to $1$ is called *unitriangular*.
The [[lower triangular matrix|00J3KZP8Y0]] has its own page.

## Remarks

The condition $i > j$ picks out the positions below the main diagonal, where the row index is larger than the column index.
So row $i$ of an upper triangular matrix starts with at least $i - 1$ zeros, and the strict version asks for at least $i$ zeros, which makes the diagonal zero too.
The definition asks for a square matrix, so that the main diagonal runs from corner to corner and products of two such matrices are defined.

For example, $\begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix}$ is upper triangular, and $\begin{pmatrix} 0 & 2 & 3 \\ 0 & 0 & 5 \\ 0 & 0 & 0 \end{pmatrix}$ is strictly upper triangular.
The matrix $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ fails the condition, since its entry $u_{21} = 3$ lies below the diagonal and is not $0$.
A diagonal matrix satisfies both the upper and the lower condition.

The concept page on the [[upper triangular matrix|0N4XY7Z3NN]] shows why the shape survives products, by the [[product theorem|45RET2Y995]], and why the diagonal gives the [[determinant|0K1KKMFHYH]] and the [[eigenvalues|0BQAA2BK3Q]].
It also explains how systems $Ux = b$ are solved by [[back substitution|0ATFVE08MW]].

## Explanations

### L1 human

An upper triangular matrix has only zeros below the main diagonal.
In $\begin{pmatrix} 1 & 2 \\ 0 & 4 \end{pmatrix}$ the only entry below the diagonal is the $0$ in the bottom left corner.
"Strictly" means that the diagonal is zero as well, as in $\begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix}$.

### L2 human

To test the condition, check each position with row index larger than column index.
For order $3$ these are the positions $(2, 1)$, $(3, 1)$ and $(3, 2)$, so a $3 \times 3$ matrix is upper triangular when these three entries are $0$.
Watch out: the transpose swaps the two conditions, so $U$ is upper triangular exactly when $U^{\mathsf{T}}$ is lower triangular.
