---
tag: 0N4XY7Z3NN
kind: concept
name: Upper triangular matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
specializes: [0JXZKX526R]
uses: [0JXZKX526R]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: Algebras of triangular matrices
inventory: [1W8C1QV0S3]
---

## Summary

An upper triangular matrix is a square matrix with only zeros below the main diagonal, so its possibly nonzero entries fill a triangle in the upper right corner.
It is the shape that elimination produces, and it is the shape in which systems, products and determinants become easy.
Exactly, a [[square matrix|0JXZKX526R]] $U = (u_{ij})$ of order $n$ is upper triangular when
$$u_{ij} = 0 \quad \text{for all } i > j,$$
and strictly upper triangular when $u_{ij} = 0$ for all $i \ge j$, so that the diagonal is zero as well.
A [[lower triangular matrix|00J3KZP8Y0]] has $u_{ij} = 0$ for $i < j$, and its [[transpose|09DXWYRD43]] is upper triangular, so every fact below has a lower twin.
The [[formal definition|0MKABWDRNC]] states all four conditions.

## Motivation

Gaussian elimination turns a system $Ax = b$ into a system $Ux = c$ with $U$ upper triangular.
The last equation of $Ux = c$ has one unknown, the one above it has two, and so on.
So we solve from the bottom up by [[back substitution|0ATFVE08MW]], one division and a few multiplications at each step.
Writing the elimination itself as a product of triangular matrices gives the [[LU decomposition|0RKG5YW66Y]] $A = LU$, a main tool of numerical linear algebra.

Triangular matrices also matter in theory.
Over the complex numbers every square matrix is [[similar to an upper triangular one|0363JMQ42Y]], and then its [[eigenvalues|0BQAA2BK3Q]] sit on the diagonal.
The topic on diagonalization and invariant subspaces builds on this.

## Notation

Upper triangular matrices are often called $U$ or $R$, and lower triangular ones $L$, as in $A = LU$ and $A = QR$.
A *unitriangular* (or unit triangular) matrix is triangular with every diagonal entry equal to $1$.
In Mathlib, `Matrix.BlockTriangular M id` says that `M i j = 0` whenever `j < i`, which is the upper triangular condition; the general [[triangular matrix|GTG8MJGDKC]] page covers it.

## Remarks

### Solving a triangular system

Take
$$U = \begin{pmatrix} 2 & 1 & -1 \\ 0 & 3 & 2 \\ 0 & 0 & 4 \end{pmatrix}, \qquad c = (3, 7, 8).$$
The last row says $4x_3 = 8$, so $x_3 = 2$.
The middle row says $3x_2 + 2 \cdot 2 = 7$, so $x_2 = 1$.
The top row says $2x_1 + 1 - 2 = 3$, so $x_1 = 2$.
Check: the top row gives $2 \cdot 2 + 1 \cdot 1 - 1 \cdot 2 = 3$.
Each step needs a division by a diagonal entry, and this is why the diagonal decides whether $U$ is [[invertible|7X1B65CTG4]].

### Products stay triangular

In [[a product of two 3 × 3 upper triangular matrices|NFJP659QFK]], the factors have diagonals $(1, 4, 6)$ and $(2, 1, 3)$:
$$\begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix} \begin{pmatrix} 2 & 0 & 1 \\ 0 & 1 & -1 \\ 0 & 0 & 3 \end{pmatrix} = \begin{pmatrix} 2 & 2 & 8 \\ 0 & 4 & 11 \\ 0 & 0 & 18 \end{pmatrix}.$$
The product is upper triangular, and its diagonal is $(1 \cdot 2, 4 \cdot 1, 6 \cdot 3)$.
This is the [[product theorem|45RET2Y995]]: in $(UV)_{ij} = \sum_k u_{ik} v_{kj}$, a nonzero term needs $i \le k \le j$.
For $i > j$ there is no such $k$, and for $i = j$ only $k = i$ is left.
Sums and scalar multiples are also upper triangular, so these matrices form a subring of $M_n(R)$.

### Strictly triangular means nilpotent

