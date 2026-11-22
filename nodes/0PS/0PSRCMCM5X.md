---
tag: 0PSRCMCM5X
kind: definition
name: Moore-Penrose inverse
msc: [15A09]
topics: [SS4EVPKT3A]
audience: ug2
defines: 0YY8VX28JR
uses: [0EX045E2BP]
sources:
  - url: https://en.wikipedia.org/wiki/Moore–Penrose_inverse
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Moore–Penrose_inverse
    locator: Existence and uniqueness
inventory: [Z0BK2ZVY1Y]
---

## Definition

The Moore-Penrose inverse of a matrix is the one matrix that satisfies four equations which replace $A X = X A = I$.
Let $A$ be an $m \times n$ complex matrix, and let $^*$ denote the [[conjugate transpose|0EX045E2BP]].
An $n \times m$ complex matrix $X$ is a *Moore-Penrose inverse*, or *pseudoinverse*, of $A$ when it satisfies the four Penrose conditions:

1. $A X A = A$.
2. $X A X = X$.
3. $(A X)^* = A X$.
4. $(X A)^* = X A$.

Every matrix has exactly one such $X$, by [[the theorem on the pseudoinverse from the SVD|Q9YN0F60ZW]], so we speak of *the* Moore-Penrose inverse and write $A^+ = X$.
For a real matrix $A$, the conditions use the transpose, and $A^+$ is real.

## Notation

Most books write $A^+$, and some write $A^\dagger$.
A matrix that satisfies condition 1 is called a generalized inverse, or a $\{1\}$-inverse, and a matrix that satisfies conditions 1 and 2 is a reflexive generalized inverse, or a $\{1, 2\}$-inverse.

## Remarks

Each condition has a reason to be there.
Condition 1 asks $X$ to undo $A$ on the vectors that $A$ actually reaches, so that $A$ followed by $X$ followed by $A$ is $A$ again.
Condition 2 is the same rule with the roles of $A$ and $X$ swapped, and it stops $X$ from being larger than needed.
Conditions 3 and 4 ask the two products $A X$ and $X A$ to be Hermitian, and with conditions 1 and 2 this makes them orthogonal projections.
The definition only names the matrix, and the existence and the uniqueness are a theorem, proved from the singular value decomposition.

For a small example, take $A = \begin{pmatrix} 1 & 1 \end{pmatrix}$ and $X = \tfrac12 \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.
Compute the two products:
$$A X = \begin{pmatrix} 1 \end{pmatrix}, \qquad X A = \frac12 \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}.$$
Both are symmetric, $A X A = (1) A = A$, and $X A X = X (1) = X$, so $X = A^+$.

Condition 2 cannot be dropped.
For $A = \operatorname{diag}(1, 0)$, both $X = A$ and $X = I_2$ satisfy conditions 1, 3 and 4, but only $X = A$ satisfies condition 2, as [[the diagonal non-example|2GME1M2784]] shows.
The [[concept page|0YY8VX28JR]] gives more examples and the least-squares meaning of $A^+$.

## Explanations

### L1 human

For an invertible matrix $A$, the inverse $X = A^{-1}$ satisfies $AX = I$ and $XA = I$.
For a rectangular or singular matrix this is impossible.
The four conditions ask for less, and they still pick out exactly one matrix $X$.
For the row $\begin{pmatrix} 1 & 1 \end{pmatrix}$, that matrix is the column $\begin{pmatrix} \tfrac12 \\ \tfrac12 \end{pmatrix}$.

### L2 human

To test whether a given $X$ is the pseudoinverse, first compute $A X$ and $X A$ and check that both are Hermitian.
Then check $A X A = A$ and $X A X = X$, using the two products that you already have.
If one condition fails, $X$ is not the pseudoinverse.
Watch out: $A X = I$ is not one of the conditions, and for a matrix with more rows than columns it never holds, since $A X$ has rank at most $n < m$.
