---
tag: 0K28YXMS7Q
kind: definition
name: Scalar multiplication of matrices
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
defines: 09V6DDACXR
uses: [0N1MY1T0W9]
sources:
  - url: https://en.wikipedia.org/wiki/Scalar_multiplication
    locator: lead section
  - book: isbn:9780321982384
    locator: Section 2.1
---

## Definition

A matrix is multiplied by a scalar by multiplying each of its entries by that scalar.
Let $R$ be a ring, let $c \in R$, and let $A = (a_{ij})$ be an $m \times n$ [[matrix|0N1MY1T0W9]] over $R$.
The *scalar multiple* $cA$ is the $m \times n$ matrix with entries
$$(cA)_{ij} = c\, a_{ij}, \qquad 1 \le i \le m, \ 1 \le j \le n.$$
The *right scalar multiple* $Ac$ has the entries $a_{ij}\, c$.
When $R$ is commutative, $cA = Ac$.

## Notation

The scalar is usually written on the left, as $cA$, and the product sign is left out.
In Mathlib the left multiple is `c • A`, defined pointwise, so `(c • A) i j = c * A i j`.

## Remarks

Each part of the definition has a job.
The scalar $c$ must lie in the same ring $R$ as the entries, so that the product $c\, a_{ij}$ is defined.
The size does not change, so $cA$ can be added to $A$ and to any other $m \times n$ matrix.
The two products $c\, a_{ij}$ and $a_{ij}\, c$ give two definitions, which agree only when the scalars commute with the entries.

For a small case, the definition with $c = -2$ gives
$$-2 \begin{pmatrix} 1 & 0 & 3 \\ -1 & 2 & 5 \end{pmatrix} = \begin{pmatrix} -2 & 0 & -6 \\ 2 & -4 & -10 \end{pmatrix}.$$

The laws of the ring pass to matrices one position at a time.
For scalars $c, d$ and matrices $A, B$ of one size, $c(A + B) = cA + cB$, $(c + d)A = cA + dA$, $c(dA) = (cd)A$ and $1A = A$ when $R$ has an identity.
Together with [[matrix addition|0BVXADM10P]], these laws make $M_{m \times n}(F)$ a [[vector space|0RE6X3BGPN]] over a field $F$.

For square matrices, $cA = (cI)A$, where $cI$ is a [[scalar matrix|067NKSBEWT]].

The side of the scalar matters over a noncommutative ring.
For the quaternions, $ij = k$ and $ji = -k$, so $i \begin{pmatrix} j \end{pmatrix} = \begin{pmatrix} k \end{pmatrix}$ but $\begin{pmatrix} j \end{pmatrix} i = \begin{pmatrix} -k \end{pmatrix}$.

## Explanations

### L1 human

To multiply a matrix by a number, multiply every entry by that number.
For example, $2 \begin{pmatrix} 1 & -3 \\ 0 & 4 \end{pmatrix} = \begin{pmatrix} 2 & -6 \\ 0 & 8 \end{pmatrix}$.
The result has the same size as the matrix you started with.

### L2 human

Scalar multiplication scales the whole matrix, and so it scales the linear map $x \mapsto Ax$ by $c$, since $(cA)x = c(Ax)$.
The typical use is in linear combinations such as $2A - 3B$, where both matrices are scaled before they are added.
The trap is to multiply only one row by $c$, which is a row operation and a different thing.
