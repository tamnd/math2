---
tag: R19GEQWP7W
kind: example
name: An array of blocks whose widths do not line up is not a block matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
not_instance_of:
  - target: 0ASDFEQS6P
    note: the blocks in one block column must have the same width, and here the first block column has widths 2 and 1
uses: [01AXG9KZQF]
sources:
  - url: https://en.wikipedia.org/wiki/Block_matrix
    locator: Formal definition
---

## Example

A pile of small matrices that fits together into a rectangle is not yet a block matrix: the cuts must form a grid.
Take the $1 \times 2$ matrices $P = \begin{pmatrix} 1 & 2 \end{pmatrix}$ and $U = \begin{pmatrix} 5 & 6 \end{pmatrix}$, and the $1 \times 1$ matrices $Q = (3)$ and $S = (4)$.
Try to form the array $\begin{pmatrix} P & Q \\ S & U \end{pmatrix}$.

1. Writing the entries in place gives the rows $(1, 2, 3)$ and $(4, 5, 6)$, so a $2 \times 3$ array of numbers does appear.
2. In the first row the vertical cut lies after column $2$, between $P$ and $Q$.
3. In the second row the vertical cut lies after column $1$, between $S$ and $U$.
4. A [[block matrix|01AXG9KZQF]] needs one column partition $n = n_1 + n_2$ that holds in every row, so the blocks of one block column must have equal widths.
5. Here the first block column holds $P$ of width $2$ and $S$ of width $1$, so the condition fails, and the array is not a block matrix.

## Remarks

The $2 \times 3$ matrix of step 1 is a block matrix for other partitions, for example rows $1 + 1$ and columns $2 + 1$.
For that partition its blocks are $P$, $Q$, $\begin{pmatrix} 4 & 5 \end{pmatrix}$ and $(6)$, not the four pieces above.

The condition matters for the rules.
The [[block multiplication rule|WR3RCF5PSQ]] multiplies a block row of $A$ against a block column of $B$, and that only works when every block in a block column has the same width.
If we take $S = \begin{pmatrix} 4 & 5 \end{pmatrix}$ and $U = (6)$ instead, both block columns have constant widths $2$ and $1$, the cut is straight, and we get a block matrix.

## Explanations

### L1 human

The lines that cut a block matrix must go all the way across it.
Here the vertical line would have to jump one column to the left between the first and the second row.
So the pieces make a rectangle, but they do not make a grid.

### L2 human

To test whether pieces form a block matrix, list the widths in each block column and the heights in each block row.
Each list must be constant.
Here the widths in the first block column are $2$ and $1$, so the test fails at that column.
