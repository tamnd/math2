---
tag: 0ASDFEQS6P
kind: concept
name: Block matrix
aliases: [partitioned-matrix]
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
specializes: [0VD9ZSWWJG]
uses: [0VD9ZSWWJG, 032Q9FB8MT]
sources:
  - url: https://en.wikipedia.org/wiki/Block_matrix
    locator: Formal definition
  - url: https://en.wikipedia.org/wiki/Block_matrix
    locator: Block matrix operations
  - book: isbn:9780321982384
    locator: Section 2.4
same_as:
  wikidata: Q884772
  wikipedia: Block matrix
inventory: [95VN171XXT]
---

## Summary

A block matrix, or partitioned matrix, is a [[matrix|0VD9ZSWWJG]] that is cut into smaller matrices, its blocks, by horizontal and vertical lines.
The [[formal definition|01AXG9KZQF]] fixes a partition of the rows and a partition of the columns.
When the column partition of $A$ matches the row partition of $B$, the [[product|032Q9FB8MT]] $AB$ is computed block by block, as if the blocks were entries.
This is the [[block multiplication rule|~439d27b5]].

## Motivation

Large matrices often have a structure that the blocks show.
A linear map $V_1 \oplus V_2 \to W_1 \oplus W_2$ has a $2 \times 2$ block matrix, one block for each pair of summands.
Block methods give short proofs, for example of the formula for the inverse of a block triangular matrix.
Computers use block multiplication to keep blocks in fast memory.

## Notation

- A $2 \times 2$ block matrix is written $\begin{pmatrix} A & B \\ C & D \end{pmatrix}$, sometimes with lines between the blocks.
- In Mathlib, `Matrix.fromBlocks A B C D` is this matrix. Its rows are indexed by the sum type `m ⊕ n`, not by `Fin (m + n)`.
- So a Mathlib block matrix and a matrix indexed by `Fin (m + n)` differ by a reindexing equivalence.

## Remarks

### Examples

- [[Multiplication of two 3 × 3 matrices in 2 + 1 blocks|~3f770ecf]].
- [[The transpose of a block matrix|~c7e81fac]].
- The augmented matrix $(A \mid b)$ of a linear system is a $1 \times 2$ block matrix.
- A matrix with columns $a_1, \dots, a_n$ is the $1 \times n$ block matrix $(a_1 \mid \cdots \mid a_n)$.

### Non-examples

- [[An array of blocks whose widths do not line up|~c2f2a0ce]] is not a block matrix.

### Basic properties

- Sums and scalar multiples of block matrices with the same partitions are computed blockwise.
- $\begin{pmatrix} A & B \\ C & D \end{pmatrix}^{\mathsf{T}} = \begin{pmatrix} A^{\mathsf{T}} & C^{\mathsf{T}} \\ B^{\mathsf{T}} & D^{\mathsf{T}} \end{pmatrix}$: the blocks move and each block is transposed.
- The block multiplication rule $(AB)_{ik} = \sum_j A_{ij} B_{jk}$ holds when the partitions match, by [[this theorem|~439d27b5]].
- The product of two block upper triangular matrices is block upper triangular.
- If $A$ and $D$ are [[invertible|0EB9N0S33C]], then $\begin{pmatrix} A & B \\ 0 & D \end{pmatrix}^{-1} = \begin{pmatrix} A^{-1} & -A^{-1} B D^{-1} \\ 0 & D^{-1} \end{pmatrix}$, as block multiplication checks.
- The [[determinant of a block triangular matrix|0J9TVTNB4K]] is the product of the determinants of the diagonal blocks.
- [[Block diagonal matrices|001T5FJDC1]] are the special case with zero blocks off the diagonal.

### Common errors

- Multiplying blocks in the wrong order. In $\sum_j A_{ij} B_{jk}$ the blocks need not commute.
- Taking $\det \begin{pmatrix} A & B \\ C & D \end{pmatrix} = \det A \det D - \det B \det C$. This is false in general, even when all blocks are square.
- Transposing each block but leaving the blocks in place.

## Explanations

### L1 human

A block matrix is a large matrix cut into smaller rectangles.
We can treat each rectangle like a single entry.
Then we add and multiply block matrices with the usual rules, as long as the sizes fit.

### L2 human

The product rule for blocks is the product rule for entries, with the sum over $j$ split into groups.
Each group of consecutive indices gives one block product $A_{ij} B_{jk}$.
The only condition is that the groups for the columns of $A$ are the same as the groups for the rows of $B$.

### L3 human

A block matrix is the matrix of a map between direct sums, with one block for each pair of summands.
The block rule is the composition rule for such maps, $(g \circ f)_{ik} = \sum_j g_{ij} \circ f_{jk}$.
In this form it holds in any additive category.
