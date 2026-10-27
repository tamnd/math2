---
tag: 0F0RPPJ2TT
kind: definition
name: Column space
msc: [15A03]
defines: 03AJKXH1AV
uses: [0HR573CHNM, 0N1MY1T0W9]
sources:
  - url: https://en.wikipedia.org/wiki/Row_and_column_spaces
    locator: lead section
inventory: [6C8HH5VHGP]
---

## Definition

Let $F$ be a field and let $A$ be an $m \times n$ matrix over $F$ with columns $a_1, \dots, a_n \in F^m$.
The *column space* of $A$ is
$$\operatorname{Col}(A) = \operatorname{span}(a_1, \dots, a_n) \subseteq F^m,$$
the [[linear span|0DTY8B9HMS]] of the columns.

## Remarks

The column space is $\{Ax : x \in F^n\}$, the image of the map $x \mapsto Ax$.
The system $Ax = b$ is [[consistent|0X6V9B1V10]] if and only if $b \in \operatorname{Col}(A)$.
The dimension of the column space is the [[rank|0ZC9YTXZRY]] of $A$.
The pivot columns of $A$ form a basis of $\operatorname{Col}(A)$.

## Explanations

### L1 human

The column space collects all the combinations of the columns of a matrix.
These are exactly the vectors $b$ for which $Ax = b$ has a solution.
For the matrix $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, the column space is the line spanned by $(1, 2)$.
