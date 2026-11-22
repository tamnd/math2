---
tag: 0F0RPPJ2TT
kind: definition
name: Column space
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
defines: 03AJKXH1AV
uses: [0HR573CHNM, 0N1MY1T0W9]
sources:
  - url: https://en.wikipedia.org/wiki/Row_and_column_spaces
    locator: lead section
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section3-5.xml#L622
    locator: src/section3-5.xml:622
inventory: [6C8HH5VHGP]
---

## Definition

The column space of a matrix is the subspace spanned by its columns.
Let $F$ be a field and let $A$ be an $m \times n$ [[matrix|0N1MY1T0W9]] over $F$ with columns $a_1, \dots, a_n \in F^m$.
The *column space* of $A$ is the [[linear span|0HR573CHNM]] of the columns,
$$\operatorname{Col}(A) = \operatorname{span}(a_1, \dots, a_n) = \{x_1 a_1 + \dots + x_n a_n : x_1, \dots, x_n \in F\} \subseteq F^m.$$

## Remarks

The definition has two parts, the field and the columns, and each one matters.
The field $F$ supplies the coefficients $x_j$, so the column space of a real matrix is a real subspace, and its vectors may have entries that are not entries of $A$.
The columns are vectors of $F^m$, with one entry for each row, so the column space sits in $F^m$ and not in the space $F^n$ of the unknowns.

Since $Ax = x_1 a_1 + \dots + x_n a_n$, the column space is also $\{Ax : x \in F^n\}$, the image of the map $x \mapsto Ax$.
So the system $Ax = b$ is [[consistent|0X6V9B1V10]] exactly when $b \in \operatorname{Col}(A)$.
For example, $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ has column space $\{(t, 2t) : t \in F\}$, so $(3, 6)$ lies in it and $(1, 0)$ does not.
The [[concept page|03AJKXH1AV]] finds bases of column spaces, and the [[pivot basis theorem|11CSKXQNG3]] shows that the pivot columns of $A$ form one, so the dimension is the [[rank|0ZC9YTXZRY]] of $A$.

## Explanations

### L1 human

The column space collects all the mixtures of the columns of a matrix.
These mixtures are exactly the right sides $b$ for which $Ax = b$ has a solution.
For the matrix $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, every mixture is a multiple of $(1, 2)$, so the column space is the line through $(1, 2)$.
