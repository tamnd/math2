---
tag: ~4cdc9c2b
kind: example
name: A block anti-diagonal matrix is not block diagonal
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
not_instance_of:
  - target: 001T5FJDC1
    note: the 4 × 4 matrix (0, I; I, 0) has its nonzero blocks off the diagonal, and no partition into two or more consecutive blocks makes it block diagonal
uses: [0M0SNKZ482, ~439d27b5]
sources:
  - url: https://en.wikipedia.org/wiki/Block_matrix
    locator: Block diagonal matrices
---

## Example

Let $I = I_2$ and
$$J = \begin{pmatrix} 0 & I \\ I & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix}.$$

1. For the partition $2 + 2$, the off-diagonal blocks are $I \neq 0$, so $J$ is not [[block diagonal|0M0SNKZ482]] for this partition.
2. Try another partition into consecutive blocks. A nonzero entry $j_{ac}$ of a block diagonal matrix needs $a$ and $c$ in the same block. So $j_{13} = 1$ puts $1$ and $3$, and hence also $2$, in the first block.
3. The entry $j_{24} = 1$ then puts $4$ in the same block. So the only possible partition is the trivial one with one block.
4. By the [[block rule|~439d27b5]], $J^2 = \begin{pmatrix} 0 \cdot 0 + I \cdot I & 0 \cdot I + I \cdot 0 \\ I \cdot 0 + 0 \cdot I & I \cdot I + 0 \cdot 0 \end{pmatrix} = I_4$, which is block diagonal.

## Remarks

$J$ exchanges the span of $e_1, e_2$ with the span of $e_3, e_4$, so these two planes are not invariant.
Every square matrix is block diagonal for the trivial partition with one block, so the notion is useful only for partitions with two or more blocks.

## Explanations

### L1 human

Here the nonzero blocks are in the corners off the diagonal.
A block diagonal matrix needs zero blocks there.

### L2 human

The matrix swaps two groups of coordinates, so it mixes the groups.
A block diagonal matrix never mixes its groups.
