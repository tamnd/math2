---
tag: 0DE5R5EB4D
kind: definition
name: Elementary row operations
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
defines: 04XWH28452
uses: [0N1MY1T0W9]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_matrix
    locator: Elementary row operations
  - book: isbn:9780321982384
    locator: Section 1.1
inventory: [ZK63DTX3QY]
---

## Definition

Let $F$ be a [[field|04C5ZBG1WT]] and let $A$ be an $m \times n$ [[matrix|0VD9ZSWWJG]] over $F$, with rows $R_1, \dots, R_m$.
An *elementary row operation* on $A$ is one of these three operations:

1. Row switching: exchange $R_i$ and $R_j$ for some $i \ne j$.
2. Row scaling: replace $R_i$ by $c R_i$ for some $c \in F$ with $c \ne 0$.
3. Row addition: replace $R_i$ by $R_i + c R_j$ for some $i \ne j$ and some $c \in F$.

## Remarks

Each elementary row operation has an inverse operation of the same type, see [[the theorem|~6410ee51]].
Each elementary row operation on $A$ is the same as the product $EA$ for an [[elementary matrix|01REXW3WWE]] $E$.
Elementary row operations on an [[augmented matrix|0T6MWGZSXA]] do not change the solution set of the system.
Elementary column operations have the same definition with columns in place of rows.

## Explanations

### L1 human

The three row operations are the moves that we make when we solve equations by hand.
We can swap two equations, multiply an equation by a nonzero number, or add a multiple of one equation to another.
None of these moves gains or loses a solution, and each move can be undone.

### L2 human

On the rows $(1, 2)$ and $(3, 4)$, the row addition $R_2 \leftarrow R_2 - 3R_1$ gives the rows $(1, 2)$ and $(0, -2)$.

1. Only $R_2$ changes.
2. The new $R_2$ is $(3 - 3, 4 - 6) = (0, -2)$.
3. The step $R_2 \leftarrow R_2 + 3R_1$ gives back $(3, 4)$.

A trap: in row addition the multiplied row $R_j$ must be a different row from $R_i$.
