---
tag: TR48YQGCCA
kind: statement
role: theorem
name: Rank-nullity theorem for matrices
msc: ["15A03", "15A04"]
topics: [S6559D61BP]
audience: ug1
about: [0ZC9YTXZRY, 0PHDYNR24D]
uses: [0ZC9YTXZRY, 0PHDYNR24D, 0APCFW7639]
sources:
  - url: https://en.wikipedia.org/wiki/Rank%E2%80%93nullity_theorem
    locator: Matrices
  - book: isbn:9780321982384
    locator: Section 4.6
  - url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ap-linear-algebra.tex#L4974
    locator: ap-linear-algebra.tex:4974
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section3-5.xml#L1162
    locator: src/section3-5.xml:1162
---

## Statement

Let $F$ be a field and let $A$ be an $m \times n$ matrix over $F$.
Let $r$ be the [[rank|0ZC9YTXZRY]] of $A$.
Let $k$ be the [[nullity|0APCFW7639]] of $A$, that is, the dimension of the [[null space|0PHDYNR24D]] of $A$.
Then the number of columns is the sum of the rank and the nullity:
$$n = r + k.$$

## Remarks

### Why each hypothesis is needed

- The count uses the number of columns $n$, not the number of rows $m$. For the $1 \times 3$ matrix $\begin{pmatrix} 1 & 0 & 0 \end{pmatrix}$, $r = 1$ and $k = 2$, so $r + k = 3 = n \ne m$.
- The entries must lie in a field, so that the null space has a dimension. Over $\mathbb{Z}/4$, the $1 \times 1$ matrix $(2)$ has the null space $\{0, 2\}$, which has no basis.

### Consequences

- If $n > m$, then $k = n - r \ge n - m > 0$, so $Ax = 0$ has a nonzero solution.
- A square matrix has a trivial null space if and only if it has full rank.
- The left null space has dimension $m - r$, by the theorem for $A^\top$ and [[row rank equals column rank|0TZAG60ZYT]].

### Converse

For all $m$, $n$ and $r \le \min(m, n)$, some $m \times n$ matrix has rank $r$ and nullity $n - r$, for example the matrix with $r$ ones on the diagonal and zeros elsewhere.

### Generalizations

The [[rank-nullity theorem|0W4FSW1TVB]] for a linear map $T \colon V \to W$ gives $\dim V = \dim \im T + \dim \ker T$.
The matrix form is the case $T(x) = Ax$ on $V = F^n$.

## History

The count of free variables in the solution of a linear system is classical elimination theory.
The name "rank-nullity theorem" is modern and comes from the textbook language of linear maps.

## Explanations

### L1 human

Every column of a matrix is either a pivot column or a free column.
The pivot columns count the rank, and the free columns count the dimension of the solutions of $Ax = 0$.
So the two numbers add up to the number of columns.

### L2 human

The null space is a subspace of $F^n$, the space of column vectors with $n$ entries.
The claim splits $n$ into the part that $A$ keeps, the rank, and the part that $A$ sends to zero, the nullity.
For the [[$3 \times 4$ example|GG03BSSZ43]], the rank is $2$ and the nullity is $2$.

### L3 human

The statement is the exactness of $0 \to \operatorname{Null}(A) \to F^n \to \operatorname{Col}(A) \to 0$, together with additivity of dimension.
