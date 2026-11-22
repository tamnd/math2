---
tag: 0Y7H3SAVA1
kind: concept
name: Matrix addition
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
specializes: [0M418FE7BB]
uses: [0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_addition
    locator: Entrywise sum
  - url: https://en.wikipedia.org/wiki/Matrix_(mathematics)
    locator: Basic operations
  - book: isbn:9780321982384
    locator: Section 2.1
  - url: https://hefferon.net/linearalgebra/
    locator: Chapter Three, Section IV
same_as:
  wikidata: Q2264115
  wikipedia: Matrix addition
inventory: [NAYXFHVVCR]
---

## Summary

Two matrices of the same size are added position by position, and a matrix is scaled by multiplying every entry by the same number.
With these two operations, the matrices of one size behave exactly like vectors, so all of vector arithmetic applies to them.
For $m \times n$ [[matrices|0VD9ZSWWJG]] $A = (a_{ij})$ and $B = (b_{ij})$ and a scalar $c$, the rules are
$$(A + B)_{ij} = a_{ij} + b_{ij}, \qquad (cA)_{ij} = c\, a_{ij}.$$
The [[definition of addition|0BVXADM10P]] and the [[definition of scalar multiplication|0K28YXMS7Q]] state them exactly, and [[scalar multiplication|09V6DDACXR]] has its own short page.
Over a field $F$, the $m \times n$ matrices form a [[vector space|0RE6X3BGPN]] of dimension $mn$ under these operations.

## Motivation

The first reason for the rules is data.
If $A$ records the sales of three products in two shops in one week, and $B$ records the sales of the next week, then the totals for both weeks are $A + B$, shop by shop and product by product.
If every sale is doubled, the new table is $2A$.

The second reason is linear maps.
Let $A$ and $B$ be the matrices of two linear maps $f, g \colon F^n \to F^m$, so that $f(x) = Ax$ and $g(x) = Bx$.
Then the map $x \mapsto f(x) + g(x)$ has the matrix $A + B$, and the map $x \mapsto c f(x)$ has the matrix $cA$.
So the entrywise rules are exactly the rules that match adding and scaling linear maps, and the [[matrix product|032Q9FB8MT]] will later match composing them.

## Notation

The difference is $A - B = A + (-1)B$, with entries $a_{ij} - b_{ij}$, and $-A$ is the matrix with entries $-a_{ij}$.
A scalar multiple is written $cA$, and over a commutative ring $Ac$ means the same.
Over a noncommutative ring the two can differ, so books say on which side the scalar acts.
In Mathlib, `A + B` and `c • A` are the pointwise operations on the functions `m → n → α`, where `m` and `n` can be any finite index types.

## Remarks

### A first computation

Take
$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \qquad B = \begin{pmatrix} 0 & 1 \\ -1 & 2 \end{pmatrix}.$$
Scale first, then subtract position by position:
$$2A - 3B = \begin{pmatrix} 2 & 4 \\ 6 & 8 \end{pmatrix} - \begin{pmatrix} 0 & 3 \\ -3 & 6 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 9 & 2 \end{pmatrix}.$$
Check: at position $(2, 1)$ the rule gives $2 \cdot 3 - 3 \cdot (-1) = 9$.
The [[worked combination 2A − 3B|R3SH1T0KYW]] checks the arithmetic laws on the same pair.

### Matrices as vectors

Every matrix splits into its entries times the [[matrix units|A4HTT7JFD1]] $E_{ij}$, which have a $1$ in position $(i, j)$ and zeros elsewhere.
For example,
$$\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} + \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} = I_2, \qquad \begin{pmatrix} a & b \\ c & d \end{pmatrix} = a E_{11} + b E_{12} + c E_{21} + d E_{22}.$$
So a $2 \times 2$ matrix is a vector with four coordinates written in a square, and $M_{m \times n}(F)$ has the basis $(E_{ij})$ of $mn$ elements, as the [[space of matrices|0RE6X3BGPN]] shows.

### The rules you can use

