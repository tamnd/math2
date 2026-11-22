---
tag: 7C93RPT1MB
kind: example
name: Multiplication of two 3 × 3 matrices in 2 + 1 blocks
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [0ASDFEQS6P]
illustrates: [WR3RCF5PSQ]
uses: [01AXG9KZQF, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Block_matrix
    locator: Block matrix operations
---

## Example

We multiply two $3 \times 3$ matrices by blocks and check the answer entry by entry.
Cut the rows and the columns of both matrices as $2 + 1$:
$$A = \left(\begin{array}{cc|c} 1 & 2 & 0 \\ 0 & 1 & 0 \\ \hline 3 & 0 & 2 \end{array}\right), \qquad B = \left(\begin{array}{cc|c} 1 & 0 & 1 \\ 1 & 1 & 0 \\ \hline 0 & 2 & 1 \end{array}\right).$$
The blocks of $A$ are $A_{11} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$, $A_{12} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$, $A_{21} = \begin{pmatrix} 3 & 0 \end{pmatrix}$ and $A_{22} = (2)$.
The blocks of $B$ are $B_{11} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$, $B_{12} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$, $B_{21} = \begin{pmatrix} 0 & 2 \end{pmatrix}$ and $B_{22} = (1)$.

1. The column cut $2 + 1$ of $A$ equals the row cut $2 + 1$ of $B$, so the [[block rule|WR3RCF5PSQ]] applies.
2. The top left block is a $2 \times 2$ product plus a zero product, because $A_{12} = 0$:
$$(AB)_{11} = A_{11} B_{11} + A_{12} B_{21} = \begin{pmatrix} 3 & 2 \\ 1 & 1 \end{pmatrix} + \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 3 & 2 \\ 1 & 1 \end{pmatrix}.$$
3. The top right block is a column:
$$(AB)_{12} = A_{11} B_{12} + A_{12} B_{22} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} + \begin{pmatrix} 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}.$$
4. The bottom left block is a row:
$$(AB)_{21} = A_{21} B_{11} + A_{22} B_{21} = \begin{pmatrix} 3 & 0 \end{pmatrix} + \begin{pmatrix} 0 & 4 \end{pmatrix} = \begin{pmatrix} 3 & 4 \end{pmatrix}.$$
5. The bottom right block is a number:
$$(AB)_{22} = A_{21} B_{12} + A_{22} B_{22} = (3) + (2) = (5).$$
6. Assemble the blocks:
$$AB = \begin{pmatrix} 3 & 2 & 1 \\ 1 & 1 & 0 \\ 3 & 4 & 5 \end{pmatrix}.$$
7. Check with the [[entry rule|076JGP6R3T]]: $(AB)_{32} = 3 \cdot 0 + 0 \cdot 1 + 2 \cdot 2 = 4$ and $(AB)_{13} = 1 \cdot 1 + 2 \cdot 0 + 0 \cdot 1 = 1$, as in step 6.

## Remarks

The zero block $A_{12}$ makes $A$ block lower triangular, and it removes one product from each of steps 2 and 3.
So $(AB)_{11} = A_{11} B_{11}$ depends only on the top left blocks of the two factors.

If we cut the rows of $B$ as $1 + 2$ instead, the rule fails at once.
Then $A_{11}$ has $2$ columns and $B_{11}$ has $1$ row, so $A_{11} B_{11}$ is not defined.
The cuts of the rows of $A$ and of the columns of $B$ are free, and they only decide the shape of the blocks of $AB$.

## Explanations

### L1 human

We multiply the $2 \times 2$ grid of blocks just like a $2 \times 2$ matrix of numbers.
Each "number" is a small matrix: a square, a column, a row or a single entry.
We must keep the order in each product, the block of $A$ on the left and the block of $B$ on the right.

### L2 human

The block products here have four shapes: $2 \times 2$ times $2 \times 2$, $2 \times 2$ times $2 \times 1$, $1 \times 2$ times $2 \times 2$, and $1 \times 2$ times $2 \times 1$.
In each one the inner sizes agree, because the cuts match.
The typical use is a matrix with a zero block, where whole block products drop out.
