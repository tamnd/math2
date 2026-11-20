---
tag: 044JNC7ZAA
kind: concept
name: Diagonal matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
specializes: [0N4XY7Z3NN, 00J3KZP8Y0]
uses: [0JXZKX526R]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonal_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Diagonal_matrix
    locator: Matrix operations
  - book: isbn:9780321982384
    locator: Section 2.1
same_as:
  wikidata: Q332791
  wikipedia: Diagonal matrix
inventory: [EZGPZWYDK2]
---

## Summary

A diagonal matrix is a [[square matrix|0JXZKX526R]] whose entries off the main diagonal are all $0$.
The [[formal definition|0Q9PGXD9E4]] writes it as $\operatorname{diag}(d_1, \dots, d_n)$.
Diagonal matrices are added, multiplied and raised to powers entry by entry on the diagonal.
As linear maps, they stretch each coordinate axis by its own factor.
A matrix that is [[similar|0E89HQATM8]] to a diagonal matrix is [[diagonalisable|07SQCNV233]], and this is the aim of much of the theory of [[eigenvalues|0BQAA2BK3Q]].

## Motivation

Computations with general matrices are hard: a power $A^{100}$ needs many products.
For a diagonal matrix, $D^{100} = \operatorname{diag}(d_1^{100}, \dots, d_n^{100})$, and $Dx$ is $(d_1 x_1, \dots, d_n x_n)$.
So diagonal matrices are the matrices for which every question has an immediate answer.
Many methods reduce a problem to a diagonal one by a change of coordinates.

## Notation

- $\operatorname{diag}(d_1, \dots, d_n)$, or $\operatorname{diag}(d)$ for a vector $d$.
- The same notation $\operatorname{diag}(A)$ sometimes means the vector of diagonal entries of a matrix $A$; check the convention.
- In Mathlib, `Matrix.diagonal d` is the diagonal matrix of a function `d : n → α`, and `Matrix.diag A` is the vector of diagonal entries.
- A rectangular matrix with $a_{ij} = 0$ for $i \neq j$ is also called diagonal by some books, for example in the singular value decomposition.

## Remarks

### Examples

- [[The powers of diag(2, −1, 3)|DAVRDS5NV4]] are $\operatorname{diag}(2^k, (-1)^k, 3^k)$.
- [[Multiplying by a diagonal matrix scales rows or columns|3BTM4ZNHX8]].
- The [[scalar matrices|067NKSBEWT]], the [[identity|06DW9BAWB1]] and the [[zero matrix|0ZTKJJDGR7]] of order $n$ are diagonal.

### Non-examples

- [[The swap matrix with zero diagonal|JP3T5EWT3M]] $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ squares to $I$, but it is not diagonal.
- An upper [[triangular matrix|0N4XY7Z3NN]] with a nonzero entry above the diagonal is not diagonal.

### Basic properties

- $\operatorname{diag}(a) + \operatorname{diag}(b) = \operatorname{diag}(a + b)$ and $\operatorname{diag}(a)\operatorname{diag}(b) = \operatorname{diag}(a_1 b_1, \dots, a_n b_n)$.
- Over a commutative ring, diagonal matrices commute with each other.
- $DA$ multiplies row $i$ of $A$ by $d_i$, and $AD$ multiplies column $j$ of $A$ by $d_j$.
- A diagonal matrix is both upper and [[lower triangular|00J3KZP8Y0]], and it is [[symmetric|0VR671PHE5]].
- Over a field, $\operatorname{diag}(d)$ is [[invertible|0EB9N0S33C]] exactly when every $d_i \neq 0$, and then the inverse is $\operatorname{diag}(d_1^{-1}, \dots, d_n^{-1})$.
- Its [[determinant|00KDZRW4C0]] is $d_1 \cdots d_n$, its [[trace|0XC1RDBY7A]] is $d_1 + \dots + d_n$, and $e_i$ is an [[eigenvector|0N6960W0BV]] with eigenvalue $d_i$.
- A diagonal matrix commutes with every matrix only when it is [[scalar|067NKSBEWT]].

### Common errors

- Assuming that a diagonal matrix commutes with every matrix.
- Assuming that a matrix with a zero diagonal behaves like the zero matrix, as in the swap non-example.
- Confusing a diagonal matrix with a [[diagonalisable|07SQCNV233]] one.

## Explanations

### L1 human

A diagonal matrix has numbers only on the main diagonal, and zeros everywhere else.
Multiplying two diagonal matrices just multiplies the numbers in the same diagonal positions.
So powers of a diagonal matrix are easy to compute.

### L2 human

The map $x \mapsto Dx$ stretches the $i$-th axis by $d_i$ and keeps the axes in place.
The diagonal matrices of order $n$ form a commutative subring of $M_n(R)$ isomorphic to $R^n$, when $R$ is commutative.
Diagonalising a matrix means choosing a basis of eigenvectors, in which the matrix becomes diagonal.

### L3 human

The diagonal matrices form the maximal torus of $GL_n$ when their entries are units.
Over a field, a set of pairwise commuting diagonalisable matrices can be [[diagonalised at the same time|0FK17N4DKA]].
The centraliser of a diagonal matrix with distinct entries is the set of all diagonal matrices.
