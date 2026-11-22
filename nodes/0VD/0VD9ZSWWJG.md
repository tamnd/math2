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

A matrix is a rectangular table of numbers, read by rows and by columns.
It is the basic object of linear algebra, because one table can hold a whole system of equations or a whole linear map.
An $m \times n$ matrix over a [[field|04C5ZBG1WT]] $F$, or more generally over a [[ring|0B1261B5ED]], has $m$ rows and $n$ columns, and its entry in row $i$ and column $j$ is written $a_{ij}$:
$$A = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix}.$$
The [[formal definition|0N1MY1T0W9]] treats $A$ as a function that assigns an entry $a_{ij}$ to each position $(i, j)$ with $1 \le i \le m$ and $1 \le j \le n$.
Two matrices are equal when they have the same size and the same entry in every position.

## Motivation

Take the system $x + 2y = 5$, $3x - y = 1$.
Everything that matters about it is in the four coefficients and the two right sides, and the letters $x$ and $y$ only mark the places.
If we write the coefficients as a table with one row for each equation, we can do elimination on the table and save the writing.
That table is the [[coefficient matrix|0HQFZAP3ND]] of the [[system of linear equations|0GT4WWGWH2]].

The second source of matrices is the [[linear map|0NRYHJPQG2]].
A linear map from $F^n$ to $F^m$ is fixed by the images of the $n$ standard basis vectors, and each image has $m$ coordinates.
So the map is again a table with $m$ rows and $n$ columns.
The rules for [[adding matrices|0Y7H3SAVA1]] and for [[multiplying them|032Q9FB8MT]] come from these two uses, and the rest of the sub-area studies them.

Outside mathematics, a matrix is the natural way to store any table of data indexed by two things.
A spreadsheet of sales by shop and product, the pixels of a grayscale image, and the links between the pages of a website are all matrices.

## Notation

The size is written $m \times n$ with the rows first, so a $2 \times 3$ matrix has 2 rows and 3 columns.
The entry in row $i$ and column $j$ of $A$ is written $a_{ij}$, $A_{ij}$, $A_{i,j}$ or $A(i, j)$, and a comma is needed once an index has two digits, as in $a_{1,10}$.
The set of $m \times n$ matrices over $R$ is written $M_{m \times n}(R)$, $M_{m,n}(R)$ or $R^{m \times n}$.
Round brackets and square brackets mean the same thing, but vertical bars $\begin{vmatrix} a & b \\ c & d \end{vmatrix}$ denote a [[determinant|00KDZRW4C0]], which is a number.

In Mathlib, `Matrix m n α` is the type of functions `m → n → α`, where the index types `m` and `n` can be any types, not only $\{1, \dots, m\}$.
Products and determinants need the index types to be finite, through `Fintype` instances.
Rows indexed by `Fin m` start at $0$, so the entry $a_{11}$ of a book is `A 0 0` in Mathlib.

## Remarks

### Reading the entries

The rule $a_{ij} = 10i + j$ on $2$ rows and $3$ columns gives the [[matrix with two-digit entries|D5H0JWNHNP]]:
$$A = \begin{pmatrix} 11 & 12 & 13 \\ 21 & 22 & 23 \end{pmatrix}.$$
The tens digit of each entry is its row and the units digit is its column, so you can read the convention off the table.
For example, $a_{12} = 12$ and $a_{21} = 21$, and these are different entries.
The entry $a_{31}$ does not exist, because there is no third row.

### Rows, columns and vectors

Row $i$ of $A$ is the list $(a_{i1}, \dots, a_{in})$, and column $j$ is the list $(a_{1j}, \dots, a_{mj})$.
A $1 \times n$ matrix is called a row vector and an $m \times 1$ matrix a column vector.
In a [[table of sales|N1N2FH8NR2]] with one row for each of 2 shops and one column for each of 3 products, row 1 lists what the first shop sold, and column 2 lists the sales of the second product in each shop.
For the system above, the coefficient matrix and the column of right sides are
$$\begin{pmatrix} 1 & 2 \\ 3 & -1 \end{pmatrix} \quad \text{and} \quad \begin{pmatrix} 5 \\ 1 \end{pmatrix}.$$

### When two matrices are equal

