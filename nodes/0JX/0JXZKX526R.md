---
tag: 0JXZKX526R
kind: concept
name: Square matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
specializes: [0VD9ZSWWJG]
uses: [0VD9ZSWWJG, 032Q9FB8MT]
sources:
  - url: https://en.wikipedia.org/wiki/Square_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Square_matrix
    locator: Main diagonal
  - book: isbn:9780321982384
    locator: Section 2.1
same_as:
  wikidata: Q2739329
  wikipedia: Square matrix
inventory: [XEKW91HDZJ]
---

## Summary

A square matrix is a [[matrix|0VD9ZSWWJG]] with the same number of rows and columns.
The [[formal definition|0CP7YY6NAG]] calls an $n \times n$ matrix a square matrix of order $n$.
The entries $a_{11}, a_{22}, \dots, a_{nn}$ form its main diagonal.
Two $n \times n$ matrices always have a [[product|032Q9FB8MT]], and the product is again $n \times n$.
So a square matrix has powers $A^2, A^3, \dots$, and the square matrices of order $n$ form a [[ring|~de637a64]].

## Motivation

A linear map from a space to itself, such as a rotation of the plane, has a square matrix.
The questions that make sense for such a map need a square matrix.
Examples are: is the map invertible, what are its fixed directions, and what happens when we apply it many times.
The [[determinant|00KDZRW4C0]], the [[trace|0XC1RDBY7A]] and the [[eigenvalues|0BQAA2BK3Q]] answer these questions, and they are defined only for square matrices.

## Notation

- The set of $n \times n$ matrices over $R$ is written $M_n(R)$, $M_{n \times n}(R)$ or $R^{n \times n}$.
- The number $n$ is the order of the matrix. Some books also call it the size.
- The main diagonal is also called the leading diagonal or the principal diagonal.
- The entries $a_{1n}, a_{2,n-1}, \dots, a_{n1}$ form the antidiagonal.

## Remarks

### Examples

- The [[3 × 3 matrix with diagonal 1, 5, 9|~b19cf784]] shows the main diagonal and the square of a square matrix.
- [[1 × 1 matrices|~10157e74]] add and multiply like their single entries.
- Every [[identity matrix|06DW9BAWB1]] $I_n$ is square.
- The rotation matrix $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ of the plane is a $2 \times 2$ square matrix.

### Non-examples

- A [[2 × 3 matrix has no square|~28cb6538]], because the product $AA$ is not defined.
- A column vector of length $n \ge 2$ is an $n \times 1$ matrix, so it is not square.

### Basic properties

- For $A, B \in M_n(R)$, the sum $A + B$ and the product $AB$ are in $M_n(R)$.
- Powers are defined by $A^0 = I_n$ and $A^{k+1} = A^k A$; then $A^j A^k = A^{j+k}$ by [[associativity|073E4XC016]].
- In general $AB \neq BA$, by the [[standard counterexample|0P506SPZP2]].
- A matrix $A$ is square if and only if both $AA^{\mathsf{T}}$ and $A^{\mathsf{T}}A$ have the size of $A$.
- Special square matrices include the [[diagonal|044JNC7ZAA]], [[triangular|0N4XY7Z3NN]], [[symmetric|0VR671PHE5]] and [[invertible|0EB9N0S33C]] matrices.

### Common errors

- Writing $A^2$ for a matrix that is not square.
- Computing $A^2$ entry by entry: the square of $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ is $\begin{pmatrix} 7 & 10 \\ 15 & 22 \end{pmatrix}$, not $\begin{pmatrix} 1 & 4 \\ 9 & 16 \end{pmatrix}$.
- Calling the antidiagonal the diagonal.

## Explanations

### L1 human

A square matrix has as many rows as columns, like a $3 \times 3$ table.
Only square matrices can be multiplied by themselves, so only they have powers like $A^2$.
The entries from the top left corner to the bottom right corner form the main diagonal.

### L2 human

A square matrix of order $n$ describes a linear map from $F^n$ to $F^n$.
Because the input space and the output space are the same, we can apply the map again and again.
This is why powers, polynomials $p(A)$, and the [[invertible matrices|0EB9N0S33C]] make sense only for square matrices.

### L3 human

The set $M_n(R)$ is a ring, and for a field $F$ it is an $F$-[[algebra|1SENAHZW5A]] of dimension $n^2$.
It is isomorphic to the [[endomorphism ring|AWSBZWWMG9]] of $F^n$.
Rectangular matrices do not form a ring, but they form a category: the objects are the integers $n \ge 0$, and the $m \times n$ matrices are the morphisms from $n$ to $m$.
