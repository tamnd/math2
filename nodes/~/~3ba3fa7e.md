---
tag: ~3ba3fa7e
kind: definition
name: Scalar matrix
msc: [15A99]
defines: ~248eb908
uses: [~bf830b1b, ~15909503]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonal_matrix
    locator: Scalar matrix
---

## Definition

Let $R$ be a ring, let $n \ge 0$ be an integer, and let $c \in R$.
The *scalar matrix* of order $n$ with value $c$ is the [[diagonal matrix|~e852257f]] $\operatorname{diag}(c, \dots, c) = c I_n$, where $I_n$ is the [[identity matrix|~15909503]].
A square matrix is a *scalar matrix* when it equals $c I_n$ for some $c \in R$.

## Remarks

Over a commutative ring, a scalar matrix commutes with every square matrix of the same order.
Over a field, the scalar matrices are exactly the $n \times n$ matrices that commute with every $n \times n$ matrix.
As a linear map, $c I_n$ multiplies each vector by $c$.

## Explanations

### L1 human

A scalar matrix has the same number at every place on the diagonal and zeros elsewhere.
Multiplying by it is the same as multiplying by that number.
For example, $3 I_2 = \begin{pmatrix} 3 & 0 \\ 0 & 3 \end{pmatrix}$ triples each vector.
