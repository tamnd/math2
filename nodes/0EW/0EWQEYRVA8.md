---
tag: 0EWQEYRVA8
kind: definition
name: Rank of a matrix
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
defines: 0ZC9YTXZRY
uses: [0F0RPPJ2TT, 05G2G0P224]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.rank
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: lead section
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section3-5.xml#L848
    locator: src/section3-5.xml:848
inventory: [5AH385RGHD]
---

## Definition

The rank of a matrix is the dimension of the space spanned by its columns.
Let $F$ be a field and let $A$ be an $m \times n$ matrix over $F$.
The *rank* of $A$ is
$$\rank A = \dim \operatorname{Col}(A),$$
where $\operatorname{Col}(A) \subseteq F^m$ is the [[column space|03AJKXH1AV]] of $A$ and $\dim$ is the [[dimension|03GSZ8RTZJ]] over $F$.

## Notation

The rank is written $\rank A$ or $\operatorname{rk} A$, and $\rank_F A$ when the field must be named.
In Mathlib it is `Matrix.rank A`, the dimension of the range of `Matrix.mulVecLin A`.

## Remarks

The definition has two ingredients, and each one matters.
The column space is a subspace of $F^m$, so it has a dimension, and that dimension is the largest number of linearly independent columns of $A$.
The field $F$ is part of the data, because the same integer matrix can have different ranks over $\mathbb{Q}$ and over $\mathbb{F}_p$.
For example, $\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ has determinant $-2$, so it has rank $2$ over $\mathbb{Q}$, but over $\mathbb{F}_2$ its two columns are both $(1, 1)$ and its rank is $1$.

A definition by rows would give the same number, by the theorem that [[row rank equals column rank|0TZAG60ZYT]].
The rank is also the number of pivots of an echelon form, by the [[theorem on the column space|11CSKXQNG3]], and the largest size of a nonzero minor.
A small case: the matrix $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ has the column space spanned by $(1, 2)$, so its rank is $1$, while a count of its nonzero rows would wrongly give $2$.
The [[concept page|0ZC9YTXZRY]] works more examples.

## Explanations

### L1 human

The rank counts how many columns of a matrix point in really new directions.
In $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, the second column is twice the first, so there is only one direction, and the rank is $1$.

### L2 human

The rank is the dimension of the image of the map $x \mapsto Ax$ from $F^n$ to $F^m$, since that image is the column space.
So it is at most $m$, because the image lies in $F^m$, and at most $n$, because the image is spanned by $n$ columns.
To compute it, row reduce and count the pivots; do not count the nonzero rows of $A$ before you reduce.
