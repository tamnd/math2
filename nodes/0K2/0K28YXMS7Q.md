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

Let $R$ be a ring, let $c \in R$, and let $A = (a_{ij})$ be an $m \times n$ [[matrix|0N1MY1T0W9]] over $R$.
The *scalar multiple* $cA$ is the $m \times n$ matrix with entries
$$(cA)_{ij} = c\, a_{ij}, \qquad 1 \le i \le m, \ 1 \le j \le n.$$
The *right scalar multiple* $Ac$ has the entries $a_{ij}\, c$.
When $R$ is commutative, $cA = Ac$.

## Remarks

- For scalars $c, d$ and matrices $A, B$ of one size: $c(A + B) = cA + cB$, $(c + d)A = cA + dA$, $c(dA) = (cd)A$ and $1A = A$.
- With [[matrix addition|0BVXADM10P]], these laws make $M_{m \times n}(F)$ a vector space over a field $F$.
- For square matrices, $cA = (cI)A$, where $cI$ is a [[scalar matrix|067NKSBEWT]].
- Over a noncommutative ring, the left and right multiples differ; for quaternions, $i \begin{pmatrix} j \end{pmatrix} = \begin{pmatrix} k \end{pmatrix}$ but $\begin{pmatrix} j \end{pmatrix} i = \begin{pmatrix} -k \end{pmatrix}$.

## Explanations

### L1 human

To multiply a matrix by a number, multiply every entry by that number.
For example, $2 \begin{pmatrix} 1 & -3 \\ 0 & 4 \end{pmatrix} = \begin{pmatrix} 2 & -6 \\ 0 & 8 \end{pmatrix}$.

### L2 human

Scalar multiplication scales the whole matrix, and so it scales the linear map $x \mapsto Ax$ by $c$.
Multiplying only one row by $c$ is a row operation, which is a different thing.
