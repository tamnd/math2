---
tag: 0ZC9YTXZRY
kind: concept
name: Rank of a matrix
aliases: [rank-of-a-matrix]
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
uses: [0VD9ZSWWJG, 03AJKXH1AV, 03GSZ8RTZJ]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: lead section
  - book: isbn:9780134860244
    locator: Section 3.2
  - book: isbn:9780321982384
    locator: Section 4.6
same_as:
  wikidata: Q656784
  wikipedia: Rank (linear algebra)
inventory: [5AH385RGHD]
---

## Summary

The rank of a matrix counts how many of its columns are really different, in the sense that none of them is built from the others.
It is the one number that tells you how much information a matrix carries, and it controls the solutions of every linear system with that matrix.
For an $m \times n$ [[matrix|0VD9ZSWWJG]] $A$ over a field $F$, the [[definition|0EWQEYRVA8]] is
$$\rank A = \dim \operatorname{Col}(A),$$
the [[dimension|03GSZ8RTZJ]] of the [[column space|03AJKXH1AV]] of $A$.
The same number is the number of pivots of an echelon form of $A$, the dimension of the [[row space|069MCGX635]], and the largest size of a nonzero minor of $A$.
It is also the [[rank of the linear map|0ZZXSBTR4J]] $x \mapsto Ax$ from $F^n$ to $F^m$.

## Motivation

A system $Ax = b$ of $m$ equations in $n$ unknowns can look bigger than it is.
If one equation is the sum of two others, it adds nothing, and if one column is twice another, two unknowns play the same role.
The rank removes this redundancy: it counts the equations that are independent and, at the same time, the columns that are independent.
Then the system has solutions for every $b$ exactly when $\rank A = m$, and the solutions of $Ax = 0$ form a space of dimension $n - \rank A$.

The rank appears far beyond linear systems.
In statistics and data science, a table of measurements of rank $r$ is described by $r$ hidden factors, and a low-rank approximation keeps the main pattern of the data.
In control theory, the rank of a matrix built from a system decides whether the system can be steered to every state.
Later in the sub-area, the rank returns in the [[four fundamental subspaces|73DVECPAT6]], in [[rank-nullity|TR48YQGCCA]], in the [[rank inequalities|02FDWY55AS]] and in the [[rank factorization|5JGAG62VN8]].

## Notation

Books write $\rank A$, $\operatorname{rk} A$, $\operatorname{rank}(A)$ or $r(A)$.
Some books first define the column rank and the row rank separately, and only call either of them "the rank" after proving that they agree.
When the field matters, write $\rank_F A$, for example $\rank_{\mathbb{F}_3} A$.
In Mathlib, `Matrix.rank A` is the dimension of the range of `Matrix.mulVecLin A`, which is the column space.

## Remarks

### A first computation

Take the matrix
$$A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}.$$
The second column $(2, 4)$ is twice the first column $(1, 2)$, so the column space is the line spanned by $(1, 2)$, and $\rank A = 1$.
Row reduction gives the same answer.
Subtract $2$ times row 1 from row 2:
$$\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} \to \begin{pmatrix} 1 & 2 \\ 0 & 0 \end{pmatrix}.$$
There is one pivot, so the rank is $1$.
Check: the determinant is $1 \cdot 4 - 2 \cdot 2 = 0$, so the only nonzero minors are the $1 \times 1$ entries, which again gives rank $1$.

### More examples

The identity matrix $I_n$ has rank $n$, and the zero matrix has rank $0$.
A diagonal matrix has rank equal to its number of nonzero diagonal entries, so $\operatorname{diag}(1, 0, 3)$ has rank $2$.
For nonzero vectors $u \in F^m$ and $v \in F^n$, the matrix $uv^{\mathsf{T}}$ has column $j$ equal to $v_j u$, so all its columns lie on the line of $u$, and its rank is $1$.

A [[3 by 4 matrix of rank 2|MDB2CHQDXJ]] shows four ways to find the same number: pivots, independent columns, independent rows and minors.
The [[matrix with entries 1 to 9|6X9G57XHMF]] has rank $2$ over $\mathbb{R}$, because its rows are in arithmetic progression.
Over the field $\mathbb{F}_3$ its rank drops to $1$, so the rank depends on the field in which we compute.

### What it is not

The number of nonzero rows of $A$ is not the rank unless $A$ is in echelon form.
The matrix above has two nonzero rows and rank $1$, and the [[page on counting rows and diagonal entries|KXG0P38NCE]] gives more cases.
The number of columns is not the rank either, as the [[example on counting columns|R7N2K2EVJP]] shows.
Both counts fail for the same reason: they see the size of the matrix, while the rank sees only the independent part.

