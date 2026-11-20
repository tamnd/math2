---
tag: ~c7e81fac
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

Cut $M = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$ with rows $1 + 1$ and columns $2 + 1$.
So $M = \begin{pmatrix} P & Q \\ S & T \end{pmatrix}$ with $P = \begin{pmatrix} 1 & 2 \end{pmatrix}$, $Q = (3)$, $S = \begin{pmatrix} 4 & 5 \end{pmatrix}$ and $T = (6)$.

1. The rule is $M^{\mathsf{T}} = \begin{pmatrix} P^{\mathsf{T}} & S^{\mathsf{T}} \\ Q^{\mathsf{T}} & T^{\mathsf{T}} \end{pmatrix}$, with rows $2 + 1$ and columns $1 + 1$.
2. Here $P^{\mathsf{T}} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$, $S^{\mathsf{T}} = \begin{pmatrix} 4 \\ 5 \end{pmatrix}$, $Q^{\mathsf{T}} = (3)$ and $T^{\mathsf{T}} = (6)$.
3. So the rule gives $\begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}$.
4. The [[transpose|0W809K6AW0]] computed entry by entry is also $\begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}$.
5. Transposing the blocks without moving them gives $\begin{pmatrix} P^{\mathsf{T}} & Q^{\mathsf{T}} \\ S^{\mathsf{T}} & T^{\mathsf{T}} \end{pmatrix}$. There $P^{\mathsf{T}}$ has $2$ rows and $Q^{\mathsf{T}}$ has $1$, so this array is not even a block matrix.

## Remarks

The rule has two parts: the off-diagonal blocks change places, and every block is transposed.
The partition of $M^{\mathsf{T}}$ is the partition of $M$ with rows and columns exchanged.

## Explanations

### L1 human

To transpose a block matrix, transpose the grid of blocks and then transpose each block.
Doing only one of the two gives the wrong answer.

### L2 human

The entry $(a, c)$ of $M$ in block $(i, j)$ goes to $(c, a)$, which lies in block $(j, i)$.
Inside the block its position is also exchanged, so the block is transposed.
