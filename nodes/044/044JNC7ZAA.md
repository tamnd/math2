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

A diagonal matrix is a square matrix that can only stretch each coordinate by its own factor.
Every computation with it happens one diagonal entry at a time, so it is the simplest kind of matrix after the scalar matrices.
Exactly, a [[square matrix|0JXZKX526R]] $D = (d_{ij})$ of order $n$ is diagonal when $d_{ij} = 0$ for all $i \ne j$, and we write
$$\operatorname{diag}(d_1, \dots, d_n) = \begin{pmatrix} d_1 & 0 & \cdots & 0 \\ 0 & d_2 & \cdots & 0 \\ \vdots & & \ddots & \vdots \\ 0 & 0 & \cdots & d_n \end{pmatrix}.$$
The [[formal definition|0Q9PGXD9E4]] states this with the entry formula $\operatorname{diag}(d_1, \dots, d_n)_{ij} = d_i \delta_{ij}$.

## Motivation

For a general matrix, a power such as $A^{100}$ costs many products, and each product mixes all the entries.
For a diagonal matrix there is nothing to mix: $D^{100} = \operatorname{diag}(d_1^{100}, \dots, d_n^{100})$, and $Dx = (d_1 x_1, \dots, d_n x_n)$.
So questions about a diagonal matrix reduce to questions about $n$ separate numbers.

This is why so much of linear algebra tries to make a matrix diagonal.
A matrix that is [[similar|0E89HQATM8]] to a diagonal matrix is called [[diagonalizable|07SQCNV233]], and the theory of [[eigenvalues|0BQAA2BK3Q]] decides when this happens.
In applications the same idea turns a coupled system of equations into $n$ independent equations, one for each axis.

## Notation

Most books write $\operatorname{diag}(d_1, \dots, d_n)$, or $\operatorname{diag}(d)$ for a vector $d$.
Watch the other meaning: some books and programs write $\operatorname{diag}(A)$ for the vector of diagonal entries of a matrix $A$.
Mathlib keeps the two apart, with `Matrix.diagonal d` for the matrix built from a function `d : n → α` and `Matrix.diag A` for the vector of diagonal entries.
Some books also call a rectangular matrix diagonal when $a_{ij} = 0$ for $i \ne j$, as in the singular value decomposition, but here a diagonal matrix is always square.

## Remarks

### A first computation

Take $A = \operatorname{diag}(2, 5)$ and $B = \operatorname{diag}(3, -1)$.
Their sum and their product are again diagonal, and both are computed in each diagonal position:
$$A + B = \operatorname{diag}(5, 4), \qquad AB = \begin{pmatrix} 2 & 0 \\ 0 & 5 \end{pmatrix} \begin{pmatrix} 3 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 6 & 0 \\ 0 & -5 \end{pmatrix}.$$
Check: the entry $(1, 2)$ of $AB$ is $2 \cdot 0 + 0 \cdot (-1) = 0$.
In general, the entry formula gives
$$\operatorname{diag}(a) \operatorname{diag}(b) = \operatorname{diag}(a_1 b_1, \dots, a_n b_n),$$
so over a commutative ring two diagonal matrices always commute.

### Powers and polynomials

The product rule, used again and again, gives $D^k = \operatorname{diag}(d_1^k, \dots, d_n^k)$.
In [[the powers of diag(2, −1, 3)|DAVRDS5NV4]] this gives $D^5 = \operatorname{diag}(32, -1, 243)$ at once.
The same holds for every polynomial $p$: $p(D) = \operatorname{diag}(p(d_1), \dots, p(d_n))$.
Over a field, $D$ is [[invertible|0EB9N0S33C]] exactly when every $d_i \ne 0$, and then $D^{-1} = \operatorname{diag}(d_1^{-1}, \dots, d_n^{-1})$.

### Scaling rows and columns

What does a diagonal matrix do to a general matrix?
On the left it scales rows, and on the right it scales columns:
$$(DA)_{ij} = d_i a_{ij}, \qquad (AD)_{ij} = a_{ij} d_j.$$
[[Multiplying by diag(2, 3)|3BTM4ZNHX8]] shows the two results side by side.
Comparing the two formulas, $DA = AD$ exactly when $a_{ij}(d_i - d_j) = 0$ for all $i$ and $j$.
So a diagonal matrix commutes with every matrix only when all $d_i$ are equal, that is, when it is a [[scalar matrix|067NKSBEWT]].