For matrices $A, B, C$ of one size and scalars $c, d$, each rule below holds because it holds for numbers in every position.
Addition is commutative and associative, $A + B = B + A$ and $(A + B) + C = A + (B + C)$.
The [[zero matrix|0ZTKJJDGR7]] is the identity, $A + 0 = A$, and $A + (-A) = 0$.
Scaling distributes, $c(A + B) = cA + cB$ and $(c + d)A = cA + dA$, and it is compatible with products of scalars, $c(dA) = (cd)A$ and $1A = A$.
Both operations also fit with the matrix product: $A(B + C) = AB + AC$ by the [[distributive law|0RXD6EZYBK]], and $A(cB) = c(AB)$ over a commutative ring.

### What it is not

A $2 \times 2$ matrix and a $2 \times 3$ matrix cannot be added, because they have no common set of positions; see [[matrices of different sizes|VRD3P83FH7]].
Adding a number to a matrix, as in $A + 1$, is not matrix addition either.
Software often reads $A + 1$ as adding $1$ to each entry, while algebra books read it as $A + I$, so the expression is ambiguous until a convention is fixed.

### Watch out

The determinant does not respect these operations.
With $A = B = I_2$ we get $\det(A + B) = \det(2 I_2) = 4$, while $\det A + \det B = 2$.
In general $\det(cA) = c^n \det A$ for an $n \times n$ matrix, not $c \det A$, because each of the $n$ rows is scaled by $c$.
Also, multiplying only one row by $c$ is a row operation, not the scalar multiple $cA$.

### History

Cayley's memoir on the theory of matrices of 1858 defined the sum of two matrices of the same size entry by entry, together with the product.

### Try it

First, compute $\begin{pmatrix} 1 & -1 \\ 0 & 2 \end{pmatrix} + 3 \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.
The scaled matrix is $\begin{pmatrix} 0 & 3 \\ 3 & 0 \end{pmatrix}$, so the sum is $\begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix}$.

Second, solve $X + \begin{pmatrix} 2 & 5 \end{pmatrix} = 2 \begin{pmatrix} 1 & 1 \end{pmatrix}$ for the $1 \times 2$ matrix $X$.
Subtract on both sides: $X = \begin{pmatrix} 2 & 2 \end{pmatrix} - \begin{pmatrix} 2 & 5 \end{pmatrix} = \begin{pmatrix} 0 & -3 \end{pmatrix}$.

## Explanations

### L1 human

To add two matrices of the same size, add the numbers in the same positions.
To multiply a matrix by a number, multiply every entry by that number.
For example, $3 \begin{pmatrix} 1 & -1 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 3 & -3 \\ 0 & 6 \end{pmatrix}$.
If two tables hold the scores of two rounds of a game, their sum holds the total scores.

### L2 human

Here is a typical use: find the matrix of the map $h(x) = 2f(x) - g(x)$, where $f(x) = Ax$ and $g(x) = Bx$ with $A = \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 1 \\ 1 & 3 \end{pmatrix}$.
Since $h(x) = 2Ax - Bx = (2A - B)x$, the matrix of $h$ is
$$2A - B = \begin{pmatrix} 2 - 0 & 0 - 1 \\ 4 - 1 & 2 - 3 \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ 3 & -1 \end{pmatrix}.$$
Check with $x = e_1$: $2f(e_1) - g(e_1) = 2(1, 2) - (0, 1) = (2, 3)$, which is the first column of $2A - B$.
The trap is to add matrices of different sizes, which would mean adding maps between different spaces.

### L3 human

The vector space $M_{m \times n}(F)$ is isomorphic to the [[space of linear maps|0X9MBPP2Z3]] $\operatorname{Hom}(F^n, F^m)$, and the isomorphism respects both operations.
Over a ring $R$, the set $M_{m \times n}(R)$ is a free left $R$-module with basis $(E_{ij})$, and also a free right module.
For square matrices, addition and the product together make $M_n(F)$ an $F$-algebra, the [[matrix ring|AB2MD5CD13]], and the sub-area on [[vector spaces|MVH97H8B2J]] treats $M_{m \times n}(F)$ as one of its standard examples.