When the diagonal is zero too, each power pushes the entries one diagonal further up.
In [[the strictly upper triangular example|NRNV4AJJ0E]],
$$N = \begin{pmatrix} 0 & 1 & 2 \\ 0 & 0 & 3 \\ 0 & 0 & 0 \end{pmatrix}, \qquad N^2 = \begin{pmatrix} 0 & 0 & 3 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}, \qquad N^3 = 0.$$
In general a strictly upper triangular matrix of order $n$ has $N^n = 0$, so it is [[nilpotent|07BSPZPSMF]], by the [[nilpotency theorem|AW5RBMW7RK]].

### The numbers on the diagonal

The [[determinant|0K1KKMFHYH]] of a triangular matrix is the product of its diagonal entries.
Over a field, $U$ is invertible exactly when no diagonal entry is $0$, and then $U^{-1}$ is upper triangular too.
The characteristic polynomial is $(x - u_{11}) \cdots (x - u_{nn})$, so the diagonal entries are the eigenvalues, each counted with its multiplicity.
A [[diagonal matrix|044JNC7ZAA]] is both upper and lower triangular.

### What is not triangular

[[The product of an upper and a lower triangular matrix|8GDWHV3EPB]] can fail both conditions:
$$\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}.$$
A $2 \times 3$ matrix in row echelon form is not triangular in this sense either, because the definition asks for a square matrix; some books call such a shape upper trapezoidal.

### Watch out

"Triangular" says nothing about the diagonal, which can hold any entries; only the strict version asks for zeros there.
Also, the diagonal gives the eigenvalues only for a triangular matrix.
The matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has diagonal $(0, 0)$, but its eigenvalues are $1$ and $-1$, since it sends $(1, 1)$ to itself and $(1, -1)$ to its negative.

### History

Banachiewicz described the factorization of a matrix into triangular factors in 1938.
Turing studied the rounding errors of this factorization in a paper of 1948.

### Try it

First, find the diagonal of $\begin{pmatrix} 2 & 5 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 4 & -1 \\ 0 & 1 \end{pmatrix}$ without the full product.
It is $(2 \cdot 4, 3 \cdot 1) = (8, 3)$, and the full product is $\begin{pmatrix} 8 & 3 \\ 0 & 3 \end{pmatrix}$.

Second, is $\begin{pmatrix} 1 & 2 \\ 0 & 0 \end{pmatrix}$ invertible?
No: it is upper triangular with a diagonal entry $0$, so its determinant is $1 \cdot 0 = 0$.

## Explanations

### L1 human

An upper triangular matrix has zeros below the diagonal that runs from the top left to the bottom right.
For example, $\begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix}$ is upper triangular.
A system of equations with such a matrix is easy to solve: the last equation has only one unknown, so you find it first and work upward.
When you multiply two such matrices, the zeros below the diagonal stay zero.

### L2 human

Why do the zeros survive a product?
Think of the matrix as a map on column vectors, and let $V_j$ be the span of $e_1, \dots, e_j$.
Column $j$ of $U$ is $Ue_j$, and the zeros below position $j$ say that $Ue_j$ lies in $V_j$.
So $U$ maps each $V_j$ into itself, and for two such matrices,
$$UV(V_j) \subseteq U(V_j) \subseteq V_j.$$
So $UV$ is upper triangular again.
Modulo $V_{j-1}$, the vector $Ue_j$ is $u_{jj} e_j$, and so $UVe_j$ is $u_{jj} v_{jj} e_j$, which gives the diagonal rule.
The typical use of this view is to prove facts about triangular matrices without writing a single sum.

### L3 human

The chain $V_1 \subset V_2 \subset \cdots \subset V_n$ is the standard flag, and the invertible upper triangular matrices are exactly the invertible matrices that preserve it.
They form the Borel subgroup of the [[general linear group|0FCHE902D7]].
The strictly upper triangular matrices form a nilpotent Lie algebra under $[A, B] = AB - BA$, and the unitriangular matrices form a nilpotent group.
For $n \ge 2$ the ring of upper triangular matrices over a field is not semisimple, and its Jacobson radical is the ideal of strictly upper triangular matrices.
