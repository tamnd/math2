---
tag: 09DXWYRD43
kind: concept
name: Transpose
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
uses: [0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Transpose
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Transpose
    locator: Properties
  - book: isbn:9780321982384
    locator: Section 2.1
same_as:
  wikidata: Q223683
  wikipedia: Transpose
---

## Summary

The transpose of a matrix is the matrix you get when its rows become its columns.
It lets us use the rows and the columns of one matrix in the same formula, and it is the operation that moves a matrix from one side of a dot product to the other.
Exactly, the transpose of an $m \times n$ [[matrix|0VD9ZSWWJG]] $A = (a_{ij})$ is the $n \times m$ matrix $A^{\mathsf{T}}$ with
$$(A^{\mathsf{T}})_{ij} = a_{ji}.$$
The [[formal definition|0W809K6AW0]] states this rule.
For a square matrix, the transpose is the reflection of the array in its main diagonal.

## Motivation

A matrix is a table, and many formulas need to read the same table both ways.
The rows of $A$ are the columns of $A^{\mathsf{T}}$, so a statement about columns, applied to $A^{\mathsf{T}}$, becomes a statement about the rows of $A$.

The transpose also explains how a matrix behaves inside a [[dot product|0S52TNNTH9]].
For column vectors $x$ and $y$ we can write $x \cdot y = x^{\mathsf{T}} y$, and then
$$(Ax) \cdot y = x \cdot (A^{\mathsf{T}} y).$$
This rule is the source of [[symmetric matrices|0VR671PHE5]], of the normal equations $A^{\mathsf{T}} A x = A^{\mathsf{T}} b$ of [[least squares|8GQVME4SZZ]], and of the dual map in the topic on [[duality|9K7FFF26QR]].

## Notation

Most books write $A^{\mathsf{T}}$ or $A^T$, and you will also see $A^t$, ${}^t\!A$, $A^{\top}$ and $A'$.
The prime is common in statistics, but in MATLAB `A'` is the [[conjugate transpose|0DXKE10PHF]] and `A.'` is the plain transpose.
Some books write $A^*$ for the conjugate transpose, while in other books $A^*$ means the adjoint of a map.
Read $A^t$ with care: the $t$ is not an exponent, and ${}^t\!A$ is not a superscript on the symbol before it.
In Mathlib, `Aᵀ` is notation for `Matrix.transpose A`, and because Mathlib indexes matrices by arbitrary finite types, `Aᵀ` is simply the function `fun i j => A j i`.

## Remarks

### A first transpose

Take the $2 \times 3$ matrix of [[the 2 × 3 example|7RHY1Z1E5Y]]:
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}, \qquad A^{\mathsf{T}} = \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}.$$
Row 2 of $A$, which is $(4, 5, 6)$, is column 2 of $A^{\mathsf{T}}$.
The size changes from $2 \times 3$ to $3 \times 2$, and the entry $a_{13} = 3$ moves to position $(3, 1)$.

### The rules you can use

Transposing twice puts every entry back, so $(A^{\mathsf{T}})^{\mathsf{T}} = A$.
The transpose acts entry by entry on sums and scalar multiples, so
$$(A + B)^{\mathsf{T}} = A^{\mathsf{T}} + B^{\mathsf{T}}, \qquad (cA)^{\mathsf{T}} = c\,A^{\mathsf{T}}.$$
For $A$ above and $B = \begin{pmatrix} 0 & 1 & 0 \\ 2 & 0 & -1 \end{pmatrix}$, both sides of the first rule equal $\begin{pmatrix} 1 & 6 \\ 3 & 5 \\ 3 & 5 \end{pmatrix}$.
So the transpose is a linear bijection from the $m \times n$ matrices to the $n \times m$ matrices.

Over a commutative ring, the transpose reverses products: $(AB)^{\mathsf{T}} = B^{\mathsf{T}} A^{\mathsf{T}}$, by the [[transpose of a product|09GK5PS824]].
It also keeps the [[trace|09E1RCZ7YT]], the [[determinant|0ZZQ2E1MTE]] and the [[rank|0ZC9YTXZRY]] of a matrix; the last fact is the theorem that [[row rank equals column rank|0TZAG60ZYT]].

### The transpose of an inverse

In [[the 2 × 2 example|G9XS9NZ7DV]], $A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}$ has inverse $\begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$, and
$$A^{\mathsf{T}} \bigl(A^{-1}\bigr)^{\mathsf{T}} = \begin{pmatrix} 2 & 5 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} 3 & -5 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}.$$
This is no accident.
Transposing $A^{-1} A = I$ gives $A^{\mathsf{T}} (A^{-1})^{\mathsf{T}} = I$, so for every [[invertible matrix|0EB9N0S33C]], $(A^{\mathsf{T}})^{-1} = (A^{-1})^{\mathsf{T}}$.