### The numbers you can read off

A diagonal matrix is both upper and [[lower triangular|00J3KZP8Y0]], and it equals its own [[transpose|09DXWYRD43]], so it is [[symmetric|0VR671PHE5]].
Its [[determinant|00KDZRW4C0]] is $d_1 d_2 \cdots d_n$ and its [[trace|0XC1RDBY7A]] is $d_1 + \dots + d_n$.
The standard basis vector $e_i$ is an [[eigenvector|0N6960W0BV]] with eigenvalue $d_i$, because $D e_i$ is column $i$ of $D$, which is $d_i e_i$.
The [[identity|06DW9BAWB1]], the [[zero matrix|0ZTKJJDGR7]] and every scalar matrix are diagonal.

### What is not diagonal

The [[swap matrix|JP3T5EWT3M]] $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ fails the condition, since its entries at $(1, 2)$ and $(2, 1)$ are not $0$.
Its square is $I$, but squaring its diagonal $(0, 0)$ would give $(0, 0)$, so the rule for powers does not apply to it.
An upper [[triangular matrix|0N4XY7Z3NN]] such as $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ also fails, because of the entry $1$ above the diagonal.

### Watch out

A diagonal matrix does not commute with every matrix.
With $D = \operatorname{diag}(1, 2)$ and $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, the product $DA$ has entry $(1, 2)$ equal to $1$, but $AD$ has entry $(1, 2)$ equal to $2$.
Only scalar matrices commute with everything.
Also, "diagonal" is not "diagonalizable": the swap matrix is diagonalizable, but it is not diagonal.

### Try it

First, compute $\operatorname{diag}(1, -2)^4$.
The answer is $\operatorname{diag}(1, 16)$, since $(-2)^4 = 16$.

Second, for which $c$ does $\operatorname{diag}(1, c)$ commute with $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$?
The condition $a_{12}(1 - c) = 0$ with $a_{12} = 2$ forces $c = 1$.

## Explanations

### L1 human

A diagonal matrix has numbers only on the main diagonal, from the top left to the bottom right, and zeros everywhere else.
It stretches the first coordinate of a vector by the first number, the second coordinate by the second number, and so on.
For example, $\operatorname{diag}(2, 3)$ sends $(1, 1)$ to $(2, 3)$.
Multiplying two diagonal matrices just multiplies the numbers in the same places, so $\operatorname{diag}(2, 3)$ times itself is $\operatorname{diag}(4, 9)$.

### L2 human

Here is a typical use: compute $A^{10}$ for $A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$.
The vectors $(1, 0)$ and $(1, 1)$ satisfy $A(1, 0) = (1, 0)$ and $A(1, 1) = (2, 2)$, so with $P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ we get $AP = PD$ for $D = \operatorname{diag}(1, 2)$.
So $A = PDP^{-1}$ with $P^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$, and the middle factors cancel in a power:
$$A^{10} = P D^{10} P^{-1} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 1024 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1023 \\ 0 & 1024 \end{pmatrix}.$$
Check with $k = 2$: the same formula gives $\begin{pmatrix} 1 & 3 \\ 0 & 4 \end{pmatrix}$, and direct multiplication gives $A^2 = \begin{pmatrix} 1 & 3 \\ 0 & 4 \end{pmatrix}$.
The hard power became a power of a diagonal matrix, which is the typical reason to diagonalize.

### L3 human

When $R$ is commutative, the diagonal matrices of order $n$ form a commutative subring of $M_n(R)$ that is isomorphic to the product ring $R^n$.
The invertible diagonal matrices form a maximal torus of the [[general linear group|0FCHE902D7]], a basic object in the theory of algebraic groups.
Over a field, a family of pairwise commuting diagonalizable matrices can be [[diagonalized at the same time|0FK17N4DKA]].
The matrices that commute with a diagonal matrix with distinct diagonal entries are exactly the diagonal matrices, by the condition $a_{ij}(d_i - d_j) = 0$.
