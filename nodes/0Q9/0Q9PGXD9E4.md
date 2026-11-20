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

Let $R$ be a ring and let $n \ge 0$ be an integer.
A [[square matrix|0CP7YY6NAG]] $D = (d_{ij})$ of order $n$ over $R$ is *diagonal* when $d_{ij} = 0$ for all $i \ne j$.
For $d_1, \dots, d_n \in R$, the matrix $\operatorname{diag}(d_1, \dots, d_n)$ is the diagonal matrix with $d_{ii} = d_i$ for each $i$.
So $\operatorname{diag}(d_1, \dots, d_n)_{ij} = d_i\, \delta_{ij}$.

## Notation

- Mathlib's `Matrix.diagonal d` builds the matrix from the function `d`; the property of being diagonal is `Matrix.IsDiag`. We record the match as a variant.

## Remarks

- The product of two diagonal matrices is diagonal: $\operatorname{diag}(a_1, \dots, a_n) \operatorname{diag}(b_1, \dots, b_n) = \operatorname{diag}(a_1 b_1, \dots, a_n b_n)$.
- Over a commutative ring, diagonal matrices commute with each other.
- The [[determinant|00KDZRW4C0]] of a diagonal matrix is the product of its diagonal entries.
- A matrix that is similar to a diagonal matrix is [[diagonalisable|07SQCNV233]].

## Explanations

### L1 human

A diagonal matrix has numbers only on the main diagonal and zeros elsewhere.
For example, $\operatorname{diag}(2, 5) = \begin{pmatrix} 2 & 0 \\ 0 & 5 \end{pmatrix}$.

### L2 human

The entry formula $d_i \delta_{ij}$ makes products easy: $\sum_k a_i \delta_{ik} b_k \delta_{kj} = a_i b_i \delta_{ij}$.
