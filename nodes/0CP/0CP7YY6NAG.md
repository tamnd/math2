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

A square matrix is a matrix with the same number of rows and columns.
Let $R$ be a ring and let $n \ge 0$ be an integer.
A *square matrix* of *order* $n$ over $R$ is an $n \times n$ [[matrix|0N1MY1T0W9]] over $R$.
Its *main diagonal* is the list of entries $a_{11}, a_{22}, \dots, a_{nn}$.
An entry $a_{ij}$ with $i \neq j$ is an *off-diagonal* entry.
The set of square matrices of order $n$ over $R$ is written $M_n(R)$.

## Notation

Books also write $M_{n \times n}(R)$ or $R^{n \times n}$ for $M_n(R)$.
In Mathlib, a square matrix is a term of `Matrix n n α`, with the same index type `n` for the rows and the columns.

## Remarks

The one condition is that the row count and the column count agree.
It is there so that a product $AB$ of two matrices of order $n$ is defined and is again of order $n$, which makes $M_n(R)$ a [[ring|AB2MD5CD13]].
For example, $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ is square of order 2, with main diagonal $1, 4$ and off-diagonal entries $2$ and $3$.
The matrix $\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$ fails the condition, since it has 2 rows and 3 columns, and so it [[has no square|TVNYJ89WDJ]].

The main diagonal is defined only for square matrices in this sense.
A rectangular matrix also has entries $a_{11}, a_{22}, \dots$, but they do not run from corner to corner.
The [[trace|0XC1RDBY7A]], the [[determinant|00KDZRW4C0]] and the [[eigenvalues|0BQAA2BK3Q]] are defined only for square matrices.
The concept page on [[square matrices|0JXZKX526R]] explains why they are the matrices of maps from a space to itself.

## Explanations

### L1 human

A square matrix has as many rows as columns, like a $3 \times 3$ table.
Only square matrices can be multiplied by themselves, so only they have powers like $A^2$.

### L2 human

The main diagonal runs from the top left corner to the bottom right corner.
In $\begin{pmatrix} 2 & 7 & 1 \\ 0 & 5 & 3 \\ 4 & 6 & 9 \end{pmatrix}$ it is $2, 5, 9$, and the other six entries are off-diagonal.
Watch out: the entries $1, 5, 4$ from the top right to the bottom left form the antidiagonal, not the diagonal.
