---
tag: 0Q9PGXD9E4
kind: definition
name: Diagonal matrix
msc: [15A99]
defines: 044JNC7ZAA
uses: [0CP7YY6NAG]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonal_matrix
    locator: lead section
---

## Definition

Let $R$ be a ring and let $n \ge 0$ be an integer.
A [[square matrix|0JXZKX526R]] $D = (d_{ij})$ of order $n$ over $R$ is *diagonal* when $d_{ij} = 0$ for all $i \ne j$.
For $d_1, \dots, d_n \in R$, the matrix $\operatorname{diag}(d_1, \dots, d_n)$ is the diagonal matrix with $d_{ii} = d_i$ for each $i$.

## Remarks

The product of two diagonal matrices is diagonal: $\operatorname{diag}(a_1, \dots, a_n) \operatorname{diag}(b_1, \dots, b_n) = \operatorname{diag}(a_1 b_1, \dots, a_n b_n)$.
Over a commutative ring, diagonal matrices commute with each other.
The [[determinant|00KDZRW4C0]] of a diagonal matrix is the product of its diagonal entries.
A matrix that is similar to a diagonal matrix is [[diagonalisable|07SQCNV233]].

## Explanations

### L1 human

A diagonal matrix has numbers only on its main diagonal, from the top left to the bottom right.
As a map, it stretches each coordinate axis by its own factor.
Diagonal matrices are easy to add, multiply and raise to powers.
