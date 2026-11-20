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

Let $R$ be a ring.
Let $m = m_1 + \cdots + m_p$ and $n = n_1 + \cdots + n_q$ with positive integers $m_i$ and $n_j$.
For each $i \le p$ and $j \le q$, let $A_{ij}$ be an $m_i \times n_j$ [[matrix|0N1MY1T0W9]] over $R$.
The *block matrix* with blocks $A_{ij}$ is the $m \times n$ matrix
$$A = \begin{pmatrix} A_{11} & \cdots & A_{1q} \\ \vdots & \ddots & \vdots \\ A_{p1} & \cdots & A_{pq} \end{pmatrix}.$$
In it, $A_{ij}$ fills rows $m_1 + \cdots + m_{i-1} + 1$ to $m_1 + \cdots + m_i$ and columns $n_1 + \cdots + n_{j-1} + 1$ to $n_1 + \cdots + n_j$.

## Notation

- The pair of partitions $(m_1, \dots, m_p)$ and $(n_1, \dots, n_q)$ is the *partition* of $A$.
- In Mathlib, `Matrix.fromBlocks A B C D` is the $2 \times 2$ block matrix, indexed by sum types.

## Remarks

- All blocks in one block row have the same height $m_i$, and all blocks in one block column have the same width $n_j$.
- Every $m \times n$ matrix is a block matrix for each choice of the two partitions.
- If the column partition of $A$ matches the row partition of $B$, then $(AB)_{ik} = \sum_j A_{ij} B_{jk}$; see the [[block multiplication rule|WR3RCF5PSQ]].

## Explanations

### L1 human

A block matrix is a large matrix cut into smaller rectangles by full horizontal and vertical lines.
Each line runs across the whole matrix.

### L2 human

Being a block matrix is not a property of the matrix but a choice of how to cut it.
The same matrix has many partitions, and a good partition shows its structure.
