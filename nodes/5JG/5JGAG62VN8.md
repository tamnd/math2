---
tag: 5JGAG62VN8
kind: statement
role: theorem
name: Rank factorization and rank-one matrices
aliases: [rank-factorization, cr-factorization]
msc: ["15A03", "15A23"]
topics: [S6559D61BP]
audience: ug1
about: [0ZC9YTXZRY]
uses: [0EWQEYRVA8, 076JGP6R3T, 0NNR68BFRY, 0BCMGDHZGR]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_factorization
    locator: Existence
  - book: isbn:9781733146678
    locator: Chapter 3
---

## Statement

Every matrix of rank $r$ is a tall matrix with $r$ columns times a wide matrix with $r$ rows, and so it is a sum of $r$ matrices of rank one.
Let $F$ be a field and let $A$ be an $m \times n$ matrix over $F$ of [[rank|0ZC9YTXZRY]] $r \ge 1$.

1. There are an $m \times r$ matrix $C$ of rank $r$ and an $r \times n$ matrix $R$ of rank $r$ with $A = CR$.
2. One choice is this: the columns of $C$ are the [[pivot columns|0BCMGDHZGR]] of $A$, and the rows of $R$ are the $r$ nonzero rows of the [[reduced row echelon form|0NNR68BFRY]] of $A$.
3. $A$ is a sum of $r$ matrices of rank $1$, and a sum of $s$ matrices of rank at most $1$ has rank at most $s$.
4. A matrix has rank $1$ if and only if it equals $uv^{\mathsf{T}}$ for some nonzero $u \in F^m$ and nonzero $v \in F^n$.

## Remarks

### A first example

The matrix
$$A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \\ 3 & 6 \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} \begin{pmatrix} 1 & 2 \end{pmatrix}$$
has rank $1$, and part 4 writes it as $uv^{\mathsf{T}}$ with $u = (1, 2, 3)$ and $v = (1, 2)$.
Entry $(i, j)$ is $u_i v_j$, so every column is a multiple of $u$ and every row is a multiple of $v$.
For a matrix of rank $2$, the [[CR factorization of a 3 by 4 matrix|CJWPF3A5TR]] works out parts 1, 2 and 3 with all the numbers.

### Why the hypotheses are needed

For $r = 0$, the matrix is $A = 0$, and the factors would be an $m \times 0$ and a $0 \times n$ matrix.
The statement then holds only with empty matrices, so we assume $r \ge 1$.

In part 2, the columns of $C$ must be the pivot columns of $A$ itself.
The pivot columns of the reduced form are standard unit vectors, and they do not span $\operatorname{Col}(A)$ in general.
For $A = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$, the reduced form is $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$, and $(1, 0)$ is not in the column space of $A$; the [[example on reduced pivot columns|K21W7FA8MQ]] gives more on this trap.

### What it gives you

From $A = CR$ we get $\operatorname{Col}(A) \subseteq \operatorname{Col}(C)$ and $\operatorname{Row}(A) \subseteq \operatorname{Row}(R)$, and comparing dimensions turns both inclusions into equalities.
In particular the row space of $A$ has dimension $r$, which is one [[proof that row rank equals column rank|S1C1ATEFW1]].
Part 3 says that the rank is the smallest number of rank-one matrices with sum $A$.
Storing $C$ and $R$ takes $r(m + n)$ numbers instead of $mn$, so a $1000 \times 1000$ matrix of rank $10$ needs $20\,000$ numbers instead of a million.

### How unique the factorization is

The factorization is not unique: for every invertible $r \times r$ matrix $G$, also $A = (CG)(G^{-1}R)$.
Every rank factorization arises in this way.
If $A = CR = C'R'$, then $C$ and $C'$ both have the column space of $A$, so $C' = CG$ for an invertible $G$, and then $CGR' = CR$ gives $GR' = R$, because $C$ has independent columns.

### Generalizations

For a linear map $T \colon V \to W$ of rank $r$, a rank factorization is a factorization $V \to F^r \to W$ into a surjection followed by an injection, through a copy of the image.
Over $\mathbb{R}$, the singular value decomposition gives a rank factorization $A = \sum_{l=1}^r \sigma_l u_l v_l^{\mathsf{T}}$ with orthonormal $u_l$ and orthonormal $v_l$.

## History

Gilbert Strang uses the name $CR$ factorization for part 2 in his textbooks.

## Explanations

### L1 human

A matrix of rank $r$ holds less information than its size suggests.
It is built from $r$ columns, which give the directions, and $r$ rows, which say how much of each direction goes into each column.
For example, the $3 \times 2$ matrix with columns $(1, 2, 3)$ and $(2, 4, 6)$ is fixed by the one column $(1, 2, 3)$ and the one row $(1, 2)$.

### L2 human

Here is the typical computation of a $CR$ factorization.
Take $A = \begin{pmatrix} 1 & 1 & 2 \\ 1 & 2 & 3 \end{pmatrix}$.
Subtracting row 1 from row 2 and then row 2 from row 1 gives the reduced form with rows $(1, 0, 1)$ and $(0, 1, 1)$, with pivots in columns 1 and 2.
So $C$ consists of columns 1 and 2 of $A$, and $R$ is the reduced form:
$$A = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{pmatrix}.$$
Check: column 3 of the product is $1 \cdot (1, 1) + 1 \cdot (1, 2) = (2, 3)$, which is column 3 of $A$.
Expanding the product column by row gives $A = (1, 1)^{\mathsf{T}}(1, 0, 1) + (1, 2)^{\mathsf{T}}(0, 1, 1)$, a sum of two rank-one matrices.
Watch out: take the columns of $C$ from $A$, and not from the reduced form.

### L3 human

A rank factorization is the factorization of $x \mapsto Ax$ through its image $\operatorname{Col}(A) \cong F^r$: first $x \mapsto Rx$ onto $F^r$, then $y \mapsto Cy$ into $F^m$.
The rank-one matrices $uv^{\mathsf{T}}$ are the linear maps $x \mapsto (v^{\mathsf{T}} x) u$, a linear form times a fixed vector, and the sub-area on [[dual spaces|9K7FFF26QR]] studies such forms.
Writing a matrix as a short sum of rank-one terms is the basis of low-rank approximation, where the singular value decomposition chooses the terms that matter most.
