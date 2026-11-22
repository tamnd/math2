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

A square matrix is a matrix with as many rows as columns.
This small condition matters a great deal: a square matrix can be multiplied by itself, so it has powers, and the square matrices of one size form a ring.
An $n \times n$ [[matrix|0VD9ZSWWJG]] is called a square matrix of order $n$, as the [[formal definition|0CP7YY6NAG]] states.
Its entries $a_{11}, a_{22}, \dots, a_{nn}$ form the main diagonal, which runs from the top left corner to the bottom right corner.

## Motivation

A rotation of the plane sends the plane to itself, so its matrix takes vectors with 2 entries to vectors with 2 entries, and it is $2 \times 2$.
Every linear map from a space to itself has a square matrix in the same way.
For such a map you can ask questions that make no sense for a map between different spaces.
You can ask what happens when you apply it a hundred times, whether it can be undone, and which directions it only stretches.

The tools that answer these questions are the [[determinant|00KDZRW4C0]], the [[trace|0XC1RDBY7A]] and the [[eigenvalues|0BQAA2BK3Q]], and all three are defined only for square matrices.
So most of the named matrices in this sub-area, and most of the later theory, are about square matrices.

## Notation

The set of $n \times n$ matrices over $R$ is written $M_n(R)$, $M_{n \times n}(R)$ or $R^{n \times n}$.
The number $n$ is the *order* of the matrix, and some books also call it the size.
The main diagonal is also called the leading diagonal or the principal diagonal.
The entries $a_{1n}, a_{2,n-1}, \dots, a_{n1}$ form the *antidiagonal*, which runs from the top right corner to the bottom left corner.

## Remarks

### A first example

Take the matrix of order 3 in [[the example with entries 1 to 9|C7N0PT179M]]:
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}.$$
Its main diagonal is $1, 5, 9$, and its antidiagonal is $3, 5, 7$.
Because $A$ has 3 columns and 3 rows, the product $AA$ is defined, and it is again $3 \times 3$:
$$A^2 = \begin{pmatrix} 30 & 36 & 42 \\ 66 & 81 & 96 \\ 102 & 126 & 150 \end{pmatrix}.$$
For instance, the entry in position $(1, 1)$ is row 1 times column 1, which is $1 \cdot 1 + 2 \cdot 4 + 3 \cdot 7 = 30$.

### The smallest cases

A [[1 × 1 matrix|WYJ95EEQFJ]] $\begin{pmatrix} a \end{pmatrix}$ adds and multiplies exactly like its one entry, so $M_1(R)$ is a copy of $R$.
The first interesting case is order 2.
The quarter turn $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ of the plane is a square matrix whose square is $-I$, which no real number can imitate.
Every [[identity matrix|06DW9BAWB1]] $I_n$ is square.

### What is not square

A $2 \times 3$ matrix is not square, and it [[has no square|TVNYJ89WDJ]]: the product $AA$ would need 3 columns to meet 2 rows.
A column vector with $n \ge 2$ entries is an $n \times 1$ matrix, so it is not square either.
The products $AA^{\mathsf{T}}$ and $A^{\mathsf{T}}A$ of a rectangular matrix with its transpose are square, but they have different orders.

### The rules you can use

For $A, B \in M_n(R)$, the sum $A + B$ and the product $AB$ are again in $M_n(R)$.
So we can define powers by $A^0 = I_n$ and $A^{k+1} = A^k A$, and the law $A^j A^k = A^{j+k}$ follows from [[associativity|073E4XC016]].
With these operations $M_n(R)$ is the [[matrix ring|AB2MD5CD13]], with the zero matrix as $0$ and $I_n$ as $1$.
This ring is not commutative for $n \ge 2$, by the [[standard counterexample|0P506SPZP2]].
The square matrices include the [[diagonal|044JNC7ZAA]], [[triangular|0N4XY7Z3NN]], [[symmetric|0VR671PHE5]] and [[invertible|0EB9N0S33C]] matrices of the later pages.

### Watch out

The square of a matrix is a matrix product, not the matrix of squared entries.
For $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ we get
$$A^2 = \begin{pmatrix} 1 + 6 & 2 + 8 \\ 3 + 12 & 6 + 16 \end{pmatrix} = \begin{pmatrix} 7 & 10 \\ 15 & 22 \end{pmatrix},$$
not $\begin{pmatrix} 1 & 4 \\ 9 & 16 \end{pmatrix}$.
In the same way, the diagonal of $A^2$ is $7, 22$, not the squares $1, 16$ of the diagonal of $A$.

### Try it

First, what is the main diagonal of $\begin{pmatrix} 2 & 0 & 1 \\ 5 & -3 & 4 \\ 0 & 6 & 7 \end{pmatrix}$?
It is $2, -3, 7$, read from the top left to the bottom right.

Second, compute the square of $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.
Row times column gives $\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$.

## Explanations

### L1 human

A square matrix has as many rows as columns, like a $3 \times 3$ grid in a game of tic-tac-toe.
The entries from the top left corner to the bottom right corner form the main diagonal.
Only a square matrix can be multiplied by itself, so only square matrices have powers like $A^2$ and $A^3$.

### L2 human

A square matrix of order $n$ describes a linear map from $F^n$ to $F^n$, and since the input and the output live in the same space, we can apply the map again and again.
Take the shear $S = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, which sends $(x, y)$ to $(x + y, y)$.
Applying it twice sends $(x, y)$ to $(x + 2y, y)$, and the matrix product agrees:
$$S^2 = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}.$$
In the same way $S^k = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$, since each application adds one more copy of $y$ to $x$.
This is the typical use: powers, polynomials $p(A)$ and [[inverses|0EB9N0S33C]] are all questions about repeating or undoing a map of a space to itself.

### L3 human

For a field $F$, the ring $M_n(F)$ is an $F$-[[algebra|1SENAHZW5A]] of dimension $n^2$, and it is isomorphic to the [[endomorphism ring|AWSBZWWMG9]] of $F^n$.
Rectangular matrices do not form a ring, but they form a category: the objects are the integers $n \ge 0$, and the $m \times n$ matrices are the morphisms from $n$ to $m$.
In that category the square matrices of order $n$ are exactly the endomorphisms of the object $n$, which is why they alone carry a ring structure.
