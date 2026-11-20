---
tag: 08WE2W7DYS
kind: statement
role: theorem
name: Cauchy–Binet formula
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug2
about: [00KDZRW4C0]
uses: [0C3CFHDN6R, 0SD528P0EK]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy–Binet_formula
    locator: Statement
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: History
same_as:
  wikidata: Q45286
  wikipedia: Cauchy–Binet formula
---

## Statement

Let $K$ be a commutative ring, let $m, n \ge 1$, let $A$ be an $m \times n$ matrix and $B$ an $n \times m$ matrix over $K$.
For a subset $S \subseteq \{1, \dots, n\}$ with $m$ elements, let $A_S$ be the $m \times m$ matrix of the columns of $A$ in $S$.
Let $B^S$ be the $m \times m$ matrix of the rows of $B$ in $S$.

1. If $m \le n$, then
$$\det(AB) = \sum_{S} \det(A_S) \det(B^S),$$
where the sum runs over all subsets $S$ of $\{1, \dots, n\}$ with $m$ elements, and $\det$ is the [[determinant|0C3CFHDN6R]].
2. If $m > n$, then $\det(AB) = 0$.

## Remarks

### Why each hypothesis is needed

The ring must be commutative, as in every use of the determinant.
The sizes must match: $A$ is $m \times n$ and $B$ is $n \times m$, so that $AB$ is square.
Without part 2 the case $m > n$ would have no formula, since there are no subsets with $m$ elements; the sum is then empty, and its value $0$ is correct.

### Consequences

- For $m = n$, the sum has one term, and the formula is [[multiplicativity|04CPJ6AF00]], $\det(AB) = \det A \det B$.
- For $m = 1$, it is the formula for the product of a row and a column.
- The determinants $\det(A_S)$ and $\det(B^S)$ are [[minors|0SD528P0EK]] of order $m$.
- Gram determinants: over $\mathbb{R}$, take $B = A^T$; then $\det(A A^T) = \sum_S \det(A_S)^2 \ge 0$.
- Equality holds if and only if the rows of $A$ are linearly dependent, by the [[rank by minors|~ffa904d5]].
- Lagrange's identity is the case $m = 2$ with rows $a$, $b$ of $A$ and $B = A^T$:
$$\Bigl(\sum_i a_i^2\Bigr)\Bigl(\sum_i b_i^2\Bigr) - \Bigl(\sum_i a_i b_i\Bigr)^2 = \sum_{i<j} (a_i b_j - a_j b_i)^2.$$
- Lagrange's identity proves the Cauchy-Schwarz inequality in $\mathbb{R}^n$, with the case of equality.

### Converse

The formula is an identity, so a converse in the usual sense does not apply.
Its terms can cancel: $\det(AB) = 0$ does not imply that each product $\det(A_S) \det(B^S)$ is $0$.
For $A = (1, 1)$ and $B = (1, -1)^T$, the two terms are $1$ and $-1$, and $\det(AB) = 0$.

### Generalizations

The same argument gives every $k \times k$ minor of $AB$ as a sum over $k$-subsets: $\det (AB)_{I, J} = \sum_S \det A_{I, S} \det B_{S, J}$.
In the language of exterior powers, this says $\Lambda^k(AB) = \Lambda^k A \, \Lambda^k B$; exterior powers belong to multilinear algebra.

## History

Binet and Cauchy presented papers on this product theorem to the Academy on the same day, 30 November 1812.

## Explanations

### L1 human

The Cauchy-Binet formula computes the determinant of a product of two rectangular matrices.
It sums products of matching minors of the two factors.
It generalizes the product rule for determinants of square matrices.

### L2 human

Take $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$ and $B = A^T$.

1. The $2 \times 2$ minors of $A$ are $\det A_{\{1,2\}} = 5 - 8 = -3$, $\det A_{\{1,3\}} = 6 - 12 = -6$ and $\det A_{\{2,3\}} = 12 - 15 = -3$.
2. Here $B^S = (A_S)^T$, so $\det B^S = \det A_S$.
3. The formula gives $9 + 36 + 9 = 54$.
4. Check directly: $A A^T = \begin{pmatrix} 14 & 32 \\ 32 & 77 \end{pmatrix}$, with determinant $1078 - 1024 = 54$.

In the other order, $A^T A$ is $3 \times 3$ and $3 > 2$, so part 2 gives $\det(A^T A) = 0$.
Check: the rows of $A^T A$ lie in the span of the two rows of $A$, so they are dependent.
The typical use is the Gram determinant of a few vectors in a large space.
A trap: the sum is over sets of columns of $A$, which are the same as the sets of rows of $B$; the two index sets are not chosen independently.

### L3 human

Cauchy-Binet is the functoriality of the top exterior power for maps between modules of different ranks.
It is the tool behind the matrix-tree theorem and many formulas in combinatorics.