### The rules you can use

Several facts follow from the definition and from the theorems of the sub-area.
The rank is at most $\min(m, n)$, because the column space lies in $F^m$ and is spanned by $n$ columns.
The rank of $A^{\mathsf{T}}$ equals the rank of $A$, which is the theorem that [[row rank equals column rank|0TZAG60ZYT]].
The rank plus the dimension of the [[null space|0PHDYNR24D]] is $n$, by [[rank-nullity for matrices|TR48YQGCCA]].
For a product, $\rank(AB) \le \min(\rank A, \rank B)$, by the [[rank of a product|02FDWY55AS]].
Multiplying by an [[invertible matrix|0EB9N0S33C]] on either side does not change the rank, since an invertible map carries a subspace onto a subspace of the same dimension.
The rank is the largest $k$ such that some $k \times k$ [[minor|0BT9BYWVRY]] of $A$ is nonzero, and the area on determinants studies this form.
So an $n \times n$ matrix is invertible exactly when its rank is $n$.

### Watch out

Two rules from ordinary numbers fail for the rank.
The rank is not additive: $\rank(A + B)$ can be smaller than $\rank A + \rank B$, as $A = I_2$ and $B = -I_2$ show, with $\rank(A + B) = 0$.
Only the inequality $\rank(A + B) \le \rank A + \rank B$ of [[subadditivity|5M6SX7JN01]] holds.
The rank of a product also depends on the order.
Take $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$:
$$AB = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}, \qquad BA = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}.$$
So $\rank(AB) = 0$ but $\rank(BA) = 1$.

### History

Frobenius used the notion of rank in his work on linear equations and bilinear forms in the nineteenth century.

### Try it

First, find the rank of $\begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 2 & 3 & 4 \end{pmatrix}$.
Row 3 is the sum of rows 1 and 2, and rows 1 and 2 are not proportional, so the rank is $2$.

Second, for which numbers $t$ does $\begin{pmatrix} 1 & t \\ t & 1 \end{pmatrix}$ have rank $1$?
The determinant $1 - t^2$ must be $0$, so $t = 1$ or $t = -1$, and the rank is never $0$ because the entry $1$ is nonzero.

## Explanations

### L1 human

Think of the columns of a matrix as arrows.
The rank counts how many of the arrows point in really new directions.
For the columns $(1, 2)$ and $(2, 4)$, the second arrow is the first one stretched to twice its length, so it adds no new direction and the rank is $1$.
For the columns $(1, 0)$ and $(0, 1)$, the two arrows point in different directions, so the rank is $2$.
Row reduction finds the rank for you: it is the number of pivots.

### L2 human

Here is a typical use: decide whether a system has a solution, and how many.
Take $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, of rank $1$, and first $b = (3, 6)$.
Reduce the augmented matrix:
$$\left(\begin{array}{cc|c} 1 & 2 & 3 \\ 2 & 4 & 6 \end{array}\right) \to \left(\begin{array}{cc|c} 1 & 2 & 3 \\ 0 & 0 & 0 \end{array}\right).$$
The augmented matrix also has rank $1$, so the system is consistent, and the solutions form a line, of dimension $2 - 1 = 1$.
Now take $b = (3, 5)$:
$$\left(\begin{array}{cc|c} 1 & 2 & 3 \\ 2 & 4 & 5 \end{array}\right) \to \left(\begin{array}{cc|c} 1 & 2 & 3 \\ 0 & 0 & -1 \end{array}\right).$$
The last row says $0 = -1$, and the augmented matrix has rank $2$.
So $Ax = b$ is solvable exactly when adding $b$ as a column does not raise the rank, which means that $b$ lies in the column space.
Watch out: you must reduce before you count, since both original matrices had only nonzero rows.

### L3 human

Two $m \times n$ matrices are [[equivalent|0CMHSGTWXB]], that is $B = QAP$ with $Q$ and $P$ invertible, exactly when they have the same rank.
Every matrix of rank $r$ is equivalent to the block matrix with $I_r$ in the top left corner and zeros elsewhere, so the rank is the only invariant of a matrix under change of basis on both sides.
For a linear map $T \colon V \to W$ with matrix $A$ in any bases, $\rank T = \rank A$, so the rank is a property of the map and not of the bases.
The [[rank factorization|5JGAG62VN8]] writes a matrix of rank $r$ as a sum of $r$ matrices $uv^{\mathsf{T}}$, and the analogous count for arrays with three indices is the tensor rank.
The tensor rank behaves worse: it can drop when the real field is enlarged to the complex field, while the rank of a matrix never changes under an extension of the field.
Over a ring that is not a field, there are several inequivalent notions of rank, and the theory of modules sorts them out.
