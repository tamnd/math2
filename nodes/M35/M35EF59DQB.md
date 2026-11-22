---
tag: M35EF59DQB
kind: example
name: The transpose of a block matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [0ASDFEQS6P]
uses: [01AXG9KZQF, 0W809K6AW0]
sources:
  - url: https://en.wikipedia.org/wiki/Block_matrix
    locator: Block matrix operations
---

## Example

To transpose a block matrix, you move the blocks and you transpose each block.
Cut
$$M = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$$
with rows $1 + 1$ and columns $2 + 1$, so $M = \begin{pmatrix} P & Q \\ S & T \end{pmatrix}$ with $P = \begin{pmatrix} 1 & 2 \end{pmatrix}$, $Q = (3)$, $S = \begin{pmatrix} 4 & 5 \end{pmatrix}$ and $T = (6)$.

1. The block rule for the [[transpose|0W809K6AW0]] is
$$M^{\mathsf{T}} = \begin{pmatrix} P^{\mathsf{T}} & S^{\mathsf{T}} \\ Q^{\mathsf{T}} & T^{\mathsf{T}} \end{pmatrix},$$
with rows cut as $2 + 1$ and columns cut as $1 + 1$.
2. Transpose each block: $P^{\mathsf{T}} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$, $S^{\mathsf{T}} = \begin{pmatrix} 4 \\ 5 \end{pmatrix}$, $Q^{\mathsf{T}} = (3)$ and $T^{\mathsf{T}} = (6)$.
3. Put them in place:
$$M^{\mathsf{T}} = \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}.$$
4. Check: the transpose computed entry by entry has rows $(1, 4)$, $(2, 5)$ and $(3, 6)$, the same matrix.
5. The wrong move is to transpose the blocks without moving them, $\begin{pmatrix} P^{\mathsf{T}} & Q^{\mathsf{T}} \\ S^{\mathsf{T}} & T^{\mathsf{T}} \end{pmatrix}$. There $P^{\mathsf{T}}$ has $2$ rows and $Q^{\mathsf{T}}$ has $1$ row, so the first block row does not even fit together.

## Remarks

The rule has two parts: the blocks $Q$ and $S$ off the diagonal change places, and every block is transposed.
The partition of $M^{\mathsf{T}}$ is the partition of $M$ with the roles of rows and columns exchanged.

For square blocks the wrong move can produce a matrix, but the wrong one.
With $Q = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $P = S = T = 0$, the correct transpose has $Q^{\mathsf{T}}$ in the lower left corner, while the wrong move leaves a block in the upper right corner.
For a symmetric block matrix, $M^{\mathsf{T}} = M$ means $P^{\mathsf{T}} = P$, $T^{\mathsf{T}} = T$ and $S = Q^{\mathsf{T}}$.

## Explanations

### L1 human

Think of the block matrix as a small table of tiles.
To transpose it, first flip the table of tiles over its diagonal, then flip each tile.
Doing only one of the two flips gives the wrong answer.

### L2 human

The reason is a statement about positions.
An entry of $M$ that lies in block $(i, j)$ moves under the transpose to the mirror position, which lies in block $(j, i)$.
Inside the block its row and column are also exchanged, so the block arrives transposed.
