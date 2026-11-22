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

A block matrix is a [[matrix|0VD9ZSWWJG]] cut into smaller matrices, its blocks, by lines that run all the way across it.
Once the cuts are made, you can add, transpose and multiply the matrix by treating each block as if it were a single entry.
Formally, fix $m = m_1 + \dots + m_p$ and $n = n_1 + \dots + n_q$; an $m \times n$ matrix is then written
$$A = \begin{pmatrix} A_{11} & \cdots & A_{1q} \\ \vdots & & \vdots \\ A_{p1} & \cdots & A_{pq} \end{pmatrix}, \qquad A_{ij} \text{ of size } m_i \times n_j.$$
The [[formal definition|01AXG9KZQF]] says which rows and columns each block fills.
When the column cuts of $A$ match the row cuts of $B$, the [[product|032Q9FB8MT]] is $(AB)_{ik} = \sum_j A_{ij} B_{jk}$, the [[block multiplication rule|WR3RCF5PSQ]].

## Motivation

Many matrices have pieces with different jobs, and the blocks make those pieces visible.
The [[augmented matrix|0T6MWGZSXA]] $[A \mid b]$ of a system is already a matrix in two blocks, the coefficients and the right side.
When a space splits as a direct sum $V = V_1 \oplus V_2$, a linear map of $V$ has a $2 \times 2$ block matrix, with one block for each pair of summands.
A zero block then says that one summand is not sent into the other.

Block notation also shortens proofs.
The inverse of a block triangular matrix, the [[determinant of a block triangular matrix|0J9TVTNB4K]] and the [[Schur complement|CA1J41NWGS]] all come out of one or two block products.
In computing, large products are done block by block so that each block fits in fast memory, and the block rule guarantees that the answer is the same.
The next page, on [[block diagonal matrices|001T5FJDC1]], treats the case where only the diagonal blocks are nonzero.

## Notation

A $2 \times 2$ block matrix is written $\begin{pmatrix} A & B \\ C & D \end{pmatrix}$, sometimes with lines between the blocks, as in $\left(\begin{array}{c|c} A & B \\ \hline C & D \end{array}\right)$.
The letters here name blocks, not entries, so $B$ inside the matrix is a matrix of its own.
In Mathlib, `Matrix.fromBlocks A B C D` is this matrix.
Its rows are indexed by the sum type `m ⊕ n`, not by `Fin (m + n)`, so a Mathlib block matrix and a book matrix of size $m + n$ differ by a reindexing.

## Remarks

### Cutting a matrix into blocks

Take the $2 \times 3$ matrix with rows $(1, 2, 3)$ and $(4, 5, 6)$, and cut its rows as $1 + 1$ and its columns as $2 + 1$:
$$M = \left(\begin{array}{cc|c} 1 & 2 & 3 \\ \hline 4 & 5 & 6 \end{array}\right) = \begin{pmatrix} P & Q \\ S & T \end{pmatrix}.$$
The blocks are $P = \begin{pmatrix} 1 & 2 \end{pmatrix}$, $Q = (3)$, $S = \begin{pmatrix} 4 & 5 \end{pmatrix}$ and $T = (6)$.
The same matrix has other cuts, for example columns $1 + 2$, so "block matrix" means a matrix together with a choice of cuts.
Two extreme cuts are useful: one block per column gives $A = (a_1 \mid \dots \mid a_n)$, the columns of $A$, and one block per entry gives back the ordinary matrix.

### What it is not

The cuts must go all the way across.
[[Pieces whose widths do not line up|R19GEQWP7W]], such as a top row cut after column $2$ and a bottom row cut after column $1$, do not form a block matrix.
In the same way, $A$ times $B$ cannot be done blockwise when $A$ has columns cut as $2 + 1$ and $B$ has rows cut as $1 + 2$, since then $A_{11}$ has $2$ columns and $B_{11}$ has $1$ row.

### Multiplying by blocks

The block rule is the ordinary row-times-column rule with blocks in place of numbers.
For two $3 \times 3$ matrices cut as $2 + 1$, [[the worked product|7C93RPT1MB]] computes each of the four blocks of $AB$ and checks the result entry by entry.
The order of each product must be kept, because blocks are matrices and $A_{ij} B_{jk}$ need not equal $B_{jk} A_{ij}$.
With block triangular matrices the zero blocks save work, and a block multiplication checks
$$\begin{pmatrix} A & B \\ 0 & D \end{pmatrix} \begin{pmatrix} A^{-1} & -A^{-1} B D^{-1} \\ 0 & D^{-1} \end{pmatrix} = \begin{pmatrix} I & -B D^{-1} + B D^{-1} \\ 0 & I \end{pmatrix} = I$$
when $A$ and $D$ are [[invertible|0EB9N0S33C]].

