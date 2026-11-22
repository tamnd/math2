---
tag: 01REXW3WWE
kind: concept
name: Elementary matrix
msc: [15A23]
topics: [P8J6QR66TJ]
audience: ug1
specializes: [0EB9N0S33C]
uses: [06DW9BAWB1, 04XWH28452, 032Q9FB8MT]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_matrix
    locator: lead section
  - book: isbn:9780321982384
    locator: Section 2.2
  - book: isbn:9780135367971
    locator: Section 1.6
  - url: https://hefferon.net/linearalgebra/
    locator: Chapter Three, Section IV.3, Mechanics of Matrix Multiplication
same_as:
  wikidata: Q609566
  wikipedia: Elementary matrix
---

## Summary

An elementary matrix is one row operation stored as a matrix, so that doing the operation becomes multiplying by the matrix.
Exactly: an elementary matrix is a square matrix that we get from the [[identity matrix|06DW9BAWB1]] by one [[elementary row operation|04XWH28452]].
There are three types: a row exchange, a scaling of one row by a nonzero scalar, and a row replacement, which adds a multiple of one row to another.
Multiplying a matrix on the left by an elementary matrix performs that row operation, and multiplying on the right performs a matching column operation, by the [[row operation theorem|F7F6AA3XQ7]].
Each elementary matrix is invertible, and its inverse is the elementary matrix of the reverse operation.

## Motivation

Row reduction is a list of steps, and lists of steps are hard to reason about.
Elementary matrices turn the steps into algebra.
The step "add $-3$ times row 1 to row 2" on a matrix with two rows is the same as the [[matrix product|032Q9FB8MT]] with $\begin{pmatrix} 1 & 0 \\ -3 & 1 \end{pmatrix}$ on the left.
So a whole reduction $A \to R$ becomes one equation, $R = E_k \cdots E_1 A$.

That equation does a lot of work in the rest of the sub-area.
It shows that [[an invertible matrix is a product of elementary matrices|1ZK55FS2BF]], it explains why [[row reduction of $[A \mid I]$|0Z83DHFMYM]] computes $A^{-1}$, and it gives the [[LU decomposition|0RKG5YW66Y]].
Later the determinant is computed from the same factorization, because each elementary matrix has a known determinant.

## Notation

We write $P_{ij}$, for $i \ne j$, for the exchange of rows $i$ and $j$; it is a [[permutation matrix|08SP3DF8NB]].
We write $D_i(c)$, for $c \ne 0$, for the scaling of row $i$ by $c$; it is the [[diagonal matrix|044JNC7ZAA]] with $c$ in position $i$ and $1$ elsewhere.
We write $T_{ij}(c) = I_n + c E_{ij}$, for $i \ne j$, for the replacement that adds $c$ times row $j$ to row $i$, where $E_{ij}$ is the matrix unit with a single $1$ in position $(i, j)$.
For $c \ne 0$ this is a [[transvection|0DTCBCKEJP]].
Books use many other letters, often a plain $E$ for a generic elementary matrix, so check which index is the source row and which is the target row.

## Remarks

### One of each type

For $n = 2$, the three types look like this:
$$P_{12} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad D_2(5) = \begin{pmatrix} 1 & 0 \\ 0 & 5 \end{pmatrix}, \qquad T_{21}(-3) = \begin{pmatrix} 1 & 0 \\ -3 & 1 \end{pmatrix}.$$
Multiply $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ on the left by the third one:
$$T_{21}(-3) A = \begin{pmatrix} 1 & 2 \\ -3 + 3 & -6 + 4 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 0 & -2 \end{pmatrix}.$$
This is $A$ after $R_2 \leftarrow R_2 - 3R_1$, the first step of elimination.
The [[row operation example|J8M8K5EXE1]] applies one matrix of each type to a $3 \times 2$ matrix, and the [[column operation example|17K9NNTCZ7]] multiplies on the right.

### What is not elementary

The matrix $\begin{pmatrix} 0 & 2 \\ 1 & 0 \end{pmatrix}$ is invertible but not elementary, because it needs two row operations on $I_2$, as [[the non-example|YYBT7MBTY6]] shows.
The matrix $\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$ is not elementary either: scaling a row by $0$ is not an elementary row operation, and the result is singular.
Watch the shape of $I_2 + E_{11} = \operatorname{diag}(2, 1)$: it is elementary of type $D_1(2)$, but it is not a replacement, because that type needs $i \ne j$.

### Undoing a row operation

