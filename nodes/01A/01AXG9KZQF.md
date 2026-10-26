---
tag: 01AXG9KZQF
kind: definition
name: Block matrix
msc: [15A99]
defines: 0ASDFEQS6P
uses: [0N1MY1T0W9]
sources:
  - url: https://en.wikipedia.org/wiki/Block_matrix
    locator: Formal definition
---

## Definition

Let $R$ be a ring.
Let $m = m_1 + \cdots + m_p$ and $n = n_1 + \cdots + n_q$ with positive integers $m_i$ and $n_j$.
For each $i \le p$ and $j \le q$, let $A_{ij}$ be an $m_i \times n_j$ [[matrix|0VD9ZSWWJG]] over $R$.
The *block matrix* with blocks $A_{ij}$ is the $m \times n$ matrix
$$A = \begin{pmatrix} A_{11} & \cdots & A_{1q} \\ \vdots & \ddots & \vdots \\ A_{p1} & \cdots & A_{pq} \end{pmatrix},$$
in which $A_{ij}$ fills rows $m_1 + \cdots + m_{i-1} + 1$ to $m_1 + \cdots + m_i$ and columns $n_1 + \cdots + n_{j-1} + 1$ to $n_1 + \cdots + n_j$.

## Remarks

If the column partition of $A$ matches the row partition of $B$, then $AB$ is computed block by block: $(AB)_{ik} = \sum_j A_{ij} B_{jk}$.
In Mathlib, `Matrix.fromBlocks` makes the $2 \times 2$ block matrix $\begin{pmatrix} A & B \\ C & D \end{pmatrix}$.
The [[determinant of a block triangular matrix|0J9TVTNB4K]] is the product of the determinants of its diagonal blocks.

## Explanations

### L1 human

A block matrix is a large matrix cut into smaller rectangles.
We can treat each rectangle like a single entry.
Then we add and multiply block matrices with the usual rules, as long as the sizes fit.