### Moving across a dot product

Take $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, $x = (1, 1)$ and $y = (2, -1)$.
Then $Ax = (3, 7)$ and $(Ax) \cdot y = 6 - 7 = -1$.
On the other side, $A^{\mathsf{T}} y = (2 - 3, 4 - 4) = (-1, 0)$ and $x \cdot (A^{\mathsf{T}} y) = -1$.
In general $(Ax) \cdot y = (Ax)^{\mathsf{T}} y = x^{\mathsf{T}} A^{\mathsf{T}} y = x \cdot (A^{\mathsf{T}} y)$.

### What it is not

[[Turning the array by a quarter turn|CZRM8TAY7T]] is not the transpose: it sends $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ to $\begin{pmatrix} 3 & 1 \\ 4 & 2 \end{pmatrix}$, which moves the diagonal entries.
Reversing the order of the rows is not the transpose either, since it gives $\begin{pmatrix} 3 & 4 \\ 1 & 2 \end{pmatrix}$ instead of $\begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}$.
A quick test: the transpose never moves a diagonal entry.

### Watch out

The transpose of a product is not the product of the transposes.
With $A$ of size $2 \times 3$ and $B$ of size $3 \times 1$, the matrix $(AB)^{\mathsf{T}}$ is $1 \times 2$, but $A^{\mathsf{T}} B^{\mathsf{T}}$ is a $3 \times 2$ matrix times a $1 \times 3$ matrix, which is not defined.
The correct rule reverses the order, $(AB)^{\mathsf{T}} = B^{\mathsf{T}} A^{\mathsf{T}}$.
For complex vectors the plain transpose can mislead: for $x = (1, i)$, [[the product x^T x is zero|5AG0M5GR5T]], and lengths need the conjugate transpose.

### History

Cayley introduced the transposed matrix in his memoir on the theory of matrices of 1858.

### Try it

First, if $A$ is a $3 \times 5$ matrix, what are the sizes of $A^{\mathsf{T}}$ and $A^{\mathsf{T}} A$?
$A^{\mathsf{T}}$ is $5 \times 3$, so $A^{\mathsf{T}} A$ is a $5 \times 3$ matrix times a $3 \times 5$ matrix, which is $5 \times 5$.

Second, check $(AB)^{\mathsf{T}} = B^{\mathsf{T}} A^{\mathsf{T}}$ for $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.
$AB = \begin{pmatrix} 2 & 1 \\ 4 & 3 \end{pmatrix}$, so $(AB)^{\mathsf{T}} = \begin{pmatrix} 2 & 4 \\ 1 & 3 \end{pmatrix}$, and $B^{\mathsf{T}} A^{\mathsf{T}} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}$ gives the same matrix.

## Explanations

### L1 human

To transpose a matrix, write its rows as columns.
The first row becomes the first column, the second row becomes the second column, and so on.
So $\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$ becomes $\begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}$, and a table with 2 rows and 3 columns becomes a table with 3 rows and 2 columns.
The numbers on the diagonal, here $1$ and $5$, stay in their places.

### L2 human

Here is a typical use: show that $A^{\mathsf{T}} A$ has a nonnegative number $x \cdot (A^{\mathsf{T}} A x)$ for every real matrix $A$ and every vector $x$.
Move one $A$ across the dot product with the rule $(Ax) \cdot y = x \cdot (A^{\mathsf{T}} y)$, read from right to left with $y = Ax$:
$$x \cdot (A^{\mathsf{T}} A x) = (Ax) \cdot (Ax) = \|Ax\|^2 \ge 0.$$
For $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $x = (1, 1)$, this number is $\|(3, 7)\|^2 = 58$.
Check: $A^{\mathsf{T}} A = \begin{pmatrix} 10 & 14 \\ 14 & 20 \end{pmatrix}$, so $A^{\mathsf{T}} A x = (24, 34)$, and $x \cdot (24, 34) = 58$.
This one line is the reason that $A^{\mathsf{T}} A$ appears in least squares and in the singular value decomposition.

### L3 human

For a linear map $f \colon V \to W$, the dual map $f^* \colon W^* \to V^*$ sends a linear form $\varphi$ to $\varphi \circ f$.
In dual bases, the [[matrix of the dual map is the transpose|0ZPB3180AY]] of the matrix of $f$, so the transpose is the coordinate form of duality.
With an inner product on both spaces, the same role is played by the adjoint map, whose matrix in orthonormal bases is the transpose over $\mathbb{R}$ and the conjugate transpose over $\mathbb{C}$.
Over a commutative ring the transpose is an anti-automorphism of $M_n(R)$; over a noncommutative ring $R$ it is an anti-isomorphism from $M_n(R)$ to $M_n(R^{\mathrm{op}})$.