Every row operation can be reversed by another row operation of the same type, and that is why every elementary matrix is invertible:
$$P_{ij}^{-1} = P_{ij}, \qquad D_i(c)^{-1} = D_i(c^{-1}), \qquad T_{ij}(c)^{-1} = T_{ij}(-c).$$
For example, the reverse of $R_2 \leftarrow R_2 - 3R_1$ is $R_2 \leftarrow R_2 + 3R_1$, and
$$T_{21}(3)\, T_{21}(-3) = \begin{pmatrix} 1 & 0 \\ 3 - 3 & 1 \end{pmatrix} = I_2.$$
The [[row operation theorem|F7F6AA3XQ7]] proves these inverses in general.

### More rules you can use

The transpose of an elementary matrix is elementary: $P_{ij}^{\mathsf{T}} = P_{ij}$, $D_i(c)^{\mathsf{T}} = D_i(c)$ and $T_{ij}(c)^{\mathsf{T}} = T_{ji}(c)$.
The determinants are $\det P_{ij} = -1$, $\det D_i(c) = c$ and $\det T_{ij}(c) = 1$, and the sub-area on [[determinants|DTBK11SR77]] builds on these values.
A square matrix over a field is invertible exactly when it is a product of elementary matrices, by [[invertibility and row reduction|1ZK55FS2BF]].

### Watch out

Left and right are easy to mix up.
Left multiplication acts on rows and right multiplication acts on columns, and the indices swap roles.
On the left, $T_{ij}(c)$ adds $c$ times row $j$ to row $i$; on the right, it adds $c$ times column $i$ to column $j$.
For example, $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} T_{21}(-3) = \begin{pmatrix} 1 - 6 & 2 \\ 3 - 12 & 4 \end{pmatrix} = \begin{pmatrix} -5 & 2 \\ -9 & 4 \end{pmatrix}$ changes column $1$ by $-3$ times column $2$.

A second slip is to invert $T_{ij}(c)$ as $T_{ij}(1/c)$.
The inverse is $T_{ij}(-c)$, which subtracts what was added.

### History

Row operations are the steps of Gaussian elimination, which is much older than matrices: the Chinese text The Nine Chapters on the Mathematical Art already uses them.
Writing each step as a product with a matrix needs the matrix product, which Cayley defined in his memoir on matrices of 1858.

### Try it

First, write the $3 \times 3$ elementary matrix that adds $4$ times row 1 to row 3, and its inverse.
It is $T_{31}(4) = I_3 + 4E_{31}$, with $4$ in position $(3, 1)$, and its inverse is $T_{31}(-4)$.

Second, which row operation does left multiplication by $D_2(\tfrac{1}{2})$ perform on a $2 \times 2$ matrix?
It halves the second row and leaves the first row alone.

## Explanations

### L1 human

An elementary matrix is a record of one row operation.
We make it by doing the operation to the identity matrix.
Then multiplying any matrix on the left by it does the same operation to that matrix.
For example, swapping the two rows of the identity gives a matrix that swaps the two rows of anything it multiplies.

### L2 human

Here is a typical use: record a short elimination as a product.
Start from $A = \begin{pmatrix} 2 & 4 \\ 1 & 3 \end{pmatrix}$.
Halve row 1 with $D_1(\tfrac{1}{2})$, which gives $\begin{pmatrix} 1 & 2 \\ 1 & 3 \end{pmatrix}$, then subtract row 1 from row 2 with $T_{21}(-1)$, which gives $\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$.
Finally subtract twice row 2 from row 1 with $T_{12}(-2)$, which gives $I_2$.
So
$$T_{12}(-2)\, T_{21}(-1)\, D_1(\tfrac{1}{2})\, A = I_2,$$
and therefore $A^{-1} = T_{12}(-2)\, T_{21}(-1)\, D_1(\tfrac{1}{2})$.
Multiplying out gives $A^{-1} = \begin{pmatrix} 3/2 & -2 \\ -1/2 & 1 \end{pmatrix}$, and the 2 × 2 formula agrees, since $ad - bc = 2$.
The problem shows the typical use: a reduction to $I_n$ is a factorization of the inverse.

### L3 human

The elementary matrices generate the [[general linear group|0FCHE902D7]] $\mathrm{GL}_n(F)$ over a field.
The replacements $T_{ij}(c)$ alone generate the [[special linear group|0V9PMN0RBH]], by the theorem on [[generation by transvections|YSS4XNY9RC]].
Over a commutative ring, elementary matrices still make sense, with $c$ a unit in $D_i(c)$, but they need not generate $\mathrm{GL}_n(R)$.
The subgroup generated by the replacements is the elementary group $E_n(R)$, and comparing it with $\mathrm{GL}_n(R)$ is a starting point of algebraic K-theory.
