---
tag: GS8WE1ZYV9
kind: statement
role: theorem
name: Sylvester's rank inequality and the Frobenius inequality
aliases: [sylvester-rank-inequality, frobenius-rank-inequality]
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug2
about: [0ZC9YTXZRY]
uses: [0EWQEYRVA8, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: Properties
---

## Statement

Let $F$ be a field.
Let $A$ be an $m \times n$ matrix, $B$ an $n \times p$ matrix and $C$ a $p \times q$ matrix over $F$.

1. (Frobenius inequality) $\rank(AB) + \rank(BC) \le \rank B + \rank(ABC)$.
2. (Sylvester's rank inequality) $\rank A + \rank B - n \le \rank(AB)$.

Here $\rank$ is the [[rank of a matrix|0ZC9YTXZRY]].

## Remarks

### Why each hypothesis is needed

- In part 2, $n$ is the inner size, the number of columns of $A$. With the outer sizes the bound fails.
  For $A = \begin{pmatrix} 1 & 0 \end{pmatrix}$ ($1 \times 2$) and $B = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$ ($2 \times 1$), $AB = 0$, and $\rank A + \rank B - 1 = 1 > 0$.
  With the inner size $n = 2$, the bound is $1 + 1 - 2 = 0 \le 0$.

### Consequences

- If $AB = 0$, then $\rank A + \rank B \le n$.
- If $A^2 = 0$ for an $n \times n$ matrix $A$, then $\rank A \le n/2$.
- $\dim \operatorname{Null}(AB) \le \dim \operatorname{Null}(A) + \dim \operatorname{Null}(B)$, for $n \times n$ matrices. This is part 2 written with nullities.

### Converse

Part 2 is sharp.
For $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$, $\rank A + \rank B - 2 = 0 = \rank(AB)$.
It can also be strict.
For $A = B = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, $\rank A + \rank B - 2 = 0$, but $AB = A$ has rank $1$.

### Generalizations

For linear maps $U \xrightarrow{C} V \xrightarrow{B} W \xrightarrow{A} X$ between finite-dimensional spaces, the same inequalities hold with $\rank$ the dimension of the image.
Part 2 is the case $B = I_n$ of part 1, with the letters renamed.

## History

The lower bound of part 2 is named after Sylvester, and part 1 is named after Frobenius.

## Explanations

### L1 human

Sylvester's inequality says that a product cannot lose too much rank.
Each factor can kill at most its own null space, and the null spaces have dimension at most $n - \rank$.

### L2 human

The map $x \mapsto Ax$ loses $\dim(\operatorname{Col}(B) \cap \operatorname{Null}(A))$ dimensions on the column space of $B$.
That number is at most $\dim \operatorname{Null}(A) = n - \rank A$.
So $\rank(AB) \ge \rank B - (n - \rank A)$.

### L3 human

The Frobenius inequality compares the loss of rank under $A$ on the two nested subspaces $\operatorname{Col}(BC) \subseteq \operatorname{Col}(B)$.
The loss on the smaller subspace is at most the loss on the larger one.