### The other rules

Sums and scalar multiples of block matrices with the same cuts are computed block by block, since each entry of a block is an entry of the matrix.
The transpose moves the blocks and transposes each one:
$$\begin{pmatrix} A & B \\ C & D \end{pmatrix}^{\mathsf{T}} = \begin{pmatrix} A^{\mathsf{T}} & C^{\mathsf{T}} \\ B^{\mathsf{T}} & D^{\mathsf{T}} \end{pmatrix}.$$
[[The transpose example|M35EF59DQB]] checks this rule with numbers.
Products of block upper triangular matrices with the same cuts are again block upper triangular, by the block rule.

### Watch out

Do not copy the $2 \times 2$ determinant formula to blocks.
Take $2 \times 2$ blocks $A = D = 0$ and $B = C = I$.
The formula $\det A \det D - \det B \det C$ gives $0 - 1 = -1$.
But the $4 \times 4$ matrix exchanges coordinates $1, 3$ and $2, 4$, two swaps, so its determinant is $+1$.
For block triangular matrices the correct rule is $\det = \det A \det D$.
A second slip is to transpose each block but leave the blocks in place; that gives the wrong matrix, and often not even a matrix.

### Try it

First, cut $\begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & 3 \end{pmatrix}$ as $(I \mid v)$ and compute its product with the column $\begin{pmatrix} x \\ 1 \end{pmatrix}$, where $x \in \mathbb{R}^2$.
The block rule gives $I x + v \cdot 1 = x + v = (x_1 + 2, x_2 + 3)^{\mathsf{T}}$.

Second, compute $\begin{pmatrix} I & B \\ 0 & I \end{pmatrix}^2$ for any square blocks.
The block rule gives $\begin{pmatrix} I & 2B \\ 0 & I \end{pmatrix}$.

## Explanations

### L1 human

A block matrix is a large table cut into smaller rectangles by straight lines that cross the whole table.
You can then treat each rectangle as one "number" and use the usual rules for adding and multiplying.
For example, a $4 \times 4$ table cut in half both ways is a $2 \times 2$ table whose entries are $2 \times 2$ tables.
The only rules are that the sizes must fit and that the order of each product stays as it is.

### L2 human

Here is a typical use: find the inverse of $M = \begin{pmatrix} 1 & 2 & 5 \\ 0 & 1 & 6 \\ 0 & 0 & 2 \end{pmatrix}$, cut as $2 + 1$.
The blocks are $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$, $B = \begin{pmatrix} 5 \\ 6 \end{pmatrix}$ and $D = (2)$, with a zero block below $A$.
First, $A^{-1} = \begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix}$ and $D^{-1} = (\tfrac12)$.
The block formula then needs only
$$-A^{-1} B D^{-1} = -\begin{pmatrix} 5 - 12 \\ 6 \end{pmatrix} \cdot \tfrac12 = \begin{pmatrix} 7/2 \\ -3 \end{pmatrix}.$$
So $M^{-1}$ has rows $(1, -2, 7/2)$, $(0, 1, -3)$ and $(0, 0, 1/2)$.
Check: row $1$ of $M$ times column $3$ of $M^{-1}$ is $7/2 - 6 + 5/2 = 0$.
The work splits into a $2 \times 2$ inverse and a $1 \times 1$ inverse, which is the point of block methods.

### L3 human

A block matrix is the matrix of a map between direct sums, $\bigoplus_j V_j \to \bigoplus_i W_i$, with the block $A_{ij}$ the component from $V_j$ to $W_i$.
The block rule is then the composition rule $(g \circ f)_{ik} = \sum_j g_{ij} \circ f_{jk}$, and in this form it holds for modules over any ring and in any additive category.
Block decompositions return in the study of [[direct sums of subspaces|041JTZCK9Q]], where a block triangular form means an invariant subspace and a block diagonal form means a pair of invariant complements.
They also organize the LU and Schur complement methods of the next sub-area, and the canonical forms built from blocks later in the area.
