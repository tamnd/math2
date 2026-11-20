---
tag: 0CP7YY6NAG
kind: definition
name: Square matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
defines: 0JXZKX526R
uses: [0N1MY1T0W9]
sources:
  - url: https://en.wikipedia.org/wiki/Square_matrix
    locator: lead section
  - book: isbn:9780321982384
    locator: Section 2.1
inventory: [XEKW91HDZJ]
---

## Definition

Let $R$ be a ring and let $n \ge 0$ be an integer.
A *square matrix* of order $n$ over $R$ is an $n \times n$ [[matrix|0N1MY1T0W9]] over $R$.
Its *main diagonal* is the list of the entries $a_{11}, a_{22}, \dots, a_{nn}$.
An entry $a_{ij}$ with $i \neq j$ is an *off-diagonal* entry.
The set of square matrices of order $n$ over $R$ is written $M_n(R)$.

## Remarks

- The product of two $n \times n$ matrices is again an $n \times n$ matrix, so $M_n(R)$ is a [[ring|~de637a64]].
- The [[trace|0XC1RDBY7A]], the [[determinant|00KDZRW4C0]] and the [[eigenvalues|0BQAA2BK3Q]] are defined only for square matrices.
- A square matrix represents a linear map from a space to itself.
- In Mathlib, a square matrix is a term of `Matrix n n α`, with the same index type for rows and columns.

## Explanations

### L1 human

A square matrix has as many rows as columns, like a $3 \times 3$ table.
Only square matrices can be multiplied by themselves, so only they have powers like $A^2$.
Many important notions, such as the determinant, apply only to square matrices.

### L2 human

The main diagonal runs from the top left corner to the bottom right corner.
A rectangular matrix also has entries $a_{ii}$, but it has no main diagonal in this sense.
