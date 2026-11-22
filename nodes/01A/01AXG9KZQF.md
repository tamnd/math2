---
tag: 01AXG9KZQF
kind: definition
name: Block matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
defines: 0ASDFEQS6P
uses: [0N1MY1T0W9]
sources:
  - url: https://en.wikipedia.org/wiki/Block_matrix
    locator: Formal definition
inventory: [95VN171XXT]
---

## Definition

A block matrix is a matrix together with a cut of its rows and a cut of its columns into consecutive groups, so that it is assembled from smaller matrices.
Let $R$ be a ring.
Let $m = m_1 + \dots + m_p$ and $n = n_1 + \dots + n_q$ with positive integers $m_i$ and $n_j$.
For each $i \le p$ and $j \le q$, let $A_{ij}$ be an $m_i \times n_j$ [[matrix|0N1MY1T0W9]] over $R$.
The *block matrix* with blocks $A_{ij}$ is the $m \times n$ matrix
$$A = \begin{pmatrix} A_{11} & \cdots & A_{1q} \\ \vdots & \ddots & \vdots \\ A_{p1} & \cdots & A_{pq} \end{pmatrix}$$
in which $A_{ij}$ fills rows $m_1 + \dots + m_{i-1} + 1$ to $m_1 + \dots + m_i$ and columns $n_1 + \dots + n_{j-1} + 1$ to $n_1 + \dots + n_j$.
The pair of tuples $(m_1, \dots, m_p)$ and $(n_1, \dots, n_q)$ is the *partition* of $A$.

## Notation

The partition is often shown by lines, as in $\left(\begin{array}{c|c} A_{11} & A_{12} \\ \hline A_{21} & A_{22} \end{array}\right)$.
In Mathlib, `Matrix.fromBlocks A B C D` is the $2 \times 2$ block matrix, with rows and columns indexed by sum types.

## Remarks

The sizes are tied together on purpose.
All blocks in block row $i$ have the same height $m_i$, and all blocks in block column $j$ have the same width $n_j$.
This is what makes the cuts straight lines across the whole matrix, so that the blocks form a grid.

For example, with $m = 1 + 1$ and $n = 2 + 1$, the blocks $\begin{pmatrix} 1 & 2 \end{pmatrix}$, $(3)$, $\begin{pmatrix} 4 & 5 \end{pmatrix}$ and $(6)$ assemble into $\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$.
In contrast, blocks of widths $2$ and $1$ in the first block column fail the width condition, as [[the misaligned array|R19GEQWP7W]] shows.

Every $m \times n$ matrix is a block matrix for every choice of the two partitions, so the definition adds a choice, not a property.
The point of the grid is the [[block multiplication rule|WR3RCF5PSQ]]: when the column partition of $A$ equals the row partition of $B$, then $(AB)_{ik} = \sum_j A_{ij} B_{jk}$.
The concept page on [[block matrices|0ASDFEQS6P]] gives the other rules and their uses.

## Explanations

### L1 human

A block matrix is a large matrix cut into smaller rectangles by lines that run across the whole matrix.
A $4 \times 5$ matrix cut after row $2$ and after column $3$ has four blocks, of sizes $2 \times 3$, $2 \times 2$, $2 \times 3$ and $2 \times 2$.

### L2 human

The same matrix has many partitions, and a good one shows its structure, such as a block of zeros.
For $\begin{pmatrix} 1 & 2 & 0 \\ 3 & 4 & 0 \\ 0 & 0 & 5 \end{pmatrix}$, the cut $2 + 1$ for rows and columns shows two zero blocks off the diagonal, while the cut $1 + 2$ hides them.
