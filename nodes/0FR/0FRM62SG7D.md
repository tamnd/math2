---
tag: 0FRM62SG7D
kind: definition
name: Scalar matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
defines: 067NKSBEWT
uses: [0Q9PGXD9E4, ~495c2486]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonal_matrix
    locator: Scalar matrix
inventory: [2HSM4TW6Y6]
---

## Definition

Let $R$ be a ring with identity, let $n \ge 0$ be an integer, and let $c \in R$.
The *scalar matrix* of order $n$ with value $c$ is the [[diagonal matrix|0Q9PGXD9E4]]
$$cI_n = \operatorname{diag}(c, \dots, c) = \begin{pmatrix} c & & \\ & \ddots & \\ & & c \end{pmatrix},$$
where $I_n$ is the [[identity matrix|~495c2486]].
Its entries are $(cI_n)_{ij} = c\,\delta_{ij}$.
A square matrix is a *scalar matrix* when it equals $cI_n$ for some $c \in R$.

## Notation

- The size is often left out: $cI$ or simply $c$.
- In Mathlib, the scalar matrix is `Matrix.scalar n c`, equal to `Matrix.diagonal (fun _ => c)`.

## Remarks

- Over a commutative ring, a scalar matrix commutes with every square matrix of the same order.
- Over a field, the scalar matrices are exactly the $n \times n$ matrices that commute with every $n \times n$ matrix, by the [[centre theorem|~c64c046f]].
- As a linear map, $cI_n$ multiplies each vector by $c$.

## Explanations

### L1 human

A scalar matrix has the same number at every place on the diagonal and zeros elsewhere.
Multiplying by it is the same as multiplying by that number.

### L2 human

Each scalar matrix is diagonal, but a diagonal matrix such as $\operatorname{diag}(1, 2)$ is scalar only when its diagonal entries are equal.
