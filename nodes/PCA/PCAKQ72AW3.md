---
tag: PCAKQ72AW3
kind: example
name: A block anti-diagonal matrix is not block diagonal
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
not_instance_of:
  - target: 001T5FJDC1
    note: "the 4 × 4 matrix (0, I; I, 0) has its nonzero blocks off the diagonal, and no partition into two or more consecutive blocks makes it block diagonal"
uses: [0M0SNKZ482, WR3RCF5PSQ]
sources:
  - url: https://en.wikipedia.org/wiki/Block_matrix
    locator: Block diagonal matrices
---

## Example

A matrix with all its nonzero blocks off the diagonal mixes its groups of coordinates, so no cut makes it block diagonal.
Let $I = I_2$ and
$$J = \begin{pmatrix} 0 & I \\ I & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix}.$$

1. For the partition $2 + 2$, the off-diagonal blocks are $I \neq 0$, so $J$ is not [[block diagonal|0M0SNKZ482]] for this partition.
2. For any partition into consecutive groups, a nonzero entry $j_{ac}$ of a block diagonal matrix forces $a$ and $c$ into the same group.
3. The entry $j_{13} = 1$ puts $1$ and $3$ in one group, and since the groups are consecutive, $2$ is in that group too.
4. The entry $j_{24} = 1$ then puts $4$ in the same group, so the only partition that works is the trivial one with a single block.
5. By the [[block rule|WR3RCF5PSQ]],
$$J^2 = \begin{pmatrix} 0 \cdot 0 + I \cdot I & 0 \cdot I + I \cdot 0 \\ I \cdot 0 + 0 \cdot I & I \cdot I + 0 \cdot 0 \end{pmatrix} = I_4,$$
which is block diagonal, so a power of a matrix can be block diagonal when the matrix is not.

## Remarks

### What goes wrong

$J$ sends $e_1, e_2$ to $e_3, e_4$ and back, so it exchanges the span of $e_1, e_2$ with the span of $e_3, e_4$.
Neither plane is invariant, and that is exactly what the nonzero off-diagonal blocks record.
Every square matrix is block diagonal for the trivial partition with one block, so the notion is useful only for partitions with two or more blocks.

### Watch out

Not being block diagonal in the standard basis does not mean that no splitting exists.
The vectors $e_1 + e_3$, $e_2 + e_4$, $e_1 - e_3$ and $e_2 - e_4$ satisfy $J v = v$ for the first two and $J v = -v$ for the last two.
In this basis $J$ becomes $\operatorname{diag}(1, 1, -1, -1)$, which is even diagonal.

## Explanations

### L1 human

Here the nonzero blocks are in the corners off the diagonal.
A block diagonal matrix needs zero blocks there.
So $J$ is a swap of two groups of coordinates, not a pair of separate moves on each group.

### L2 human

The test of steps 2 to 4 is mechanical.
Draw an edge between $a$ and $c$ whenever $j_{ac} \neq 0$, and the groups of any block diagonal form must contain whole connected pieces of this picture, filled in to be consecutive.
For $J$ the edges $\{1, 3\}$ and $\{2, 4\}$ together with consecutiveness force one group.
A change of basis, as in the Watch out remark, can still split the matrix, because block diagonal form is a property of the matrix in a given basis.
