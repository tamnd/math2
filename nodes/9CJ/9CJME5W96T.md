---
tag: 9CJME5W96T
kind: statement
role: proposition
name: Rank of the adjugate
msc: ["15A09", "15A03"]
topics: [DTBK11SR77]
audience: ug2
about: [07W9H8QF38]
uses: [0GMPYM0NSR, 0ZC9YTXZRY, 0QA8CHH8MG]
sources:
  - url: https://en.wikipedia.org/wiki/Adjugate_matrix
    locator: Properties
---

## Statement

The rank of the adjugate takes only three values, and the rank of the matrix decides which one.
Let $F$ be a [[field|0QA8CHH8MG]], let $n \ge 2$, and let $A$ be an $n \times n$ matrix over $F$.
Then the [[rank|0ZC9YTXZRY]] of its [[adjugate|0GMPYM0NSR]] is
$$\operatorname{rank} \operatorname{adj} A = \begin{cases} n & \text{if } \operatorname{rank} A = n, \\ 1 & \text{if } \operatorname{rank} A = n - 1, \\ 0 & \text{if } \operatorname{rank} A \le n - 2. \end{cases}$$
In the second case, the columns of $\operatorname{adj} A$ span the kernel of $A$.

## Remarks

### Three matrices, three cases

Take $n = 3$.
The matrix $\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 10 \end{pmatrix}$ has rank $3$, and its adjugate is $-3$ times its inverse, so it has rank $3$ as well; the [[worked example|BDHT6DBGC9]] computes it.
The matrix $\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$ has rank $2$, and the [[singular example|H98NXA00NZ]] finds the adjugate $\begin{pmatrix} -3 & 6 & -3 \\ 6 & -12 & 6 \\ -3 & 6 & -3 \end{pmatrix}$, of rank $1$.
The matrix $\begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 3 & 6 & 9 \end{pmatrix}$ has rank $1$.
Any two of its rows are proportional, so every $2 \times 2$ minor is $0$, and the adjugate is the zero matrix.

### Why each hypothesis is needed

The rank is a notion over a field, so the statement needs $F$ to be a field.
The condition $n \ge 2$ only keeps away the convention $\operatorname{adj}(a) = (1)$ for $1 \times 1$ matrices.
With that convention the statement still holds for $n = 1$: the matrix $(0)$ has rank $0 = n - 1$, and its adjugate $(1)$ has rank $1$ and spans the kernel $F$.
For $n = 2$ the third case means $A = 0$, and then $\operatorname{adj} A = 0$ as well.

### What it gives you

A singular matrix has adjugate $0$ exactly when its rank is at most $n - 2$.
When the rank is $n - 1$, any nonzero column of $\operatorname{adj} A$ is a basis of the kernel of $A$, and any nonzero row is a basis of the kernel of $A^{\mathsf{T}}$.
So the adjugate never has a rank strictly between $1$ and $n$.

### The converse

The rank of $\operatorname{adj} A$ determines the rank of $A$ when $n \ge 3$ and $\operatorname{adj} A \neq 0$, because the values $n$ and $1$ are then different.
When $\operatorname{adj} A = 0$, we only learn that $\operatorname{rank} A \le n - 2$.
For $n = 2$ the adjugate $\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ has the same entries as $A$ up to order and sign, so it always has the same rank as $A$.

### Generalizations

The $k$-th compound matrix of $A$ is the matrix of all $k \times k$ minors, and over a field it has rank $\binom{r}{k}$ when $A$ has rank $r$.
The adjugate is the compound of order $n - 1$ up to signs and a transpose.
For $r = n - 1$ and $k = n - 1$ this gives $\binom{n-1}{n-1} = 1$, which is the middle case.

## Explanations

### L1 human

For an invertible matrix, the adjugate is invertible too.
If the matrix only just fails to be invertible, with rank one less than its size, then all columns of its adjugate lie along one line.
If the matrix fails by more, then its adjugate is the zero matrix.

### L2 human

Here is a typical use: find a nonzero solution of $Ax = 0$ for
$$A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 2 & 1 \end{pmatrix}.$$
Row $3$ is row $1$ plus row $2$, and rows $1$ and $2$ are independent, so $\operatorname{rank} A = 2 = n - 1$.
The first column of $\operatorname{adj} A$ consists of the cofactors of row $1$:
$$C_{11} = 1 \cdot 1 - 1 \cdot 2 = -1, \qquad C_{12} = -(0 \cdot 1 - 1 \cdot 1) = 1, \qquad C_{13} = 0 \cdot 2 - 1 \cdot 1 = -1.$$
Check: $A (-1, 1, -1) = (-1 + 1, \ 1 - 1, \ -1 + 2 - 1) = (0, 0, 0)$.
By the theorem, $(-1, 1, -1)$ spans the kernel.
Watch out: if the column you pick is zero, try another one, since only some columns need to be nonzero.

### L3 human

In the space of $n \times n$ matrices, the matrices of rank $n - 1$ form the smooth part of the hypersurface $\det A = 0$.
The gradient of $\det$ at $A$ is $(\operatorname{adj} A)^{\mathsf{T}}$, so it is nonzero exactly on this smooth part, and it vanishes on the matrices of rank at most $n - 2$, which form the singular part.
The [[proof|RCA9H1Z5SB]] uses the [[rank by minors|HVHQ50TJB1]] for the outer cases and the [[adjugate identity|0528HKWZ1Z]] for the middle one.
