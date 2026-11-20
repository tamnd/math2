---
tag: 0M79HRJCRR
kind: definition
name: Elementary matrix
msc: [15A23]
topics: [P8J6QR66TJ]
audience: ug1
defines: 01REXW3WWE
uses: [06DW9BAWB1, 0DE5R5EB4D]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_matrix
    locator: lead section
  - book: isbn:9780321982384
    locator: Section 2.2
---

## Definition

Let $F$ be a field and let $n \ge 1$ be an integer.
An $n \times n$ *elementary matrix* over $F$ is a matrix that results from the [[identity matrix|06DW9BAWB1]] $I_n$ by one [[elementary row operation|04XWH28452]].
There are three types:

1. $P_{ij}$, for $i \ne j$: exchange rows $i$ and $j$ of $I_n$.
2. $D_i(c)$, for $c \ne 0$: multiply row $i$ of $I_n$ by $c$.
3. $T_{ij}(c)$, for $i \ne j$ and $c \in F$: add $c$ times row $j$ of $I_n$ to row $i$.

## Notation

Let $E_{ij}$ be the $n \times n$ matrix with entry $1$ in position $(i, j)$ and $0$ in all other positions.
Then $T_{ij}(c) = I_n + c E_{ij}$, and $D_i(c) = I_n + (c - 1) E_{ii}$.
The matrix $P_{ij}$ equals $I_n - E_{ii} - E_{jj} + E_{ij} + E_{ji}$.

## Remarks

The type $T_{ij}(0)$ is the identity matrix, and some books exclude it.
The concept page lists the main facts: left multiplication by an elementary matrix performs its row operation, and each elementary matrix is invertible.
The same definition works over a commutative ring, when $c$ in type 2 is a unit.

## Explanations

### L1 human

An elementary matrix stores one row operation as a matrix.
To do the operation on $A$, we multiply $A$ on the left by this matrix.
Then a whole elimination becomes a product of elementary matrices.

### L2 human

For $n = 3$, the three types include $P_{13} = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix}$, $D_2(5) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 5 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ and $T_{31}(-2) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ -2 & 0 & 1 \end{pmatrix}$.
In $T_{31}(-2)$ the entry $-2$ sits in row $3$ and column $1$: the operation changes row $3$ by a multiple of row $1$.
A trap: in type 2 the scalar must be nonzero, since multiplying a row by $0$ loses information.
