---
tag: 0FRM62SG7D
kind: definition
name: Scalar matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
defines: 067NKSBEWT
uses: [0Q9PGXD9E4, 6NHZRCKJNW]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonal_matrix
    locator: Scalar matrix
inventory: [2HSM4TW6Y6]
---

## Definition

Let $R$ be a ring with identity, let $n \ge 1$ be an integer, and let $c \in R$.
The *scalar matrix* of order $n$ with value $c$ is the [[diagonal matrix|0Q9PGXD9E4]]
$$cI_n = \operatorname{diag}(c, \dots, c) = \begin{pmatrix} c & & \\ & \ddots & \\ & & c \end{pmatrix},$$
where $I_n$ is the [[identity matrix|6NHZRCKJNW]].
Its entries are $(cI_n)_{ij} = c\,\delta_{ij}$, so $c$ on the diagonal and $0$ off it.
A square matrix is called a *scalar matrix* when it equals $cI_n$ for some $c \in R$.

## Notation

The size is often left out, as in $cI$, and some books write just $c$.
In Mathlib, the scalar matrix is `Matrix.scalar n c`, which equals `Matrix.diagonal (fun _ => c)`.

## Remarks

### Examples

In size $2$ over $\mathbb{R}$,
$$2I_2 = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}, \qquad -I_2 = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}, \qquad 0I_2 = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$$
are scalar matrices, while $\operatorname{diag}(1, 2)$ is diagonal but not scalar.

### What the definition gives

For every $n \times n$ matrix $A$, the products are $(cI_n)A = cA$ and $A(cI_n) = Ac$.
So over a commutative ring, a scalar matrix commutes with every square matrix of the same order.
Over a field, the scalar matrices are exactly the $n \times n$ matrices that commute with every $n \times n$ matrix, by the [[center theorem|DVZ1V4A884]].
As a linear map of $F^n$, the matrix $cI_n$ multiplies each vector by $c$.

## Explanations

### L1 human

A scalar matrix has the same number at every place on the diagonal and zeros elsewhere.
Multiplying by it is the same as multiplying by that number.

### L2 human

Each scalar matrix is diagonal, but a diagonal matrix is scalar only when all its diagonal entries are equal.
To test a matrix, check two things: every entry off the diagonal is $0$, and the diagonal entries agree.
For example, $\operatorname{diag}(1, 2)$ passes the first test and fails the second.
