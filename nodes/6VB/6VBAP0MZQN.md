---
tag: 6VBAP0MZQN
kind: example
name: The trace of AᵀA is the sum of the squares of the entries
msc: ["15A15"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [0XC1RDBY7A]
uses: [07PTPSZPME, 0W809K6AW0, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Frobenius_inner_product
    locator: lead section
---

## Example

The diagonal of $A^{\mathsf{T}} A$ holds the squared lengths of the columns of $A$, so its trace adds up the squares of all the entries.
Let
$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \qquad A^{\mathsf{T}} = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}.$$

1. The [[product|076JGP6R3T]] is
$$A^{\mathsf{T}} A = \begin{pmatrix} 1 + 9 & 2 + 12 \\ 2 + 12 & 4 + 16 \end{pmatrix} = \begin{pmatrix} 10 & 14 \\ 14 & 20 \end{pmatrix}.$$
2. By the [[definition|07PTPSZPME]], $\operatorname{tr}(A^{\mathsf{T}} A) = 10 + 20 = 30$.
3. The sum of the squares of the entries of $A$ is $1 + 4 + 9 + 16 = 30$, the same number.
4. In general, $(A^{\mathsf{T}} A)_{jj} = \sum_i a_{ij}^2$ is the squared length of column $j$, and summing over $j$ gives
$$\operatorname{tr}(A^{\mathsf{T}} A) = \sum_{i,j} a_{ij}^2.$$
5. The other order gives
$$A A^{\mathsf{T}} = \begin{pmatrix} 1 + 4 & 3 + 8 \\ 3 + 8 & 9 + 16 \end{pmatrix} = \begin{pmatrix} 5 & 11 \\ 11 & 25 \end{pmatrix},$$
a different matrix with the same trace $30$, as the cyclic property $\operatorname{tr}(A A^{\mathsf{T}}) = \operatorname{tr}(A^{\mathsf{T}} A)$ predicts.
Its diagonal holds the squared lengths $5$ and $25$ of the rows.

## Remarks

### What it gives you

The number $\sqrt{\operatorname{tr}(A^{\mathsf{T}} A)} = \sqrt{30}$ is the [[Frobenius norm|JT8Q204E4R]] of $A$.
For real $A$, a sum of squares is $0$ only when every term is $0$, so $\operatorname{tr}(A^{\mathsf{T}} A) = 0$ only when $A = 0$.
This is the fact that makes $\operatorname{tr}(A^{\mathsf{T}} B)$ an inner product.

### Watch out

Over $\mathbb{C}$ the transpose gives the wrong answer.
For $A = (i)$ you get $\operatorname{tr}(A^{\mathsf{T}} A) = i^2 = -1$, which is not a length.
The right form uses the conjugate transpose, $\operatorname{tr}(A^* A) = \sum_{i,j} |a_{ij}|^2$, which gives $|i|^2 = 1$ here.

## Explanations

### L1 human

Multiply a matrix by its transpose and add up the diagonal.
The result is the sum of the squares of all the entries.
So this trace is never negative for a real matrix, and it is $0$ only for the zero matrix.

### L2 human

The diagonal of $A^{\mathsf{T}} A$ holds the squared lengths of the columns, and the diagonal of $A A^{\mathsf{T}}$ holds the squared lengths of the rows.
Both traces are therefore the squared length of $A$ seen as a vector with $n^2$ coordinates.
The off-diagonal entries of $A^{\mathsf{T}} A$ are the dot products of different columns, here $14 = 1 \cdot 2 + 3 \cdot 4$, and the trace ignores them.
