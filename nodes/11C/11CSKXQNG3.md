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

Row reduction tells us which columns of a matrix to keep, and those columns of the original matrix are a basis of its column space.
Let $F$ be a field and let $A$ be an $m \times n$ matrix over $F$.

1. The [[column space|03AJKXH1AV]] $\operatorname{Col}(A)$ is a [[subspace|00YC1D652K]] of $F^m$, and $\operatorname{Col}(A) = \{Ax : x \in F^n\}$.
2. The columns of $A$ in the [[pivot|0BCMGDHZGR]] positions of a row echelon form of $A$ form a [[basis|0KCQ9Y3QKA]] of $\operatorname{Col}(A)$.
3. The [[dimension|03GSZ8RTZJ]] of $\operatorname{Col}(A)$, which is the [[rank|0ZC9YTXZRY]] of $A$, equals the number of pivot positions.

## Remarks

### Why each hypothesis is needed

The basis consists of columns of $A$ itself.
The pivot columns of the reduced row echelon form are in general not in $\operatorname{Col}(A)$: for $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, the reduced form has the pivot column $(1, 0)$, while the column space is the line through $(1, 2)$, as the [[trap example|K21W7FA8MQ]] works out.

The entries must lie in a field, because the proof divides by the pivots.
Over $\mathbb{Z}$, the $1 \times 2$ matrix $\begin{pmatrix} 2 & 3 \end{pmatrix}$ is in echelon form with its pivot in column 1.
Its column space is $2\mathbb{Z} + 3\mathbb{Z} = \mathbb{Z}$, since $1 = 3 - 2$, but the pivot column alone spans only $2\mathbb{Z}$.

### What it gives you

There is at most one pivot in each row and in each column, so $\operatorname{rank} A \le \min(m, n)$.
The system $Ax = b$ is consistent for every $b \in F^m$ exactly when $A$ has a pivot in every row, that is, when $\operatorname{rank} A = m$.
The columns of $A$ are linearly independent exactly when every column is a pivot column, that is, when $\operatorname{rank} A = n$.

For a worked use, take the [[3 by 4 matrix with columns (1, 2, 3), (2, 4, 6), (0, 1, 1), (1, 4, 5)|AGHYPF25CY]].
Its echelon form has pivots in columns 1 and 3, so the rank is $2$, and the basis is $(1, 2, 3), (0, 1, 1)$.
Since $2 < 3$, some right sides $b \in \mathbb{R}^3$ give no solution, and since $2 < 4$, the four columns are dependent.

### The converse

A basis of $\operatorname{Col}(A)$ chosen among the columns need not be the set of pivot columns.
For $A = \begin{pmatrix} 1 & 1 \end{pmatrix}$, the second column alone is a basis, but only the first column is a pivot column.
The pivot columns are the basis that a scan from left to right finds: a column is kept when it is not a combination of the columns before it.

### Generalizations

For a linear map $T \colon V \to W$ with matrix $A$ in some bases, the coordinate map of $W$ carries the image of $T$ onto $\operatorname{Col}(A)$.
So the same computation gives a basis of $\operatorname{im} T$: the images of the basis vectors of $V$ at the pivot positions.

## Explanations

### L1 human

Row reduce the matrix and note which columns get a pivot.
The same columns of the original matrix are a basis of the column space.
Their number is the rank.
For $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ only column 1 gets a pivot, so $(1, 2)$ is a basis, and the rank is $1$.

### L2 human

Why does it work?
Row operations do not change the linear relations among the columns, because they do not change the solutions of $Ax = 0$.
In the reduced form the pivot columns are distinct unit vectors, and every other column is a combination of the pivot columns to its left.
These relations hold for the columns of $A$ as well, so the pivot columns of $A$ are independent and span all the columns.
The [[proof|F7HCY6S61E]] writes this out step by step.
Watch out: an echelon form that is not reduced gives the same pivot positions, so either form works for finding them.

### L3 human

The theorem says that the rank of a matrix can be read from any row echelon form.
In the language of maps, the invertible matrix $E$ with $EA = R$ is an isomorphism of $F^m$ that carries $\operatorname{Col}(A)$ onto $\operatorname{Col}(R)$, so it keeps the dimension but moves the subspace.
Together with the [[basis of the null space|5NKND0CPKP]], which counts the free columns, the theorem gives the [[rank-nullity theorem for matrices|TR48YQGCCA]].
