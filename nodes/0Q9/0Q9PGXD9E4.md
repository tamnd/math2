---
tag: 0Q9PGXD9E4
kind: definition
name: Diagonal matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
defines: 044JNC7ZAA
uses: [0CP7YY6NAG]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.diagonal
    match: variant
sources:
  - url: https://en.wikipedia.org/wiki/Diagonal_matrix
    locator: lead section
  - book: isbn:9780321982384
    locator: Section 2.1
inventory: [EZGPZWYDK2]
---

## Definition

A diagonal matrix is a square matrix whose only nonzero entries lie on the main diagonal.
Let $R$ be a ring and let $n \ge 0$ be an integer.
A [[square matrix|0CP7YY6NAG]] $D = (d_{ij})$ of order $n$ over $R$ is *diagonal* when $d_{ij} = 0$ for all $i \ne j$.
For $d_1, \dots, d_n \in R$, the matrix $\operatorname{diag}(d_1, \dots, d_n)$ is the diagonal matrix with $d_{ii} = d_i$ for each $i$, so that
$$\operatorname{diag}(d_1, \dots, d_n)_{ij} = d_i \, \delta_{ij},$$
where $\delta_{ij}$ is $1$ for $i = j$ and $0$ otherwise.

## Notation

Mathlib builds the matrix from a function with `Matrix.diagonal d`, and it states the property of being diagonal with `Matrix.IsDiag`.
The binding above is to the construction, so it is recorded as a variant of the definition.

## Remarks

The definition asks for a square matrix, because the main diagonal of a square matrix is where the row index equals the column index.
The condition $d_{ij} = 0$ for $i \ne j$ says nothing about the diagonal entries themselves, so they may be zero.
For example, $\operatorname{diag}(2, 0) = \begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix}$ is diagonal, and so is the zero matrix.
The matrix $\begin{pmatrix} 2 & 1 \\ 0 & 0 \end{pmatrix}$ is not, since its entry at $(1, 2)$ is $1$.

The entry formula makes products short.
For two diagonal matrices, the sum over $k$ in the product keeps only the term $k = i = j$:
$$\sum_k a_i \delta_{ik} \, b_k \delta_{kj} = a_i b_i \, \delta_{ij}.$$
So $\operatorname{diag}(a) \operatorname{diag}(b) = \operatorname{diag}(a_1 b_1, \dots, a_n b_n)$, and over a commutative ring two diagonal matrices commute.
The concept page on [[diagonal matrices|044JNC7ZAA]] develops powers, the scaling of rows and columns, and the link with [[diagonalizable|07SQCNV233]] matrices.

## Explanations

### L1 human

A diagonal matrix has numbers only on the main diagonal and zeros elsewhere.
For example, $\operatorname{diag}(2, 5) = \begin{pmatrix} 2 & 0 \\ 0 & 5 \end{pmatrix}$.
The numbers on the diagonal can be anything, even zero.

### L2 human

To test whether a matrix is diagonal, look only at the entries off the diagonal.
The matrix $\begin{pmatrix} 3 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & -1 \end{pmatrix}$ is $\operatorname{diag}(3, 0, -1)$.
Watch out: a matrix with a zero diagonal, such as $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, is not diagonal, because its nonzero entries are off the diagonal.
