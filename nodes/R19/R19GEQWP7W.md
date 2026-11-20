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

Take the $1 \times 2$ matrices $P = \begin{pmatrix} 1 & 2 \end{pmatrix}$ and $U = \begin{pmatrix} 5 & 6 \end{pmatrix}$, and the $1 \times 1$ matrices $Q = (3)$ and $S = (4)$.
Try to form $\begin{pmatrix} P & Q \\ S & U \end{pmatrix}$.

1. Writing the entries in place gives the rows $(1, 2, 3)$ and $(4, 5, 6)$, so a $2 \times 3$ array of numbers exists.
2. In the first row the vertical cut lies after column $2$, and in the second row it lies after column $1$.
3. A [[block matrix|01AXG9KZQF]] needs one cut for the columns that runs through all the rows.
4. So the blocks $P$ and $S$ in the first block column have different widths, $2$ and $1$, and the array of blocks is not a block matrix.

## Remarks

The $2 \times 3$ matrix of step 1 is a block matrix for other partitions, for example rows $1 + 1$ and columns $2 + 1$.
For that partition its blocks are $P$, $Q$, $\begin{pmatrix} 4 & 5 \end{pmatrix}$ and $(6)$, not the blocks above.
The block rules, such as [[block multiplication|WR3RCF5PSQ]], need full cuts.

## Explanations

### L1 human

The lines that cut a block matrix must go all the way across.
Here the vertical line would have to jump, so these pieces do not form a block matrix.

### L2 human

The condition says that the blocks form a grid.
A grid is needed so that a block row of $A$ can meet a block column of $B$ in matching sizes.
