---
tag: 0VD9ZSWWJG
kind: concept
name: Matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
uses: [0B1261B5ED, 04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_(mathematics)
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Matrix_(mathematics)
    locator: History
  - book: isbn:9780321982384
    locator: Section 2.1
  - url: https://hefferon.net/linearalgebra/
    locator: Chapter One, Section I
same_as:
  wikidata: Q44337
  wikipedia: Matrix (mathematics)
---

## Summary

A matrix is a rectangular array of numbers, or of elements of a [[ring|0B1261B5ED]], arranged in $m$ rows and $n$ columns.
The [[formal definition|0N1MY1T0W9]] treats an $m \times n$ matrix as a family $(a_{ij})$ indexed by the pairs $(i, j)$.
The entry $a_{ij}$ is in row $i$ and column $j$.
Matrices record [[systems of linear equations|0GT4WWGWH2]], [[linear maps|0NRYHJPQG2]] between coordinate spaces, and tables of data.
Their sums and products make them the main computational tool of linear algebra.

## Motivation

A system of linear equations is determined by its coefficients and its right-hand sides.
If we write the coefficients in a rectangular table, we can do elimination on the table and not on the equations.
A linear map $F^n \to F^m$ over a [[field|04C5ZBG1WT]] $F$ is determined by the images of the $n$ standard basis vectors.
Each image has $m$ coordinates, so the map is also a table with $m$ rows and $n$ columns.
The rules for adding and multiplying matrices come from these two uses.

## Notation

- The size is written $m \times n$, rows first: a $2 \times 3$ matrix has 2 rows and 3 columns.
- The entry in row $i$ and column $j$ of $A$ is written $a_{ij}$, $A_{ij}$, $A_{i,j}$ or $A(i, j)$.
- The set of $m \times n$ matrices over $R$ is written $M_{m \times n}(R)$, $M_{m,n}(R)$ or $R^{m \times n}$.
- Books use round brackets $\begin{pmatrix} 1 & 2 \end{pmatrix}$ or square brackets $\begin{bmatrix} 1 & 2 \end{bmatrix}$ with the same meaning.
- Vertical bars $\begin{vmatrix} a & b \\ c & d \end{vmatrix}$ denote a [[determinant|00KDZRW4C0]], which is a number and not a matrix.
- In Mathlib, `Matrix m n α` is the type of functions `m → n → α`, for arbitrary index types `m` and `n`.
- Most Mathlib theorems about products and determinants need `Fintype m` and `DecidableEq m`.
- Mathlib rows and columns are indexed by `Fin m`, which starts at $0$, or by any other finite type, so the entry $a_{11}$ of a book is `A 0 0` there.

## Remarks

### Examples

- The [[matrix with entries 10i + j|D5H0JWNHNP]], $a_{ij} = 10i + j$, is $\begin{pmatrix} 11 & 12 & 13 \\ 21 & 22 & 23 \end{pmatrix}$, a $2 \times 3$ matrix.
- A [[table of sales|~bd27cc08]] of 3 products in 2 shops is a $2 \times 3$ matrix.
- The [[coefficient matrix|0HQFZAP3ND]] of the system $x + 2y = 5$, $3x - y = 1$ is $\begin{pmatrix} 1 & 2 \\ 3 & -1 \end{pmatrix}$.
- A column vector of $\mathbb{R}^3$ is a $3 \times 1$ matrix, and a row vector is a $1 \times 3$ matrix.
- The [[zero matrix|0ZTKJJDGR7]] and the [[identity matrix|06DW9BAWB1]] are matrices of every size and of every square size.

### Non-examples

- A [[ragged array|~53e75452]] whose rows have different lengths is not a matrix.
- A list of numbers with no row and column structure, such as $(1, 2, 3, 4)$, is not a $2 \times 2$ matrix until we choose an arrangement.
- The determinant $\begin{vmatrix} 1 & 2 \\ 3 & 4 \end{vmatrix} = -2$ is a number, not a matrix.

### Basic properties

- Two matrices are equal exactly when they have the same size and the same entry in each position.
- So $\begin{pmatrix} 1 & 2 & 3 \end{pmatrix} \neq \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$, although the entries are the same.
- Over a field $F$, the $m \times n$ matrices form a [[vector space|0RE6X3BGPN]] of dimension $mn$ under [[addition and scalar multiplication|0Y7H3SAVA1]].
- An $m \times n$ matrix and an $n \times p$ matrix have a [[product|032Q9FB8MT]], which is $m \times p$.
- The $n \times n$ matrices form the [[matrix ring|~de637a64]] $M_n(R)$.
- Each matrix $A \in M_{m \times n}(F)$ gives the [[linear map|094V2VBJXJ]] $x \mapsto Ax$ from $F^n$ to $F^m$, and each linear map $F^n \to F^m$ comes from exactly one matrix.

### History

- Rectangular arrays of coefficients were used to solve linear systems in the Chinese text *The Nine Chapters on the Mathematical Art*.
- Sylvester introduced the word "matrix" in 1850, for an array from which determinants can be formed.
- Cayley defined the sum and the product of matrices in his memoir on the theory of matrices of 1858.

### Common errors

- Reading the size as columns by rows. The size $m \times n$ always gives the rows first.
- Exchanging the subscripts: $a_{12}$ is in row 1 and column 2, and it is usually different from $a_{21}$.
- Treating matrices of different sizes as equal because they have the same entries.
- Confusing the matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ with its determinant $\begin{vmatrix} a & b \\ c & d \end{vmatrix}$.

## Explanations

### L1 human

A matrix is a table of numbers with a fixed number of rows and a fixed number of columns.
The table $\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$ has 2 rows and 3 columns, so it is a $2 \times 3$ matrix.
We find an entry by its row and then by its column: the entry in row 2 and column 1 is $4$.
Matrices of the same size can be added, and some pairs of matrices can be multiplied.

### L2 human

An $m \times n$ matrix over a field $F$ is a function from the set of positions $\{1, \dots, m\} \times \{1, \dots, n\}$ to $F$.
This point of view explains equality: two functions are equal when they have the same domain and the same values.
It also explains why the size is part of the matrix.
The main use of a matrix is the linear map $x \mapsto Ax$ from $F^n$ to $F^m$.
Column $j$ of $A$ is the image of the $j$-th [[standard basis vector|0V7ZD6P7RK]].

### L3 human

For finite sets $I$ and $J$ and a ring $R$, an $I \times J$ matrix is an element of $R^{I \times J}$.
This is the convention of Mathlib, where `Matrix I J R` is `I → J → R`.
The free module $R^J$ has the basis $(e_j)$, and $\operatorname{Hom}_R(R^J, R^I)$ is identified with $R^{I \times J}$ by $f \mapsto (e_i^* f(e_j))$.
Under this identification, composition of homomorphisms becomes the matrix product.
The identification needs a chosen basis, and a change of basis changes the matrix by [[similarity|0E89HQATM8]] or by equivalence.
