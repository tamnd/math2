---
tag: 11CSKXQNG3
kind: statement
role: proposition
name: Dimension and pivot basis of the column space
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
about: [03AJKXH1AV]
uses: [03AJKXH1AV, 0ZC9YTXZRY, 03GSZ8RTZJ, 0KCQ9Y3QKA, 00YC1D652K, 0BCMGDHZGR]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section3-5.xml#L860
    locator: src/section3-5.xml:860
  - url: https://en.wikipedia.org/wiki/Row_and_column_spaces
    locator: Basis
  - book: isbn:9780321982384
    locator: Section 4.3
---

## Statement

Let $F$ be a field and let $A$ be an $m \times n$ matrix over $F$.

1. The [[column space|03AJKXH1AV]] $\operatorname{Col}(A)$ is a [[subspace|00YC1D652K]] of $F^m$, and $\operatorname{Col}(A) = \{Ax : x \in F^n\}$.
2. The columns of $A$ that hold the [[pivot|0BCMGDHZGR]] positions of $A$ form a [[basis|0KCQ9Y3QKA]] of $\operatorname{Col}(A)$.
3. The [[dimension|03GSZ8RTZJ]] of $\operatorname{Col}(A)$, which is the [[rank|0ZC9YTXZRY]] of $A$, is the number of pivot positions of $A$.

## Remarks

### Why each hypothesis is needed

- The basis consists of columns of $A$ itself. The pivot columns of the reduced row echelon form are in general not in $\operatorname{Col}(A)$, as the [[trap example|K21W7FA8MQ]] shows.
- The entries must lie in a field. Over $\mathbb{Z}$, the $1 \times 2$ matrix $\begin{pmatrix} 2 & 3 \end{pmatrix}$ is in echelon form with its pivot in column 1.
  Its column space is $2\mathbb{Z} + 3\mathbb{Z} = \mathbb{Z}$, since $1 = 3 - 2$, but the pivot column spans only $2\mathbb{Z}$.

### Consequences

- The rank of $A$ is at most $\min(m, n)$, since there is at most one pivot in each row and in each column.
- The system $Ax = b$ is consistent for each $b \in F^m$ if and only if $A$ has a pivot in each row, that is, $\rank A = m$.
- The columns of $A$ are linearly independent if and only if every column is a pivot column, that is, $\rank A = n$.

### Converse

If a set of columns of $A$ is a basis of $\operatorname{Col}(A)$, it need not be the set of pivot columns.
For $A = \begin{pmatrix} 1 & 1 \end{pmatrix}$, the second column alone is a basis, but only the first column is a pivot column.
The pivot columns are the first basis that a scan from left to right finds.

### Generalizations

For a linear map $T \colon V \to W$ with matrix $A$ in some bases, the image of $T$ corresponds to $\operatorname{Col}(A)$ under the coordinate map of $W$.
So the same computation gives a basis of $\im T$.

## Explanations

### L1 human

Row reduce the matrix and note which columns get a pivot.
The same columns of the original matrix are a basis of the column space.
Their number is the rank.

### L2 human

Row operations do not change the linear relations among the columns.
In the reduced form, the pivot columns are distinct unit vectors, and every other column is a combination of the pivot columns to its left.
These relations hold for the columns of $A$ as well.
So the pivot columns of $A$ are independent, and they span all the columns.
