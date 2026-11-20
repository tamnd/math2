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

An elementary matrix is a square matrix that we get from the [[identity matrix|06DW9BAWB1]] by one [[elementary row operation|04XWH28452]].
There are three types: a row exchange, a row scaling by a nonzero scalar, and a row replacement.
A row replacement adds a multiple of one row to another row.
Multiplying a matrix on the left by an elementary matrix performs that row operation, by the [[row operation theorem|~11309c07]].
Multiplying on the right performs a matching column operation.
Each elementary matrix is invertible, and its inverse is the elementary matrix of the inverse operation.
Elementary matrices turn Gaussian elimination into matrix algebra: a whole elimination is a product of elementary matrices.

## Motivation

Row reduction is a sequence of steps on the rows of a matrix.
To prove facts about it, we want to write each step as an algebraic operation.
Take the step "add $-3$ times row 1 to row 2" on a matrix with two rows.
This step is the same as the [[matrix product|032Q9FB8MT]] with $\begin{pmatrix} 1 & 0 \\ -3 & 1 \end{pmatrix}$ on the left.
Then a reduction $A \to R$ becomes an equation $R = E_k \cdots E_1 A$.
This equation lets us compute inverses, prove the [[invertible matrix theorem|~9b681771]] and find factorizations such as the [[LU decomposition|0RKG5YW66Y]].

## Notation

- $P_{ij}$, for $i \ne j$, exchanges rows $i$ and $j$; it is a [[permutation matrix|08SP3DF8NB]].
- $D_i(c)$, for $c \ne 0$, multiplies row $i$ by $c$; it is the [[diagonal matrix|044JNC7ZAA]] with $c$ in position $i$ and $1$ elsewhere.
- $T_{ij}(c) = I_n + c E_{ij}$, for $i \ne j$, adds $c$ times row $j$ to row $i$. Here $E_{ij}$ is the matrix unit with entry $1$ in position $(i, j)$ and $0$ elsewhere. For $c \ne 0$ it is a [[transvection|0DTCBCKEJP]].
- Some books write $E$ for a generic elementary matrix, or use other letters for the three types.

## Remarks

### Examples

- For $n = 2$: $P_{12} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, $D_2(5) = \begin{pmatrix} 1 & 0 \\ 0 & 5 \end{pmatrix}$ and $T_{21}(-3) = \begin{pmatrix} 1 & 0 \\ -3 & 1 \end{pmatrix}$.
- The [[row operation example|~c061c582]] applies one matrix of each type to a $3 \times 2$ matrix.
- The [[column operation example|~9fa7c479]] multiplies on the right and checks the inverses.

### Non-examples

- The matrix $\begin{pmatrix} 0 & 2 \\ 1 & 0 \end{pmatrix}$ is invertible but not elementary, since it needs two row operations on $I_2$; see the [[non-example|~562eb430]].
- $D_1(0) = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$ is not elementary: scaling a row by $0$ is not an elementary row operation, and the result is singular.
- $I_2 + E_{11} = \operatorname{diag}(2, 1)$ is elementary of type $D_1(2)$, but it is not of type $T_{ij}(c)$, because that type needs $i \ne j$.

### Basic properties

- $EA$ is the result of the row operation of $E$ on $A$. Also, $AE$ is the result of a column operation, by the [[row operation theorem|~11309c07]].
- $P_{ij}^{-1} = P_{ij}$, $D_i(c)^{-1} = D_i(c^{-1})$ and $T_{ij}(c)^{-1} = T_{ij}(-c)$, by the same theorem.
- The transpose of an elementary matrix is elementary: $P_{ij}^{\mathsf{T}} = P_{ij}$, $D_i(c)^{\mathsf{T}} = D_i(c)$ and $T_{ij}(c)^{\mathsf{T}} = T_{ji}(c)$.
- $\det P_{ij} = -1$, $\det D_i(c) = c$ and $\det T_{ij}(c) = 1$; the sub-area on [[determinants|DTBK11SR77]] uses these values.
- A square matrix over a field is invertible if and only if it is a product of elementary matrices, by [[invertibility and row reduction|1ZK55FS2BF]].

### History

Row operations are the steps of Gaussian elimination, which is much older than matrices.
The Chinese text The Nine Chapters on the Mathematical Art already uses them.
To write each step as a product with a matrix, one needs the matrix product, which Cayley defined in his memoir of 1858.

### Common errors

- Students multiply on the wrong side. Left multiplication acts on rows and right multiplication acts on columns.
- Students mix up the indices of $T_{ij}(c)$. On the left, $T_{ij}(c)$ adds $c$ times row $j$ to row $i$. On the right, it adds $c$ times column $i$ to column $j$.
- Students invert $T_{ij}(c)$ as $T_{ij}(1/c)$. The inverse is $T_{ij}(-c)$, which subtracts what was added.

## Explanations

### L1 human

An elementary matrix is a record of one row operation.
We make it by doing the operation to the identity matrix.
Then multiplying any matrix on the left by it does the same operation to that matrix.

### L2 human

Worked example: let $E = T_{21}(-3) = \begin{pmatrix} 1 & 0 \\ -3 & 1 \end{pmatrix}$ and $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$.

1. $EA = \begin{pmatrix} 1 & 2 \\ -3 + 3 & -6 + 4 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 0 & -2 \end{pmatrix}$, which is $A$ after $R_2 \to R_2 - 3R_1$.
2. The inverse operation is $R_2 \to R_2 + 3R_1$, with matrix $T_{21}(3)$.
3. Check: $T_{21}(3) T_{21}(-3) = \begin{pmatrix} 1 & 0 \\ 3 - 3 & 1 \end{pmatrix} = I_2$.

The typical use is to turn the statement "$A$ row reduces to $R$" into the equation $R = EA$ with an invertible $E$.

### L3 human

The elementary matrices generate the [[general linear group|0FCHE902D7]] $\mathrm{GL}_n(F)$ over a field.
The matrices $T_{ij}(c)$ alone generate the [[special linear group|0V9PMN0RBH]], by the theorem on [[generation by transvections|~b06f837f]].
Over a commutative ring, elementary matrices still make sense, with $c$ a unit in $D_i(c)$, but they need not generate $\mathrm{GL}_n(R)$.
The subgroup they generate is studied in algebraic K-theory.
