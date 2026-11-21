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

An elementary row operation changes one row of a matrix in one of three simple ways.
Let $F$ be a [[field|04C5ZBG1WT]] and let $A$ be an $m \times n$ [[matrix|0VD9ZSWWJG]] over $F$, with rows $R_1, \dots, R_m$.
An *elementary row operation* on $A$ is one of these three operations:

1. Row switching: exchange $R_i$ and $R_j$ for some $i \ne j$.
2. Row scaling: replace $R_i$ by $c R_i$ for some $c \in F$ with $c \ne 0$.
3. Row addition: replace $R_i$ by $R_i + c R_j$ for some $i \ne j$ and some $c \in F$.

All other rows stay as they are.

## Notation

We write $R_i \leftrightarrow R_j$ for a switch, $R_i \leftarrow cR_i$ for a scaling and $R_i \leftarrow R_i + cR_j$ for a row addition.

## Remarks

### Why the two conditions

The condition $c \ne 0$ in row scaling makes the step reversible: scaling by $c^{-1}$ undoes it, and $c^{-1}$ exists because $F$ is a field.
Scaling by $0$ would turn a row into zeros, and nothing could bring it back.

The condition $i \ne j$ in row addition does the same job.
With $j = i$ and $c = -1$, the step $R_i \leftarrow R_i - R_i$ would also make a zero row.
With $i \ne j$, the row $R_j$ does not change, so $R_i \leftarrow R_i - cR_j$ undoes the step.

### What follows from the definition

Each elementary row operation has an inverse operation of the same type, by the [[theorem on row operations|K41GT10YM6]].
Each one is the same as the product $EA$ for an [[elementary matrix|01REXW3WWE]] $E$, namely the result of the operation on $I_m$.
Elementary row operations on an [[augmented matrix|0T6MWGZSXA]] do not change the solution set of the system.

### Column operations

Elementary column operations have the same definition with columns in place of rows.
They are right multiplications by elementary matrices.
They can change the solution set of a system, because they mix the unknowns, so elimination uses rows only.

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

Watch out: in row addition the multiplied row $R_j$ must be a different row from $R_i$.
