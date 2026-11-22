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

A scalar matrix is a square matrix that has one fixed element at every place of the main diagonal and zeros everywhere else.
Let $R$ be a ring with identity, let $n \ge 1$ be an integer, and let $c \in R$.
The *scalar matrix* of order $n$ with value $c$ is the [[diagonal matrix|0Q9PGXD9E4]]
$$cI_n = \operatorname{diag}(c, \dots, c) = \begin{pmatrix} c & & \\ & \ddots & \\ & & c \end{pmatrix},$$
where $I_n$ is the [[identity matrix|6NHZRCKJNW]].
Its entries are $(cI_n)_{ij} = c\,\delta_{ij}$, where $\delta_{ij}$ is the Kronecker delta.
A square matrix $A$ over $R$ is a *scalar matrix* when $A = cI_n$ for some $c \in R$.

## Notation

Books often drop the size and write $cI$, and some write only $c$ when the meaning is clear from the context.
In Mathlib the scalar matrix is `Matrix.scalar n c`, which equals `Matrix.diagonal (fun _ => c)`.

## Remarks

The definition has two conditions, and a matrix must pass both.
The first is that every entry off the main diagonal is $0$, which makes the matrix diagonal.
The second is that all the diagonal entries are the same element $c$.
For example, over $\mathbb{R}$,
$$2I_2 = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$$
passes both tests.
The matrix $\operatorname{diag}(1, 2)$ passes the first test and fails the second, so it is diagonal but not scalar.
The matrix $\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$ has equal diagonal entries but fails the first test.

The value $c = 0$ is allowed, so the zero matrix of order $n$ is a scalar matrix, and $c = 1$ gives $I_n$ itself.

Why do we ask for a ring with identity?
The identity $1 \in R$ is needed to form $I_n$, although the entries $c\,\delta_{ij}$ make sense without it.
With the identity, the products are easy to read:
$$\big((cI_n) A\big)_{ij} = \sum_{k} c\,\delta_{ik}\, a_{kj} = c\, a_{ij}, \qquad \big(A (cI_n)\big)_{ij} = \sum_{k} a_{ik}\, c\,\delta_{kj} = a_{ij}\, c.$$
So $(cI_n)A = cA$ and $A(cI_n) = Ac$ for every $n \times n$ matrix $A$.
Over a commutative ring these agree, and a scalar matrix commutes with every square matrix of its order.
Over a field the converse holds too: by the [[theorem on the center of the matrix ring|DVZ1V4A884]], the matrices that commute with all others are exactly the scalar matrices.
The concept page on [[scalar matrices|067NKSBEWT]] tells the whole story.

## Explanations

### L1 human

A scalar matrix has the same number at every place on the diagonal and zeros elsewhere, like $\begin{pmatrix} 5 & 0 \\ 0 & 5 \end{pmatrix}$.
Multiplying a matrix or a vector by it gives the same result as multiplying by the number $5$.

### L2 human

To test whether a square matrix is scalar, check two things in order.
First, every entry off the diagonal must be $0$.
Second, the diagonal entries must all be equal.
For $\operatorname{diag}(3, 3, 3)$ both checks pass, and the matrix is $3I_3$.
Watch out: a diagonal matrix with different diagonal entries, such as $\operatorname{diag}(1, 2)$, is not scalar, and it does not commute with $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.
Check: $\operatorname{diag}(1, 2) \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, while $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \operatorname{diag}(1, 2) = \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix}$.
