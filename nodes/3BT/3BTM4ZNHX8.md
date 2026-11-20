---
tag: 3BTM4ZNHX8
kind: example
name: Multiplying by a diagonal matrix scales the rows or the columns
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
instance_of: [044JNC7ZAA]
uses: [0Q9PGXD9E4, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonal_matrix
    locator: Matrix operations
---

## Example

Let $D = \operatorname{diag}(2, 3)$ and $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$.

1. By the [[product rule|076JGP6R3T]], $(DA)_{ij} = d_i a_{ij}$. So $DA = \begin{pmatrix} 2 \cdot 1 & 2 \cdot 2 \\ 3 \cdot 3 & 3 \cdot 4 \end{pmatrix} = \begin{pmatrix} 2 & 4 \\ 9 & 12 \end{pmatrix}$: row $i$ is multiplied by $d_i$.
2. Also $(AD)_{ij} = a_{ij} d_j$. So $AD = \begin{pmatrix} 1 \cdot 2 & 2 \cdot 3 \\ 3 \cdot 2 & 4 \cdot 3 \end{pmatrix} = \begin{pmatrix} 2 & 6 \\ 6 & 12 \end{pmatrix}$: column $j$ is multiplied by $d_j$.
3. So $DA \neq AD$, although $D$ is [[diagonal|0Q9PGXD9E4]].
4. With $D' = \operatorname{diag}(5, 7)$, the product $DD' = \operatorname{diag}(10, 21) = D'D$.

## Remarks

Scaling rows on the left and columns on the right is used to balance a matrix before a numerical computation.
In the sales example, a diagonal matrix of prices on the right turns units into money for each product.

## Explanations

### L1 human

A diagonal matrix on the left multiplies each row by a number.
A diagonal matrix on the right multiplies each column by a number.
The two results differ.

### L2 human

Two diagonal matrices commute, but a diagonal matrix and a general matrix usually do not.
They commute exactly when $a_{ij}(d_i - d_j) = 0$ for all $i, j$.