Equality asks for the same size and the same entry in each position.
So the row $\begin{pmatrix} 1 & 2 & 3 \end{pmatrix}$ and the column with entries $1$, $2$, $3$ are different matrices, although they hold the same numbers.
This is natural when a matrix is a function on positions: two functions are equal only when they have the same domain and the same values.

### What a matrix is not

An array whose rows have different lengths is not a matrix, because some positions of the rectangle have no entry; see [[the ragged array|8F1WW3852E]].
A list such as $(1, 2, 3, 4)$ is not a $2 \times 2$ matrix until we choose how to arrange it, and the two natural choices give different matrices.
The determinant $\begin{vmatrix} 1 & 2 \\ 3 & 4 \end{vmatrix} = 1 \cdot 4 - 2 \cdot 3 = -2$ is a number computed from a matrix, not a matrix.

### What you can do with matrices

Over a field $F$, the $m \times n$ matrices form a [[vector space|0RE6X3BGPN]] of dimension $mn$ under entrywise addition and scalar multiplication.
An $m \times n$ matrix and an $n \times p$ matrix have a product, which is $m \times p$.
The square $n \times n$ matrices form the [[matrix ring|AB2MD5CD13]] $M_n(R)$.
Each $A \in M_{m \times n}(F)$ gives the [[linear map|094V2VBJXJ]] $x \mapsto Ax$ from $F^n$ to $F^m$, and each linear map $F^n \to F^m$ comes from exactly one matrix.
The [[zero matrix|0ZTKJJDGR7]] and the [[identity matrix|06DW9BAWB1]] play the roles of $0$ and $1$.

### Watch out

The size gives rows first: a matrix with 3 rows and 2 columns is $3 \times 2$, not $2 \times 3$.
In the same way, $a_{12}$ sits in row 1 and column 2, and in the matrix $A$ above it is $12$ while $a_{21} = 21$.
If you swap the subscripts, you read the [[transpose|09DXWYRD43]] instead of the matrix.

### History

Arrays of coefficients were used to solve linear systems in the Chinese text *The Nine Chapters on the Mathematical Art*.
Sylvester introduced the word "matrix" in 1850, for an array from which determinants can be formed.
Cayley defined the sum and the product of matrices in his memoir on the theory of matrices of 1858.

### Try it

First, write the $3 \times 2$ matrix with $a_{ij} = i - j$.
The rows are $(0, -1)$, $(1, 0)$ and $(2, 1)$.

Second, for which numbers $x$ and $y$ is $\begin{pmatrix} x & 2 \\ 3 & y \end{pmatrix}$ equal to $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$?
The sizes agree, so we compare entries, and we need $x = 1$ and $y = 4$.

## Explanations

### L1 human

A matrix is a table of numbers with a fixed number of rows and a fixed number of columns.
The table $\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$ has 2 rows and 3 columns, so we call it a $2 \times 3$ matrix.
To find a number, give its row and then its column, like a seat in a theater.
The number in row 2 and column 1 is $4$.

### L2 human

Here is how a matrix turns a problem about equations into a problem about a table.
The system $2x + y - z = 3$, $x - y = 0$ has 2 equations in 3 unknowns, so its coefficient matrix is $2 \times 3$:
$$A = \begin{pmatrix} 2 & 1 & -1 \\ 1 & -1 & 0 \end{pmatrix}.$$
The entry $a_{23} = 0$ records that $z$ does not appear in the second equation, and it must be written, or the table would lose its shape.
Column 3, with entries $-1$ and $0$, collects the coefficients of $z$ in the two equations.
Row operations on $A$, together with the right sides, now do all the work of elimination.
This is the typical use of a matrix: it keeps the positions of the numbers, and the positions carry the meaning.

### L3 human

For finite sets $I$ and $J$ and a ring $R$, an $I \times J$ matrix is an element of $R^{I \times J}$, and Mathlib uses exactly this convention.
The free module $R^J$ has the basis $(e_j)$, and $\operatorname{Hom}_R(R^J, R^I)$ is identified with $R^{I \times J}$ by sending $f$ to the family of coordinates $e_i^*(f(e_j))$.
Under this identification, composition of homomorphisms becomes the matrix product.
The identification depends on the chosen bases, and the later sub-area on matrices of linear maps shows that a change of basis changes the matrix by [[similarity|0E89HQATM8]] or by equivalence.
