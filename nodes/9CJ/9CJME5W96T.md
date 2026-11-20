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

Let $F$ be a [[field|0QA8CHH8MG]], let $n \ge 2$, and let $A$ be an $n \times n$ matrix over $F$.
Then the [[rank|0ZC9YTXZRY]] of the [[adjugate|0GMPYM0NSR]] is
$$\operatorname{rank} \operatorname{adj} A = \begin{cases} n & \text{if } \operatorname{rank} A = n, \\ 1 & \text{if } \operatorname{rank} A = n - 1, \\ 0 & \text{if } \operatorname{rank} A \le n - 2. \end{cases}$$
In the second case the columns of $\operatorname{adj} A$ span the kernel of $A$.

## Remarks

### Why each hypothesis is needed

The rank is defined over a field.
For $n = 1$ the convention $\operatorname{adj}(a) = (1)$ gives rank $1$ also for $a = 0$, so the rule needs $n \ge 2$.

### Consequences

- A singular matrix has adjugate $0$ if and only if its rank is at most $n - 2$.
- For rank $n - 1$, any nonzero column of $\operatorname{adj} A$ is a basis of the kernel of $A$, and any nonzero row is a basis of the kernel of $A^{T}$.
- $\operatorname{adj} A$ is never of rank strictly between $1$ and $n$.

### Converse

The rank of $\operatorname{adj} A$ determines the rank of $A$ when $n \ge 3$ and $\operatorname{adj} A \neq 0$.
For $n = 2$, $\operatorname{adj} A$ has the same rank as $A$.

### Generalizations

The $k$-th compound matrix of a matrix of rank $r$ has rank $\binom{r}{k}$.
The adjugate is the compound of order $n - 1$ up to signs and transpose, and $\binom{n-1}{n-1} = 1$ gives the middle case.

## Explanations

### L1 human

For an invertible matrix the adjugate is invertible too.
If the matrix just fails to be invertible, its adjugate has all columns along one line.
If the matrix fails by more, its adjugate is the zero matrix.

### L2 human

For $S = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$, of rank $2$, the adjugate has rank $1$; see the [[singular example|H98NXA00NZ]].
For $\begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 3 & 6 & 9 \end{pmatrix}$, of rank $1$, every $2 \times 2$ minor is $0$, so the adjugate is $0$.
A trap: for $n = 2$ the third case is the zero matrix only, since rank $\le 0$ means $A = 0$.

### L3 human

In the space of matrices, the set of rank $n - 1$ is the smooth part of the determinant hypersurface, and $\operatorname{adj} A$ is the gradient of $\det$ there.
So the gradient vanishes exactly on the singular locus, the matrices of rank at most $n - 2$.
